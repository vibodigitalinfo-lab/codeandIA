# -*- coding: utf-8 -*-
"""Recalcula la cadena de fechas del blog codeandIA.

Regla: el mas reciente tiene la fecha de HOY y los demas van hacia atras
un dia cada uno, formando una cadena contigua si falta. No toca _entrada.
Preserva CRLF (los archivos son CRLF).
"""
import glob
import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(r"C:\Users\ivanm\OneDrive\Documentos\codeandIA")
TODAY = date(2026, 9, 20)  # fecha de hoy
DIRS = ["articulos/guias", "articulos/reviews", "articulos/comparativas", "articulos/listas"]

# Recoger todos los articulos publicados con su fecha actual
entries = []  # (path, fecha_actual)
for d in DIRS:
    for p in glob.glob(str(ROOT / d / "*.md")):
        data = Path(p).read_bytes()
        m = re.search(rb"^date: (\d{4}-\d{2}-\d{2})", data, re.MULTILINE)
        if not m:
            print("SIN FECHA (se ignora):", p)
            continue
        entries.append((p, m.group(1).decode(), data))

n = len(entries)
entries.sort(key=lambda e: (e[1], Path(e[0]).name))  # por fecha actual, luego nombre

# Cadena contigua: el mas antiguo (indice 0) empieza en hoy-(n-1)
start = TODAY - timedelta(days=n - 1)
print("Articulos: %d" % n)
print("Rango: %s -> %s" % (start.isoformat(), TODAY.isoformat()))

changed = 0
for i, (p, old, data) in enumerate(entries):
    new_date = start + timedelta(days=i)
    new_s = new_date.isoformat()
    if old != new_s:
        new_data = re.sub(
            rb"^date: \d{4}-\d{2}-\d{2}",
            b"date: " + new_s.encode(),
            data,
            count=1,
            flags=re.MULTILINE,
        )
        Path(p).write_bytes(new_data)
        changed += 1
        print("CAMBIADO %s -> %s   %s" % (old, new_s, p))

print("Total de archivos con fecha modificada: %d de %d" % (changed, n))