"""Articulos publicados en los ultimos dias, para armar la edicion semanal.

La newsletter sale los jueves por la tarde (ver AGENTS.md -> Newsletter semanal).
Este script lista lo publicado en la ventana, con fecha, categoria y URL, para no
dejarse ninguna pieza al redactar la edicion.

Uso:
    python scripts/newsletter_semana.py          # ultima semana (7 dias)
    python scripts/newsletter_semana.py 10       # ultimos 10 dias
"""
import datetime
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(RAIZ, 'articulos')


def campo(fm, nombre):
    m = re.search(r'^%s:\s*"?(.*?)"?\s*$' % nombre, fm, re.M)
    return m.group(1) if m else ''


def articulos():
    """Articulos publicados (sin _entrada) con su fecha, titulo, categoria y URL."""
    salida = []
    for root, dirs, files in os.walk(ART):
        dirs[:] = [d for d in dirs if d != '_entrada']
        for f in sorted(files):
            if not f.endswith('.md'):
                continue
            p = os.path.join(root, f)
            t = io.open(p, encoding='utf-8', errors='replace').read()
            if not t.startswith('---'):
                continue
            nl = '\r\n' if '\r\n' in t else '\n'
            fin = t.find(nl + '---', 3)
            if fin == -1:
                continue
            fm = t[3:fin]
            if re.search(r'^layout:\s*redirect', fm, re.M):
                continue
            rel = os.path.relpath(p, RAIZ).replace('\\', '/')
            partes = rel.split('/')
            url = '/articulos/%s/%s/' % (partes[1], os.path.splitext(partes[2])[0])
            salida.append({
                'date': campo(fm, 'date'),
                'title': campo(fm, 'title'),
                'cat': campo(fm, 'category'),
                'url': url,
            })
    return salida


def main():
    args = sys.argv[1:]
    dias = 7
    if args and args[0].isdigit():
        dias = int(args[0])
    hoy = datetime.date.today()
    desde = hoy - datetime.timedelta(days=dias)
    filas = []
    for a in articulos():
        try:
            d = datetime.date(*map(int, a['date'].split('-')))
        except (ValueError, TypeError):
            continue
        if desde <= d <= hoy:
            filas.append((d, a))
    filas.sort(reverse=True)
    print('Ventana: %s .. %s (%d dias) | %d articulos'
          % (desde.isoformat(), hoy.isoformat(), dias, len(filas)))
    for d, a in filas:
        print('\n[%s] %s (%s)' % (d.isoformat(), a['title'], a['cat']))
        print('  https://codeandia.com%s' % a['url'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
