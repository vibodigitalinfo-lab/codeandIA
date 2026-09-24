---
layout: article
title: "Depurar con IA: mi método para que te arregle el código de verdad"
description: "Guía para depurar código con IA sin que te arregle el síntoma: reproducir, clasificar el error, dar contexto y pedir causa, no parche."
category: "Guía"
date: 2026-09-21
readtime: 7
---

Lunes por la tarde en el módulo de programación, delante del IntelliJ, con un `NullPointerException` que no había por donde cogerlo. El profe había dejado caer que "con una IA bien usada esto lo tienes en diez minutos", y ahí estaba yo: pegando el stack trace entero en el chat y recibiendo una respuesta que apuntaba a una línea que no era. La IA me había dado una pista (más o menos), pero yo no había sabido pedírsela. Metí la misma pregunta de otra forma, la IA me pasó un parche, y el código se rompió por otro lado. Ese día entendí que **depurar con IA no es preguntarle qué falla: es tener un método para que la respuesta te sirva**. Te cuento el mío.

## Lo primero: por qué el "por qué no funciona" no funciona

El error clásico de todos es abrir el chat y escribir *"no funciona, arréglamelo"*. La IA te devuelve algo, lo pegas, y a veces funciona porque sí. Pero no aprendiste nada y el parche suele ser un apósito: arregla el síntoma, no la causa. Con un simple fallo de compilación quizá te salves; con un error lógico de un array de apuntes que sale descolocado, el parche te va a estar persiguiendo toda la tarde.

El truco es invertir los papeles: **tú eres el detective, la IA es tu ayudante de laboratorio**. Ella lee y propone, pero la hipótesis y la comprobación son tuyas. Fue justo lo que me pasó con el `NullPointerException`: no necesitaba que me lo "arreglase", necesitaba que me dijera qué objeto podía ser null en esa llamada y por qué. Cuando pregunté eso, la respuesta encajó.

## Paso a paso: el método que uso en clase

Esto es lo que hago ahora cada vez que algo se rompe, y me ha quitado horas:

**1. Reproduce el error antes de tocar nada.** Si no puedes reproducirlo y explicarlo en una frase, no tienes un error, tienes un rumor. Con suelo hacer un "caso mínimo": quitar partes del código hasta que el fallo siga apareciendo. El mínimo reproducible es oro: se lo das a la IA y dejas de mandarle diez ficheros por si acaso. En DAW este paso es doblemente útil: montar el caso mínimo en un ejercicio de clase te obliga a entender qué parte del código depende de qué.

**2. Clasifica el error.** Antes de preguntar, decide qué tipo de fallo es:
- **Compilación**: el lenguaje te dice dónde. Este normalmente lo resuelve el propio IDE.
- **Runtime**: se la da en tiempo de ejecución (null, índices fuera de rango, conexión). Aquí la IA brilla: suele verlo rápido.
- **Lógica**: no hay error, pero el resultado es raro (te saca las notas descolocadas, el total no cuadra). Aquí es donde más se equivoca la IA si no le das contexto.

No es lo mismo "me da error al compilar" que "compila pero el total es incorrecto". Yo me di cuenta de que el 80% de mis preguntas mal hechas mezclaban estos tres casos sin decirlo.

**3. Dale contexto, no solo el error.** Mi plantilla favorita ahora es: *"Estoy haciendo X en [lenguaje/módulo]. Espero que pase Y, pero pasa Z. Este es el fragmento. ¿Por qué?"*. Ojo al "por qué": pido **causa, no parche**. Si la respuesta empieza con "aquí tienes el código corregido", paro y reescribo: le pido que me explique la causa primero y la solución después. Esto cambia todo, porque lo que yo necesito como estudiante es entender, no copiar.

**4. El parche también se revisa línea a línea.** Cuando me da una solución, la leo y pregunto *"¿qué has cambiado y por qué?"*. Si en la explicación no me cuadra algo, no lo pego. He pasado de "funciona" a "sé por qué funciona" y esa es la diferencia de la que hablo siempre en [la lista de errores que cometí programando con IA](/articulos/listas/errores-comunes-programando-con-ia/).

**5. Usa la IA para que escriba el test que reproduce**, no para arreglar. Si sospechas qué función falla, pídele un test pequeño que la ponga a prueba con tus datos. Verlo fallar primero y pasar después es la prueba de que estaba roto y de que el arreglo es de verdad. Esto engancha muy bien con [escribir tests con IA](/articulos/guias/escribir-tests-con-ia-2026/), porque el hábito de testear antes de arreglar es el mismo.

## Errores que cometí (para que no los repitas)

- **Pegar el error sin el contexto.** Un stack trace de Spring puede tener razón en una librería y no en tu código; sin contexto, la IA te va a apuntar a la librería y perderás la tarde. Le doy siempre: qué intento hacer, qué módulo, qué línea de mi código me señala.
- **Aceptar el primer parche.** La primera respuesta no es la más acertada; suele ser la más segura. Pedir *"¿hay otra forma de verlo?"* ha pillado errores que el primer intento no.
- **Dejar que me arregle lo que no entiendo.** Si no entiendo el código que me da, lo pido otra vez: *"explica cada línea como a alguien de primero"*. Si sigue sin entrar, lo más probable es que ni siquiera sea necesario ese fragmento, y ahí ya interviene [refactorizar sin romper nada](/articulos/guias/refactorizar-codigo-con-ia-sin-romper/).
- **Olvidar el "estado anterior".** Cuando el bug existía antes de un cambio tuyo, contárselo a la IA le evita "arreglarte" algo que ya iba bien. *"Esto ya venía pasando antes de tocar X"* es una frase que ahorra mucho.

## Lo que haría diferente

Si volviera a empezar, aprendería antes a **leer el stack trace por mí mismo**. La IA te lo resume, pero saber distinguir "la línea de mi código" de "la línea de la librería" es lo que te salva cuando el modelo no está inspirado. Hoy dedico un rato a practicarlo a mano con errores viejos, y cuando tropiezo, la IA me corrige: es la misma idea que teníamos para [aprender Java en DAW sin volverse dependiente](/articulos/guias/aprender-java-con-ia-daw/).

También haría **una buena config de contexto** (un `AGENTS.md` con las reglas del proyecto y tus módulos) nada más empezar: el modelo responde mucho mejor cuando sabe por dónde vas, y te lo cuento en [la guía de AGENTS.md](/articulos/guias/agents-md-guia-2026/).

## Mi veredicto

**Depurar con IA funciona de verdad, pero solo si el método está de tu lado.** La culpa casi nunca es de la IA: es de cómo le estamos pidiendo. Reproduce, clasifica, da contexto, pide causa y revisa línea a línea. Con esas cinco cosas, la IA pasa de "adivinadora de parches" a "compañera de depuración": te da la hipótesis, y tú decides si es cierta.

Y cuando la tengas bien montada, guarda los prompts que te funcionan. Yo tengo los míos para errores de compilación, runtime y lógica en [esta lista de prompts para corregir errores](/articulos/guias/mejores-prompts-chatgpt-corregir-errores-codigo-junior/). Si te atascas en un error concreto de tus módulos y no consigues que la IA te dé una causa que cuadre, escríbeme a ivan@codeandia.com con el código y te digo qué contexto le falta.