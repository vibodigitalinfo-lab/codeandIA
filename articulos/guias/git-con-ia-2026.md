---
layout: article
title: "Git con IA: mensajes de commit, rebase y blame asistidos"
description: "Aprende a usar Git con IA: mensajes de commit que explican el porqué, rebase sin miedo, blame entendible y cómo deshacer errores. Guía para DAW."
category: "Guía"
date: 2026-09-09
readtime: 9
---

## El día que me comí un merge que no entendía

En el módulo de Programación me propuse subir cada práctica a GitHub antes de irme a dormir. Funcionaba, hasta que un viernes dejé el repo con un título que era una obra maestra de vaguería: *"cambios"*. A la semana siguiente, repasando para el examen, abrí mi propio historial y no tenía ni idea de qué había tocado, por qué lo había tocado ni si lo que subí estaba a medias. Ese es el verdadero problema de Git cuando empiezas: no son los comandos, es que el historial es tu memoria, y yo la había llenado de ruido.

La IA no arregla tus commits por ti. Pero sí puede convertirlos en la libreta que nunca te llega a aburrir: te explica qué cambió, por qué, y te saca de los apuros cuando el árbol se cruza. En esta guía te cuento el flujo que uso en 2026, con los comandos y prompts exactos.

## Por qué el mensaje de commit no es un adorno

En DAW nadie te evalúa los mensajes de commit. Pero tus futuros compañeros, tu yo del mes que viene y (esto importa) quien te haga la entrevista técnica sí los miran. El historial de commits es la primera huella que dejas como profesional: se lee en dos minutos y cuenta una historia de cómo escribes código.

Un buen mensaje de commit no dice *qué* cambió (eso lo ve el diff), dice *por qué*. "Cambios" no dice nada. "Corrijo el filtro de búsqueda que rompía con tildes" salva media tarde. La diferencia es mental, y la IA la hace gratis si se lo pides bien.

## Mensajes de commit que explican el porqué

La forma más rápida con la que he encontrado de no volver a escribir "cambios": deja que la IA lo redacte, pero dándole contexto. Mi flujo:

1. `git diff` de lo que toqué (o `git diff --staged` si ya hice `git add`).
2. Se lo pego a la IA con un prompt corto y le explico el contexto en una frase.

El prompt que uso para las prácticas:

```text
Tengo este diff de mi práctica de Desarrollo Web. Escribe un mensaje de
commit en una línea que explique POR QUÉ hice este cambio, no qué cambió.
No menciones que el código funciona. Contexto: [una frase tuya]
```

Y entonces edito lo que me devuelve. Casi siempre lo acorto a la mitad, porque la IA tiende a explicar de más, pero el formato de "una línea + por qué" me ha quitado un hábito malo: commitear en piloto automático.

Si usas GitHub Copilot en el editor, la versión de comandos (`gh copilot suggest-commit`) te propone el mensaje a partir del diff sin salir de la terminal. Y si ya tienes montado un agente en la terminal como te conté en la [guía de IA en terminal para DAW](/articulos/guias/ia-en-terminal-estudiantes-daw/), puedes pedirle lo mismo pidiendo rebase interactivo.

## Blame que de verdad entiendes

`git blame` es de esos comandos que parecen de otro planeta hasta que los necesitas. Sirve para ver, línea a línea, quién tocó cada línea y en qué commit. Los estudiantes lo odiamos porque las líneas salen con hashes que no dicen nada: `a3f9c1e (Iván 2026-09-14)`. Ahí la IA brilla.

Mi truco: `git blame` del archivo, lo pego en el chat y le digo:

```text
Explícame este git blame línea a línea en lenguaje de estudiante:
qué cambió cada commit, y si algún commit parece que introdujo un bug.
```

La respuesta convierte el árbol en una conversación: "el commit de ayer cambió la variable de sesión y por eso ahora el carrito se resetea". A partir de ahí sabes exactamente dónde mirar. Esto me ha ahorrado horas que antes perdía leyendo código de semana pasada como si fuera ajeno.

## Rebase sin miedo

El rebase asusta porque cambia el historial, y cambiar el historial da miedo hasta que entiendes que Git lo guarda todo. Mi receta para no liarla:

