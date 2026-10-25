---
layout: article
title: "Mi web dejó de cargar en España por un bloqueo de LaLiga a Cloudflare"
description: "El 17 de octubre codeandia.com dejó de cargar. No era mi servidor: un bloqueo de LaLiga a Cloudflare se llevó las IP compartidas donde vivía. Así lo detecté."
category: "Guía"
date: 2026-10-18
readtime: 4
last_modified_at: 2026-10-25
---

El 17 de octubre sobre las 14:50 abrí codeandia.com y la página no cargaba. No era un error a mitad de carga ni una pantalla rara: el navegador se quedaba girando hasta que se rendía. Probé otras páginas y todo iba con normalidad, así que descarté al principio lo de mi conexión.

Al principio pensé que me habían baneado o algo y me agobié un momento. Pero no había hecho nada malo, así que en cuanto lo comprobé me puse directamente a investigar, con la ayuda de Claude, y ahí salió la causa: el problema no era mío. Ese día había partido, y mi web había quedado atrapada en un bloqueo que no iba dirigido a mí.

## Qué había pasado el día anterior

El 16 de octubre había puesto codeandia.com detrás del proxy de Cloudflare. Lo hice por las redirecciones 301 de los artículos antiguos que había movido de sitio. Detrás del proxy, el tráfico de la web no va directo: pasa antes por las IP de Cloudflare, que son las mismas que usan miles de webs más.

## El bloqueo

Según explica [hayahora.futbol](https://hayahora.futbol), desde una sentencia de diciembre de 2024 LaLiga y Telefónica Audiovisual Digital pueden comunicar a los operadores (Movistar, MásOrange, Vodafone y DIGI, entre otros) las direcciones IP que deben bloquear durante los partidos. El bloqueo recae sobre IP y no sobre dominios, y las IP de Cloudflare las comparten miles de webs. Mi web no era el objetivo, pero compartía IP con otras que sí lo eran. Según su historial, esas dos IP aparecían bloqueadas a partir de las 13:40 de ese día.

## Cómo lo detecté

Lo primero que hice fue descartar que el problema fuera mío:

- Las páginas de estado de Cloudflare y de GitHub no decían nada: ninguna incidencia publicada.
- Con `nslookup`, el dominio apuntaba a las IP del proxy de Cloudflare, no a GitHub Pages:

```text
$ nslookup codeandia.com
Address: 188.114.96.5
Address: 188.114.97.5
```

- Con `curl` no recibía respuesta.
- En cambio, `www.codeandia.com` respondía (con una redirección 301 al dominio raíz, servida por GitHub), así que GitHub Pages estaba funcionando. Lo que no funcionaba era el camino que pasaba por el proxy.

Para no quedarme con la duda entré en hayahora.futbol. Aparecía que sí que había fútbol ese día, y con el buscador de webs que tienen busqué codeandia.com: estaba bloqueada. Además, su comprobador marcaba **2 de 2 IPs bloqueadas en Movistar, Vodafone, MásMóvil y DIGI**. Ahí tenía la confirmación.

## El arreglo

Pasé los cuatro registros A del dominio raíz (los que apuntan a GitHub Pages, como explico en [qué dominio comprar para tu primer proyecto web](/articulos/guias/que-dominio-comprar-primer-proyecto-web/)) a **DNS only**. Con el proxy apagado, el tráfico va directo del navegador a GitHub Pages y no toca las IP bloqueadas.

![Esquema: con el proxy de Cloudflare activado el navegador pasa por una IP compartida bloqueada; con DNS only va directo a GitHub Pages](/assets/img/laliga-proxy-vs-dns-only.svg){: width="680" height="280"}

Después del cambio, el mismo `nslookup` devolvía las IP de GitHub Pages:

```text
$ nslookup codeandia.com
Address: 185.199.108.153
Address: 185.199.109.153
Address: 185.199.110.153
Address: 185.199.111.153
```

Y `curl -vI` respondió con `HTTP/1.1 200 OK`. La web volvió a cargar.

Así siguen hoy los registros, con la nube gris de DNS only:

![Panel DNS de Cloudflare con los cuatro registros A de codeandia.com hacia las IP de GitHub Pages y el CNAME de www, todos en DNS only](/assets/img/cloudflare-dns-codeandia.png){: width="1066" height="336"}

*Mi zona DNS en Cloudflare. He sustituido mi usuario de GitHub por `TU-USUARIO` en el CNAME.*

## Qué quedó por detrás

El arreglo no es permanente: los bloqueos son dinámicos y el proxy seguía siendo una opción con ese riesgo encima. Además, al apagar el proxy perdí las redirecciones 301 que tenía montadas en Cloudflare; ahora las cubren unas páginas stub que deja el propio blog, que cumplen, aunque no son un 301 de verdad.

## Lo aprendido

- Si una web no carga y el resto de internet va bien, hay dónde mirar: en hayahora.futbol puedes comprobar si hay un bloqueo de este tipo y si afecta a tu dominio.
- Cuando toque depurar conexiones, `curl -v` y no `curl -s`: sin la «v» no ves lo que pasa de verdad en la conexión.
- El proxy de Cloudflare es una dependencia con riesgo si tu audiencia, como la mía, está en España: compartes IP con miles de webs, y si a una de ellas le cae un bloqueo, te puedes ir con ella.
