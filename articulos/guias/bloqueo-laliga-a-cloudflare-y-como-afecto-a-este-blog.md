---
layout: article
title: "Bloqueo de LaLiga a Cloudflare y cómo afectó a este blog"
description: "El 17 de octubre el blog dejó de cargarse: estaba bloqueado por LaLiga. Esto es lo que pasó y cómo lo solucioné."
category: "Guía"
date: 2026-10-18
readtime: 3
last_modified_at: 2026-10-18
---

El 17 de octubre intenté entrar en codeandia.com y la página no cargaba. Todo lo demás sí funcionaba, así que empecé a investigar.

## ¿Por qué no cargaba?

Con ayuda de Claude vimos que el bloqueo no era de mi conexión: era por LaLiga. Ese día había partido y al buscar el dominio en [hayahora.futbol](https://hayahora.futbol/) aparecía bloqueado.

## Cómo lo solucioné

Pasé los registros A de Cloudflare a **DNS only** y, al poco, la web volvió a responder correctamente. Al principio pensé que me habían baneado y me agobió un momento, pero no había hecho nada malo.

## Esa semana

Estuve en un trabajo en grupo para mejorar digitalmente una empresa. Aprendí a usar Git y GitHub: hubo momentos de caos con la terminal, pero con Gemini pasándole el error y los comandos que había usado conseguí solucionarlo. También usamos Trello por obligación: es intuitivo y visual y ayuda a saber qué estaba pendiente y qué completado.

## Programación y bases de datos

En programación seguimos con Eclipse en primero de DAW. Crear proyectos y clases va bien. A veces cuesta por pereza, clases largas o distracciones, y prefiero hacerlo en casa. Allí le paso a Claude los ejercicios hechos en clase, cómo los quiere el profesor, pido más ejercicios, correcciones y explicaciones, y así voy entendiendo.

En bases de datos estamos con diagramas entidad-relación y el modelo relacional (tablas). Al principio en papel era fácil equivocarse con las cardinalidades. Ahora usamos [erdplus.com](https://erdplus.com/) para hacer los diagramas: es cómodo, intuitivo y cumple lo que necesitamos.

## Sigue por aquí

- [Aprender Java en DAW con IA y no volverte dependiente](/articulos/guias/aprender-java-con-ia-daw/)
- [Qué portátil necesita un estudiante de DAW: mi caso con i3 y 8 GB](/articulos/guias/que-portatil-comprar-estudiar-daw-2026/)
