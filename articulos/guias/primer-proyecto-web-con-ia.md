---
layout: article
title: "Tu primer proyecto web con IA: del vacío a publicarlo sin morir"
description: "Cómo diseñar tu primer proyecto web con IA para aprender de verdad: idea pequeña, stack mínimo, tareas cortas, git desde el día uno y publicación gratis."
category: "Guía"
date: 2026-09-20
readtime: 7
---

Vacío. Ese es el sentimiento exacto del primer proyecto web. Tienes un editor abierto, la idea vaga de "hacer una página" y una IA dispuesta a generar lo que le pidas, que es precisamente el problema: **si le pides "dame un proyecto web completo", tendrás un proyecto que no entiendes**. Lo digo porque lo hice. Mi primera vez con IA terminó en un montón de archivos que no sabía por qué funcionaban y que se rompieron en cuanto quité una línea. Con el tiempo aprendí que el primer proyecto con IA no se construye pidiéndole el resultado, sino **troceándolo en decisiones que tú vas tomando**. Así lo haría hoy, paso a paso, siendo estudiante de DAW.

## Paso 0: quita miedo y elige una idea pequeña de verdad

Lo primero, y lo que nadie dice: **el proyecto no tiene que ser original**. Todo lo contrario. La mejor idea para un primer proyecto es que resuelva algo tuyo: la web de recetas de tu madre, el control de tus apuntes, el "to-do" de tus series. Cuanto más aburrido, mejor: el contenido no te distraerá del código. Y si lo tuyo es el portafolio para las prácticas, en [ideas para portafolio en un fin de semana](/articulos/listas/5-proyectos-portfolio-desarrollador-ia-fin-de-semana/) tienes cinco que salen en horas.

Una idea que le funcione a un principiante cumple tres reglas: **cabe en una pantalla de pizarra** (una lista, un formulario, tres secciones), **se puede dividir en 5-7 tareas** y **no se le ocurre al típico ejemplo de "tienda online"**. Si la idea no te la explica en dos frases, es demasiado grande.

## Paso 1: decide el stack mínimo antes de abrir la IA

La indecisión técnica es la que más horas roba, y la IA no te ayuda porque te devuelve la pregunta. Decídelo tú en dos minutos:

- **Página estática de una web**: HTML + CSS + un poco de JavaScript. Nada más.
- **Web con datos que cambian**: aquí yo iría a React con Vite para el front y una API sencilla, que es lo que tocas en el módulo de [conectar un frontend a una API](/articulos/guias/conectar-frontend-api-con-ia-2026/).
- **Publicación**: olvídate del hosting de pago; para empezar sirve publisharlo gratis, que es exactamente lo que cuento en [cómo publicar tu primera web gratis](/articulos/guias/como-publicar-primera-web-internet-barato-ia/).

Si dudas entre dos, elige la que ya tuvieras instalada. El stack mínimo que no te obliga a decidir es el que vas a llegar a terminar.

## Paso 2: promete a la IA una tarea, no el proyecto

Este es el cambio mental que más me costó. En lugar de abrir el chat y escribir *"construye una web de recetas"* (spoiler: te devuelve 3.000 líneas y no sabes por dónde entrar), la sesión va así:

1. *"Soy estudiante, clientes-para-relax: quiero un `index.html` con una cabecera y una sección de recetas en grid. Nada más."*
2. Reviso, abro el archivo, lo veo en el navegador.
3. Siguiente tarea: *"ahora el formulario para añadir una receta, guardando en localStorage"*.

Cada ronda produce algo que **entiendes y funciona**. Al final del día tienes un proyecto completo montado a base de piezas que tú has ido encajando, no un monolito de desconocidos. Esto engancha con la [lista de prompts para que la IA te enseñe en vez de hacerte el trabajo](/articulos/listas/8-prompts-programacion-daw-2026/), porque la filosofía es la misma: una instrucción corta que tú revisas.

## Paso 3: git desde el día 1, aunque sea feo

"Para un proyecto de clases no necesito git" — era yo mismo antes de que la IA me lo pidiera tres veces. Ahora lo tengo clarísimo: **si una IA te va a tocar el código, git es tu cinturón**. Antes de cada ronda de "pásame a oscuro", hago *commit*, así si la IA rompe algo puedo volver atrás sin drama. Y me arrepiento cada día de no haber aprendido git el primer día del curso; por eso lo puse al principio de [la guía de git para estudiantes](/articulos/guias/git-con-ia-2026/). Los commits feos se arreglan; los proyectos sin respaldo se lloran.

## Paso 4: la IA arregla, tú decides

Llegará el momento (normalmente hacia la tarde) en que algo no funciona y pegues el error. Vale, pero con método: dale **contexto** (qué tarea hiciste, qué esperabas, qué pasa), pídele **causa** y no copiar el parche hasta entenderlo. Ese instinto se entrena, y está todo en el método de [depurar con IA](/articulos/guias/depurar-codigo-con-ia-guia-2026/). Cuanto más revises y preguntes *"¿por qué esto y no aquello?"*, más código tuyo habrá dentro del proyecto.

También te va a tocar algo que no te esperas: **los estilos**. La IA te propone un CSS bonito, lo pegas, y te queda una web que parece de un plugin. Yo lo que hago es pedirle pocas clases, colores que decido yo y que mire la web en el móvil, porque [el diseño responsive en un primer proyecto](/articulos/guias/crear-portfolio-desarrollador-web-con-ia/) se descuida mucho. El "que se vea bien en un móvil" es una tarea más; no un extra.

## Paso 5: publícalo, aunque "no esté listo"

El truco final: **no existe el proyecto listo, existe el proyecto publicado**. Publicar pronto (aunque esté a medias) te obliga a tocar cosas reales: subir, ver la URL, romperla, arreglarla. Esas segundas de "no me carga" son el mejor profesor, y [dominar y dónde alojarla](/articulos/guias/que-dominio-comprar-primer-proyecto-web/) se hacen mucho menos tristes cuando tu web ya se ve en un móvil de verdad.

## Lo que haría diferente

Mirando atrás con mis primeros proyectos: habría **dibujado la web en un papel** antes de abrir el editor (una caja para la cabecera, otra para el grid...). Cuesta dos minutos y hace que la IA te entienda mejor, porque le das estructura en vez de humo. Y habría apostado por **una sola función a la vez**: mi error era pedir bloques, y el "bloque" es siempre demasiado grande para aprender algo de él.

## Mi veredicto

**Tu primer proyecto con IA es completamente posible y es de las mejores formas de aprender… si lo troceas.** Idea pequeña, stack decidido por ti, tareas de una en una, git por delante y revisión de cada paso. La IA acelera, pero el dueño del proyecto eres tú. Porque publicar web número uno te engancha, y la segunda te sale sola. Si te estancas en alguna tarea y no sabes ni por dónde preguntarle, escríbeme a ivan@codeandia.com y te digo cómo trocearla.

## Sigue por aquí

- [v0 by Vercel y alternativas 2026: IA que genera interfaces](/articulos/listas/v0-vercel-ia-ui-generacion-lista-herramientas/)
