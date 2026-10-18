---
layout: article
title: "La Liga bloqueó mi web: así lo arreglé en Cloudflare"
description: "El 17 de octubre codeandia.com dejó de cargar. No era mi conexión: había partido. Así lo detecté y lo solucioné."
category: "Guía"
date: 2026-10-18
readtime: 2
last_modified_at: 2026-10-18
---

El 17 de octubre abrí codeandia.com y la página no cargaba. No era un error a mitad de carga ni una pantalla rara: el navegador se quedaba girando hasta que se rendía.

Lo sospechoso vino después. Probé otras páginas y todo lo demás iba con normalidad, así que descarté al principio lo de mi conexión. Seguí investigando con la ayuda de Claude, probando cosas, y ahí salió la causa: el problema no era mío, estaba bloqueado por La Liga.

Ese día había partido.

## La comprobación

Para no quedarme con la duda entré en hayahora.futbol. Aparecía que sí que había fútbol, y con el buscador de webs que tienen integrado busqué codeandia.com: estaba bloqueada.

## Lo que hice

La solución estaba en Cloudflare. Pasé los registros A a «DNS only» y, al poco, la web volvió a responder correctamente.

También vale la pena decirlo tal cual: al principio pensé que me habían baneado o algo y me agobié un momento. Pero no había hecho nada malo, así que en cuanto lo comprobé me puse directamente a buscarle una solución.

## Qué me llevo de esto

Me sirvió más no quedarme quieto que el arreglo en sí. Lo primero que hice bien fue comprobar que el problema no venía de mi lado: si el resto de internet funcionaba, el culpable tenía que estar en el otro sitio. Desde ahí ya fue cuestión de confirmarlo y buscar dónde se cortaba.

## Sigue por aquí

- [Aprender Java en DAW con IA y no volverte dependiente](/articulos/guias/aprender-java-con-ia-daw/)
- [Qué portátil necesita un estudiante de DAW: mi caso con i3 y 8 GB](/articulos/guias/que-portatil-comprar-estudiar-daw-2026/)
