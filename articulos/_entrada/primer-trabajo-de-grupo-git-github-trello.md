---
layout: article
title: "Mi primer trabajo en grupo con Git, GitHub y Trello: ramas, push rechazados y caos"
description: "Cómo organizamos un trabajo de DAW entre 5 personas con Git, GitHub y Trello: tres niveles de ramas, los push que fallaban y lo que haría distinto."
category: "Guía"
date: 2026-10-27
readtime: 6
---

## Un trabajo en el que lo importante no era el trabajo

Hace unas semanas, en primero de DAW, nos tocó un trabajo en grupo. El profesor nos dio una empresa y el ejercicio era más o menos guiado: analizarla y proponer mejoras. Del enunciado no voy a contar más, porque es material suyo y no me corresponde publicarlo.

Además, no era lo importante. El objetivo de verdad era aprender a trabajar en equipo, cinco personas, con tres herramientas que casi ninguno había usado en serio: **Git**, **GitHub** y **Trello**. El contenido era la excusa. Lo que se evaluaba de fondo era si sabíamos repartirnos el trabajo sin pisarnos.

Te cuento cómo nos organizamos, qué nos falló una y otra vez y qué cambiaría la próxima vez.

## Cómo montamos las ramas: main, revisado y una por persona

Lo primero fue decidir cómo íbamos a usar las ramas. Al final quedó así, con tres niveles:

1. **`main`**: solo para la entrega final. Nadie trabajaba ahí. Lo que llegaba a `main` era lo que se iba a entregar.
2. **Una rama intermedia** con el contenido ya revisado. Cuando alguien terminaba una parte y el resto le daba el visto bueno, pasaba aquí.
3. **Una rama personal para cada uno**. Ahí cada persona trabajaba y hacía sus commits a su ritmo, sin molestar a nadie.

Visto ahora, es un esquema bastante sensato para cinco personas que están aprendiendo. La rama personal te deja equivocarte tranquilo: si rompes algo, lo rompes en lo tuyo. La rama intermedia sirve de filtro, y `main` queda limpia hasta el final.

Lo que no te cuentan es que, con tres niveles y cinco personas, hay muchos momentos en los que alguien tiene que juntar cosas. Ahí es donde empezaron los problemas.

## El problema que más se repitió: push que no entraban

Lo que más veces nos pasó fueron los push retrasados. Alguien iba a subir sus cambios y Git no le dejaba, porque otra persona había subido algo antes a esa misma rama y su copia ya no estaba al día. Nos pasó un montón de veces, a casi todos.

Si te pasa, lo que te está diciendo Git es esto: **en GitHub hay commits que tú no tienes en tu ordenador**. No te deja subir los tuyos encima sin que antes traigas esos cambios y los juntes con lo que has hecho tú. Suele salir un mensaje con palabras como `rejected` y `fetch first`, que la primera vez asusta más de lo que debería.

La forma general de salir es:

```bash
git pull          # traer lo que han subido los demás y juntarlo con lo tuyo
# si hay conflictos, resolverlos en los archivos y luego:
git add .
git commit
git push          # ahora sí debería entrar
```

Lo que **no** conviene hacer es lo que a veces aparece como solución rápida, `git push --force`. Eso machaca lo que han subido tus compañeros. En un trabajo en grupo es la forma más rápida de borrar el trabajo de otro sin querer.

Nosotros lo fuimos sacando entre todos, mirando el error juntos, y con ayuda de la IA. Le pasaba el error tal cual y también los comandos que había ido escribiendo antes. Eso fue lo que más ayudó: con solo un «no me deja hacer push», la IA te da una respuesta genérica, pero con tu rastro de comandos puede ver dónde se torció el paso. Es lo mismo que cuento en [cómo uso la IA para aprender Java sin volverme dependiente](/articulos/guias/aprender-java-con-ia-daw/): pregunto por la causa y no voy cambiando cosas a ciegas.

## Trello: columnas sencillas que sí funcionan

Trello nos lo impusieron, pero la verdad es que es intuitivo y visual. Lo montamos con columnas del estilo:

- **Por hacer**
- **En curso**
- **Completado**

No tiene ningún misterio, y por eso funciona: abres el tablero y sabes qué tienes pendiente, qué está en marcha y qué ya está completado. Cuando estás con varias cosas a la vez, ver el tablero y saber dónde estás vale más de lo que parece.

## Lo que haría distinto

No te voy a decir que todo fue bien. Hubo momentos de caos. El problema no era que una herramienta fallara, sino no saber en cada momento cómo había que hacer cada cosa: quién juntaba qué, cuándo había que actualizar la rama personal o qué hacer cuando un push no entraba.

Si lo repitiera, me organizaría mejor desde el primer día:

- **Escribir las reglas antes de empezar**: qué rama es para qué, quién pasa cosas a la rama revisada y quién toca `main`, y qué hacer cuando un push no entra. Con eso apuntado, gran parte del caos se habría evitado.
- **Hacer `git pull` antes de ponerse a trabajar**, siempre. Un push rechazado casi siempre significa que estabas trabajando sobre una copia que ya no estaba al día.
- **Commits pequeños y frecuentes.** Cuanto más tiempo pasas sin subir, más difícil es juntar lo tuyo con lo de los demás.
- **Una tarjeta de Trello por tarea pequeña**, no tarjetas enormes que se quedan semanas en «En curso».

## Lo que me llevo

Antes de este trabajo no había usado Git de verdad, y menos con otras cuatro personas. Ahora entiendo para qué sirven las ramas y por qué un push no entra. También he aprendido que la mitad de usar Git en equipo no es técnica, sino ponerse de acuerdo.

Si estás empezando DAW o cualquier ciclo de programación y te toca un trabajo así, mi consejo es sencillo: acordad las ramas por escrito y haced pull antes de empezar a trabajar. Os ahorraréis la mayoría de los sustos que tuvimos nosotros.

Si estás con algo parecido y te has atascado con Git, puedes escribirme a ivan@codeandia.com.
