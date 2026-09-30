"""Verificación integral de calidad de codeandIA según AGENTS.md

Comprueba:
1. Fechas: sin futuras, sin repetidas, sin huecos de más de 3 días (fechas_check.py)
2. Fechas de revisión: coherentes con last_modified_at (marcar_actualizado.py --check)
3. Enlaces internos: sin 404 ni rutas inexistentes
4. Frontmatter YAML válido en todos los artículos
5. Categorías exactas: "Guía", "Comparativa", "Lista", "Review"
6. Título <= 70 car, descripción entre 70 y 160 car
7. Sin caracteres CJK/cirílico/árabe/hebreo
8. Liquid dentro de bloques de código protegido con {% raw %}
9. Cierre con bloque "Sigue por aquí"
10. _config.yml parsea correctamente
"""
import glob
import os
import re
import sys
import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def error(msg):
    print(f"  [ERROR] {msg}")

def advertencia(msg):
    print(f"  [AVISO] {msg}")

def verificar():
    fallos = 0
    avisos = 0

    print("=== 1. Comprobando _config.yml ===")
    cfg_path = os.path.join(RAIZ, "_config.yml")
    try:
        with open(cfg_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        if not isinstance(cfg, dict):
            error("_config.yml no es un diccionario YAML válido")
            fallos += 1
        else:
            print("  _config.yml parseado OK")
    except Exception as e:
        error(f"Error parseando _config.yml: {e}")
        fallos += 1

    print("\n=== 2. Comprobando artículos y reglas editoriales ===")
    articulos = sorted(glob.glob(os.path.join(RAIZ, "articulos", "*", "*.md")))
    articulos_validos = [p for p in articulos if "_entrada" not in p]

    # Recopilar URLs válidas para enlaces
    site_pages = [
        '/', '/articulos', '/guias', '/comparativas', '/listas', '/reviews',
        '/cheatsheets', '/rutas', '/ofertas', '/sobre-mi', '/buscar',
        '/guardados', '/aviso-legal', '/privacidad'
    ]
    urls = set(site_pages)
    for p in articulos_validos:
        rel = os.path.relpath(p, os.path.join(RAIZ, "articulos")).replace("\\", "/")
        slug = rel.replace(".md", "")
        urls.add(f"/articulos/{slug}")

    categorias_validas = {"Guía", "Comparativa", "Lista", "Review"}

    for p in articulos_validos:
        rel = os.path.relpath(p, RAIZ).replace("\\", "/")
        with open(p, "r", encoding="utf-8") as f:
            contenido = f.read()

        # CJK / Cirílico / Árabe / Hebreo
        cjk = re.findall(r'[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af\u0400-\u04ff\u0600-\u06ff\u0590-\u05ff]', contenido)
        if cjk:
            error(f"{rel}: contiene caracteres prohibidos: {''.join(cjk[:10])}")
            fallos += 1

        # Frontmatter
        if not contenido.startswith("---"):
            error(f"{rel}: no empieza con ---")
            fallos += 1
            continue

        partes = contenido.split("---", 2)
        if len(partes) < 3:
            error(f"{rel}: frontmatter incompleto")
            fallos += 1
            continue

        try:
            fm = yaml.safe_load(partes[1])
        except Exception as e:
            error(f"{rel}: error al parsear YAML: {e}")
            fallos += 1
            continue

        titulo = fm.get("title", "")
        desc = fm.get("description", "")
        cat = fm.get("category", "")

        if len(titulo) > 70:
            error(f"{rel}: título > 70 caracteres ({len(titulo)}): '{titulo}'")
            fallos += 1
        elif len(titulo) == 0:
            error(f"{rel}: título vacío")
            fallos += 1

        if len(desc) < 70 or len(desc) > 160:
            advertencia(f"{rel}: descripción fuera del rango [70, 160] ({len(desc)}): '{desc}'")
            avisos += 1

        if cat not in categorias_validas:
            error(f"{rel}: categoría inválida '{cat}'. Debe ser una de {categorias_validas}")
            fallos += 1

        # Comprobar H1 en el cuerpo
        cuerpo = partes[2]
        # Quitar bloques de código antes de buscar H1
        sin_codigo = re.sub(r'```.*?```', '', cuerpo, flags=re.DOTALL)
        sin_codigo = re.sub(r'`[^`\n]+`', '', sin_codigo)
        h1s = [l for l in sin_codigo.splitlines() if l.startswith("# ")]
        if h1s:
            error(f"{rel}: contiene H1 en el cuerpo: {h1s}")
            fallos += 1

        # Liquid desprotegido en bloques de código
        sin_raw = re.sub(r'\{% raw %\}.*?\{% endraw %\}', '', cuerpo, flags=re.DOTALL)
        bloques_codigo = re.findall(r'```.*?```', sin_raw, flags=re.DOTALL)
        for bc in bloques_codigo:
            if "{{" in bc or "{%" in bc:
                error(f"{rel}: Liquid sin raw dentro de bloque de código: {bc[:60]}...")
                fallos += 1

        # Enlaces internos rotos
        enlaces = re.findall(r'\]\((/[^\)\s#]*)', cuerpo)
        for link in enlaces:
            t = link.rstrip("/") or "/"
            if t not in urls and not t.startswith("/assets") and not t.startswith("/feed"):
                error(f"{rel}: enlace roto a '{link}'")
                fallos += 1

        # Cierre "Sigue por aquí"
        if "Sigue por aqu" not in cuerpo:
            advertencia(f"{rel}: no contiene bloque 'Sigue por aquí'")
            avisos += 1

    print(f"  {len(articulos_validos)} artículos analizados.")

    print("\n=== 3. Comprobando fechas del calendario (fechas_check.py) ===")
    import subprocess
    r_fc = subprocess.run([sys.executable, os.path.join(RAIZ, "fechas_check.py")])
    if r_fc.returncode != 0:
        error("fechas_check.py falló")
        fallos += 1

    print("\n=== 4. Comprobando coherencia de updated y last_modified_at ===")
    r_ma = subprocess.run([sys.executable, os.path.join(RAIZ, "scripts", "marcar_actualizado.py"), "--check"])
    if r_ma.returncode != 0:
        error("marcar_actualizado.py --check falló")
        fallos += 1

    print("\n=== Resumen ===")
    print(f"Fallos detectados: {fallos}")
    print(f"Avisos detectados: {avisos}")
    return 0 if fallos == 0 else 1

if __name__ == "__main__":
    sys.exit(verificar())
