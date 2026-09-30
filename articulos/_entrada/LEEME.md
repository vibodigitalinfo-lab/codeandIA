# 📥 Bandeja de entrada de artículos

Esta carpeta es **solo para dejar artículos nuevos pendientes de publicar**.

## Cómo usarla

1. **Deja aquí el archivo `.md`** con tu artículo nuevo (con su portada/frontmatter).
2. Avísame y **yo me encargo del resto**: lo moveré a la carpeta que le corresponde según su categoría, le asignaré la fecha correcta, quitaré el `# H1` duplicado si lo tiene y haré el commit + push.

## ⏱️ La regla de las fechas (importante)

**Se suben 2 o 3 por semana. El sitio se ve como una publicación casi diaria.**

Las fechas se reparten hacia atrás, así que nunca hay dos artículos el mismo día:

- Todos los artículos se publican. No se queda ninguno en `_entrada/` por falta de fecha.
- La tanda se numera hacia atrás desde hoy: el primero lleva la fecha de hoy, el resto
  fechas de días anteriores, dejando huecos de 1 a 3 días entre ellos.
- La más reciente nunca puede quedar a más de 3 días de hoy, ni `date:` pasar de hoy.
- Cada vez que subes 2 o 3, el **inicio del archivo se retrasa** esos mismos días. Por eso
  el rango de fechas se va haciendo más largo hacia atrás.

Resultado: desde fuera parece una publicación continua y el rango no se acaba nunca.

**Ejemplo.** Si hoy es el 30-sep y subes 3 artículos: el primero queda el 30-sep, el
segundo el 28-sep y el tercero el 25-sep. Quedan huecos de 2 y 3 días, que es lo normal
con esta cadencia, y el archivo sigue sin fecha repetida ni huecos de más de 3 días.

**Comprobación:** `python fechas_check.py` avisa de fechas futuras, repetidas, sin
artículo reciente o con huecos de más de 3 días antes de commitear.

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