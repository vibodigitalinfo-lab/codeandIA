"""Publica el siguiente articulo programado de articulos/_entrada/.

Un articulo esta programado si su frontmatter lleva `publicar: AAAA-MM-DD`.
Lo que no lleve ese campo (borradores, piezas en pausa) nunca se publica solo.

Cada dia se publica como mucho UN articulo, el mas antiguo cuya fecha
`publicar` ya haya llegado, y solo si respeta la cadencia (regla del
2026-10-25, la misma que vigila fechas_check.py):

- nunca dos dias seguidos;
- maximo 2 por semana natural (lunes a domingo).

Si hoy no toca, el articulo espera al siguiente dia libre. Asi una fecha mal
puesta en `publicar` nunca rompe la cadencia: como mucho retrasa la pieza.

Al publicar: mueve el fichero a articulos/<categoria>/, pone `date`,
`last_modified_at` (y `updated`, si lo tenia) a la fecha de hoy y quita
`publicar`. Nada de fechas hacia atras ni en el futuro.

Uso:
    python scripts/publicar_programados.py            # publica si toca hoy
    python scripts/publicar_programados.py --plan     # calendario previsto, sin tocar nada
Hoy por defecto es la fecha del sistema; se puede forzar con HOY=2026-10-27.
"""
import datetime
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(RAIZ, 'articulos')
ENTRADA = os.path.join(ART, '_entrada')
CARPETAS = {'Guía': 'guias', 'Lista': 'listas', 'Review': 'reviews',
            'Comparativa': 'comparativas'}
MAX_SEMANA = 2


def hoy():
    h = os.environ.get('HOY')
    return datetime.date(*map(int, h.split('-'))) if h else datetime.date.today()


def fecha(texto, clave):
    m = re.search(r'^%s:\s*(\S+)' % clave, texto, re.M)
    if not m:
        return None
    return datetime.date(*map(int, m.group(1).strip('\'"').split('-')))


def fechas_publicadas():
    """Fechas `date` de los articulos indexables ya publicados."""
    fechas = []
    for root, dirs, files in os.walk(ART):
        dirs[:] = [d for d in dirs if d != '_entrada']
        for f in files:
            if not f.endswith('.md'):
                continue
            t = io.open(os.path.join(root, f), encoding='utf-8').read()
            if re.search(r'^noindex:\s*true', t, re.M):
                continue
            d = fecha(t, 'date')
            if d:
                fechas.append(d)
    return fechas


def programados():
    """(fecha publicar, ruta) de lo que hay en _entrada con `publicar`."""
    cola = []
    for root, dirs, files in os.walk(ENTRADA):
        for f in files:
            if not f.endswith('.md'):
                continue
            p = os.path.join(root, f)
            d = fecha(io.open(p, encoding='utf-8').read(), 'publicar')
            if d:
                cola.append((d, p))
    return sorted(cola)


def motivo_para_esperar(dia, fechas):
    """None si `dia` respeta la cadencia; si no, el motivo para esperar."""
    if dia in fechas:
        return 'ya hay un articulo publicado hoy'
    if dia - datetime.timedelta(days=1) in fechas:
        return 'ayer ya se publico (nunca dos dias seguidos)'
    semana = dia.isocalendar()[:2]
    n = sum(1 for d in fechas if d.isocalendar()[:2] == semana)
    if n >= MAX_SEMANA:
        return 'esta semana ya hay %d articulos (maximo %d)' % (n, MAX_SEMANA)
    return None


def destino(ruta):
    t = io.open(ruta, encoding='utf-8').read()
    m = re.search(r'^category:\s*"?([^"\n]+)"?', t, re.M)
    if not m or m.group(1).strip() not in CARPETAS:
        sys.exit('%s: category desconocida o ausente (validas: %s)'
                 % (ruta, ', '.join(CARPETAS)))
    nombre = os.path.basename(ruta)
    if nombre == 'borrador.md':
        nombre = os.path.basename(os.path.dirname(ruta)) + '.md'
    return os.path.join(ART, CARPETAS[m.group(1).strip()], nombre)


def publicar(ruta, dia):
    dest = destino(ruta)
    if os.path.exists(dest):
        sys.exit('ya existe %s: no se sobrescribe' % dest)
    t = io.open(ruta, encoding='utf-8').read()
    cab, sep, cuerpo = t.partition('\n---\n')
    hoy_iso = dia.isoformat()
    cab = re.sub(r'^publicar:.*\n?', '', cab, flags=re.M)
    cab = re.sub(r'^date:.*$', 'date: %s' % hoy_iso, cab, flags=re.M)
    cab = re.sub(r'^updated:.*$', 'updated: %s' % hoy_iso, cab, flags=re.M)
    if re.search(r'^last_modified_at:', cab, re.M):
        cab = re.sub(r'^last_modified_at:.*$', 'last_modified_at: %s' % hoy_iso,
                     cab, flags=re.M)
    else:
        cab = cab.rstrip('\n') + '\nlast_modified_at: %s' % hoy_iso
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    io.open(dest, 'w', encoding='utf-8', newline='\n').write(cab + sep + cuerpo)
    os.remove(ruta)
    return dest


def plan(dia):
    """Simula los proximos 90 dias sin tocar ningun fichero."""
    fechas = fechas_publicadas()
    cola = programados()
    if not cola:
        print('No hay nada programado en _entrada/ (falta `publicar:`).')
        return
    for _ in range(90):
        listos = [c for c in cola if c[0] <= dia]
        if listos and not motivo_para_esperar(dia, fechas):
            prog, ruta = listos[0]
            retraso = (dia - prog).days
            print('%s %s  %s%s' % (dia, dia.strftime('%a'),
                                   os.path.relpath(ruta, RAIZ).replace('\\', '/'),
                                   '  (programado %s, +%d dias)' % (prog, retraso)
                                   if retraso else ''))
            fechas.append(dia)
            cola.remove(listos[0])
            if not cola:
                return
        dia += datetime.timedelta(days=1)
    print('Quedan sin hueco en 90 dias: %d' % len(cola))


def main():
    dia = hoy()
    if '--plan' in sys.argv:
        plan(dia)
        return
    listos = [c for c in programados() if c[0] <= dia]
    salida = os.environ.get('GITHUB_OUTPUT')
    if not listos:
        print('%s: nada programado para hoy' % dia)
        return
    motivo = motivo_para_esperar(dia, fechas_publicadas())
    if motivo:
        print('%s: %s; %d en espera' % (dia, motivo, len(listos)))
        return
    dest = publicar(listos[0][1], dia)
    rel = os.path.relpath(dest, RAIZ).replace('\\', '/')
    print('%s: publicado %s' % (dia, rel))
    if salida:
        with open(salida, 'a') as f:
            f.write('publicado=%s\n' % rel)


if __name__ == '__main__':
    main()
