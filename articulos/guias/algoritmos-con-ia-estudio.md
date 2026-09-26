---
layout: article
title: "Algoritmos con IA: cómo estudiar sin que te haga los ejercicios"
description: "Cómo estudiar algoritmos y estructuras de datos con IA sin que te haga los ejercicios: método por fases, prompts que te obligan a pensar y qué pedir si fallas."
category: "Guía"
date: 2026-09-23
readtime: 9
---

Hay un ejercicio donde la IA es peligrosamente buena: los algoritmos. Le pides "búsqueda binaria" y te devuelve una implementación impecable, con Big O anotado y los casos límite ya cubiertos. En treinta segundos tienes la solución que en un examen te habría costado veinte minutos. Y ese es exactamente el problema.

El ejercicio **es** el aprendizaje. Si la IA te lo resuelve, te quedas con una solución que reconoces pero que no sabes reproducir. Y el día que aparezca en un examen sin red, descubres que no la sabías hacer: solo la sabías leer.

Después de llevar dos años usando IA para todo, mi regla es esta: **la IA no escribe el algoritmo, lo juzga**. Te explico el método por fases que uso, que es lo contrario de pedir la solución.

## Fase 0: escribe tu versión cutre antes de abrir el chat

Antes de escribirle nada a la IA, escribe lo primero que se te ocurra. Lo más burro que funcione: recorrer la lista entera comparando uno a uno, aunque sea `O(n²)` y aunque tarde una eternidad.

Esto no es opcional ni opcionalmente recomendable. Sin esa versión cutre no tienes contra qué medir, y el motivo real por el que existen las estructuras de datos es precisamente que las versiones cutres no escalan. Si nunca has sufrido la lentitud, no entiendes por qué el mapa existe.

Un `for` doble con dos `if` mal puestos es un punto de partida perfectamente válido. Es feo y funciona. Sigue.

## Fase 1: pide pistas, no respuestas

Este es el prompt que uso literalmente, y funciona porque está diseñado para no darte nada:

> "Voy a resolver X. No me des la solución todavía. Hazme una sola pregunta cada vez que te responda, y solo si me equivoco me dices en qué concepto estoy fallando. Empieza preguntándome por los casos límite que tengo que considerar."

Lo que hace es convertir a la IA en un examinador, que es el rol en el que sí es buena. Te va a preguntar por la lista vacía, por un solo elemento, por duplicados, por el orden. Esas son exactamente las cuatro cosas que luego te salvan el ejercicio, y las estás pensando tú, no leyéndolas.

Si se lo pides bien, ni siquiera te da el código en el segundo turno. Te dice *"bien, ya has cubierto el caso vacío. ¿qué pasa si el array tiene un único elemento?"* y eso es justo lo que necesitabas oír.

## Fase 2: que critique tu código, no que lo reemplace

Cuando ya tengas algo escrito, la pregunta cambia por completo. Ahora sí quieres código ajeno, pero del tipo que te hace pensar:

> "Aquí va mi solución. No me la reescribas. Dime solo tres cosas: dónde se va a romper, qué caso no he contemplatesdo, y si hay una forma más simple de escribir lo mismo."

Esta fase es la que más rinde y la que menos cuesta. Estás pasando tu código por un revisor que te señala los agujeros sin quitarte la responsabilidad de arreglarlos. Si en la fase 1 el modelo te daba pistas, aquí te devuelve las correcciones de tu versión concreta, que es información mucho más valiosa que una solución genérica.

Un aviso: si le pides "corrígemelo", te devuelve el código corregido y no aprendes. Si le pides "dime qué está mal", te devuelve un diagnóstico y lo arreglas tú. La diferencia entre esas dos frases es la diferencia entre practicar y ver.

## Fase 3: donde la IA sí te sirve de verdad

Hay una fase donde la IA es tu herramienta ideal y no debes sentirte culpable: **los tests y los casos límite**.

> "Escribe los casos de prueba para este problema: vacío, un elemento, todos iguales, ordenados, con negativos, y un caso grande que revele el rendimiento."

Los tests son la parte aburrida de los ejercicios y la que menos te enseña a escribir a mano. Delegarlos en la IA no es trampa, es reparto de trabajo inteligente. Además, los tests son el mejor detector de errores que vas a tener nunca: si tu algoritmo pasa el test de mil elementos aleatorios, es que casi con total seguridad funciona.

Ahí es donde la IA te ahorra tiempo de verdad, y donde no debes sentir culpa por usarla.

## La recursión es el caso especial

Si hay un tema donde dejarse llevar por la IA es especialmente dañino, ese es la recursión. Es un tema que **se** aprende **confrontando** la base y el caso recursivo una y otra vez hasta que te sale sin pensar.

