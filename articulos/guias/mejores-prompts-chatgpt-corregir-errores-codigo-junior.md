---
layout: article
title: "Los mejores prompts de ChatGPT para corregir errores de código como un junior"
description: "Prompts chatgpt para corregir código junior que uso yo mismo cuando mi código no compila y no sé por qué."
category: "Guía"
date: 2026-08-21
readtime: 7
affiliate_text: "Si depuras código todos los días, ChatGPT Plus te ahorra horas de sufrimiento"
affiliate_url: "https://chatgpt.com/plus"
affiliate_label: "Probar ChatGPT Plus"
---

Llevo desde segundo de DAW usando prompts chatgpt para corregir código junior casi todos los días, y no lo digo para quedar bien: es literalmente lo que hago cuando llevo cuarenta minutos mirando una consola que me devuelve un error que no entiendo. Al principio copiaba y pegaba el error tal cual, sin más, y la respuesta que me daba ChatGPT era tan genérica que no me servía para nada. Con el tiempo fui cambiando la forma de preguntar y ahí es donde note la diferencia real.

## Por qué los prompts genéricos no sirven para corregir código

"Corrige este código" es probablemente el prompt más inútil que existe. Lo he probado mil veces y lo que consigues es una versión reescrita del código, sin explicación de qué estaba mal, y muchas veces con cambios de estilo que ni te habían pedido. Eso no te enseña nada, solo te da un parche.

Lo que cambió mi forma de trabajar fue entender que ChatGPT responde según el contexto que le das. Si tú le das poco contexto, te devuelve poco valor. Y en programación el contexto es casi todo: el lenguaje, la línea exacta del error, qué esperabas que pasara y qué pasó en realidad. Cuando empecé a incluir eso en el prompt, las respuestas pasaron de ser "aquí tienes tu código arreglado" a explicaciones que de verdad entendía.

## Los prompts que uso yo para depurar código real

Estos son los que tengo guardados en mis notas y reutilizo casi a diario, con pequeñas variaciones según el lenguaje.

### Cuando el error no te dice nada

Hay errores de Java o de C# que parecen escritos en otro idioma. Para esos uso algo como: "Actúa como un programador senior explicándole a un junior. Este es mi código en [lenguaje] y este es el error exacto que me da la consola: [pegar error completo]. Explícame en lenguaje sencillo qué está fallando antes de darme la solución, y dime en qué línea está el problema real, no solo dónde salta el error." La clave está en pedirle que separe la explicación de la solución. Si no lo pides, te suelta las dos cosas mezcladas y acabas leyendo por encima sin aprender nada.

### Cuando el código "funciona" pero no hace lo que quieres

Esto me pasa mucho con bucles y condicionales, sobre todo en JavaScript. El prompt que uso es: "Este código no da error pero el resultado no es el esperado. Esperaba [resultado esperado] y en cambio obtengo [resultado real]. Aquí está el código: [pegar código]. Dime paso a paso qué está haciendo el código realmente, sin corregirlo todavía." Pedirle que no corrija todavía es un truco que aprendí después de fallar varias veces: si le dejas corregir directamente, se salta la parte de explicarte el flujo real del programa, que es justo la parte que te hace mejor programador.

### Cuando quieres entender el error, no solo quitarlo

Para practicar antes de un examen o una prueba técnica uso: "Genera un ejercicio de código en [lenguaje] con un error típico de nivel junior relacionado con [tema, por ejemplo bucles anidados o punteros nulos]. No me des la solución todavía, solo dame el código con el error y una pista pequeña." Esto lo utilizo bastante con ChatGPT Plus porque en la versión gratuita a veces las respuestas se quedan cortas o repiten el mismo tipo de error una y otra vez, y con Plus noto que varía más los ejercicios y aguanta mejor conversaciones largas de depuración sin perder el hilo de lo que ya habíamos hablado antes.

## Cómo aprender de tus errores en vez de solo copiar la solución

Aquí tengo que ser sincero: durante mi primer año copiaba directamente lo que me daba ChatGPT sin pensar mucho, y en el examen de prácticas me di cuenta de que no sabía explicar por qué esa solución funcionaba. Desde entonces cambié la estrategia y siempre añado al final de mis prompts algo como "explícamelo como si tuviera que defenderlo en un examen oral". Suena raro, pero obliga a la IA a darte razones, no solo código, y a ti a leerlas de verdad porque sabes que las vas a necesitar.

También me ha ayudado pedirle que compare mi solución equivocada con la correcta, línea por línea, en vez de simplemente sustituir el bloque entero. Así ves exactamente qué cambió y por qué, en lugar de memorizar un bloque de código nuevo que en el fondo no entiendes.

## ¿Merece la pena pagar ChatGPT Plus para esto?

Te lo digo desde mi experiencia como estudiante con presupuesto limitado: con la versión gratuita puedes sobrevivir para errores sueltos y preguntas rápidas, pero cuando estás depurando un proyecto entero, con varios archivos y varias conversaciones seguidas sobre el mismo bug, la diferencia se nota. La versión gratuita se satura antes, responde más genérico cuando la conversación se alarga y en según qué horas va más lento. Cuando empecé a usar ChatGPT Plus para mis prácticas de empresa, dejé de tener que repetir todo el contexto cada dos mensajes, que era justo lo que más tiempo me quitaba.

No digo que sea obligatorio desde el primer día de clase, pero si ya estás en la fase de proyectos de fin de curso o en prácticas, donde los bugs son más grandes y los prompts los repites constantemente, sí que se nota en el tiempo que ahorras cada semana.

Al final, la diferencia entre corregir código como un junior perdido y corregir código como alguien que está aprendiendo de verdad no está en la herramienta, está en cómo le preguntas. Estos prompts no son magia, son solo la forma en que yo he ido aprendiendo a pedir ayuda sin dejar de entender lo que hago.
