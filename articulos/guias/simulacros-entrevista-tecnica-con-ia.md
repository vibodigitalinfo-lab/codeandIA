---
layout: article
title: "Simulacros de entrevista técnica con IA para tu primer trabajo"
description: "Cómo practicar la entrevista técnica de tu primer trabajo de programador con IA: simulacros realistas, los ejercicios que más caen en DAW y cómo corregirte."
category: "Guía"
date: 2026-10-12
readtime: 9
last_modified_at: 2026-10-12
---

Casi nadie te lo avisa en clase: el título de DAW no te da trabajo, te da derecho a que te hagan una entrevista. Y esa entrevista tiene una parte técnica que casi nadie practica, y menos de la forma en que se da. No hay temario, no hay simulacros y la mayoría de la gente llega sin haber dicho en voz alta una línea de código delante de nadie.

La IA te sirve aquí para algo muy concreto: no para darte las respuestas, sino para **hacerte las preguntas**. Un modelo al que le pides que actúe de entrevistador te monta un simulacro en dos minutos, te aguanta las rondas que hagan falta y no se cansa de ti. Lo que sigue es cómo aprovecharlo sin convertirlo en un atajo inútil.

## Qué te preguntan de verdad

Antes de practicar hay que saber contra qué. Para un perfil junior de DAW, la entrevista técnica suele tener cuatro bloques:

- **Live coding.** Un ejercicio pequeño delante de alguien, casi siempre sobre arrays, cadenas, colecciones o una consulta SQL. No buscan la solución más limpia: buscan que pienses en voz alta mientras la escribes.
- **Prueba para casa.** Un mini proyecto con tiempo límite. Aquí se evalúa el proceso: cómo troceas el problema, qué commits haces, si hay un README que explique las decisiones.
- **Tu propio proyecto.** Te preguntan por algo que has entregado. Es donde más gente se hunde, no por falta de nivel, sino por no acordarse de por qué tomó cada decisión.
- **Fundamentos.** Git, POO, bases de datos, el framework del puesto. Preguntas cortas que se van sumando.

Si no practicas cada bloque por separado, el simulacro se queda en "hazme una entrevista" y sale tan genérico que no te prepara para nada.

## El prompt para que la IA haga de entrevistador

El truco está en darle contexto y reglas. Sin eso, la IA te suelta un cuestionario de repaso, que no es lo mismo que un simulacro:

> Vas a ser el entrevistador técnico de una empresa que busca desarrollador junior. Estoy terminando DAW: manejo Java, algo de JavaScript y bases de datos relacionales. Hazme **una sola pregunta** por turno y espera mi respuesta. No me des la solución: si me atasco, dame una pista pequeña. Al final de cada turno, ponme una nota del 1 al 5 y explica por qué.

Cuatro reglas que marcan la diferencia:

1. **Una pregunta por turno.** Si te suelta tres de golpe, dejas de responder como responderías en una sala.
2. **Que no te dé la respuesta hasta que se la pidas.** Si te la suelta al primer fallo, no estás practicando: estás leyendo.
3. **Que te obligue a razonar en voz alta.** Pídele que te pregunte por tu razonamiento antes de decirte si está bien.
4. **Que te corrija con una rúbrica.** Sin nota ni explicación no hay forma de saber si mejoras.

Guarda ese mensaje en un archivo y pégalo al empezar cada sesión. Tardas cero y el simulacro cambia por completo.

## Los ejercicios que más caen

No hace falta preparar mil ejercicios. Con estos cinco bloques cubres la mayoría de lo que te pueden pedir de junior:

- **Cadenas y arrays.** Invertir, contar, buscar duplicados, ordenar por un criterio. En Java, manejar con soltura `String`, `List` y `Map`.
- **SQL.** Un `JOIN`, un `GROUP BY` con `HAVING` y saber explicar la diferencia entre `WHERE` y `HAVING`. Cae muchísimo.
- **POO.** Explicar herencia frente a composición, qué es una interfaz y cuándo la usarías en lugar de una clase base.
- **Git.** Qué hace `rebase`, en qué se diferencia de `merge` y qué harías si te has equivocado de rama.
- **Tu stack.** Las tres o cuatro cosas de tu framework que no sabes explicar sin mirar.

