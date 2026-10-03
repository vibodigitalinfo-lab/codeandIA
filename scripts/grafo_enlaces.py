"""Grafo de enlaces reales contra produccion.

La comprobacion de huerfanos sobre el codigo no sirve: las paginas de categoria
enlazan a todos los articulos con bucles Liquid, asi que un articulo puede no
tener ni un solo enlace escrito a mano y aun asi estar enlazado. Esto descarga
las paginas de verdad y cuenta de donde llega cada URL.

    python scripts/grafo_enlaces.py [dominio]

Un articuto esta huerfano si ningun OTRO articulo lo enlaza, ni ninguna pagina
hub que no sea la suya. Eso es lo que ve un crawler al recorrer el sitio.
"""
import concurrent.futures as cf
import os
import re
import sys
from collections import defaultdict
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = sys.argv[1] if len(sys.argv) > 1 else "https://codeandia.com"

UA = {"User-Agent": "codeandIA-auditoria/1.0 (enlace interno)"}

LISTADO = re.compile(r'<article[^>]*\shref="(/articulos/[^"]+)"', re.I)
HREF = re.compile(r'href="(/[^"#?]*)"')
SITEMAP = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>")


def descargar(url):
    try:
        req = Request(url, headers=UA)
        with urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as e:
        print("  ! %s -> %s" % (url, e))
        return ""


def norm(u):
    u = urlsplit(u).path
    return u.rstrip("/") or "/"


def main():
    print("sitemap:", DOMINIO + "/sitemap.xml")
    sm = descargar(DOMINIO + "/sitemap.xml")
    urls = [norm(u) for u in SITEMAP.findall(sm)]
    articulos = sorted(u for u in urls if u.startswith("/articulos/"))
    hubs = sorted(
        u for u in urls
        if not u.startswith("/articulos/")
    )
    print("URLs en el sitemap: %d (%d articulos, %d paginas)" % (len(urls), len(articulos), len(hubs)))

    todas = articulos + hubs
    with cf.ThreadPoolExecutor(max_workers=8) as pool:
        htmls = dict(zip(todas, pool.map(descargar, [DOMINIO + u for u in todas])))

    # enlaces por pagina: los href de las tarjetas de articulo y los href de ahi
    salidas = {}
    for u, h in htmls.items():
        enlaces = set(norm(x) for x in HREF.findall(h))
        tarjetas = set(norm(x) for x in LISTADO.findall(h))
        salidas[u] = enlaces | tarjetas

    # categoria a la que pertenece cada articulo, para no contar su propio listado
    cat_de = {}
    for h, u in [("/guias/", "guias"), ("/listas/", "listas"),
                 ("/reviews/", "reviews"), ("/comparativas/", "comparativas")]:
        for a in sorted(x for x in articulos if f"/articulos/{u}/" in x):
            cat_de[a] = h
        for a in sorted(x for x in articulos if f"/articulos/{u}/" in x):
            cat_de.setdefault(a, h)

    entradas = defaultdict(set)
    for origen, enlaces in salidas.items():
        for destino in enlaces:
            entradas[destino].add(origen)

    print()
    huerfanos = []
    for a in articulos:
        origenes = {o for o in entradas.get(a, set()) if o != a and o != cat_de.get(a)}
        if not origenes:
            huerfanos.append(a)

    print("=== articulos SIN inlinks (ni desde articulos ni desde hubs, excluido su listado)")
    if not huerfanos:
        print("ninguno")
    for a in huerfanos:
        print("  " + a)

    print()
    print("=== articulos enlazados solo por su pagina de categoria (inlinks debiles)")
    debiles = [a for a in articulos
               if not huerfanos_or(a, huerfanos, set(entradas.get(a, set())), cat_de)]
    for a in debiles:
        print("  " + a + "  <- " + ", ".join(sorted(entradas.get(a, set()))[:3]))
    if not debiles:
        print("ninguno")

    # enlaces rotos reales: el sitemap no lista assets ni las paginas con
    # sitemap: false, asi que se anaden a mano (mismo criterio que AGENTS.md)
    ESTATICOS = ("/assets", "/styles.css", "/favicon", "/apple-touch-icon",
                 "/feed", "/buscar", "/guardados", "/sitemap.xml")
    validas = set(urls) | {"/"}
    rotos = set()
    for origen, enlaces in salidas.items():
        for e in enlaces:
            if e.startswith(ESTATICOS) or e.endswith(
                (".css", ".js", ".svg", ".png", ".jpg", ".jpeg", ".gif",
                 ".ico", ".xml", ".webmanifest", ".txt")
            ):
                continue
            if e not in validas:
                rotos.add((origen, e))
    print()
    print("=== enlaces internos rotos (todas las paginas del sitemap)")
    if not rotos:
        print("ninguno")
    for o, e in sorted(rotos):
        print("  %s -> %s" % (o, e))


def huerfanos_or(a, huerfanos, origenes, cat_de):
    """True si el articulo NO esta en la lista de huerfanos (para la segunda lista)."""
    return a not in huerfanos


if __name__ == "__main__":
    main()