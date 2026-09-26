# 📥 Bandeja de entrada de artículos

Esta carpeta es **solo para dejar artículos nuevos pendientes de publicar**.

## Cómo usarla

1. **Deja aquí el archivo `.md`** con tu artículo nuevo (con su portada/frontmatter).
2. Avísame y **yo me encargo del resto**: lo moveré a la carpeta que le corresponde según su categoría, le asignaré la fecha correcta, quitaré el `# H1` duplicado si lo tiene y haré el commit + push.

## ⏱️ La regla de las fechas (importante)

**Un artículo por día. Nunca dos con la misma fecha. Nunca una fecha futura.**

- Cada artículo lleva `date:` con un día distinto. Aunque se publiquen varios en la misma sesión.
- `date:` nunca puede pasar de hoy. Un artículo con fecha de mañana es un artículo que todavía no existe.
- Si escribes varios y no quedan días libres hasta hoy, **solo se publica el primero**: el resto se queda aquí en `_entrada/` con su `date:` provisional, y se van sacando uno a uno en días distintos.
- La fecha de un borrador no cuenta como fecha de publicación. Al mover el archivo fuera de `_entrada/` se le pone el día real.

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