1. Crea una rama para la práctica: `git checkout -b practica-5`.
2. Trabaja, commitea con mensajes que digan algo.
3. Cuando toque unir con `main`, en vez de `git merge` (que dibuja un nudo cuando ambos ramas han avanzado), hago `git rebase main`.

El miedo de verdad viene cuando rebase te pide resolver conflictos. Aquí la IA es oro puro: le pego el conflicto (el bloque con `<<<<<<<` y `>>>>>>>`) y le digo:

```text
Resuelve este conflicto de merge. Mantén las dos funcionalidades.
La rama izquierda es mi trabajo, la derecha son los cambios de mi
compañero. Explícame QUÉ has fusionado y por qué.
```

Y no te quedes con el resultado: léeme su explicación antes de aceptar. Rebase deja el historial como una línea recta, que es exactamente lo que se ve limpio en una entrevista y lo que hará que tu entrenador de prácticas deje de fruncir el ceño.

## Deshacer errores sin llorar

El día que le diste a `git reset` equivocado y perdiste media práctica, ¿dónde estaba el botón de "partir de cero"? En `git reflog`. Git no borra: guarda un registro de cada movimiento de tu HEAD, incluso los que parecen catastróficos.

Cuando algo se rompe, mi secuencia con IA:

- `git reflog` → se lo enseño y pregunto `¿En qué punto estaba antes de mis últimas 3 operaciones?`
- `git reset --hard <hash>` al punto correcto.
- Si simplemente me equivoqué de archivo: `git checkout -- <archivo>` para deshacer un archivo concreto (ojo: pierde los cambios sin commitear).

El punto es que ninguna de estas cosas es magia ni requiere memoria de elefante: todas son un comando que se pega en el historial. La IA me sirve de mapa cuando el árbol se pone feo, no de conductor.

## Errores que ya no cometo con IA

En la práctica he caído en tres trampas que repaso aquí para que no las pagues tú:

- **Dejar que la IA haga Git por mi cuenta.** Si no entiendes qué comando está ejecutando, es un atajo que te va a costar carísimo el día que no haya IA en el entorno de trabajo. Pídele *explica y hazlo junto a mí*, no *hazlo por mí*.
- **Prompts sin contexto.** "Hazme el commit" solo funciona si te tiraste dos horas y `git diff` dice todo eso por sí solo. La mitad de las veces el diff no cuenta el porqué, y sin tu frase de contexto el mensaje sale genérico.
- **Commitear a medias.** El 70% de mis conflictos nacían de commits grandes que mezclaban tres tareas. Ahora divido en commits pequeños con la IA ayudándome a separar el diff por responsabilidad (`git add -p`), y el número de conflictos ha caído en picado.

## La rutina que me funciona

Esta es la secuencia de un día normal, para que veas que no es una película de hackers:

1. `git checkout -b practica-6` al empezar.
2. Cada subtarea: `git add -p` + commit con mensaje "por qué" (IA redacta, yo edito).
3. Al terminar: rebase contra `main` con IA en los conflictos.
4. Antes de subir: pido una revisión del diff entero preguntando *"¿hay algo que rompa en entornos que no he probado?"* — me ha pillado problemas de case-sensitive de rutas en Windows/Linux que ni vi.
5. `git push` con `git log` limpio como mi tarjeta de visita.

Esto encaja con el día a día que cuento en [GitHub Actions para DAW](/articulos/guias/github-actions-estudiantes-daw/) (si pones los commits de este estilo, los pipelines automáticos dejan de ser cajas negras) y con la [lista de errores comunes programando con IA](/articulos/listas/errores-comunes-programando-con-ia/). Y si tu equipo ya usa [AGENTS.md](/articulos/guias/agents-md-guia-2026/), mete ahí tu convención de commits para que la IA la respete sola.

## Veredicto

Git sigue siendo de lo menos glamuroso de programar y de lo que más dinero te ahorra a medio plazo. La IA no te quita el trabajo de entender qué hiciste: te quita el trabajo de recordarlo. Y en un examen práctico o una primera entrevista, que te pregunten por tu historial y puedas explicarlo commit a commit es la diferencia entre parecer estudiante y parecer programador.

Empieza hoy: crea un repo de práctica, deja un commit feo a propósito y dedícale una tarde a los comandos de aquí. Cuando dentro de un mes entiendas tu propio historial de un vistazo, dime si Git todavía te da miedo.
