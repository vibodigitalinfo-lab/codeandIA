---
layout: article
title: "Cómo aprendo Java con IA sin volverme dependiente"
description: "Cómo uso la IA para estudiar Java: los ejercicios de clase, las correcciones y por qué no entrego código que no entiendo."
category: "Guía"
date: 2026-09-08
updated: 2026-10-26
readtime: 7
last_modified_at: 2026-10-26
---

Java es el primer mazazo de primero de DAW, el ciclo de FP de desarrollo de aplicaciones web en España. Encima llevas una IA que te puede escribir la clase entera en dos segundos, y la tentación de copiarla tal cual es enorme.

Yo ya he caído en eso. Copié código generado por la IA sin entenderlo en el módulo de Java y me di cuenta. Ese es exactamente el problema: no que la IA escriba mal, sino que tú te quedes con algo en las manos que no sabes explicar.

Eso fue lo que me hizo cambiar el enfoque. Desde entonces tengo una regla clara: **solo entrego lo que sé defender**.

## Cómo lo estudio en casa

En clase no siempre sale todo claro. A veces da pereza, las clases son largas y es fácil distraerse, así que muchas veces prefiero dejarlo para casa y atacarlo allí con calma.

Lo que hago es pasarle a Claude los ejercicios que hemos hecho en clase, contarle cómo los hace el profesor y cómo quiere que los hagamos nosotros, y a partir de ahí pedirle más ejercicios (enseño mi código real, con fallos incluidos, en [mis ejercicios de Java de primero](/articulos/guias/ejercicios-java-basicos-daw/)), correcciones y explicaciones. En la práctica es como tener un profesor de programación cuando te pones: le explico cómo trabaja el mío en clase y me prepara ejercicios al mismo estilo, ajustados a lo que estoy viendo.

La parte de las explicaciones es la que más me aporta. Ir viendo, preguntando y recibiendo correcciones hace que al final se vaya entendiendo todo. No te voy a decir que sea fácil, pero una vez que lo ves, va todo sobre ruedas.

## Un ejemplo real: los dos días antes del examen de Java

Dos días antes de mi primer examen de Java le escribí a Claude más o menos esto: «Tengo examen de Java en 2 días, sé que aún no es mucho nivel, pero necesito ayuda». Le pasé los enunciados que habíamos hecho en clase y, para no mandarle todos los archivos, solo el último ejercicio, que era el más completo. Y le puse una condición: todavía no habíamos visto `if` ni controlar que no salgan resultados negativos, así que no quería que me lo pidiera ni que me lo marcara como fallo.

A partir de ahí hicimos una especie de bucle:

1. Claude me preparaba un **examen de práctica** al estilo de los de clase: un zoo con animales, visitantes y cuidadores, o una escuela de música con instrumentos, alumnos y profesores.
2. Yo lo hacía en Eclipse.
3. Le pasaba mis clases y me lo corregía con la rúbrica del profesor: qué criterio cumplía, cuál no y por qué, con la línea exacta que fallaba.

Hice cinco, y esta es la nota que me estimó en cada uno:

![Gráfica de las notas estimadas por Claude en mis cinco exámenes de práctica: 7, 7,5, 6,5, 8,5 y 8,9](/assets/img/java-notas-examenes-practica.svg){: width="640" height="300"}

No es una línea recta, pero lo importante no era la nota, sino ver qué fallo se repetía. Los errores de cálculo desaparecieron pronto. El que se me quedó hasta el final fue **olvidarme de un método que el enunciado pedía**: un `getRecaudacion()` en el zoo, un `getNombre()` y un `getIngresos()` en la escuela de música. El código funcionaba, pero si el enunciado dice «debe tener un método que devuelva…» y no está, te quitan puntos. El consejo que me dio para el examen: antes de entregar, **subrayar cada método que nombra el enunciado y tacharlo cuando lo encuentres en tu código**.

### Cuando la IA no tiene razón del todo

En una corrección me penalizaba por no reutilizar métodos y por escribir `Aplicacion app = new Aplicacion();` en el `main`, que en Eclipse sale como aviso amarillo. Le contesté que mi profesor lo hace así y no reutiliza esos métodos, así que yo tampoco. Lo aceptó y me recalculó la nota, pero me hizo una precisión: **en la forma, sigue el estilo del profesor; pero lo que dice el enunciado manda**. Si pide un método o un `double`, hay que ponerlo aunque en clase no se haga.

Esto es importante: la IA no sabe cómo trabaja tu profesor si no se lo dices, y a veces te corrige cosas que en tu clase están bien. Hay que leer la corrección con criterio, no tragártela entera.

### El examen de verdad

La noche antes le pregunté hasta cómo se exporta un proyecto en Eclipse para entregarlo (clic derecho en el proyecto, *Export*, *General*, *Archive File* y guardarlo en ZIP). Después del examen le pasé lo que había entregado. Mis cálculos estaban bien, pero tuve un fallo de diseño: un objeto que tenía que crear otro dentro de su constructor lo recibía desde fuera. En el `main` creé uno solo y se lo pasé a dos objetos distintos, así que compartían ese objeto interno y sus datos se mezclaban. Otra vez, todo venía de una frase del enunciado, y otra vez faltaba un método que devolviera un valor.

Me estimó alrededor de un 7, quizá algo más si el profesor no tenía en cuenta un cálculo que nos dijo que daba igual. La nota oficial fue un **8,6**, bastante más de lo que esperaba. La estimación de Claude me sirvió para ver mis fallos, pero se quedó corta con la nota: al final, quien corrige es el profesor.

## Qué uso y para qué

- **Eclipse**: es el IDE con el que doy Java en clase, y es donde me lo encuentro cada día.
- **Claude, a diario**: para pasarle errores, enunciados y dudas.
- **ChatGPT**, con el plan gratuito: para crear imágenes, y de vez en cuando como respaldo cuando falla Gemini, pero rara vez.
- **Cursor**, solo con el plan gratuito. De pago no tengo nada.

## Qué evito

No entrego código que no entiendo. Antes de dar una solución por buena la hago mía: la leo, la explico y, si hace falta, la rehago a mano para comprobar que de verdad la tengo. Cómo lo aplico cuando llegan los exámenes lo cuento en [cómo estudio para exámenes de programación con IA](/articulos/guias/estudiar-daw-con-ia-sin-copiar-codigo/).

También evito el «a ver si funciona». Si algo no va, miro el error y pregunto por la causa, en vez de ir cambiando cosas hasta que por fin arranca.

## En corto

La IA no me ha quitado el trabajo de entender Java, y para eso está bien: explica, corrige y da práctica. La parte de pensar sigue siendo mía, y es justo la que quiero quedarme.
