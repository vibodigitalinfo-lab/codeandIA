# 📥 Bandeja de entrada de artículos

Esta carpeta es **solo para dejar artículos nuevos pendientes de publicar**.

## Cómo usarla

1. **Deja aquí el archivo `.md`** con tu artículo nuevo (con su portada/frontmatter).
2. Avísame y **yo me encargo del resto**: lo moveré a la carpeta que le corresponde según su categoría, le asignaré la fecha correcta, quitaré el `# H1` duplicado si lo tiene y haré el commit + push.

## ⏱️ La regla de las fechas (actualizada el 2026-10-25)

**1 o 2 artículos por semana (lunes a domingo), con la fecha real del día en que se publican.**

- Lo que dejes aquí **espera su turno**. No se publica todo de golpe.
- Días orientativos: **martes y viernes**. Nunca 3 en la misma semana ni, si se puede evitar, dos días seguidos.
- Al publicar, `date:` es **ese día**: ni hacia atrás ni en el futuro (una fecha futura hace que Jekyll no publique el artículo).
- Si hay cola, sale una pieza por hueco en las semanas siguientes.

## 🤖 Publicación automática

Para que un artículo se publique solo, añade a su portada `publicar: AAAA-MM-DD` (el día previsto, idealmente martes o viernes).

- Cada mañana el workflow **Publicar programados** publica como mucho **uno**: el más antiguo cuya fecha `publicar` ya ha llegado.
- Si ese día rompe la cadencia (ayer ya se publicó, o ya van 2 esa semana), **espera** al siguiente día libre. Una fecha mal puesta solo retrasa la pieza; nunca la adelanta ni rompe la regla.
- Lo mueve a su carpeta según `category`, pone `date` y `last_modified_at` a ese día y quita `publicar`.
- **Sin `publicar` no se publica nunca.** Así los borradores y las piezas en pausa están a salvo.
- Calendario previsto: `python scripts/publicar_programados.py --plan`.

**Comprobación:** `python fechas_check.py` falla con fechas futuras, repetidas o 3+ en una semana, y avisa de días seguidos o de más de 10 días sin publicar.

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