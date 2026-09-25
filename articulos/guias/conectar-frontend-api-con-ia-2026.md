---
layout: article
title: "Conectar tu frontend al API con IA: la guía de DAW que falta en clase"
description: "Del HTML a la API real: cómo conectar tu frontend de DAW a un backend con fetch, resolver CORS y generar el código con IA sin morir en el intento."
category: "Guía"
date: 2026-09-08
readtime: 5
---

El módulo de cliente y el de servidor van cada uno por su lado hasta el día que te piden juntarlos, y ahí empieza el caos: tu HTML de toda la vida llamando a tu API de Spring Boot, y el navegador poniéndote una barrera roja. Esta guía es el puente que no me contaron en clase: cómo conectar el frontend a un API real usando la IA como traductora entre dos mundos que ella conoce muy bien.

## Antes de empezar: el fetch y por qué te hará falta

Conectar un frontend a un API significa, en su forma más simple, que JavaScript le pida datos a otra parte de la red y los pinte en la página. La herramienta es `fetch`, que va con el propio lenguaje, sin instalar nada:

```javascript
fetch("http://localhost:8080/api/alumnos")
  .then(r => r.json())
  .then(alumnos => console.log(alumnos));
```

Ese bloque parece trivial, pero detrás hay dos trampas que van a aparecer sí o sí, y aquí está lo bueno: si ya hiciste la API con mi guía de Spring Boot, estos son los dos puntos donde ella y tú te chocáis.

## La trampa número uno: los nombres de los campos

Tu API devuelve JSON con unos nombres de propiedad concretos, y tu JavaScript los usa buscándolos literalmente. Si en Java el campo se llama `nombreCompleto` y en el frontend escribes `nombre`, te devuelve `undefined` sin avisar ni una vez. No es un error que salte: es silencio.

Mi técnica con la IA: primero imprimo el JSON real con `console.log(alumnos)`, se lo enseño, y le pido: "genera la función que pinta cada alumno en una tabla usando exactamente estos campos, sin inventar ninguno". El JSON real como contexto mata el 90% de los malentendidos.

## La trampa número dos: CORS, el bloqueo del navegador

Aquí llega la dichosa barrera roja. Si tu frontend está en un sitio y la API en otro (distinto puerto cuenta como distinto sitio), el navegador bloquea la petición por seguridad y te muestra el clásico "has been blocked by CORS policy". El mensaje da miedo, pero la solución es sencilla: la API debe decir al navegador "este otro origen puede llamarme".

En Spring Boot, la forma más rápida para tu proyecto de DAW es el `@CrossOrigin` en el controlador, que ya dejé resuelto en la guía de la primera API. Punto importante: la IA te va a proponer un montón de configuraciones de CORS con filtros y beans; para un proyecto de clase, el `@CrossOrigin` basta y es mucho más fácil de explicar cuando te pregunten.

## El patrón que te saca de apuros: pintar, enviar y esperar

Una vez superadas las dos trampas, el flujo de un CRUD clásico es siempre el mismo triángulo:

1. **Pintar**: cargar la lista al abrir la página y generar los elementos con el JSON real.
2. **Enviar**: un formulario HTML que en el `submit` hace un `POST` con los datos. Dos errores típicos aquí: no poner `type="button"` en el botón (la página se recarga y pierdes todo) y no cambiar el fetch a `POST` con el `body` correcto en JSON.
3. **Esperar**: la petición es asíncrona. Mientras llega, la página debería mostrar algo, aunque sea un "cargando...", porque si no, da la sensación de que la app está muerta.

La IA genera este triángulo muy bien, pero una vez más ganas más pidiéndole el patrón que la solución del ejercicio concreto: "explícame el flujo para cargar una lista y enviar un formulario con fetch, paso a paso". Así te llevas la plantilla y la entiendes, en vez de depender de ella para cada pantalla.

## Depurar cuando "no hace nada"

El momento más frustrante es cuando el código parece correcto y la página no pinta nada. Mi orden de revisión, siempre el mismo:

- **La pestaña Red (Network)** del navegador: ¿la petición salió? ¿Qué status devolvió? Si ves el 200 y luego nada en pantalla, el fallo está en tu JavaScript, no en la API.
- **La consola**: los `undefined` de los nombres de campo aparecen aquí.
- **El formato**: ¿es JSON de verdad? Hay APIs que devuelven el contenido con `Content-Type` raro y `r.json()` explota.

Lección que pagué cara: "arregla este fetch" a la IA sin contexto es inútil. "El fetch devuelve 200 pero no pinta nada y en consola sale undefined en 'nombre', aquí está el JSON y la función" — ese prompt sí vale. Igual que en la guía de corregir errores, el error se arregla solo cuando consigues ponérselo delante con detalle.

## El veredicto

Conectar el front y el backend es el momento en que tu proyecto de DAW pasa de "ejercicios sueltos" a "parece una aplicación de verdad". El camino es corto: un `fetch`, controlar CORS, no inventar nombres de campos y saber mirar la pestaña Red cuando algo falla. La IA te va a ahorrar horas de escribir JavaScript repetitivo, pero el que tiene que saber qué campos espera el API eres tú. Si tu frontend y tu API se pelean y no sabes si el problema es de formato o de CORS, me pegas el error y me dices qué devuelve la pestaña Red, y te digo dónde está el fallo.