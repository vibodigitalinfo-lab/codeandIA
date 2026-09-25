---
layout: article
title: "Hostinger vs Netlify: dónde alojar tu primer proyecto de DAW"
description: "Hostinger vs Netlify para tu primer proyecto de DAW: comparo hosting de pago y plataforma gratis, cuándo elige cada uno y cuánto pagas de verdad."
category: "Comparativa"
date: 2026-09-03
readtime: 7
affiliate_text: "Para el proyecto de PHP + MySQL yo uso Hostinger: unos 3 €/mes el primer año, con dominio gratis y SSH incluido."
affiliate_url: "https://www.hostinger.com/es"
affiliate_label: "Ver planes de Hostinger"
---

Cuando en segundo de DAW nos mandaron levantar una web con login, sesiones y una tabla de usuarios, me encontré delante de la pregunta que se repite en clase cada año: ¿dónde la subo? Mis compañeros dudaban entre Hostinger y Netlify, no porque hubieran probado los dos, sino porque son los dos nombres que salen cuando buscas "alojar web estudiante". El problema es que son servicios distintos, y compararlos sin contexto no tiene ningún sentido. Llevo meses usando los dos para proyectos distintos, y esta es la comparativa que me habría ahorrado el primer mes de dudas.

## Qué miro antes de decidir (y por qué)

Antes de hablar de precios, me hago tres preguntas. La primera: ¿el proyecto necesita un servidor que ejecute código, o es una página estática? Esto es lo que separa a los dos servicios y casi nadie lo explica en un titular.

La segunda: ¿cuánto me va a costar dentro de un año, no el primer mes? El plan gratuito de Netlify es gratis siempre. El hosting de pago suele cobrar poco el primer año y subir en la renovación, que es donde están todas las sorpresas.

La tercera: ¿quiero un enlace para el CV o algo que se comporte como una aplicación real? Si la diferencia no te importa, son dos caminos válidos, pero llegan a sitios distintos.

## Hostinger: el hosting de pago para proyectos "de verdad"

Hostinger es un hosting compartido. Traducción: pagas unas decenas de euros al año y te dan un servidor donde puedes ejecutar PHP, montar una base de datos MySQL/MariaDB, crear correos y hasta entrar por SSH. O sea, exactamente lo que pide la práctica típica de DAW del módulo de Desarrollo Web en Entorno Servidor.

Lo que me convenció fue la experiencia con la práctica de la tienda: un PHP con sesiones, un carrito en una tabla `productos` y un panel de admin. Lo subí con el instalador de WordPress (esto es lo que la mayoría usa), pero el motivo de fondo es que el servidor puede ejecutar ese código. Eso en Netlify, sin configuraciones raras, no existe: su capa de funciones va con Node.js y Edge, no con PHP clásico y MySQL.

Detalles que valen la pena siendo estudiante: el plan más básico anda en torno a los 3 €/mes el primer año si pagas anual (luego sube en la renovación, no se libra nadie), incluye dominio gratis el primer año, el panel (hPanel) está en español y el soporte por chat responde en español. El certificado SSL va incluido, que es otro quebradero menos.

Lo que no me gusta: el precio de renovación es el clásico truco del sector, y si solo vas a colgar una página estática, estás pagando por un servidor que no necesitas. Para eso ya tienes opciones gratis. Desgrané todo esto con calma en su [review de Hostinger](/articulos/reviews/hostinger-review-2026/), por si quieres la versión larga. Y si tu módulo es justo el de servidor, la [guía de qué hosting elegir en DAW](/articulos/guias/que-hosting-elegir-estudiantes-daw-2026/) termina justo donde empieza esta comparativa: ahonda en los planes, las renovaciones y la letra pequeña que aquí solo he rozado.

## Netlify: la plataforma gratis para lo estático

Netlify es un servicio de despliegue pensado para webs construidas con HTML, CSS, JavaScript y herramientas como React o Vite. El plan gratuito incluye, en torno a: 100 GB de ancho de banda al mes, 300 minutos de build al mes y formularios con límite gratuito. Para un portfolio de prácticas de desarrollo web, eso sobra.

Lo que más me gusta es que el despliegue va pegado a Git: conectas el repo y cada `git push` a la rama principal compila y publica solo. El día que presenté el portfolio de React en clase, subí el cambio desde la terminal y en dos minutos tenía la URL lista para enseñar. También trae funciones serverless (en Node) y desplegues de vistas previas por pull request, algo que usamos para probar ramas sin romper la versión publicada.

Lo que no me gusta: no es un servidor de aplicaciones. Si tu proyecto depende de PHP, MySQL o tienes que configurar un `wp-config.php`, Netlify no es tu sitio. Y el ancho de banda gratuito, aunque da para mucho, tiene límite: si publicas un proyecto con imágenes grandes y lo enseñas en el grupo de clase, un mes de tráfico se va rápido. Para el caso concreto del portfolio, mírate también la comparativa con [Vercel y GitHub Pages](/articulos/comparativas/vercel-vs-netlify-vs-github-pages-2026/), porque ahí están las tres opciones gratis cara a cara.

## La tabla que resume lo que me costó un mes entender

| | Hostinger | Netlify |
|---|---|---|
| Tipo | Hosting compartido de pago | Deploy estático con plan gratis |
| Código dinámico | ✅ PHP, MySQL, SSH, cron | ❌ Solo funciones Node/Edge |
| Coste | ✅ En torno a 3 €/mes el 1er año (renovación sube) | ✅ Gratis (100 GB/mes, 300 min build) |
| Dominio | ✅ Free el primer año | ⚠️ Compras aparte |
| Panel / soporte | ✅ hPanel en español, chat 24/7 | ✅ Documentación enorme, sin chat |
| Ideal para | Práctica de PHP + MySQL, tienda, app con login | Portfolio estático, landing, página de presentación |

## Mi veredicto por caso de uso

Si eres de los míos y cuentas el dinero del mes en el bar, el criterio es sencillo: **estático, Netlify sin pagar nada. Algo con base de datos o un módulo de servidor, Hostinger.**

Concretando para los casos que se repiten en DAW:

- **Portfolio para prácticas o el CV** (React, Vite o HTML a secas): Netlify con el plan gratuito. No hay debate.
- **Práctica de PHP + MySQL** (login, registro de usuarios, carrito): Hostinger. Tu profesor valora el script PHP como servidor, no como archivo muerto.
- **Quieres enseñar algo "de verdad" en la entrevista**: sube la app dinámica a Hostinger y deja el portfolio en Netlify. Son 44 € el primer año por decir en la entrevista "la subí yo, con su base de datos real". Lo barato que es en comparación con lo que cuenta.
- **Solo necesitas un enlace que abra en el móvil**: Netlify. Ya te tienes que preocupar de que cargue rápido.

Mi combinación actual: el portfolio corre en Netlify y la tienda de la práctica vive en Hostinger. No es indecisión, es que cada una está donde le toca. Lo único que haría distinto si empezara de nuevo es no pasarme un mes leyendo opiniones de gente que compara los dos como si fueran lo mismo. Se deciden por el tipo de proyecto en diez minutos, y el resto del tiempo da igual. Si me cuentas en qué módulo estás y qué te toca subir, te ahorro el mes de dudas.