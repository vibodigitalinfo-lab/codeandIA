"""Regla de fechas del sitio: `date` dentro de la ventana [lanzamiento, hoy],
sin fechas repetidas y nunca posterior a `updated`.

Solo cuentan los articulos indexables: los retirados con `noindex: true` no
forman parte de la cadencia publica (el dia de lanzamiento, la fecha mas
antigua, puede agrupar el bloque inicial).

Uso:  python fechas_check.py [hoy_ISO]
Hoy por defecto es la fecha del sistema; se puede forzar con HOY=2026-09-26.
"""
import collections
import datetime
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(RAIZ, 'articulos')
assert os.path.isdir(ART), 'no encuentro articulos/ junto al script: %s' % RAIZ
HOY = sys.argv[1] if len(sys.argv) > 1 else os.environ.get('HOY')
HOY = datetime.date(*map(int, HOY.split('-'))) if HOY else datetime.date.today()


def articulos_publicados():
    for root, dirs, files in os.walk(ART):
        dirs[:] = [d for d in dirs if d != '_entrada']
        for f in files:
            if f.endswith('.md'):
                yield os.path.join(root, f)


fechas = {}
sin_fecha = []
for p in articulos_publicados():
    rel = os.path.relpath(p, RAIZ).replace('\\', '/')
    t = io.open(p, encoding='utf-8').read()
    # Los articulos retirados (noindex) no cuentan para la cadencia publica.
    if re.search(r'^noindex:\s*true', t, re.M):
        continue
    m = re.search(r'^date:\s*(\S+)', t, re.M)
    if not m:
        sin_fecha.append(rel)
        continue
    fechas[rel] = datetime.date(*map(int, m.group(1).split('-')))

fallos = []

if not fechas:
    print('ERROR: no se ha encontrado ningun articulo en %s' % ART)
    sys.exit(2)

# 1. Ninguna fecha futura
for rel, d in sorted(fechas.items()):
    if d > HOY:
        fallos.append('FECHA FUTURA %s -> %s (hoy es %s)' % (rel, d, HOY))

# 2. Ninguna fecha repetida, salvo el dia de lanzamiento (la fecha mas antigua),
#    que agrupa el bloque inicial con el que abre el blog.
conteo = collections.Counter(fechas.values())
lanzamiento = min(conteo) if conteo else None
for d, n in sorted(conteo.items()):
    if n > 1 and d != lanzamiento:
        fallos.append('FECHA REPETIDA %s x%d:' % (d, n))
        for rel in sorted(k for k, v in fechas.items() if v == d):
            fallos.append('    %s' % rel)

# 3. Ventana de fechas valida: desde el lanzamiento del dominio (2026-09-08)
#    hasta hoy. No se fabrica historia hacia atras ni se fechan piezas en el
#    futuro. El hueco entre fechas ya no se limita: la hoja de ruta post-crisis
#    marca 1-2 articulos por semana, sin picos.
MIN_DATE = datetime.date(2026, 9, 8)
ds = sorted(conteo)
if ds:
    print('%d articulos | %s .. %s' % (len(fechas), ds[0], ds[-1]))
for rel, d in sorted(fechas.items()):
    if d < MIN_DATE:
        fallos.append('FECHA ANTERIOR AL LANZAMIENTO %s -> %s (min %s)'
                      % (rel, d, MIN_DATE))

for rel in sin_fecha:
    fallos.append('SIN date: %s' % rel)


# 4. Fechas de revision: 'updated' (lo que ve el lector) y 'last_modified_at' (<lastmod>)
def ficheros_con_frontmatter():
    lista = list(articulos_publicados())
    for f in ('aviso-legal.md', 'privacidad.md', 'sobre-mi.md', 'promociones.md'):
        p = os.path.join(RAIZ, f)
        if os.path.isfile(p):
            lista.append(p)
    return lista


def campo(texto, clave):
    m = re.search(r'^%s:\s*(\S+)' % clave, texto, re.M)
    if not m:
        return None
    try:
        return datetime.date(*map(int, m.group(1).strip('\'"').split('-')))
    except ValueError:
        return None


avisos = []
for p in ficheros_con_frontmatter():
    rel = os.path.relpath(p, RAIZ).replace('\\', '/')
    t = io.open(p, encoding='utf-8').read()
    u, lm, d = campo(t, 'updated'), campo(t, 'last_modified_at'), campo(t, 'date')
    if u and u > HOY:
        fallos.append('UPDATED FUTURO %s -> %s' % (rel, u))
    if lm and lm > HOY:
        fallos.append('LAST_MODIFIED_AT FUTURO %s -> %s' % (rel, lm))
    if lm and u and lm < u:
        fallos.append('LAST_MODIFIED_AT ANTERIOR A updated %s -> %s < %s' % (rel, lm, u))
    if lm and d and lm < d:
        fallos.append('LAST_MODIFIED_AT ANTERIOR A date %s -> %s < %s' % (rel, lm, d))
    if u and d and d > u:
        fallos.append('DATE POSTERIOR A updated %s -> %s > %s' % (rel, d, u))
    if u and not lm:
        avisos.append('%s (updated %s)' % (rel, u))

print('hoy: %s' % HOY)
print()
if avisos:
    print('AVISOS (%d): updated sin last_modified_at, esas URLs iran sin <lastmod>:' % len(avisos))
    for a in avisos:
        print('  - %s' % a)
    print()
if fallos:
    print('FALLOS (%d):' % len(fallos))
    for f in fallos:
        print('  - %s' % f)
    sys.exit(1)
print('OK: fechas dentro de rango (desde %s), sin futuras ni repetidas' % MIN_DATE)