Pídele a la IA que te prepare un ejercicio de cada bloque y que, cuando falles, te diga **en qué concepto has fallado**, no solo la respuesta correcta. Ahí está el valor: la respuesta la olvidas, el concepto no.

## Convierte tu propio proyecto en preguntas

Esta es la parte que casi nadie prepara y la que más duele. Te van a preguntar por tu proyecto final o por la práctica que entregaste, y no te vas a acordar de nada. No es que no lo entiendas: es que han pasado meses.

Dale a la IA un resumen de tu proyecto o su README y pídele esto:

> A partir de esta descripción de mi proyecto, hazme diez preguntas que me haría un entrevistador técnico para comprobar si de verdad lo entiendo: por qué elegí esta base de datos, por qué separé el código así o qué haría si el proyecto creciera diez veces. No me des las respuestas.

Si hay alguna que no sabes contestar, acabas de encontrar el hueco que te habría hundido en la entrevista. Mejor descubrirlo ahora que delante del entrevistador.

## Cómo practicar el live coding de verdad

Un chat no es un live coding, porque en la entrevista hay reloj, hay alguien mirando y no hay autocompletado. Para acercarte todo lo posible:

- **Ponte un tiempo.** Veinte minutos para un ejercicio pequeño. Se te va a olvidar el tiempo igual que en la entrevista real.
- **Sin autocompletado.** Desactiva las sugerencias de IA del editor. En la entrevista no vas a tener Copilot al lado.
- **Habla en voz alta y grábate.** Suena ridículo y es incómodo, pero es la única forma de practicar la parte que de verdad se evalúa.
- **No busques la solución.** Si te atascas, pide una pista, no la respuesta.

## Lo que la IA no te puede dar

Conviene tenerlo claro para no confundir un buen simulacro con estar preparado:

- **Los nervios.** Escribir delante de alguien con el reloj corriendo no se parece a escribir en tu habitación. Eso solo se entrena con público.
- **La conversación.** El entrevistador no mira solo si resuelves: mira si serías un compañero razonable. Eso se practica con personas.
- **El código que no es tuyo.** Si la IA te da una solución perfecta que no entiendes, en la entrevista se nota a la primera pregunta de seguimiento.

Por eso el simulacro con IA es la mitad del entrenamiento, no el entrenamiento entero. La otra mitad la cubres con un compañero de clase haciéndote de entrevistador, aunque no tenga ni idea del tema. Con eso ya entrenas los nervios.

## Errores que arruinan el simulacro

- **Pedir solo respuestas.** Convertir la IA en una chuleta no engaña a nadie el día de la entrevista.
- **Cambiar de ejercicio cada vez que te atascas.** Aguanta hasta el final, como en la sala.
- **No repasar los fallos.** Si no vuelves a hacer el ejercicio que te salió mal, el simulacro sirvió de poco.
- **Memorizar la solución.** Repetir el mismo ejercicio hasta sabértelo de memoria no es aprender a resolver.

## Un aviso de ética, en tres líneas

Usar la IA para prepararte es legítimo y hasta recomendable. Usarla para resolver una prueba técnica que te han puesto es otra cosa. La mayoría de procesos lo detectan con preguntas de seguimiento o mirando el historial de commits, y aunque no lo detecten, te estarías contratando para un puesto que no vas a poder sostener. Prepara con la IA; responde tú.

## Cómo saber si has mejorado

Lleva un registro feo pero útil: por cada sesión, apunta el ejercicio, la nota que te pusieron y el concepto que fallaste. En dos semanas verás repetirse los mismos conceptos: ese es tu temario de verdad. Cuando dejen de repetirse, el simulacro ya no te aporta y toca practicar con personas.

Al final, la entrevista técnica es como el código: no se aprende leyéndola, se aprende escribiéndola mal y corrigiéndola. La IA solo te da la rueda para poder hacerlo muchas más veces de las que harías solo.

## Sigue por aquí

- [De las prácticas al primer empleo con IA](/articulos/guias/de-practicas-a-primer-curro-con-ia/) — lo que va antes y después de la entrevista.
- [El portfolio que consigue prácticas de DAW](/articulos/guias/portfolio-que-consigue-practicas-daw/) — el proyecto del que te van a preguntar.
- [Aprender a programar con IA sin volverte dependiente](/articulos/guias/aprender-programar-con-ia-sin-volverse-dependiente/) — la línea que no conviene cruzar.
