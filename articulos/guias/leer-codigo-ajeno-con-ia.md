---
layout: article
title: "Cómo leer código ajeno con IA: el método de 4 pasos para entenderlo de verdad"
description: "Aprende a leer y entender código que no escribiste tú usando IA, sin quedarte con un resumen bonito que no te sirve. Método de 4 pasos con prompts concretos."
category: "Guía"
date: 2026-09-25
readtime: 8
---

El día que llegas a un trabajo, a unas prácticas o a un proyecto de un compañero y te encuentras con un archivo de 800 líneas que no has escrito tú, pasa algo incómodo: no entiendes nada, y la IA te da un resumen muy bonito que no te sirve para nada. "Este archivo gestiona las notas del usuario", dice, y tú te quedas igual. He visto a muchos compañeros pasar por eso, y el truco no es pedirle a la IA que te lo explique entero. El truco es **usar la IA como lupa, no como traductor**: que te vaya señalando dónde mirar, en vez de darte una explicación genérica. Esta es la guía de cómo hacerlo, con los prompts exactos que uso.

## Por qué el resumen no te salva

El problema de pedirle "explícame este código" es que la IA optimiza por darte una respuesta que *parece* buena, no una que te enseñe. Te devuelve un párrafo:módulo, gestiona datos, y ya. Eso no es entender, es aceptar. Y mañana, cuando tengas que cambiar algo, no sabrás por dónde empezar.

Lo que necesitas es lo contrario: partir el código en piezas, mirar una cosa a la vez, y reconstruir tú el mapa mental. La IA sirve de guía, que te va enseñando por partes. Es la misma diferencia entre mirar el resumen de un libro y leer el libro, y aplica igual al código.

## Paso 1: el mapa general (qué hace y de qué está hecho)

Antes de leer una línea, necesitas una vista de pájaro. Pero no una vista de pájaro genérica: una que te diga la **estructura**. El prompt que uso:

> "Este es un archivo de un proyecto ajeno. No me lo resumas todavía. Dime: 1) qué hace el archivo a nivel general, 2) qué funciones o clases define y qué hace cada una en una línea, 3) qué librerías o dependencias usa, 4) qué otras funciones del proyecto llama."

Con eso te quedas con un índice. No entiendes el código todavía, pero sabes qué hay dentro y por dónde se entra. Es como la tabla de contenidos de un libro: no te da la historia, pero te permite saltar a la parte que te interesa.

## Paso 2: una función a la vez (el corazón del método)

Aquí es donde se cocina la comprensión. Una función del archivo, preferably la que más te llame, y le pides cosas concretas, no un resumen. Aquí está la diferencia entre entender y no entender:

> "Explícame la función `crearNota`. No me digas qué hace en general. Dime: qué parámetros recibe y para qué sirve cada uno, qué devuelve, qué otras funciones llama, y qué pasa si le paso un parámetro vacío."

Esas cuatro preguntas (parámetros, retorno, llamadas, casos límite) son las que necesitas para poder *modificar* una función, no solo leerla. Y fíjate en la última: "qué pasa si le paso un parámetro vacío". Esa es la que te ahorra el error, porque la mayoría de bugs no están en lo que el código hace bien, sino en lo que hace cuando le pasas algo que no esperaba.

Y si no te queda claro, el paso extra que me funciona: **pídele que te invente una llamada**. "Dame un ejemplo de cómo llamo a `crearNota` con datos reales". Ver el uso concreto de una función te enseña su forma más rápido que tres párrafos de teoría.

## Paso 3: traza el flujo (aquí se junta todo)

Ya tienes el mapa y ya entiendes las funciones sueltas. El siguiente paso es la pregunta que responde el "de dónde sale esto":

> "Cuando el usuario hace clic en 'Guardar', ¿qué funciones se ejecutan, en qué orden, y qué datos se van pasando entre ellas? Enséñame el recorrido paso a paso."

