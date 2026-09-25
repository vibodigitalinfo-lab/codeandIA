---
layout: article
title: "Vite vs Next.js vs Astro para tu primer proyecto con IA"
description: "Qué framework elegir para tu primer proyecto web si usas IA: Vite, Next.js o Astro. Comparativa honesta de dificultad, rendimiento y cuándo tiene sentido cada uno."
category: "Comparativa"
date: 2026-09-25
readtime: 9
---

Cuando empiezas un proyecto web y le preguntas a la IA "¿con qué lo hago?", su respuesta suele ser "depende", y te suelta las tres opciones más de moda del panorama: React, Next.js o Astro. Luego tú, con tres pestañas abiertas y cero decisiones tomadas, te quedas bloqueado media hora antes de escribir la primera línea de código. Este problema lo tengo visto en todos mis compañeros, y por eso me he pasado las últimas semanas usando las tres con proyectos reales para responder a la única pregunta que importa: **cuál de estas tres me va a hacer terminar el proyecto antes de que me aburra**. Spoiler: depende mucho menos de cuál sea "mejor" y mucho más de cuál te da menos cosas que aprender de golpe.

## La pregunta que nadie hace: cuánto tengo que saber antes de empezar

Antes de comparar herramientas, comparo requisitos, porque es el error que más veo. Un framework que en manos de un senior es cómodo, en manos de alguien que lleva tres meses en DAW es una barrera. La diferencia real entre estas tres opciones no está en la velocidad final (todas dan páginas rápidas) sino en **la cantidad de conceptos nuevos que te meten por la puerta el primer día**:

- **Vite** te da un servidor de desarrollo y un bundler moderno, y ya. Lo demás lo eliges tú.
- **Next.js** te mete routing, server components, renderizado en servidor, y un montón de decisiones con las que aún no estás familiarizado.
- **Astro** te da páginas estáticas muy rápidas y te deja meter JavaScript solo donde lo necesitas.

Ese es el eje que importa cuando el proyecto es "mi primera web": menos conceptos de entrada, más probabilidad de terminarlo. Y es exactamente lo que cambia cuando hablas de un proyecto ya en marcha, donde lo que cuenta es el rendimiento y la escalabilidad. Separaremos los dos casos, porque la respuesta es distinta.

## Vite: el punto de partida más honesto

Si tuviera que recomendar **una sola cosa** a alguien que empieza su primer proyecto con IA, sería Vite. La razón es simple: es el que menos te esconde. Montas `npm create vite`, eliges React, y tienes un proyecto que corre, con hot-reload, y que entiendes de principio a fin porque no hay una capa de abstracción misteriosa encima.

Con la IA esto funciona especialmente bien, porque el ciclo es cortísimo: describes un componente, lo ves en el navegador, lo pides bien, y repites. No hay servidor que reiniciar, ni decisiones de renderizado que te despisten. Es el mismo esquema de "tarea pequeña, ves el resultado, sigues" que describí en [tu primer proyecto web con IA](/articulos/guias/primer-proyecto-web-con-ia/), y por eso funciona tan bien.

La contra es que cuando el proyecto crece, la responsabilidad de las decisiones (enrutado, dónde va la lógica, cómo se despliega) es toda tuya. Para el proyecto del curso o de prácticas eso está perfecto. Para una web con contenido que cambia cada día y mucho tráfico, te va a faltar algo que Vite no da por sí solo.

## Next.js: potente, pero con factura de entrada

Next.js es la opción por defecto de la industria, y merece su fama: renderizado en servidor, rutas file-based, y un ecosistema enorme. Una tienda, un blog con contenido dinámico, una app con login: Next.js lo resuelve solo y bien.

El problema es la factura de entrada. A la primera le pido a la IA una página y me devuelve una estructura con `app/`, `page.tsx`, `layout.tsx`, Server Components, y una capa de caché que no entiendo. Me devuelve veinte archivos para pintar un formulario. Es el efecto contrario al que buscamos: en vez de aprender algo pequeño y terminable, me bombardea con conceptos que no había pedido. Y aquí es donde muchas de las decisiones que tomó la IA ni siquiera eran necesarias.

