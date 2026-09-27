"""Pistas para el enlazado interno: catalogo de articulos y lineas enlazables.

Uso:
    python scripts/pistas_enlaces.py --catalogo
    python scripts/pistas_enlaces.py articulos/guias/x.md [mas.md ...]

El modo fichero imprime los encabezados y las lineas que mencionan herramientas
o tecnologias pero que todavia no llevan ningun enlace, que es donde se puede
meter un enlace interno sin forzar el texto.
"""
import glob
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAVES = (
    'Cursor', 'Copilot', 'ChatGPT', 'Claude', 'Gemini', 'DeepSeek', 'Ollama', 'LM Studio',
    'VS Code', 'VSCode', 'JetBrains', 'IntelliJ', 'NeoVim', 'Warp', 'Zed', 'Trae', 'Windsurf',
    'Docker', 'SQL', 'Postgres', 'MySQL', 'SQLite', 'Supabase', 'Stripe',
    'React', 'Vue', 'Next', 'Vite', 'Astro', 'Tailwind', 'TypeScript', 'JavaScript',
    'Java', 'Spring', 'Python', 'Node', 'npm', 'Git', 'GitHub', 'Actions', 'API', 'REST',
    'MCP', 'prompt', 'monitor', 'teclado', 'raton', 'ratón', 'silla', 'portatil', 'portátil',
    'dominio', 'hosting', 'despliegue', 'portafolio', 'portfolio', 'README', 'apuntes',
    'examen', 'DAW', 'WSL', 'Mac', 'Windows', 'terminal', 'accesibilidad', 'RAG', 'test',
    'debug', 'refactor', 'productividad', 'asignatura', 'practicas', 'prácticas',
)


def articulos():
    for p in sorted(glob.glob(os.path.join(RAIZ, 'articulos', '*', '*.md'))):
        if '_entrada' in p:
            continue
        yield p


def titulo(texto):
    m = re.search(r'^title:\s*(.+)$', texto, re.M)
    return m.group(1).strip().strip('"') if m else '(sin titulo)'


def catalogo():
    filas = []
    for p in articulos():
        t = io.open(p, encoding='utf-8').read()
        rel = os.path.relpath(p, RAIZ).replace('\\', '/')
        cat = rel.split('/')[1]
        filas.append((cat, rel[rel.rfind('/') + 1:-3], titulo(t)))
    for cat, slug, tit in sorted(filas):
        print('%-14s %-58s %s' % (cat, slug, tit))
    print('\n%d articulos' % len(filas))


def pistas(rutas):
    for ruta in rutas:
        p = ruta if os.path.isabs(ruta) else os.path.join(RAIZ, ruta)
        if not os.path.isfile(p):
            print('ERROR: no existe %s' % ruta)
            continue
        print('=' * 78)
        print(ruta)
        for i, l in enumerate(io.open(p, encoding='utf-8').read().split('\n'), 1):
            if l.startswith('#') or l.startswith('Sigue por aqu'):
                print('  %4d %s' % (i, l[:110]))
            elif any(k in l for k in CLAVES) and '](/' not in l and len(l) > 70:
                print('    *%4d %s' % (i, l[:165]))


def main():
    args = sys.argv[1:]
    if not args or args[0] == '--catalogo':
        catalogo()
        return 0
    pistas(args)
    return 0


if __name__ == '__main__':
    sys.exit(main())
