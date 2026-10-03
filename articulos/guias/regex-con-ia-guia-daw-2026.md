---
layout: article
title: "Regex con IA: cómo aprender expresiones regulares en DAW"
description: "Las expresiones regulares son la parte de JavaScript que más cuesta. Te enseño a pedirle a una IA que te las explique token a token y no te suelte un monstruo."
category: "Guía"
date: 2026-09-09
readtime: 8
last_modified_at: 2026-10-03
---

La primera vez que vi una expresión regular me pareció una amenaza. Era un `^\\s*([a-zA-Z0-9._-]+)\\s*=\\s*(.*)$` metido en una línea de un proyecto que no era mío, y lo que leí fue «nadie va a entender esto nunca». Hoy sé lo que hace cada trozo, y no fue leyendo un tutorial de cuarenta minutos: fue usando una IA con la instrucción correcta. Esa es exactamente la diferencia que te voy a contar aquí.

## El error que cometía yo

Abría el chat, escribía «dame una regex para validar emails» y me devolvía un bloque de veinte líneas con `(?=...)`, `(?<=...)` y banderas que yo no había visto en mi vida. Copiado, pegado, funcionaba. Hasta que cinco días después fallaba con un caso raro y yo no tenía ni idea de por qué.

El problema no era la IA. Era el encargo. Le estaba pidiendo la **solución**, y la solución es justo la parte que no se aprende. Si en lugar de eso le pido que me **enseñe**, todo cambia.

## El prompt que sí funciona

Este es el que uso yo, y funciona incluso con modelos pequeños:

> Soy estudiante de DAW y estoy aprendiendo expresiones regulares en JavaScript. Necesito validar que un email tenga formato válido. No me des la regex final todavía. Explícame primero qué significa cada parte de un intento de expresión regular, en una frase por token, y dime qué se está suponiendo que quiero validar. Después te pediré la versión final.

Cuatro cosas que acabo de pedir ahí, y que son las que importan:

1. **Que no me dé la respuesta final.** Si la tiene delante, mi cerebro la copia y no aprende nada.
2. **Una frase por token.** `\d+` es «uno o más dígitos». Con eso ya sé lo que estoy leyendo.
3. **Que me diga qué está suponiendo.** Aquí es donde aparecen los supuestos equivocados que luego rompen todo.
4. **Que me explique las alternativas.** Un buen profesor de regex siempre te enseña al menos dos formas de hacerlo, porque solo una suele ser la que se parece a lo que quieres.

## Construye la regex conmigo, trozo a trozo

El truco real es no pedir el patrón entero. Es construirlo trozo a trozo, como si fuera una cadena que montas tú:

> Vale. Ahora dime cómo se escribe «empieza por una o más letras minúsculas». Solo ese trozo, con una explicación de una frase.

Y así, token a token, hasta tener algo parecido a:

```js
const emailBasico = /^[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}$/;
```

Fíjate en tres cosas que ahora entiendes porque las has construido:

- El `^` ancla al principio y el `$` al final. Sin ellos, `contacto: marta@example.com` pasaría la validación, porque la regex buscaría el email en cualquier parte.
- El `{2,}` dice «dos o más» caracteres. `{2}` sería exactamente dos, y eso es un error muy común: no hay dominios de un solo carácter.
- El `\.` es un punto escapado. Sin la barra, el punto significaría «cualquier carácter» y aceptaría `casa@mioXcom`.

El punto de inflexión mental es este: **una regex es una frase escrita con piezas muy precisas**. En cuanto la lees como frase en vez de como código, se entiende. Ese fue mi salto real.

## Pídele los casos que NO deben pasar

Este es el consejo que más me costó descubrir y el que más errores me ha ahorrado. Una regex que solo sabes que funciona con `marta@example.com` no está probada.

> Dame una tabla de entradas: cuáles debería aceptar y cuáles debería rechazar, y por qué. Incluye al menos un caso límite.

Siete u ocho filas de tabla, y de golpe te aparecen los agujeros. Con la de email, mis entradas fueron: sin arroba, con arroba pero sin dominio, con doble arroba, con punto al principio, con dominio de una sola letra, con espacios dentro y con un email todo en mayúsculas. Cinco de mis siete pruebas fallaban. Eso no lo habría visto nunca probando solo el caso bueno.

## Aprende a leer los errores

En JavaScript, una regex mal escrita no da error: simplemente no encuentra lo que buscas. Esa es la trampa.

> Aquí tienes mi regex y esta entrada. Dime por qué `test()` devuelve `false` cuando debería devolver `true`, token a token: qué ha pasado exactamente.

Cuando una IA te explica **por qué** falla, empiezas a ver los mecanismos. A mí me pasó con el `$`: en JavaScript casa también justo antes de un salto de línea al final, así que una cadena con un salto de línea final pasaba la validación. Eso es un comportamiento real y documentado del lenguaje, no invención de la IA.

La misma técnica vale para otros lenguajes, y ahí las diferencias importan mucho: `String.matches` en Java lanza excepción en vez de devolver `false`, y `re.match` en Python devuelve el grupo de captura, no un booleano. La IA conoce esas diferencias si se lo preguntas, y saberlas es justo lo que te salva el examen.

## Lo que NO le dejes hacer a la IA

Un par de advertencias, porque aquí la herramienta también te puede hundir:

- **No aceptes el primer candidato.** Pide dos o tres versiones y compáralas. La más corta suele ser la más legible, y un `(?=.*[A-Z])` se puede reescribir con dos llamadas a `test`.
- **No aceptes banderas que no entiendas.** La `g` cambia el comportamiento de `.test()`, porque lleva un `lastIndex` interno: el segundo `test` puede devolver `false` aunque la regex sea correcta. La `i`, para ignorar mayúsculas y minúsculas, es la única que suelo pedir.
- **No la uses para validar entradas de seguridad críticas sin entender el patrón.** Una regex perfecta no te protege de una inyección SQL ni de un prompt injection. Eso es otro problema, y lo trato en [prompt injection y seguridad en apps con IA](/articulos/guias/prompt-injection-seguridad-apps-ia-2026/).

## Cómo practico yo

Mi rutina cuando toca un módulo de cadenas es simple: **una regex al día, explicada con palabras, y una tabla de entradas**. Cinco minutos. Al mes tienes treinta patrones distintos, y curiosamente los que uso de verdad en proyectos son cinco: validar un email, quitar espacios, partir una fecha, comprobar un número y escapar texto para meterlo dentro de otra regex.

Hay un truco más que uso cuando me atasco: pídele que la regex vaya al revés. Dile algo como «dime qué expresión regular describiría exactamente estas cinco cadenas, y nada más». Cuando te devuelve el patrón, lo lees e identificas qué carácter representa cada cosa. Enseñar y aprender funcionan en las dos direcciones.

Y la conclusión que te quiero dejar, porque es lo más importante: una regex no es un idioma que haya que aprenderse entero. Es un puñado de piezas con nombre, y con que te sepas las quince más usadas te defiendes en cualquier práctica y en cualquier entrevista corta. Si quieres, te paso la lista que uso yo; solo escríbeme a ivan@codeandia.com.

## Sigue por aquí

- [Los 8 prompts que me salvan el curso de DAW](/articulos/listas/8-prompts-programacion-daw-2026/)
- [Cómo leer código ajeno con IA: mi método de 4 pasos](/articulos/guias/leer-codigo-ajeno-con-ia/)
- [Aprender Java en DAW con IA y no volverte dependiente](/articulos/guias/aprender-java-con-ia-daw/)
