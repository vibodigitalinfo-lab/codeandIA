"""Auditoria mecanica de todo el sitio: lo que un revisor sin navegador no puede ver.

No sustituye a mirar el diseno, pero cubre de forma exhaustiva (no muestreada)
lo que un crawler lee: metadatos, unicidad, grafo de enlaces internos,
redirecciones, JSON-LD y etiquetas sociales.

    python scripts/auditoria_completa.py

Salida: FAIL (roto), AVISO (revisar a mano) y el recuento de cada bloque.
"""
import glob
import json
import os
import re
import sys
import unicodedata

import yaml

from rutas import enlace_roto, rutas_validas

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORIAS = {"Gu" + chr(0xED) + "a", "Comparativa", "Lista", "Review"}
TITULO_MAX = 70
DESC_MIN, DESC_MAX = 70, 160

fail = []
aviso = []
info = []


def norm(s):
    """Minusculas sin tildes, para comparar titles que solo cambian en eso."""
    s = unicodedata.normalize("NFKD", str(s or ""))
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def leer(path):
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read()
    if not txt.startswith("---"):
        return None, txt
    partes = txt.split("---", 2)
    try:
        fm = yaml.safe_load(partes[1]) or {}
    except Exception as e:  # frontmatter invalido: es un FAIL, no una excepcion
        fail.append(f"{path}: frontmatter no parsea ({e})")
        return None, partes[2] if len(partes) > 2 else ""
    return fm, partes[2] if len(partes) > 2 else ""


def url_de(path, fm):
    if fm.get("permalink"):
        return str(fm["permalink"]).strip().rstrip("/") or "/"
    base = os.path.basename(path)
    if path.startswith(os.path.join(RAIZ, "articulos")):
        rel = os.path.relpath(path, os.path.join(RAIZ, "articulos"))
        rel = rel.replace("\\", "/")[:-3]  # quita .md
        return ("/articulos/" + rel).rstrip("/")
    if base.startswith("index."):
        return "/"
    return "/" + base.rsplit(".", 1)[0]


