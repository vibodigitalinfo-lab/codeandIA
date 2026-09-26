# 📥 Bandeja de entrada de artículos

Esta carpeta es **solo para dejar artículos nuevos pendientes de publicar**.

## Cómo usarla

1. **Deja aquí el archivo `.md`** con tu artículo nuevo (con su portada/frontmatter).
2. Avísame y **yo me encargo del resto**: lo moveré a la carpeta que le corresponde según su categoría, le asignaré la fecha correcta, quitaré el `# H1` duplicado si lo tiene y haré el commit + push.

## ⏱️ La regla de las fechas (importante)

**Se suben 4 o 5 al día. El archivo se ve como uno al día.**

Las fechas se reparten hacia atrás, así que nunca hay dos artículos el mismo día ni huecos:

- Todos los artículos se publican. No se queda ninguno en `_entrada/` por falta de fecha.
- La tanda del día se numera hacia atrás desde hoy: el primero lleva la fecha de hoy, el siguiente la de ayer, y así hasta el primero del archivo.
- Cada vez que subes 4 o 5, el **inicio del archivo se retrasa** los mismos días. Por eso el rango de fechas se va haciendo más largo hacia atrás.
- `date:` nunca puede pasar de hoy. Nunca hay dos artículos con la misma fecha.

Resultado: desde fuera parece que publicas un artículo al día, sin huecos, y el rango no se acaba nunca.

**Ejemplo.** Si hoy es el 26-sep y subes 4 artículos, y el archivo llegaba hasta el 23-sep: el primero queda el 26-sep, el segundo el 25, el tercero el 24 y el cuarto el 23. El archivo pasa a empezar 3 días antes y sigue sin huecos.

**Comprobación:** `python fechas_check.py` avisa de fechas futuras, repetidas o huecos antes de commitear.

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