Aun así, hay un momento en el que Next.js es la elección correcta: cuando tu proyecto ya no es "una web sencilla" sino algo con datos que vienen de una base de datos, usuarios autenticados y varias páginas que comparten estado. Si vas por ahí, los extras de Next.js te ahorran meses. Y si eso es lo que quieres aprender, el camino es [conectar un frontend a una API](/articulos/guias/conectar-frontend-api-con-ia-2026/) pero con el framework que ya te da el andamiaje. Solo no lo elijas para tu primer "hola mundo".

## Astro: cuando lo que quieres es contenido, no aplicación

Astro ocupa un espacio distinto: está pensado para páginas que son principalmente contenido (un blog, una documentación, una landing) con interactivity puntual. Su filosofía es "HTML por defecto, JavaScript solo donde lo necesitas", y en la práctica significa que una página de artículos que solo tiene texto y un poco de estilo carga muchísimo menos JavaScript que la misma página en Next o Vite.

Para un estudiante, Astro es la herramienta ideal para un tipo muy concreto de proyecto: un portafolio o un blog con muchas páginas estáticas, donde quieres que se cargue rapidísimo y que cada artículo sea una página independiente. En eso es difícil de superar. Y la parte bonita es que no compite con tu aprendizaje de JavaScript: si ya sabes React, puedes meter componentes React puntuales donde los necesites, sin reescribir todo.

La curva es más suave de lo que parece para este caso de uso, pero no es la mejor elección si lo que quieres es aprender a construir una aplicación con estado, porque Astro está diseñado justo para lo contrario.

## La tabla que resumo antes de que preguntes

| | Vite | Next.js | Astro |
|---|---|---|---|
| Ideal para | Tu primer proyecto, SPAs | Apps con datos y usuarios | Blogs, docs, contenido estático |
| Conceptos al empezar | Pocos | Muchos | Pocos-medios |
| Velocidad final | Muy buena | Muy buena | Excelente |
| Con IA, funciona... | Muy bien (ciclo corto) | Regular (te inunda) | Bien (simple de pedir) |
| Lo que te toca aprender | Las decisiones son tuyas | Renderizado, caché, rutas | Layouts, islands, estáticas |

## Mi recomendación honesta, en orden

Si estás leyendo esto siendo estudiante y es tu primer proyecto serio con IA, mi orden de preferencia es este:

1. **Vite + React**, sin duda. Es donde más aprendes por cosa que escribes, y donde la IA te ayuda en vez de ahogarte. Con las recetas de [tu primer proyecto con IA](/articulos/guias/primer-proyecto-web-con-ia/) llegas lejos.
2. **Astro**, si lo que quieres es un blog o un portafolio con muchas páginas y te importa que vuelen. Es casi tan fácil como Vite y el resultado en rendimiento es bastante mejor.
3. **Next.js**, cuando ya tengas un proyecto funcionando y quieras darle una base de datos, usuarios o contenido que cambia. Para entonces, los conceptos que te confundían ya los habrás visto en otro sitio y los entiendes.

El error que veo cada año es el contrario: empezar por Next.js porque es "el que usan", quedarse una semana configuring el framework sin escribir una línea de lógica, y abandonar el proyecto. La mejor herramienta para terminar tu primer proyecto no es la más potente, es la que te deja llegar al lunes siguiente con algo funcionando. Y si al final te da igual y quieres probarlos todos, mi sugerencia es hacerlos como ejercicios: el mismo "to-do" en Vite, luego en Astro, y así ves las diferencias con tus propios ojos en vez de con vídeos de YouTube.

¿Quieres que te detalle el paso a paso de alguno en concreto? Escríbeme a ivan@codeandia.com y lo montamos juntos, que en esto de elegir stack, la mejor ayuda es tener a alguien que te diga "ese, y ya". Y si quieres ver el resultado final de un proyecto tuyo, pásate por [cómo publicar tu primera web](/articulos/guias/como-publicar-primera-web-internet-barato-ia/).