Cuando le pides a un modelo "escribe recursión para recorrer un árbol binario", te devuelve algo sintácticamente perfecto y pedagógicamente inútil: una función que copias y pegas sin entender por qué el `null` va donde va. Y no es culpa del modelo, es que la recursión no se explica, se practica.

Mi consejo aquí es más duro que en el resto de fases: **la recursión no se toca con la IA hasta que la hayas implementado a mano al menos tres veces**. Punto. Después, cuando la tengas automatizada, usarla para entender variantes es otra historia.

Si la recursión se te resiste, el problema casi nunca es la falta de ejemplos, sino la falta de práctica deliberada: pocas repeticiones y sin corregir los errores.

## Estructuras de datos: cuáles te van a pedir de verdad

Para DAW no te aprendas todas. Estas cuatro cubren el 90% de lo que te van a preguntar, en este orden de utilidad real:

1. **Array y lista enlazada**: la base. Entiende de verdad la diferencia entre acceso por índice y acceso secuencial.
2. **Pila (stack)**: paréntesis balanceados, deshacer, y la gestión de llamadas. Es pequeña y aparece mucho.
3. **Cola (queue)**: procesamiento en orden, BFS.
4. **Mapa o diccionario**: hash, `HashMap` en Java, `Map` en JS, `dict` en Python. Es la estructura más usada en la vida real con diferencia.

HashMaps, árboles y grafos quedan para segundo curso. Si te absorben ahora, no avanzas. La estrategia correcta es dominarlas bien y tenerlas fichadas; nadie te va a preguntar por un AVL en un examen de primer año.

## El día del examen: qué hacer con la IA

La pregunta que me llega por DM siempre es la misma: *"¿puedo usarla en el examen?"*. Mi respuesta es que la pregunta está mal planteada. La relevante es otra: **¿sabes hacerlo sin ella?**

Si lo sabes, la IA solo te hace más rápido y no te aporta nada. Si no lo sabes, la IA es un examen en modo listón muy fino: te da la respuesta perfecta, te da un 10, y el día que curras en una entrevista real no te sirve de nada.

La prueba de fuego no es el examen, es la entrevista. Ahí no hay ChatGPT al lado, hay un Senior mirándote las manos. Y a ese Senior no le vale de nada una búsqueda binaria que sabes que funciona porque la pegaste. Así que estudia con el ordenador cerrado primero, y usa la IA para entender la duda que te queda después. En ese orden.

## Mi veredicto honesto

La IA no está bien ni mal para aprender algoritmos. Depende de en qué fase la pongas. Ponerla en la fase de "dame la solución" es como pedirle a un compañero que te haga los ejercicios de clase: te da la nota y no te da el oficio. Ponerla en la fase de "hazme preguntas y dame pistas" es como tener un buen profesor particular que nunca te regala el resultado.

La diferencia entre las dos no es el modelo que uses. Es si has escrito algo antes de abrir el chat. Ese es todo el truco.

## Resumen del método

- Escribe tu versión cutre siempre primero. Sin excepción.
- Pide pistas y preguntas, nunca la solución.
- Pide críticas sobre tu código, no que lo reescriba.
- Delega los tests sin culpa: ahí sí te ahorra tiempo real.
- La recursión a mano tres veces antes de tocar la IA.
- Domina array, pila, cola y mapa. El resto, para segundo curso.

Es más trabajo que copiar y pegar la respuesta. También es la diferencia entre saber programar y saber escribir código.

*Si te interesa el resto del método para no depender de la IA, te lo expliqué en [Programar con IA sin volverte dependiente](/articulos/guias/aprender-programar-con-ia-sin-volverse-dependiente/). Y si quieres los prompts concretos que uso en cada fase, están en [Los 8 prompts que me salvan el curso de DAW](/articulos/listas/8-prompts-programacion-daw-2026/).*

## Sigue por aquí

Si ya tienes claro cómo pedir ayuda sin que te lo resuelvan todo, el siguiente paso es afinar el proceso: [preparar exámenes prácticos de DAW con IA](/articulos/guias/preparar-examenes-practicos-daw-con-ia/) y [escribir tests con IA en 2026](/articulos/guias/escribir-tests-con-ia-2026/), que es justo la fase 3 de este método aplicada a tu código real.

- [Programar con IA sin volverte dependiente: guía para estudiantes DAW](/articulos/guias/aprender-programar-con-ia-sin-volverse-dependiente/)
- [Los 8 prompts que me salvan el curso de DAW (con ejemplos reales)](/articulos/listas/8-prompts-programacion-daw-2026/)
