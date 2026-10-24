"""Descarga datos de Google Search Console a _informes/gsc/ (fuera de git).

Usa una cuenta de servicio con permiso de solo lectura en la propiedad de
Search Console. La clave JSON vive FUERA del repo; nunca dentro.

Uso:
    python scripts/gsc_datos.py              # ultimos 28 dias
    python scripts/gsc_datos.py 90           # ultimos 90 dias
    python scripts/gsc_datos.py --sitios     # lista las propiedades accesibles

Clave: variable GSC_CLAVE o, por defecto, ~/.secrets/gsc.json.
Propiedad: variable GSC_SITIO o, por defecto, la primera de codeandia.com que
encuentre (sc-domain:codeandia.com o https://codeandia.com/).

Salida en _informes/gsc/<hoy>/: consultas.csv, paginas.csv, paises.csv,
dias.csv, consulta_pagina.csv y resumen.txt (este periodo frente al anterior).
"""
import csv
import datetime
import os
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAVE = os.environ.get('GSC_CLAVE',
                       os.path.join(os.path.expanduser('~'), '.secrets', 'gsc.json'))
ALCANCE = ['https://www.googleapis.com/auth/webmasters.readonly']
# Search Console tarda 2-3 dias en consolidar los datos.
RETRASO = 3


def servicio():
    if not os.path.isfile(CLAVE):
        sys.exit('No encuentro la clave en %s (o define GSC_CLAVE).' % CLAVE)
    if os.path.abspath(CLAVE).startswith(RAIZ):
        sys.exit('La clave esta dentro del repo: muevela fuera antes de seguir.')
    cred = service_account.Credentials.from_service_account_file(CLAVE, scopes=ALCANCE)
    return build('searchconsole', 'v1', credentials=cred, cache_discovery=False)


def sitios(sc):
    return [s['siteUrl'] for s in sc.sites().list().execute().get('siteEntry', [])]


def elegir_sitio(sc):
    if os.environ.get('GSC_SITIO'):
        return os.environ['GSC_SITIO']
    disponibles = sitios(sc)
    for s in ('sc-domain:codeandia.com', 'https://codeandia.com/'):
        if s in disponibles:
            return s
    sys.exit('La cuenta de servicio no ve codeandia.com. Propiedades visibles: %s\n'
             'Anade su email en Search Console > Configuracion > Usuarios y permisos.'
             % (disponibles or 'ninguna'))


def consulta(sc, sitio, inicio, fin, dims, filas=25000):
    cuerpo = {'startDate': inicio.isoformat(), 'endDate': fin.isoformat(),
              'dimensions': dims, 'rowLimit': filas}
    r = sc.searchanalytics().query(siteUrl=sitio, body=cuerpo).execute()
    return r.get('rows', [])


def guardar(ruta, dims, filas):
    with open(ruta, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(dims + ['clics', 'impresiones', 'ctr', 'posicion'])
        for r in filas:
            w.writerow(r['keys'] + [r['clicks'], r['impressions'],
                                    round(r['ctr'] * 100, 2), round(r['position'], 1)])


def totales(filas):
    c = sum(r['clicks'] for r in filas)
    i = sum(r['impressions'] for r in filas)
    return c, i, (c / i * 100 if i else 0)


def main():
    args = sys.argv[1:]
    sc = servicio()
    if '--sitios' in args:
        print('\n'.join(sitios(sc)) or 'ninguna propiedad visible')
        return
    dias = int(args[0]) if args else 28
    sitio = elegir_sitio(sc)
    fin = datetime.date.today() - datetime.timedelta(days=RETRASO)
    inicio = fin - datetime.timedelta(days=dias - 1)
    ant_fin = inicio - datetime.timedelta(days=1)
    ant_inicio = ant_fin - datetime.timedelta(days=dias - 1)

    salida = os.path.join(RAIZ, '_informes', 'gsc', datetime.date.today().isoformat())
    os.makedirs(salida, exist_ok=True)

    informes = {
        'consultas': ['query'],
        'paginas': ['page'],
        'paises': ['country'],
        'dias': ['date'],
        'consulta_pagina': ['query', 'page'],
    }
    for nombre, dims in informes.items():
        guardar(os.path.join(salida, nombre + '.csv'), dims,
                consulta(sc, sitio, inicio, fin, dims))

    actual = consulta(sc, sitio, inicio, fin, ['date'])
    anterior = consulta(sc, sitio, ant_inicio, ant_fin, ['date'])
    ca, ia, ctra = totales(actual)
    cp, ip, ctrp = totales(anterior)
    resumen = (
        'Propiedad: %s\n'
        'Periodo:   %s .. %s (%d dias)\n'
        'Anterior:  %s .. %s\n\n'
        '            actual   anterior\n'
        'Clics       %6d   %8d\n'
        'Impresiones %6d   %8d\n'
        'CTR         %5.2f%%   %7.2f%%\n'
        % (sitio, inicio, fin, dias, ant_inicio, ant_fin, ca, cp, ia, ip, ctra, ctrp))
    with open(os.path.join(salida, 'resumen.txt'), 'w', encoding='utf-8') as f:
        f.write(resumen)
    print(resumen)
    print('CSV en %s' % os.path.relpath(salida, RAIZ))


if __name__ == '__main__':
    main()
