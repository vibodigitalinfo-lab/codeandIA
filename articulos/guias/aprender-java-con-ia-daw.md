---
layout: article
title: "Aprender Java en DAW con IA y no volverte dependiente"
description: "Cómo usar la IA para estudiar Java en DAW: prompts tutor, leer stack traces, ejercicios sin soluciones y la regla de no entregar código que no entiendas."
category: "Guía"
date: 2026-09-08
updated: 2026-10-17
readtime: 8
last_modified_at: 2026-10-18
---

Java es el primer mazazo del curso para casi todo el mundo en DAW. POO, herencia, las mil ventanas de `StackOverflow` abiertas a la vez… y ahora encima tienes una IA que te puede escribir la clase entera en dos segundos. La tentación es real y lo sé porque caí en ella. El problema no es Java ni la IA: es que copiar código de IA en este módulo es la forma más rápida de llegar al examen sin saber nada.

La buena noticia: usada bien, la IA es el mejor profesor particular que he tenido. Te explico el sistema que me funciona y que me ha hecho entender POO de verdad, no de memoria.

## Por qué las clases generadas no te enseñan

Cuando le pides a ChatGPT "dame una clase Empleado con herencia", recibes tres archivos perfectos. Los entregas, apruebas la práctica… y al día siguiente en el examen oral no sabes explicar por qué `super()` va dónde va. Firmaste un código que no puedes defender. Y en programación, quien no puede defender el código que firma, no sabe programar.

La regla que interioricé después de varios sustos: **la IA puede escribir código; tú tienes que poder explicarlo frase por frase.** Si no puedes, es tu problema, no de la IA. Es la misma regla que ya usé con SQL y con el módulo de la ruta del curso: nunca entregues lo que no entiendes.

## Los 5 prompts que me enseñan Java (y no me resuelven la vida)

**1. "Actúa como tutor de Java nivel principiante. No escribas código hasta que yo lo intente."** Con este prompt la IA deja de ser el que hace los deberes y se convierte en el profe que te corrige. Tú escribes tu intento, ella te dice qué está mal y por qué, y solo al final te muestra cómo se haría. Cambia la dinámica por completo.

**2. "Explícame este `Exception` sin decirme qué línea cambiar."** Esta es la joya. Pegas el stack trace completo y le pides la causa, no el parche. Aprender a leer un stack trace en Java es el 50% de aprobar: la IA te enseña a recorrerlo tú. Cuando entiendes qué te está diciendo `NullPointerException` en la línea 14, dejas de odiar Java.

**3. "Dame 5 ejercicios de [herencia / colecciones / JDBC] sin soluciones, y corrígeme el mío."** Reutilizo este patrón para todo. La IA te genera retos en orden de dificultad y corrige tu solución como un profesor. Es entrenamiento gratis con corrección inmediata, que es justo lo que no te da el instituto a las 11 de la noche.

**4. "Explícame hacia atrás: qué he aceptado de lo que acabo de copiar de Internet."** Cuando sí usas código de fuera (de la IA, de un tutorial), le pegas el fragmento y le pides que te lo explique **como si lo estuvieras defendiendo**. Es la forma más rápida de convertir texto ajeno en conocimiento propio.

**5. "Enséñame a depurar esto paso a paso, sin arreglarlo."** El último y quizá el más importante. Le pides que te guíe con el depurador (en qué breakpoint mirar, qué variables revisar). No es que arregle el bug: es que te enseña a encontrarlo, que es lo que se evalúa.

## El entorno: Eclipse y una IA que no te haga el trabajo

Una cosa que me costó aprender: **la IA te ayuda más cuando el proyecto compila y le das contexto real**. Si le pegas código a medias, adivina y se equivoca más. Mi kit para Java en DAW:

- **Eclipse.** Es el IDE con el que doy Java en el ciclo. No es tan moderno como VS Code ni tan cómodo como IntelliJ, pero es el que uso en clase y el que me voy a encontrar en muchas prácticas, así que me quedo con él en vez de repartirme entre dos entornos.
- **Claude, a diario.** Es la IA que uso para aprender Java: le pego el error, el fragmento o el enunciado y la llevo en modo tutor con los prompts de arriba. Sin salirme del plan que ya uso.
- **Cursor, solo el plan gratuito.** Lo he probado por encima y su chat contextual está muy bien para revisar código, pero no pago por él: con Eclipse para Java y el plan gratis de Cursor tengo de sobra para el módulo.
- Para las dudas de APIs o Spring, leo la **documentación actualizada**, como en la guía de tu primera API REST con Spring. La IA con contexto reciente responde mejor que la que trabaja solo de memoria.

Ah, y un matiz del currículo para que no te asustes: en el Real Decreto que regula tu ciclo (el RD 405/2023), Java vive en el módulo de Programación de primero (POO, excepciones, colecciones y JDBC) y **Spring no está en las enseñanzas mínimas** — es de cada centro. Así que lo que la IA te resuelva en el módulo de Java, casi siempre son fundamentos, no "aplicaciones de primavera".

## Los 4 errores que te delatan en el examen oral

Da igual cómo hayas llegado a tu código: hay errores que el profesor (y después el entrevistador) caza al momento:

**1. No leer el stack trace.** Piden "arréglalo" sin pegar el error, o pegan el trace y esperan que la IA piense por ellos. El que sabe prog, pega el trace y busca la línea.

**2. Saltarse POO.** Piden el código funcional directo y nunca entienden qué hace `abstract`, `interface` o cuándo reescribir `equals()`. Es el módulo entero: no te lo saltes.

**3. No revisar lo que genera la IA.** Aceptas 4 archivos de golpe sin mirar ni un diff. Cuando preguntan "¿y esto que hace?", en blanco. Revisa todo lo que firmas.

**4. Debug aleatorio.** "Cambia cosas hasta que funcione". La IA refuerza este vicio si la dejas: mejor quedarse quieto y trazar el flujo con el depurador.

## Mi veredicto

**Aprender Java con IA es la mejor decisión del primer año… si tú escribes, ella corrige.** La IA no te va a quitar el miedo a la POO, pero sí te ahorra las dos horas de "por qué no compila esto" y te enseña a depurar como lo haría alguien con experiencia. El coste real es cero (los models gratuitos sobran para esto) y el beneficio es que llegues al examen pudiendo defender **cada línea que entregas**.

Empieza esta tarde: abre tu proyecto, escribe una clase a mano con tu intento de herencia, y pídele el prompt 1 antes de que te dé la solución. Cuando la tengas, pídele el prompt 2 con el primer error que te salga y aprende a leerlo sola. Y si quieres, mándame tu temario al correo ivan@codeandia.com y te preparo una tanda de ejercicios tipo examen para entrenar con la IA.

## Sigue por aquí

- [Qué portátil necesita un estudiante de DAW: mi caso con i3 y 8 GB](/articulos/guias/que-portatil-comprar-estudiar-daw-2026/)
- [Prompts de ChatGPT para corregir errores de código (nivel junior)](/articulos/guias/mejores-prompts-chatgpt-corregir-errores-codigo-junior/)
- [Practicar la entrevista técnica junior con IA](/articulos/guias/simulacros-entrevista-tecnica-con-ia/)
