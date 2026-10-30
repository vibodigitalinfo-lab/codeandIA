---
layout: article
title: "Hice un inspector de webs con Claude Code y lo primero que revisó fue mi blog"
description: "Cómo nació Pikolete, mi auditor web gratuito hecho con Claude Code: de un dominio sin usar a una herramienta que me encontró fallos en este blog."
category: "Guía"
date: 2026-11-10
publicar: 2026-11-10
readtime: 4
---

## Un dominio comprado y sin usar

Te aviso desde el principio: **Pikolete es un proyecto mío**. No es una recomendación neutral, es la historia de cómo lo hice y para qué lo uso.

Todo empezó con un dominio. Había comprado pikolete.com en Namecheap para otro proyecto que al final no salió, y lo tenía ahí, pagado y sin usar. Si estás pensando en comprar uno, te conté cómo elegirlo en [qué dominio comprar para tu primer proyecto web](/articulos/guias/que-dominio-comprar-primer-proyecto-web/).

Cuando empecé a pagar Claude Pro, quise darle un uso. Le dije a Claude, básicamente, que quería hacer un proyecto y que tenía ese dominio libre. «Pikolete» suena casi igual que «picoleto», que en España es una forma coloquial de llamar a un guardia civil. A partir de ahí, Claude propuso la idea: un inspector de páginas web, alguien que va revisando webs y poniendo multas.

## Qué hace Pikolete

[Pikolete](https://pikolete.com) hace dos cosas:

- **Revisa el SEO de una web y le pone nota.** Le pasas una dirección pública y en unos segundos te da una puntuación de 0 a 100, con lo que está bien y lo que falla en SEO, velocidad, seguridad y estructura. Para cada fallo te dice cómo corregirlo.
- **Comprueba si una página es fiable**, con un buscador integrado, para que puedas mirar rápido si una web es de fiar antes de meterte en ella.

Lo hice porque quería justo eso: una herramienta para comprobar páginas rápido. Y la parte de SEO la uso sobre todo con este blog. Cuando detecta un error, lo corrijo directamente.

Es gratis. Para algunas funciones extra te pide el email, pero el análisis básico no necesita nada.

## Cómo lo hicimos

Aquí tengo que ser honesto: **el código lo escribió Claude, al 100 %**. Yo no escribí ni una línea. Mi papel fue decir qué quería y elegir entre las opciones que me iba proponiendo: cómo mostrar los resultados, qué revisar, cómo llamar a cada cosa.

No hubo grandes fallos. Claude me preguntaba si prefería una cosa u otra, yo elegía y seguíamos.

Está alojado en Vercel, en el plan gratuito, así que tenerlo online no me cuesta nada aparte del dominio. Y, como este blog, su código es público en [GitHub](https://github.com/vibodigitalinfo-lab/pikolete).

## Lo que encontró en mi propio blog

Una de las primeras webs que le pasé fue codeandia.com, y me encontró cosas que no había visto:

- **La descripción de la portada era demasiado larga**: 178 caracteres, cuando lo recomendable es no pasar de unos 160, porque Google corta el resto en los resultados de búsqueda. Dos artículos programados también se pasaban. Los acorté.
- **Faltaban cabeceras de seguridad**: unas instrucciones que el servidor manda al navegador para protegerte de algunos ataques, como que otra web meta la tuya dentro de un marco para engañarte.

Lo de las descripciones lo arreglé en un rato. Lo de las cabeceras, no del todo, y la razón es interesante. Este blog está en GitHub Pages, que es gratis pero no te deja configurar las cabeceras que manda el servidor. La única que se puede declarar desde el propio HTML es `Referrer-Policy`, así que la añadí así:

```html
<meta name="referrer" content="strict-origin-when-cross-origin">
```

El resto (`X-Content-Type-Options`, `X-Frame-Options` y HSTS) solo se podría poner con otro servicio delante del blog, como Cloudflare. De momento no merece la pena complicarlo.

## Cómo sale el blog ahora

Este es el análisis de hoy, 28 de octubre:

- **Nota A, 96 sobre 100.**
- 26 controles revisados: 24 en regla, 1 infracción y 1 advertencia.
- La infracción son las cabeceras de seguridad, y la advertencia es HSTS, que es otra cabecera de seguridad. Es justo lo que GitHub Pages no me deja tocar.
- El servidor responde en 68 milisegundos y la portada pesa 11,8 KB.

Hay un detalle gracioso: Pikolete sigue marcando que falta `Referrer-Policy`, aunque ya la puse como etiqueta en el HTML. Revisa las cabeceras del servidor, no las etiquetas de la página. Así que mi propia herramienta me pone una multa por algo que ya arreglé a medias. Me lo apunto como mejora para Pikolete.

## Lo que viene

Pikolete lleva muy poco tiempo online, así que todavía no te puedo contar cómo funciona con mucha gente usándolo. Ahora mismo estamos trabajando para que Google lo indexe y empiece a tener visitas. Si sale bien, lo contaré.

Si pruebas Pikolete con tu web y ves algo raro, o crees que se equivoca en algo, escríbeme a vibo@codeandia.com. Al ser mío, cualquier fallo que me cuentes lo puedo arreglar.
