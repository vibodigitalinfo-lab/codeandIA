import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rutas import rutas_validas, enlace_roto

urls = rutas_validas()

broken = []
for p in glob.glob('articulos/**/*.md', recursive=True):
    if '_entrada' in p:
        continue
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    for link in re.findall(r'\]\((/[^\)\s#]*)', c):
        if enlace_roto(link, urls):
            broken.append((p, link))

# Tambien en HTML de paginas y layouts
for h in glob.glob('*.html') + glob.glob('_layouts/*.html') + glob.glob('_includes/*.html') + ['promociones.md']:
    with open(h, 'r', encoding='utf-8') as f:
        c = f.read()
    for link in re.findall(r'href=[\"\'](/[^\"\'\s#{%]+)', c):
        if enlace_roto(link, urls):
            broken.append((h, link))

print(f"Total urls validas: {len(urls)}")
print(f"Total enlaces rotos detectados: {len(broken)}")
for b in broken:
    print(f"  {b[0]} -> {b[1]}")


