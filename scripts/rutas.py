"""Rutas internas v\u00e1lidas del sitio, derivadas de los ficheros reales.

La lista de URLs viv\u00eda escrita a mano en los scripts de auditor\u00eda y se qued\u00f3
obsoleta: `/hosting/` daba falsos positivos en seis art\u00edculos porque el hub
existe (hosting.html, permalink /hosting/) pero no estaba en la lista. Ahora se
lee el frontmatter de todo lo que Jekyll publica, as\u00ed que a\u00f1adir una p\u00e1gina o
un art\u00edculo no obliga a tocar ning\u00fan script.
"""
import glob
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PERMALINK = re.compile(r"^permalink:\s*(.+)$", re.MULTILINE)


def _normalizar(url):
    return url.strip().strip("'\"").rstrip("/") or "/"


def _paginas(raiz):
    """URLs de las p\u00e1ginas de la ra\u00edz (los .html y .md con frontmatter)."""
    urls = set()
    for p in glob.glob(os.path.join(raiz, "*.html")) + glob.glob(os.path.join(raiz, "*.md")):
        with open(p, "r", encoding="utf-8") as f:
            contenido = f.read()
        if not contenido.startswith("---"):
            continue
        m = PERMALINK.search(contenido.split("---", 2)[1])
        if m:
            urls.add(_normalizar(m.group(1)))
        elif os.path.basename(p).startswith("index."):
            urls.add("/")
    return urls


def _articulos(raiz):
    """URLs de los art\u00edculos publicados en articulos/<categor\u00eda>/."""
    urls = set()
    patron = os.path.join(raiz, "articulos", "*", "*.md")
    for p in glob.glob(patron):
        if "_entrada" in os.path.normpath(p):
            continue
        with open(p, "r", encoding="utf-8") as f:
            contenido = f.read()
        m = PERMALINK.search(contenido)
        if m:
            urls.add(_normalizar(m.group(1)))
            continue
        rel = os.path.relpath(p, os.path.join(raiz, "articulos")).replace("\\", "/")
        urls.add(_normalizar("/articulos/" + rel.replace(".md", "")))
    return urls


def rutas_validas(raiz=RAIZ):
    """Conjunto de URLs internas v\u00e1lidas, sin barra final (salvo la ra\u00edz)."""
    return _paginas(raiz) | _articulos(raiz)


def enlace_roto(link, urls):
    """True si un enlace interno apunta a una ruta que no existe."""
    t = link.rstrip("/") or "/"
    return t not in urls and not t.startswith("/assets") and not t.startswith("/feed")