Esto es trazar una ruta: pulsas guardar → se llama esta función → toca esta otra → acaba aquí. Es la diferencia entre leer código y entender *cómo funciona*. Y cuando la IA te lo da, tú tienes que comprobar que tiene sentido: si en algún paso te pierdes, vuelves al Paso 2 con esa función concreta. Es iterativo, y funciona.

## Paso 4: hazlo tuyo (la prueba de fuego)

El último paso, y el que casi nadie hace, es comprobar que has entendido. Pídele a la IA un pequeño ejercicio de modificación sobre el código que acabas de leer:

> "Ahora dame un ejercicio: cambia esta función para que también acepte X, pero **no me des la solución**. Solo dime qué tendrías que tocar."

Si sabes qué archivos y qué funciones tocar, lo has entendido. Si no sabes ni por dónde empezar, es que te has quedado en la Fase 1. Este paso es brutalmente honesto contigo mismo, pero es el que de verdad consolida lo aprendido, y es gratis (solo le das al botón de regenerate hasta que acierte).

## Los prompts que uso de fábrica

Para que no tengas que reconstruirlos cada vez, aquí van mis favoritos, listos para copiar. Los nombro por lo que hacen:

- **"Estructura"**: el del Paso 1, el mapa general.
- **"Función"**: el del Paso 2, con las cuatro preguntas.
- **"Llamada"**: "dame un ejemplo de cómo se llama esta función con datos reales".
- **"Flujo"**: el del Paso 3, trazar un recorrido.
- **"Ejercicio"**: el del Paso 4, la prueba de fuego.

Es también el mismo principio que uso cuando le pido a la IA que me enseñe cosas de Java o JavaScript: no le pido la respuesta, le pido que me ponga en la situación donde tengo que aplicar lo que sé. Esa diferencia entre "dame el código" y "hazme un ejercicio" es la misma que separa aprender de copiar, y aplica igual a leer código ajeno.

## Un aviso: no te fíes del todo

La IA se equivoca al leer código, y con más frecuencia de lo que parece. Los errores típicos son: inventar una función que no existe, asumir que una función hace algo parecido pero distinto, o resumir mal la lógica de un caso límite. Por eso el método va en pasos: en cada paso **compruebas con el código real** (el nombre de la función existe, la llamada está donde dijo, el parámetro es ese). Si la IA te dice algo y al buscarlo no está, es que se lo inventó, y tu trabajo es detectarlo. Esacombina de "IA dice" + "yo compruebo" es la que te convierte en alguien que entiende el código, no en alguien que lo copia con IA.

Y ojo con un detalle de seguridad: si el código viene de un repositorio ajeno, no le pidas a la IA que lo ejecute ni que lo "pruebe" automáticamente sin leerlo. Primero entiéndelo, luego si eso ejecutalo. Es lo mismo que te dije en [la guía de seguridad con apps de IA](/articulos/guias/prompt-injection-seguridad-apps-ia-2026/): el código que no entiendes no lo tocas.

## Mi veredicto

Leer código ajeno con IA no es pedirle que te lo explique: es usarla como lupa que te va guiando por el código mientras tú reconstruyes el mapa. Los cuatro pasos (estructura, función, flujo, ejercicio) están diseñados para que en cada momento sepas qué preguntarle y, sobre todo, para que al final **sepas tú más que la IA**, porque habrás pasado por el código. Ese es el objetivo: salir de leer un proyecto con la capacidad de modificarlo, no con un resumen bonito que se te olvida al día siguiente.

Mi consejo: aplica el método tal cual a un archivo la primera vez (aunque lleve media hora), y a partir de ahí irá más rápido porque ya sabrás qué preguntar. Y cuando estés atascado, o cuando el código esté en un framework que no controlas, esto sigue funcionando: no necesitas saber React para entender un archivo de React, solo necesitas este método y curiosidad. Si te atascas en un proyecto concreto y quieres que lo veamos juntos, escríbeme a ivan@codeandia.com. Y si lo que necesitas es justo tu primer contacto con código de proyecto real, empieza por [tu primer proyecto web con IA](/articulos/guias/primer-proyecto-web-con-ia/) y luego aplica aquí los cuatro pasos.
