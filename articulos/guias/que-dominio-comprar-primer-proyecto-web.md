---
layout: article
title: "Qué dominio comprar para tu primer proyecto web: .com vs .es"
description: "Qué elegir para tu primer proyecto web: .com o .es, cuánto pagué por el mío y cómo apunté el DNS a GitHub Pages."
category: "Guía"
date: 2026-09-08
readtime: 3
updated: 2026-10-18
last_modified_at: 2026-10-18
---

Cuando tienes un proyecto de clase o personal y quieres publicarlo con dominio propio, la pregunta llega rápido: ¿`.com` o `.es`? Parece una tontería, pero es la primera decisión que toma alguien que está empezando y la que más dudas deja.

## La diferencia real entre las dos

El `.com` es el que todo el mundo reconoce. Si alguien va a buscar tu proyecto o va a escribirlo de memoria, va a pensar en `.com` antes que en nada, y funciona igual de bien si algún día el proyecto quiere salir de España.

El `.es`, por su parte, deja clarísimo que el proyecto es español y encaja bien con cosas locales: un trabajo de clase con alcance nacional, una web de tu pueblo, una comunidad en español.

Como consejo general, y no como experiencia: **primero comprueba la disponibilidad y después enamórate del nombre**. Muchas veces el nombre que tenías en la cabeza ya está cogido, y entonces compensa ajustar el nombre antes que complicarlo con guiones o números que luego cuesta explicar.

## Lo que hice yo

El dominio de este blog es **codeandia.com** y lo compré el **8 de septiembre de 2026** en **Namecheap**, por **6,99 $ el primer año**. Elegí `.com` porque me parece el más conocido y el más útil a nivel mundial, y porque el nombre que quería estaba libre.

Lo que más me costó no fue el registro, sino entender qué va detrás. Un dominio solo te da el nombre; para que la web funcione tienes que decirle a internet a dónde apunta, y eso se hace con los registros DNS.

## Cómo apunté el DNS

El blog está alojado en **GitHub Pages**, que te da una dirección de su tipo `usuario.github.io`. Lo que hice fue dejar el dominio en Namecheap y apuntar los DNS a **Cloudflare**, que es quien resuelve el dominio y lo lleva hasta GitHub.

En la zona DNS de `codeandia.com` tengo, para el dominio raíz, cuatro registros **A** con destino a las IPs de GitHub Pages, todos en modo **DNS only**:

```
codeandia.com      A    185.199.108.153    DNS only
codeandia.com      A    185.199.109.153    DNS only
codeandia.com      A    185.199.110.153    DNS only
codeandia.com      A    185.199.111.153    DNS only
```

Y para la versión con `www`, un registro **CNAME** que apunta al hosting:

```
www.codeandia.com  CNAME  vibodigitalinfo-lab.github.io    DNS only
```

(Ese `TU-USUARIO` es el nombre de usuario de GitHub con el que tienes la cuenta.)

El resto de registros que hay en la zona (correo, newsletter) los gestiona cada servicio que los necesita; para que la web cargue, con los de arriba basta.

El modo **DNS only** es el que usan los cuatro registros del dominio raíz, y conviene fijarse en él: el proxy de Cloudflare se puede activar o desactivar por registro, y ese interruptor tiene consecuencias. Lo cuento en [este otro artículo sobre el día en que la web dejó de cargar](/articulos/guias/bloqueo-laliga-a-cloudflare-y-como-afecto-a-este-blog/).

## En corto

Si tu proyecto es más bien internacional o quieres que suene serio, `.com`. Si es claramente español y el nombre está libre, `.es`. En cualquier caso, comprueba la disponibilidad antes de decidirte y, cuando lo tengas, dedica el rato a entender los registros DNS: no es difícil, pero si los tocas a ojo se te puede caer algo sin que sepas por qué.
