---
layout: article
title: "Cómo preparar exámenes prácticos de DAW con IA (sin copiar en el examen)"
description: "Preparar exámenes prácticos de DAW con IA sin volverte dependiente: el método que uso para practicar con la IA de profesor y sobrevivir el día del examen."
category: "Guía"
date: 2026-09-08
readtime: 8
---

Suspendí mi primer examen práctico de programación por una razón tonta: sabía "darle a la IA las instrucciones", pero no sabía programar sin ella. En clase, con ChatGPT al lado, resolvía los ejercicios de maravilla. En la mesa del examen, con pantalla negra y sin copiloto, me quedé en blanco como media hora mirando un enunciado que no sabía ni por dónde empezar.

El suspenso no fue de la IA. Fue mío, por usar la IA como muleta en vez de como profesora. Desde entonces preparo los exámenes de otra forma, y no he vuelto a suspender uno práctico. Te cuento el método por si estás en el mismo momento en el que estaba yo.

## El error de fondo: usar la IA como la respuesta, no como la pregunta

Todos caemos en lo mismo: le pegas el enunciado a ChatGPT y te devuelve el código completo. Te lo copias, te funciona, apruebas el ejercicio... y no has aprendido nada de lo que evaluaban. La IA te da el pescado, pero en un examen no puedes pedir pescado.

Lo que hay que cambiar es el papel que le das a la IA. No es una respondona, es una **profesora que no se cansa**: te hace preguntas, te corrige sin darte la solución antes de tiempo y te genera material de práctica infinito. Ahí es donde está todo el valor.

## Fase 1: entender los conceptos, no memorizar código

Cuando llego a un tema nuevo, lo primero que hago es pedirle a la IA que me lo explique de forma concreta. Pero nunca le pido que me resuelva el ejercicio de clase. Le pido que me enseñe el concepto detrás.

Un ejemplo real que uso con mis prompts: si estamos viendo arrays en Java, no le pido "código para ordenar un array". Le pido que me explique "qué diferencia hay entre un `ArrayList` y un array normal, cuándo conviene cada uno y en qué momento del examen me vendría bien usar cada uno". Eso abre el diálogo. La IA me responde con teoría, me hace una pregunta de comprobación, y yo le respondo.

La prueba de que has entendido no es que te "suene". Es que seas capaz de contestarle a la IA cuando ella te pregunta a ti. Ese intercambio de preguntas y respuestas es lo que te está preparando para el examen.

## Fase 2: pedir ejercicios de examen, con dificultad creciente

Aquí está el truco que más me ha cambiado la forma de estudiar. En vez de resolver los ejercicios que ya están resueltos en el libro, le pido a la IA que me genere enunciados nuevos, tipo examen, con niveles.

Le dejo claro cómo quiero los niveles: "nivel 1, para calentar, un `if` y un bucle; nivel 3, que sea lo que te caería en la parte difícil del examen de DAW". La IA es una máquina de generar práctica. Un solo tema me puede producir diez enunciados distintos, y yo los resuelvo en papel o en un editor sin IA abierta.

Y aquí es donde separo el trigo de la paja: **resuelvo el enunciado yo primero, y solo después** le pido a la IA que lo corrija. No antes.

## Fase 3: que me corrija sin darme la solución

Cuando ya tengo una solución, le pido a la IA que la revise con instrucciones muy concretas: "no me reescribas el código entero. Dime qué línea falla, por qué falla, y deja que lo arregle yo. Si hay tres fallos, dame solo la pista del primero".

Esto parece un capricho, pero tiene una razón técnica de fondo: si la IA te devuelve el código completo corregido, no ejercitas la parte de tu cerebro que va a tener que localizar errores en el examen. En cambio, si ella te dice "mira la línea 12, el bucle se sale del array", tú tienes que entender, pensar y arreglar. Ese proceso es exactamente lo que puntúan en un examen práctico.

El día del examen de recuperación me pasó justo esto: un ejercicio con un error de índices que en realidad era el típico fallo de "me paso en una unidad". Como llevaba semanas corrigiendo mis propios errores con pistas, lo vi al momento. No habría tenido ni idea si me hubiera limitado a copiar soluciones buenas durante tres semanas.

## Fase 4: simulacros con tiempo, sin IA

Esta fase es la que menos me gusta y la que más me salva. Unos días antes del examen, cojo los enunciados que me ha generado la IA, me pongo un cronómetro con el tiempo real del examen y me siento a resolverlos **sin abrir nada de IA**.

La primera vez que hice esto me di cuenta de una cosa que no sabía: la mitad de mi "saber programar" era en realidad saberle pedir a la IA. Cuando me vi solo ante el enunciado, hasta las cosas que creía dominar me costaban el doble de lo que tardaba con el editor.

Repetí el simulacro tres o cuatro veces con enunciados distintos hasta que el tiempo empezó a sobrarme. Es aburrido, soy consciente. Pero es el momento en el que de verdad estudias para el examen, y no a la IA.

## El día del examen

Tres reglas que me puse yo y que me han funcionado:

1. **Empiezo por el ejercicio que mejor sé.** Parece de libro, pero con la ansiedad de un examen práctico todo el mundo empieza por el primero, que suele ser el más difícil. Si arranco ganando confianza, el resto va rodado.
2. **Escribo el esquema en una hoja antes de tocar el teclado.** Cinco minutos de pseudocódigo a mano me evitan quedarme en blanco en mitad del código y me dan un mapa al que volver si me pierdo.
3. **Si me atasco, no me quedo clavado.** Marco el sitio con un comentario, paso al siguiente ejercicio y vuelvo al final cuando el examen ya está, encima, resuelto en su mayoría. El miedo a dejar un hueco es peor que el hueco.

## Lo que haría distinto si volviera a empezar

Si tuviera que repetir mi primer trimestre de DAW, la regla de oro sería una: **la IA nunca me da el código final. Me da el camino.** Cada vez que me sorprendo pidiéndole que me resuelva algo entero, me detengo, lo borro, y se lo pido como pista.

Y no me equivocaría al decirte que con esta forma de trabajar he tardado el doble que mis compañeros en hacer los ejercicios, al principio. Pero cuando llega el examen, los que copiaban soluciones están en modo pánico y yo estoy resolviendo. Prefiero aprender despacio y aprobar que ir deprisa y quedarme atrás.

Si quieres los prompts exactos que uso en cada fase (los de explicación, los de generar ejercicios, los de corregir con pistas), te dejo [los 8 prompts que me salvan el curso de DAW](/articulos/listas/8-prompts-programacion-daw-2026/), donde los tienes listos para copiar. Y si aún no has montado tu flujo de IA en el editor, esta [guía de cómo usar GitHub Copilot en las prácticas](/articulos/guias/como-usar-github-copilot-practicas-daw/) te viene bien.