def main():
    art = {}
    paginas = {}
    for pat, destino in (
        (os.path.join(RAIZ, "articulos", "*", "*.md"), art),
        (os.path.join(RAIZ, "redirects", "*.md"), art),
        (os.path.join(RAIZ, "*.md"), paginas),
        (os.path.join(RAIZ, "*.html"), paginas),
    ):
        for p in sorted(glob.glob(pat)):
            if "_entrada" in os.path.normpath(p):
                continue
            fm, cuerpo = leer(p)
            if fm is None:
                continue
            rel = os.path.relpath(p, RAIZ).replace("\\", "/")
            destino[rel] = {"fm": fm, "cuerpo": cuerpo, "url": url_de(p, fm)}

    articulos = {k: v for k, v in art.items() if v["fm"].get("layout") != "redirect"}
    redirecciones = {k: v for k, v in art.items() if v["fm"].get("layout") == "redirect"}
    validas = rutas_validas(RAIZ)

    # ---- 1. metadatos de articulos
    for rel, d in sorted(articulos.items()):
        fm = d["fm"]
        t, desc = fm.get("title"), fm.get("description")
        if not t:
            fail.append(f"{rel}: sin title")
        elif len(t) > TITULO_MAX:
            aviso.append(f"{rel}: title de {len(t)} caracteres (max {TITULO_MAX})")
        if not desc:
            fail.append(f"{rel}: sin description")
        else:
            n = len(desc)
            if not (DESC_MIN <= n <= DESC_MAX):
                aviso.append(f"{rel}: description de {n} caracteres (fuera de {DESC_MIN}-{DESC_MAX})")
        cat = fm.get("category")
        if cat not in CATEGORIAS:
            fail.append(f"{rel}: category invalida {cat!r}")
        for campo in ("date", "readtime"):
            if not fm.get(campo):
                fail.append(f"{rel}: falta {campo}")
        if fm.get("updated") and not fm.get("last_modified_at"):
            fail.append(f"{rel}: updated sin last_modified_at")
        if "Sigue por aquí" not in d["cuerpo"] and "Sigue por aquí" not in desc_of(d):
            aviso.append(f"{rel}: sin bloque 'Sigue por aqui'")

    # ---- 2. unicidad de title y description
    for campo, limite in (("title", None), ("description", None)):
        visto = {}
        for rel, d in sorted(articulos.items()):
            v = d["fm"].get(campo)
            if not v:
                continue
            k = norm(v)
            visto.setdefault(k, []).append((rel, d["url"]))
        for k, grupo in sorted(visto.items()):
            if len(grupo) > 1:
                fail.append(f"{campo} duplicado ({len(grupo)}): " + " | ".join(r for r, _ in grupo))

    # ---- 3. titles/description duplicados entre si (mismo texto en los dos campos)
    for rel, d in sorted(articulos.items()):
        if d["fm"].get("title") and norm(d["fm"].get("title")) == norm(d["fm"].get("description")):
            aviso.append(f"{rel}: title y description son el mismo texto")

    # ---- 4. redirecciones
    for rel, d in sorted(redirecciones.items()):
        bruto = str(d["fm"].get("redirect_to", ""))
        destino = bruto.strip().rstrip("/") or "/"
        if not bruto:
            fail.append(f"{rel}: redireccion sin redirect_to")
        elif enlace_roto(destino, validas):
            fail.append(f"{rel}: apunta a {destino}, que no existe")
        if "//" in bruto.rstrip("/"):
            fail.append(f"{rel}: redirect_to con barra doble ({bruto})")
        if d["fm"].get("sitemap") is not False:
            aviso.append(f"{rel}: redireccion sin 'sitemap: false'")

    # ---- 5. grafo de enlaces internos y enlaces rotos
    LINK = re.compile(r"\]\((/[^)\s]*)\)")
    entradas = {}
    for rel, d in list(articulos.items()) + list(paginas.items()):
        entradas[d["url"]] = set(LINK.findall(d["cuerpo"]))

    for url, enlaces in sorted(entradas.items()):
        for link in sorted(enlaces):
            limpio = link.split("#")[0].split("?")[0].rstrip("/") or "/"
            if limpio.startswith("/assets") or limpio.startswith("/feed"):
                continue
            if enlace_roto(limpio, validas):
                fail.append(f"{url}: enlace interno roto {link}")

    enlazados = set()
    for origen, enlaces in entradas.items():
        for link in enlaces:
            enlazados.add(link.split("#")[0].split("?")[0].rstrip("/") or "/")
    # los hubs tambien cuentan como enlace entrante
    huerfanos = sorted(
        rel for rel, d in articulos.items()
        if d["url"] not in enlazados and d["url"] != "/"
    )
    if huerfanos:
        # no es un problema: las paginas de categoria enlazan con bucles Liquid y
        # aqui no se ven. El que vale es grafo_enlaces.py, contra produccion.
        info.append(
        "enlaces internos: %d huerfanos aparentes en fuente (usa grafo_enlaces.py "
        "para el grafo real)" % len(huerfanos)
    )

    # ---- 6. JSON-LD y etiquetas sociales en las plantillas
    with open(os.path.join(RAIZ, "_layouts", "default.html"), encoding="utf-8") as f:
        default = f.read()
    with open(os.path.join(RAIZ, "_layouts", "article.html"), encoding="utf-8") as f:
        layout_art = f.read()

    if "dateModified" not in layout_art:
        fail.append("article.html: el JSON-LD no declara dateModified")
    if 'property="article:modified_time"' not in default:
        aviso.append("default.html: falta la meta article:modified_time (si la hay en el JSON-LD)")
    if 'rel="canonical"' not in default:
        fail.append("default.html: falta canonical")
    for etiqueta in ("og:image", "og:title", "og:description", "og:url", "twitter:card"):
        if etiqueta not in default:
            fail.append(f"default.html: falta {etiqueta}")

    # los bloques JSON-LD tienen que cerrar llaves y corchetes
    for nombre, txt in (("default.html", default), ("article.html", layout_art)):
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', txt, re.S):
            bloque = m.group(1)
            limpio = re.sub(r"\{\{.*?\}\}", '"X"', bloque)
            limpio = re.sub(r"\{%.*?%\}", "1", limpio)
            try:
                json.loads(limpio.replace("\n", " "))
            except Exception:
                # con placeholders no tiene por qué ser JSON valido: solo avisos groseros
                if limpio.count("{") != limpio.count("}"):
                    aviso.append(f"{nombre}: bloque JSON-LD con llaves descompensadas")

    # ---- 7. paginas de servicio: metadatos minimos
    for rel, d in sorted(paginas.items()):
        fm = d["fm"]
        if not fm.get("title") and not rel.startswith("404"):
            aviso.append(f"{rel}: pagina sin title en frontmatter")
        if not fm.get("description") and not rel.startswith("404"):
            aviso.append(f"{rel}: pagina sin description")

    # ---- resumen
    print("=== 1. metadatos de los %d articulos" % len(articulos))
    print("=== 2. unicidad de title/description")
    print("=== 3. redirecciones: %d" % len(redirecciones))
    print("=== 4. grafo de enlaces internos: %d articulos, %d huerfanos" % (len(articulos), len(huerfanos)))
    print("=== 5. plantillas (JSON-LD, canonical, OG)")
    print("=== 6. paginas de servicio: %d" % len(paginas))
    print()
    for m in info:
        print("INFO:", m)
    for m in aviso:
        print("AVISO:", m)
    for m in fail:
        print("FAIL :", m)
    print()
    print("Fallos: %d | Avisos: %d" % (len(fail), len(aviso)))
    return 1 if fail else 0


def desc_of(d):
    return d["fm"].get("description") or ""


if __name__ == "__main__":
    sys.exit(main())