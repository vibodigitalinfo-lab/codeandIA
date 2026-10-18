---
layout: article
title: "Mi web cayó en España por un bloqueo judicial pedido por LaLiga"
description: "El 17 de octubre codeandia.com dejó de cargar. No era mi servidor: un bloqueo judicial contra otra web se llevó la IP de Cloudflare donde vivía. Así lo detecté."
category: "Guía"
date: 2026-10-18
readtime: 4
last_modified_at: 2026-10-18
---

El 17 de octubre sobre las 14:50 abrí codeandia.com y la página no cargaba. No era un error a mitad de carga ni una pantalla rara: el navegador se quedaba girando hasta que se rendía. Probé otras páginas y todo lo demás iba con normalidad, así que descarté al principio lo de mi conexión.

Con la ayuda de Claude fui investigando y probando cosas, y ahí salió la causa: el problema no venía de mi servidor ni de mi wifi. Ese día había partido, y mi web había quedado atrapada en un bloqueo judicial que no iba dirigido a mí.

Al principio pensé que me habían baneado o algo y me agobié un momento. Pero no había hecho nada malo, así que en cuanto lo comprobé me puse directamente a buscarle una solución.

## Qué había pasado el día anterior

El 16 de octubre había puesto codeandia.com detrás del proxy de Cloudflare. Lo hice por las cinco redirecciones 301 de los artículos antiguos que había movido de sitio. Detrás del proxy, el tráfico de la web no va directo: pasa antes por las IP de Cloudflare, que son las mismas que usan miles de webs más.

Ese mismo 16 de octubre, LaLiga y Telefónica Audiovisual pidieron un bloqueo judicial contra hayahora.futbol, una web de fútbol. Según explicaba la propia hayahora, la medida iba contra ella. El problema es que esa web y la mía compartían red: cuando se bloquearon las IP de Cloudflare por las que pasaba el tráfico, mi web cayó con la suya, sin que yo tuviera nada que ver.

## Cómo lo detecté

Lo primero que hice fue descartar que el problema fuera mío:

- Las páginas de estado de Cloudflare y de GitHub no decían nada: ninguna incidencia publicada.
- Con `nslookup`, el dominio apuntaba a las IP del proxy de Cloudflare (188.114.96.5 y 188.114.97.5), no a GitHub Pages.
- Con `curl` no recibía respuesta.
- En cambio, `www.codeandia.com` apuntaba directo a GitHub Pages (rango 185.199.x) y sí cargaba. El blog entero estaba ahí, intacto; lo que no funcionaba era el camino que pasaba por el proxy.

Para no quedarme con la duda entré en hayahora.futbol. Aparecía que sí que había fútbol ese día, y con el buscador de webs que tienen busqué codeandia.com: estaba bloqueada. Ahí tenía la confirmación.

## El arreglo

Pasé los registros A de Cloudflare a «DNS only». Con el proxy apagado, el tráfico va directo del navegador a GitHub Pages y no toca las IP bloqueadas. Al poco, `nslookup` devolvía el rango 185.199.x de GitHub Pages, `curl -vI` respondía con 200 y la web volvió a cargar.

Pero el arreglo tiene su precio: al apagar el proxy, las cinco redirecciones 301 dejaron de funcionar. DNS only salva el acceso, no el problema de fondo: el bloqueo seguía ahí, y yo seguía sin proxy.

## Qué me llevo de esto

Me sirvió más no quedarme quieto que el arreglo en sí. Lo primero que hice bien fue comprobar que el problema no venía de mi lado: si el resto de internet funcionaba, el culpable tenía que estar en el camino de en medio. Las páginas de estado, un `nslookup` y un `curl` te dicen bastante en cinco minutos; y si un `curl` no te da pistas, con `-v` ves lo que pasa de verdad en la conexión.

También me llevo una idea que no tenía detrás del proxy de Cloudflare no estás solo. Compartes IP con miles de webs, y si a una de ellas le cae un bloqueo en tu país, te puedes ir con ella. Estoy en España y mi audiencia sobre todo también: es algo a tener en cuenta antes de poner el proxy sin necesidad.

## Sigue por aquí

- [Qué dominio comprar para tu primer proyecto web](/articulos/guias/que-dominio-comprar-primer-proyecto-web/)
- [Aprender Java en DAW con IA y no volverte dependiente](/articulos/guias/aprender-java-con-ia-daw/)
