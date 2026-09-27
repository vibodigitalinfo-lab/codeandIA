import glob
import os
import re

site_pages = [
    '/', '/articulos', '/guias', '/comparativas', '/listas', '/reviews',
    '/cheatsheets', '/rutas', '/ofertas', '/sobre-mi', '/buscar',
    '/guardados', '/aviso-legal', '/privacidad'
]
urls = set(site_pages)

for p in glob.glob('articulos/**/*.md', recursive=True):
    if '_entrada' in p:
        continue
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'^permalink:\s*(.+)$', c, re.MULTILINE)
    if m:
        urls.add(m.group(1).strip().strip('\'\"').rstrip('/'))
    else:
        rel = os.path.relpath(p, 'articulos').replace('\\', '/')
        slug = rel.replace('.md', '')
        urls.add(f'/articulos/{slug}')

broken = []
for p in glob.glob('articulos/**/*.md', recursive=True):
    if '_entrada' in p:
        continue
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    for link in re.findall(r'\]\((/[^\)\s#]*)', c):
        t = link.rstrip('/') or '/'
        if t not in urls and not t.startswith('/assets') and not t.startswith('/feed'):
            broken.append((p, link))

# Tambien en HTML de paginas y layouts
for h in glob.glob('*.html') + glob.glob('_layouts/*.html') + glob.glob('_includes/*.html') + ['promociones.md']:
    with open(h, 'r', encoding='utf-8') as f:
        c = f.read()
    for link in re.findall(r'href=[\"\'](/[^\"\'\s#{%]+)', c):
        t = link.rstrip('/') or '/'
        if t not in urls and not t.startswith('/assets') and not t.startswith('/feed'):
            broken.append((h, link))

print(f"Total urls validas: {len(urls)}")
print(f"Total enlaces rotos detectados: {len(broken)}")
for b in broken:
    print(f"  {b[0]} -> {b[1]}")


