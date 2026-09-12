---
layout: article
title: "Los 8 prompts que me salvan el curso de DAW (con ejemplos reales)"
description: "Los prompts de IA que uso cada semana en DAW: explicar conceptos, generar ejercicios, corregir con pistas, aprender Java y MySQL y preparar exámenes."
category: "Lista"
date: 2026-09-10
readtime: 6
---

Tengo una carpeta en mi portátil llamada `prompts-que-funcionan`. Cada vez que descubro un prompt que me hace el día más fácil en el curso, lo guardo ahí con un comentario de cuándo lo uso. Unos cuantos salieron de experimentar a lo bruto; otros los saqué de [la guía para corregir errores con ChatGPT](/articulos/guias/mejores-prompts-chatgpt-corregir-errores-codigo-junior/) y los ajusté a mi forma de trabajar.

Estos son los 8 que de verdad me ahorran horas cada semana. No son magia: el 90% del valor está en cómo están planteados, que es *para que no te den la respuesta gratis*.

## 1. El que me explica conceptos nuevos

Cuando en clase sacan un tema que me suena a chino, antes de mirar apuntes le digo a la IA:

> "Explícame qué es X como si tuvieras que decírselo a un alumno de 16 años y sin usar jerga técnica. Pon un ejemplo tan pequeño que quepa en un tweet."

Funciona porque le pones dos restricciones: público concreto y tamaño máximo. Sin restricciones, la IA te suelta un muro de texto técnico que parece que entiendes y no entiendes. Con estas dos, se ve obligada a simplificar de verdad.

## 2. El que me hace entender mi propio código

Este me lo enseñó un compañero y es el que más veces he usado:

> "No me corrijas todavía. Lee este código, dime qué hace línea a línea y señala los dos sitios donde crees que puede fallar. No arregles nada, solo explícame."

La clave es "no me corrijas todavía". Así la IA analiza, tú entiendes tu propio código a fondo, y cuando llega el fallo real sabes dónde mirar en vez de aplicar un parche que te han dado hecho.

## 3. El de los ejercicios con dificultad creciente

Para practicar antes de un examen de Java o de MySQL:

> "Genera 5 ejercicios de [tema] con dificultad creciente. El 1 debe ser fácil, para calentar; el 5 debe ser el nivel del examen de DAW. Sin soluciones, solo enunciados."

No te das cuenta de lo valioso que es esto hasta que has resuelto cinco enunciados distintos del mismo tema. La IA te saca práctica infinita de un tema que el profesor solo te ha dado en tres ejercicios de clase. Y sin soluciones: abajo te explico por qué.

## 4. El del fallo escondido

Este es el que me cambió la forma de estudiar debugging:

> "Méteme un fallo intencionado en esta función de Java, no me digas cuál es, y descríbeme los síntomas que tendría. A partir de ahí lo busco yo."

Resulta que darle la vuelta al proceso funciona genial: en vez de buscar errores en código ajeno, tú escribes código "correcto" en tu cabeza, la IA lo rompe, y tú tienes que encontrarlo leyendo. En los exámenes prácticos te caen errores que parecen esto todo el rato, y llevar tantos detectados te quita el miedo al rato.

## 5. El que corrige sin reescribir

Este es el más importante para no convertirte en copión dependiente de la IA:

> "Corrige mi código sin reescribirlo entero. Dime la línea exacta que falla, por qué falla, y dame solo la pista para que lo arregle yo. Si hay varios fallos, dame solo el primero."

Es la versión "profesor severo" de la IA. No te da el código corregido: te da el mapa para que tú lo arregles. Cuando haces esto con cada ejercicio, llegas al examen habiendo arreglado fallos tú mismo docenas de veces, y esa es exactamente la habilidad que te puntúan.

## 6. El de las comparaciones con tabla

Para conceptos que son dos hermanos difíciles de distinguir (array vs ArrayList, `WHERE` vs `HAVING`, sesión vs cookie):

> "Explícame las diferencias entre X e Y con una tabla comparativa y un ejemplo de código de cada uno. Al final, dime en qué situación elegirías cada uno."

El ejemplo de código es lo que hace que no sea una tabla de la Wikipedia. Y la última frase ("en qué situación elegirías") es la que te prepara para la típica pregunta de examen de "¿cuándo se usa esto?" que no viene en los apuntes.

## 7. El del test tipo examen

Unos días antes de cada examen parcial me pongo esto:

> "Hazme un test tipo examen de [módulo] con 10 preguntas de opción múltiple de nivel de DAW. No las respondas: página aparte con las soluciones y explicación."

Dos partes clave: "nivel de DAW" (si no lo dices, te pone preguntas de experto o de niño pequeño) y "no las respondas" (para no hacer trampa leyendo la respuesta por el rabillo del ojo). Después me lo corrijo yo con la hoja de soluciones que me da al final, y las que fallo me las explico una a una.

## 8. El de la analogía para memorizar

Cuando un concepto se me borra a los dos días, le pido que me lo ancle:

> "Dame una analogía de la vida real para [concepto] que tenga sentido en un proyecto de tienda online, mi proyecto de DAW."

Es tonto, pero funciona. "La sesión es como el tique de un parking que guarda tu coche en una caseta" lo recuerdo mucho mejor que "objeto que persiste el estado entre peticiones HTTP". Y al pedirle que lo enchufe a una tienda online —mi proyecto— el ejemplo queda pegado a algo que he hecho yo, y no se me olvida.

## Mi regla de oro

Si un prompt me da la respuesta *sin esfuerzo*, está mal planteado. He aprendido a detectar la señal de alarma: cuando copio y pego el resultado directamente, ese prompt me está quitando aprendizaje. Mis prompts de verdad son los que me obligan a seguir pensando después de que la IA responde.

Con esta filosofía, la IA pasa de ser una máquina de hacer tareas a ser exactamente lo que necesito en el curso: una profesora infinita, que no se cansa y que está disponible a las dos de la madrugada cuando el ejercicio no compila.

Si todavía estás trasteando qué papel le das a la IA en el curso, te cuento [el método que uso para preparar exámenes prácticos sin volverme dependiente](/articulos/guias/preparar-examenes-practicos-daw-con-ia/), que es la otra mitad de esta historia. Y si te da pereza copiar prompts a mano, llévate la idea de fondo a tu propia forma de preguntar: restricción, contexto concreto y "no me des la solución, dame la pista". Con eso ya vas mejor que con el prompt más largo del mundo.