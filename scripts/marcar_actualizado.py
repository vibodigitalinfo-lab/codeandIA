"""Fechas de revision de articulos y paginas: 'updated' y 'last_modified_at'.

Los dos campos existen y NO significan lo mismo:

- updated:           revision de contenido que ve el lector ("Actualizado el ...").
                     Se toca cuando se revisan precios, datos o el texto de verdad.
- last_modified_at:  ultima modificacion real del fichero. Es el unico campo que
                     jekyll-sitemap lee en site.html_pages para escribir <lastmod>
                     en sitemap.xml, asi que sin el la URL va sin fecha y Google
                     decide por su cuenta cuando volver a rastrearla.

Uso:
    python scripts/marcar_actualizado.py --check
    python scripts/marcar_actualizado.py --sincronizar
    python scripts/marcar_actualizado.py --tocar articulos/guias/x.md [YYYY-MM-DD]
"""
import datetime
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(RAIZ, 'articulos')
PAGINAS_SUELTAS = ('aviso-legal.md', 'privacidad.md', 'sobre-mi.md', 'promociones.md')
CAMPOS = ('updated', 'last_modified_at')


def ficheros():
    """Articulos publicados (sin _entrada) y las paginas sueltas con frontmatter."""
    salida = []
    for root, dirs, files in os.walk(ART):
        dirs[:] = [d for d in dirs if d != '_entrada']
        for f in sorted(files):
            if f.endswith('.md'):
                salida.append(os.path.join(root, f))
    for f in PAGINAS_SUELTAS:
        p = os.path.join(RAIZ, f)
        if os.path.isfile(p):
            salida.append(p)
    return salida


def limites(texto):
    """(salto_de_linea, indice donde empieza el '---' de cierre) o None."""
    if not texto.startswith('---'):
        return None
    nl = '\r\n' if '\r\n' in texto else '\n'
    fin = texto.find(nl + '---', 3)
    if fin == -1:
        return None
    return nl, fin


def campos(texto):
    """Valores de los campos que nos interesan, tal cual esten escritos."""
    lim = limites(texto)
    if not lim:
        return {}
    fm = texto[:lim[1]]
    salida = {}
    for c in CAMPOS:
        m = re.search(r'^%s:\s*(\S+)' % c, fm, re.M)
        if m:
            salida[c] = m.group(1).strip('\'"')
    return salida


def escribir(texto, clave, valor):
    """Devuelve el texto con 'clave: valor' puesto o actualizado en el frontmatter."""
    lim = limites(texto)
    if not lim:
        return texto
    nl, fin = lim
    lineas = texto[3:fin].split(nl)
    patron = re.compile(r'^%s:' % clave)
    for i, linea in enumerate(lineas):
        if patron.match(linea):
            lineas[i] = '%s: %s' % (clave, valor)
            return texto[:3] + nl.join(lineas) + texto[fin:]
    # No estaba: se inserta despues de 'updated:' si existe, y si no al final.
    destino = len(lineas) - 1 if lineas and lineas[-1] == '' else len(lineas)
    for i, linea in enumerate(lineas):
        if linea.startswith('updated:'):
            destino = i + 1
            break
    lineas.insert(destino, '%s: %s' % (clave, valor))
    return texto[:3] + nl.join(lineas) + texto[fin:]


def fecha_valida(v):
    try:
        return datetime.date(*map(int, v.split('-')))
    except (AttributeError, TypeError, ValueError):
        return None


def sincronizar():
    """Pone last_modified_at igual a updated en todo fichero que tenga 'updated'."""
    tocados = []
    for p in ficheros():
        t = io.open(p, encoding='utf-8').read()
        c = campos(t)
        if c.get('updated') and c.get('updated') != c.get('last_modified_at'):
            nuevo = escribir(t, 'last_modified_at', c['updated'])
            if nuevo != t:
                io.open(p, 'w', encoding='utf-8', newline='').write(nuevo)
                tocados.append((os.path.relpath(p, RAIZ).replace('\\', '/'), c['updated']))
    print('sincronizados: %d' % len(tocados))
    for rel, f in tocados:
        print('  - %s -> last_modified_at: %s' % (rel, f))
    return 0


def tocar(ruta, fecha):
    """Marca un fichero como modificado hoy (o en la fecha que se le pase)."""
    p = ruta if os.path.isabs(ruta) else os.path.join(RAIZ, ruta)
    if not os.path.isfile(p):
        print('ERROR: no existe %s' % ruta)
        return 2
    nueva = fecha_valida(fecha)
    if nueva is None:
        print('ERROR: fecha invalida %s (formato YYYY-MM-DD)' % fecha)
        return 2
    t = io.open(p, encoding='utf-8').read()
    c = campos(t)
    anterior = fecha_valida(c.get('last_modified_at'))
    if anterior and anterior >= nueva:
        print('%s: se queda en %s (no se retrocede)' % (ruta, c['last_modified_at']))
        return 0
    io.open(p, 'w', encoding='utf-8', newline='').write(escribir(t, 'last_modified_at', fecha))
    print('%s -> last_modified_at: %s (antes: %s)'
          % (ruta, fecha, c.get('last_modified_at', 'sin campo')))
    return 0


def check(hoy):
    fallos, avisos = [], []
    lista = ficheros()
    for p in lista:
        rel = os.path.relpath(p, RAIZ).replace('\\', '/')
        c = campos(io.open(p, encoding='utf-8').read())
        u, lm, d = (fecha_valida(c.get('updated')), fecha_valida(c.get('last_modified_at')),
                    fecha_valida(c.get('date')))
        if lm and lm > hoy:
            fallos.append('last_modified_at futuro %s -> %s' % (rel, c['last_modified_at']))
        if u and u > hoy:
            fallos.append('updated futuro %s -> %s' % (rel, c['updated']))
        if lm and u and lm < u:
            fallos.append('last_modified_at (%s) anterior a updated (%s) en %s'
                          % (c['last_modified_at'], c['updated'], rel))
        if lm and d and lm < d:
            fallos.append('last_modified_at (%s) anterior a date (%s) en %s'
                          % (c['last_modified_at'], c['date'], rel))
        if u and not lm:
            avisos.append('%s tiene updated: %s y ningun last_modified_at' % (rel, c['updated']))
    print('%d ficheros revisados' % len(lista))
    if avisos:
        print('\nAVISOS (%d): estas URLs iran sin <lastmod> en sitemap.xml' % len(avisos))
        for a in avisos:
            print('  - %s' % a)
    if fallos:
        print('\nFALLOS (%d):' % len(fallos))
        for f in fallos:
            print('  - %s' % f)
        return 1
    print('\nOK: fechas de revision coherentes')
    return 0


def main():
    args = sys.argv[1:]
    hoy = datetime.date.today()
    modo = args[0] if args else '--check'
    if modo == '--sincronizar':
        return sincronizar()
    if modo == '--tocar':
        if len(args) < 2:
            print(__doc__)
            return 2
        return tocar(args[1], args[2] if len(args) > 2 else hoy.isoformat())
    if modo == '--check':
        return check(hoy)
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main())
