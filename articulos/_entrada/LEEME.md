# 📥 Bandeja de entrada de artículos

Esta carpeta es **solo para dejar artículos nuevos pendientes de publicar**.

## Cómo usarla

1. **Deja aquí el archivo `.md`** con tu artículo nuevo (con su portada/frontmatter).
2. Avísame y **yo me encargo del resto**: lo moveré a la carpeta que le corresponde según su categoría, ajustaré las fechas (para que el de hoy sea siempre el último), quitaré el `# H1` duplicado si lo tiene y haré el commit + push.

## Por qué existe esta carpeta

- El nombre empieza por `_` → **Jekyll la ignora**, así que nada de lo que dejes aquí se publica ni se indexa por accidente. Estás a salvo de publicar un borrador sin querer.
- Mantiene la raíz de `articulos/` limpia con solo 4 carpetas ordenadas.

## Estructura de articulos/

- `reviews/` → categoría **Review** (herramienta analizada a fondo)
- `comparativas/` → categoría **Comparativa** (Herramienta A vs B)
- `guias/` → categoría **Guía** (paso a paso / tutorial)
- `listas/` → categoría **Lista** (mejores X / N herramientas)
- `_entrada/` → **aquí dejas los artículos nuevos** 🙌

## Notas

- Cada artículo debe llevar su frontmatter con `layout: article`, `title`, `description`, `category`, `date` y, si quieres, los campos de afiliado `affiliate_text` / `affiliate_url` / `affiliate_label` y `readtime`.
- No hace falta que me des la URL de salida: el permalink se genera solo como `/articulos/nombre-del-archivo/`.