---
layout: article
title: "Tailwind con IA: cómo evitar 40 clases en un div"
description: "Cómo usar IA con Tailwind sin acabar con un div de 40 clases: los 3 patrones que siempre genera mal, los prompts que los evitan y cómo refactorizar."
category: "Guía"
# PROVISIONAL: no es fecha de publicacion. Se cambia al mover el archivo
# fuera de _entrada/, a un dia libre y nunca posterior a hoy.
date: 2026-09-26
readtime: 9
---

Tailwind con IA tiene un problema que no tiene con otros temas: el resultado **parece** correcto. La interfaz se ve bien, las clases están todas, el CSS no tiene ni una línea. Todo pasa las revisiones. Y luego abres el `div` del botón y hay esto:

```html
<a class="inline-flex items-center justify-center gap-2 rounded-lg bg-blue-600 px-6 py-3 text-base font-semibold text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors duration-200 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed sm:px-8 lg:px-10" href="/">
  Empezar
</a>
```

Funciona. Y es ilegible, y no lo vas a poder modificar en tres meses, y cuando el cliente pida el botón en verde vas a tener que editar quince utilidades sin saber qué significan.

La causa no es que el modelo sea tonto. Es que le pediste un botón y te dio todo lo que un botón puede tener. Te explico los tres patrones que siempre genera mal, cómo pedirlo bien y cómo arreglar lo que ya está en tu proyecto.

## Patrón 1: el componente repetido tres veces

El síntoma es clarísimo: el mismo grupo de clases aparece en el botón de la home, en el del login y en el del perfil. Son tres bloques de veinte clases idénticos con dos diferencias.

La IA no ha hecho nada incorrecto desde su punto de vista: cada sitio es un elemento independiente. Pero el resultado es que cambiar el estilo de los botones implica editar tres sitios, y el cuarto que añadas mañana inherits de la nada.

La causa profunda es que le diste el **código**, no la **decisión**. Cuando le pides "dame el botón", ella cumple. Cuando le pides "estamos construyendo una aplicación con tres tipos de botón, primario, secundario y de terciario, y quiero que compartan estructura", ya está pensando en reutilización.

> "Voy a montar una interfaz con Tailwind. Necesito tres variantes de botón: primario, secundario y de texto. Escribe un componente con una clase base compartida y las diferencias en cada variante. Usa las clases más pocas posibles y justify cada decisión."

La última frase es la que más importa. Cuando le pides que justifique, deja de llenar el `div` por si acaso y empieza a preguntarse qué necesita cada utilidad.

## Patrón 2: el `lg:` que no existe

Este es el que más daño hace y el que más rápido se detecta si buscas los breakpoints de la cola.

La IA escribe breakpoints de frameworks que ha visto más veces en los datos: `sm:`, `md:`, `lg:`, `xl:`. Tailwind **no tiene `lg` en la versión 4 con la escala por defecto de la misma forma**, y sobre todo las clases de grid cambió bastante. El resultado son utilities que no existen o que existen con otro significado, y aparecen discretamente en el HTML como si fueran válidas.

Síntoma: la maquetación se ve bien en tu pantalla y se rompe en un móvil, porque `md:grid-cols-3` no hace nada y te queda una columna.

Mi comprobación es rápida: después de cada bloque de Tailwind que genera, hago `grep` de los prefijos de breakpoint y los comparo con la escala de Tailwind. Si aparece uno que no reconozco, a revisar.

> "Usa solo estas variantes de breakpoint de Tailwind: sm, md, lg, xl. Si necesitas algo responsive que no cabe con esas, dilo y lo resolvemos con otro enfoque, no inventando una variante nueva."

## Patrón 3: `!important` y `inline style` para resolver un conflicto

Cuando la IA se encuentra con un estilo que no puede resolver con clases, no busca la causa. Pone `!bg-blue-600` o mete un `style="margin-top: 12px"` y sigue. Has tapado el problema con cinta aislante.

El motivo casi siempre es que el elemento está dentro de otro que ya define ese estilo. Un `!important` ahí significa que hay dos capas compitiendo por el mismo atributo, y la próxima vez que cambies el contenedor se rompe algo que no sabías que estaba atado.

> "Antes de usar `!important` o estilos inline, encuentra la regla que está ganando y elimínala. Dime qué la causaba. Si de verdad no se puede evitar, usa el variante `!` solo como último recurso y explica por qué no hay otra forma."

## El prompt base que uso para todo componente

Cuando voy a encargar un bloque de interfaz, esta es la estructura que me funciona:

