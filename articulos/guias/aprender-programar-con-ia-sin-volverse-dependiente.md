---
layout: article
title: "Programar con IA sin volverte dependiente: guía para estudiantes DAW"
description: "Cómo usar la IA en clase como profesor y no como sustituto: reglas prácticas para aprender a programar de verdad mientras la IA te acompaña."
category: "Guía"
date: 2026-09-05
readtime: 7
---

La primera semana que dejé que la IA hiciera los ejercicios por mí fui el más rápido de la clase. También el que menos entendía: en el primer parcial de programación, sin internet y sin autocompletar, el editor me pedía que escribiera un bucle y mi mente estaba en blanco. No es que no supiera el tema, es que nunca lo había aprendido: había estado copiando, no programando. Esta guía es la lista de reglas que me hubiera dado el profe si fuera honesto con lo que pasa en clase desde que existe la IA.

## La señal de que vas mal: puedes explicar lo que pegaste

El test más barato del mundo es preguntarte a ti mismo: "¿y esto por qué funciona?". Si la respuesta es "porque la IA lo dijo", estás en modo copiar-pegar. No digo que sea ilegal usar IA, al contrario — es la herramienta del futuro y a tu yo de segundo de carrera le va a exigir que la uses —, pero si no sabes explicar el código que acabas de entregar, no has aprendido nada y lo pagarás el día del examen.

Mi señal de alarma particular: podía pasarme todo el módulo de servidor con la consola en verde y suspender casualmente la prueba teórica. Si ves que apruebas prácticas a base de IA y luego te quedas en blanco en papel, este mensaje va por ti.

## Regla 1: que te explique, no que te escriba

La diferencia no está en la IA, está en el prompt. Cambia "dame el código de un CRUD" por "explícame cómo funciona un controlador en Spring Boot con un ejemplo mínimo". Con la primera petición te devuelve un bloque que no entiendes; con la segunda te da un profesor. Si necesitas que genere algo, pídele que primero te describa qué va a hacer y por qué cada pieza está ahí, antes de ver una sola línea.

Esto es el mismo principio que uso en mi [guía de pedir prompts para corregir errores](/articulos/guias/mejores-prompts-chatgpt-corregir-errores-codigo-junior/): la IA rinde el doble cuando la tratas como un tutor que pregunta que cuando la tratas como un portero de discoteca que te deja pasar sin preguntar.

## Regla 2: rehazlo a ciegas

Esto me lo dijo un compañero que ya curraba y es lo más valioso que me llevé de clase. Cuando terminas un ejercicio y crees que "ya has entendido", borra la solución y vuelve a hacerlo desde cero, sin IA y sin mirar notas. La primera vez cuesta, la segunda sale un poco descolocada y la tercera sale sola.

La ciencia lleva años diciendo que recuperar de memoria funciona mejor que reler, y con la IA se vuelve todavía más importante: si no lo rehaces, solo practicas reconocer código ajeno, no producirlo. Mi objetivo es que cada ejercicio importante lo rehaga dos veces: una a los dos días y otra antes del examen.

## Regla 3: el error es tuyo, la pista es de la IA

Lo único que mata el aprendizaje es que la IA te dé la solución final. Lo que funciona es pedir la pista, no el arreglo. Cuando tu programa falle, el prompt no es "arregla esto" sino "dime qué está fallando sin decirme cómo arreglarlo" o "¿qué línea debo mirar?". Luego te toca a ti razonar por qué.

Tengo una [lista de errores comunes programando con IA](/articulos/listas/errores-comunes-programando-con-ia/) que he ido hurtando de mis propios sustos, y casi todos siguen el mismo patrón: el fallo era revelador, pero como la IA me lo había arreglado sin explicaciones, no aprendí nada de él. El día que empecé a pedir pistas en vez de soluciones, los sustos dejaron de repetirse.

## Regla 4: el apagón de IA

Cada cierto tiempo, programas a pelo, con el editor limpio. Quince, veinte minutos sin IA, escribiendo tú cada línea. Es la simulación más barata de un examen que existe, y además te regala un dato importante: qué te sabes de verdad y qué solo sabes pedir.

Cuando empieces las prácticas de empresa o el primer trabajo de verdad, nadie te va a pedir que apagues la IA — todo lo contrario —, pero sí te van a hacer preguntas de qué habías hecho y por qué. El apagón diario entrenaba el músculo que te permite contestar sin tartamudear. Y de paso, es el momento perfecto para practicar el flujo con git que te dije en la [guía de git con IA](/articulos/guias/git-con-ia-2026/), porque cuando no hay autocompletar te das cuenta de si el historial de tu proyecto te salva o te condena.

## Regla 5: mide con tus manos

La IA te va a felicitar siempre. El compilador y los tests, no tanto. Por eso la última línea de defensa no es la IA, es tu propio control manual: leer el diff antes de hacer commit, ejecutar los tests, tocar los datos de verdad en la consola de la base de datos en vez de fiarte de que "el POST fue 200". Cuantos menos sitios tengas donde esconder el error, antes aprendes dónde tiende a esconderse.

En el módulo de servidor, por ejemplo, el fallo del mundo era que el endpoint respondía pero no persistía nada, y la mitad de la clase lo daba por bueno porque "daba 201". Si no lo compruebas tú, el curso entero pasa sin que sepas diferenciar entre que funciona y que finge que funciona.

## El veredicto: la IA no es el problema, el mando a distancia sí

La IA va a estar en tu puesto de trabajo y va a multiplicar tu velocidad. El problema no es usarla, es usarla como mando a distancia: pedir el resultado sin hacer el camino. El que sabe programar y usa IA va el triple de rápido; el que solo sabe pedir, se queda colgado el día que le cambian las herramientas. Y eso pasa siempre.

Mi consejo práctico para este curso: elige un par de ejercicios por semana y hazlos con las cinco reglas — explicar, rehacer, pedir pista, apagón y medir. No son un sacrificio, son la diferencia entre sacar el módulo copiando y llegar a las prácticas sabiendo hacer el trabajo. Si quieres, me pasas un ejercicio concreto que te traiga de cabeza y te digo por dónde empezar a controlarlo tú en vez de soltárselo a la IA.

## Sigue por aquí

- [Cómo usar ChatGPT para aprender JavaScript siendo principiante](/articulos/guias/chatgpt-para-aprender-javascript-principiante/)
