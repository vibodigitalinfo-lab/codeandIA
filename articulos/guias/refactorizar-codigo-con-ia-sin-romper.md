---
layout: article
title: "Refactorizar código con IA sin romper nada: mi proceso"
description: "Cómo refactorizar código con IA en 2026 sin romper nada: git en rama, tests antes, prompts seguros, revisión de diffs y los límites reales de los agentes."
category: "Guía"
date: 2026-09-20
readtime: 7
---

Hay un escalón que todo estudiante sube tarde: al principio da miedo escribir código, y meses después da más miedo **tocarlo**. Llega el proyecto del trimestre, juntas 800 líneas que funcionan "a ver si mañana", y la idea de refactorizarlas te da más respeto que el examen. La tentación de abrir un chat de IA y soltarle "refactorízame todo esto" es enorme. La he probado: el resultado es una base de código que no reconozco y una noche entera arreglando lo que "refactorizó". Ese es el camino malo.

El camino bueno es un flujo, y te lo dejo aquí. No elimina el riesgo, pero lo convierte en algo que puedes controlar con git.

## Regla 1: la IA no toca nada sin una rama y una red de seguridad

Antes de que la IA vea una sola línea, hago tres cosas:

1. **Confirmo lo que hay.** `git commit` del estado actual. Aunque sea feo, este es mi punto de retorno.
2. **Creo una rama por petición.** Una rama por tarea de refactor (`ai/refactor-clase-Cliente`, por ejemplo). Así si un cambio sale mal, la deshago en una línea y el resto del código ni se entera. Este patrón ("una rama por petición") es la práctica que más recomiendan en 2026 para trabajar con IA en git, y por algo será: vuelve el riesgo manejable.
3. **Escribo tests antes de tocar nada.** Si el proyecto no tiene tests (lo normal en el primer año), le pido a la IA que me genere **tests de caracterización**: tests que capturan lo que el código hace AHORA, aunque sea feo. Cuando esos tests pasan, empieza a refactorizarse. Si tras el cambio los tests siguen pasando, no has roto el comportamiento aparente.

Con esto ya puedes permitirte equivocarte.

## Regla 2: el prompt tiene que pedir "sin cambio de comportamiento"

El prompt de refactor más común es "refactorízame esto" y es el peor: no le das al modelo qué significa "mejor". Lo que yo uso es:

> "Refactoriza [clase/archivo] para mejorar [readabilidad | quitar duplicación | separar responsabilidades] pero **sin cambiar el comportamiento observable**. Plantea primero el plan en 4 pasos y no edites hasta que lo apruebe. Ejecuta los tests al final y enséñame el diff."

Nota las tres piezas: **objetivo concreto**, **plan antes de tocar**, y **tests al final**. Sin eso, el modelo vuela por libre y hace lo que le parece más bonito, que no siempre es lo que tu proyecto necesita.

## Regla 3: los agentes se usan en modo "poco a poco", no "all-in"

He probado los dos extremos. El modo "agente autónomo, hazlo todo" es espectacular y desastroso a partes iguales. Lo que funciona:

- **Primera pasada en solo lectura.** Claude Code y Cursor tienen forma de explorar sin editar. Primero le digo "audita este proyecto en read-only y dime qué cambiarías y en qué orden". Nada de editar.
- **Refactor por incrementos pequeños.** Le pido UNA clase, no el proyecto. Si me sale un diff de más de 200-250 líneas o que toca 5 archivos, le pido que lo parta. Los diffs pequeños se revisan; los grandes, se rezan.
- **El humano aprueba cada paso.** Literalmente: los agentes de Cursor te enseñan el diff en vivo y te dejan "restaurar checkpoint". En GitHub, el copiloto-agente abre la rama, edita, ejecuta tests y te pone la PR **esperando tu aprobación**; la CI ni siquiera corre hasta que tú la dejas. Esa es la dinámica sana: la IA propone, tú decides.

## Regla 4: revisa el diff como si te lo mandara otra persona

Esto es lo que más separa al que mejora del que se hunde. Cuando la IA termina, abro `git diff` y lo **reviso como si fuera una PR de un compañero**: ¿qué cambia?, ¿por qué?, ¿añadió tests?, ¿borró algo que no debía? Si alguna parte no la entiendo, la deshago o le pido explicación antes de aceptarla. La regla de oro del artículo de [git con IA](/articulos/guias/git-con-ia-2026/) aplica aquí al pie de la letra: no firmes ningún cambio que no puedas defender.

Y para la segunda lectura, existen revisores automáticos: **CodeRabbit** (tiene plan gratuito básico y te marca bugs y seguridad en cada PR) y **Qodo/PR-Agent**. No son mágicos, pero cazan cosas que se te escapan en un refactor de 300 líneas. De los dos hablé en [esta comparativa de testing con IA](/articulos/comparativas/qa-wolf-vs-qodo-ai-testing-estudiantes/) y en la [review de CodeRabbit](/articulos/reviews/coderabbit-review-ai-code-review/): sirven de segunda opinión, no de dueño de tu código.

## Los límites que nadie te cuenta

Sé honesto con lo que la IA **no** hace bien, porque en 2026 la evidencia ya es clara:

- **No ve el negocio.** Le puedes decir "esto es un CRUD de matrículas", pero no sabe que *"los alumnos sin nota de septiembre no se borran"* es la regla que no está escrita en ninguna parte. Esa intuición la tienes tú.
- **El contexto es finito.** Cuanto más grande es tu proyecto, peor retiene la primera mitad del código. Por eso los refactors de "todo el proyecto de golpe" fallan: no es que la IA sea tonta, es que no cabe todo en su ventana.
- **No siempre mejora.** Hay evidencia (estudios grandes de 2026) de que la IA puede **aumentar los "code smells"** al refactorizar si la dejas sola — hace el código más "bonito por fuera" y más feo por dentro. El humano que revisa es lo que evita eso.

Por eso el flujo no es "suelta al agente": es "agente propone, tests verifican, tú decides, y el diff se revisa".

## Lo que haría diferente

Si tuviera que repetir mi primer refactor con IA, haría dos cosas distintas: **escribiría los tests de caracterización yo mismo** (la primera vez se los encargué a la IA y tardé dos días en fiarme de que los tests hicieran lo que decían) y **partiría el trabajo en 4 ramas pequeñas en vez de 2 medianas**. El resto del proceso lo mantendría clavado: git primero, esta vez sí que sí.

## Mi veredicto

**Refactorizar con IA, bien hecho, es una de las habilidades que más te van a pagar en el primer curro** — el código heredado existe en todas las empresas y quien lo toca sin miedo vale oro. Y el "sin miedo" se consigue con un flujo, no con valor: rama por petición, tests antes, diffs pequeños, revisión humana.

Ese es exactamente el tipo de práctica que te van a examinar: trabajar en ramas limpias, que la CI pase y poder explicar cada cambio que haces. Dominarlo ahora, en tus prácticas de clase, es media entrevista técnica ganada. Si quieres que te prepare una práctica real de refactor con IA (código feo + tests de caracterización + revisión), escríbeme a ivan@codeandia.com y te la dejo montada.