> "Componente: tarjeta de artículo con título, categoría, fecha y tiempo de lectura. Usa Tailwind. Contexto: la tarjeta aparece en una rejilla de 3 columnas en escritorio y 1 en móvil, y las tarjetas tienen alturas distintas porque los títulos varyan. Quiero altura uniforme con `line-clamp`, no alturas fijas. No uses `!important` ni estilos inline. Si el diseño necesita algo que Tailwind no da bien, dímelo en vez de forzar una solución."

Fíjate en las tres últimas cosas. El contexto de cómo se usa el componente, el requisito explícito de cómo debe comportarse en el caso raro (las alturas distintas), y el permiso para decir "esto no se puede hacer bien aquí". Ese último evita los apaños.

## Cómo arreglar lo que ya está mal

Si ya tienes el proyecto lleno de `div` de veinte clases, no lo reescribas de golpe. El orden que me funciona:

**Primero, `npx prettier` con el plugin de Tailwind.** No arregla el problema pero ordena las clases en un orden estándar, que hace visible qué se repite. Este paso solo, sin más, ya reduce bastante el ruido.

**Segundo, busca el bloque de clases duplicado.** Busca las utilidades que aparecen más de diez veces en tu proyecto. Esas son tus candidatos a componente. Con una búsqueda de una clase muy concreta (`gap-2 rounded-lg px-6`) tienes el 80% de los casos.

**Tercero, extrae por bloques, no por línea.** No intentes hacer un componente "de todo". Empieza por el botón, que es el que más se repite, y ve viendo si el siguiente es una tarjeta o un campo de formulario.

**Cuarto, define las variantes con `cva`, no con props sueltos.** `cva` (class-variance-authority) es el patrón estándar para esto y hace que las variantes se declaren en un sitio:

```js
const boton = cva(
  "inline-flex items-center justify-center gap-2 rounded-lg px-6 py-3 font-semibold transition-colors",
  {
    variants: {
      tono: {
        primario: "bg-blue-600 text-white hover:bg-blue-700",
        secundario: "bg-transparent text-blue-600 hover:bg-blue-100",
      },
    },
  }
);
```

Ese `"base + variantes"` es exactamente lo que la IA nunca te da sola, y es la mitad del trabajo de tener un sistema de diseño.

## Un apunte sobre cuándo no usar Tailwind

Con mucho HTML generado por IA, Tailwind llega a un punto en el que el `class` es más largo que el resto del componente. Ahí no es un problema de Taste: es que la utilidad no está cubriendo tu caso.

La señal es clara: estás usando `grid` con `col-span-7` y `col-span-5` para algo que es medio formulario, medio ilustración. Cuando pasas por ahí, una clase propia de tres líneas en tu hoja de estilos es más legible que ocho utilidades. No es cuestión de gusto: es que la utilidad dejó de justificarse.

Y el criterio es simple: si tardas más de cinco segundos en entender qué hace un `class`, ese `class` ya es una reliquia. Sácalo a una clase propia.

## Resumen

- La IA llena el elemento de todo lo posible porque le pediste un elemento, no una decisión.
- Pide siempre las variantes y la reutilización explícitamente.
- Verifica los breakpoints que genera: se inventa los que no existen y rompen el móvil.
- Nada de `!important` ni estilos inline: que busque la regla que gana.
- Arregla lo existente extrayendo por bloques repetidos, empezando por el botón.
- Si la utilidad no se explica en cinco segundos, es momento de una clase propia.

El problema de fondo aquí es el mismo que en cualquier código generado: la IA optimiza para que la cosa funcione ahora, no para que puedas mantenerla dentro de seis meses. En Tailwind se nota antes porque el `class` es el sitio donde vive todo el estilo.

*Si quieres ver el resultado de esto aplicado a un proyecto entero, en [crear tu portfolio de desarrollador con IA](/articulos/guias/crear-portfolio-desarrollador-web-con-ia/) lo montamos paso a paso, y en [V0 y las mejores herramientas de IA para generar interfaces](/articulos/listas/v0-vercel-ia-ui-generacion-lista-herramientas/) comparo las que generan la interfaz por ti.*

## Sigue por aquí

Dos cosas que se cruzan con esto: el diseño visual y el despliegue.

- [V0 y las mejores herramientas de IA para generar interfaces](/articulos/listas/v0-vercel-ia-ui-generacion-lista-herramientas/)
- [Cómo publicar tu primera web por poco con IA](/articulos/guias/como-publicar-primera-web-internet-barato-ia/)
- [Conectar el frontend con una API usando IA](/articulos/guias/conectar-frontend-api-con-ia-2026/)
