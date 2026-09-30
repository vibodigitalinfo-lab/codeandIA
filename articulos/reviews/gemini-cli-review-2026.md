---
layout: article
title: "Gemini CLI en 2026: el agente de Google que corre en tu terminal"
description: "Gemini CLI es el agente de terminal de Google: instalación, cómo lee tu repositorio, permisos, precio con AI Studio y si le gana a Codex CLI o Claude Code."
category: "Review"
date: 2026-09-16
readtime: 6
version: "@google/gemini-cli con la clave gratis de AI Studio"
tiempo: "una temporada entera en las prácticas, desde que se lanzó"
proyecto: "la API REST de Spring Boot como conejillo de indias"
limites: "pide confirmación a cada rato y Google cambia el nombre a los productos cada poco"
last_modified_at: 2026-09-30
---

Google llevaba un año llenándonos la cabeza con agentes: los tienes en el editor, en la web y en sus planes de pago, todos repasados en [las herramientas de IA de Google](/articulos/listas/herramientas-ia-google-2026/). La pieza que me faltaba era la del sitio donde vivo cuando programo: la terminal. Hace unas semanas la lanzaron con todo el mohín del mundo y decidí dejarla una temporada en las prácticas para contarte si es una alternativa real a [Codex CLI](/articulos/reviews/codex-cli-openai-review-2026/) y a [Claude Code](/articulos/reviews/claude-code-cli-review-2026/), o si es Google añadiendo una pestaña más.

## Qué es Gemini CLI y cómo se instala

Gemini CLI es el agente de programación de Google que corre en tu máquina, en la terminal, sobre tu repositorio. A diferencia de los dos que ya hemos probado por aquí, no es un complemento de un plan cerrado: es un paquete abierto de npm, por si te da susto meter a un extraño en tu disco.

```bash
npm install -g @google/gemini-cli
```

Escribes `gemini` y arranca una sesión interactiva donde le puedes pedir que explique, genere o edite código. También admite `gemini -p "texto"` para llamarlo de una vez en un script o en una tubería, que es justo el formato que acabará usando quien automatiza cosas.

En Windows lo suyo es WSL, como pasa con el resto de agentes de terminal. La instalación no dio guerra, que ya es mucho decir en este mundo.

## Cómo entra: AI Studio o tu plan de Google

Aquí Google hace una jugada que no esperaba. Puedes usarlo con una **clave de API de AI Studio**, el laboratorio gratuito de Google, o conectarlo a tu cuenta de Gemini para que el consumo salga del plan que ya tengas.

- **Con clave de AI Studio** funciona gratis y sin suscripción, con límites por ventana de tiempo. Es la puerta de entrada que no tiene nadie más hoy: un agente de terminal sin pasar por caja.
- **Con tu plan de Gemini** el uso cuenta dentro de lo que ya pagas o del nivel gratuito del plan. Si eres de los que usa Gemini para el resto de tu vida digital, esto es lo que te ahorra una suscripción más.

Los modelos que mueve por defecto son los de Gemini con razonamiento, y dejan elegir entre el modelo de siempre y las variantes rápidas para lo que escribe respuestas cortas. Sin los precios de cada plan aquí, porque los tienes actualizados en [herramientas de IA de Google](/articulos/listas/herramientas-ia-google-2026/); lo que sí te confirmo es que no pide tajada extra por la herramienta en sí.

## Mi experiencia real: lo que hace bien

Lo dejé sobre la [API REST de Spring Boot](/articulos/guias/primera-api-rest-spring-boot-ia-daw/) que uso como conejillo de indias para todo. El punto fuerte lo vi el primer día: **entiende el contexto de la carpeta sin que se lo cuentes**. Le pides que te explique un controlador y te responde señalando el fichero exacto, con enlaces a las líneas, y desde ahí mantiene el hilo de la conversación como si hubiera leído el repositorio entero.

El flujo de edición es prudente: te muestra el cambio antes de escribirlo y te pide confirmación antes de tocar. Para un proyecto de clase, donde el que más miedo tiene eres tú, esa sensación de que el agente levanta la mano vale más que mil funciones de autocompletado.

Y tiene una gracia que no veo en los otros: el chat acepta **imágenes**, así que le puedes pasar una captura de un error o un diagrama de una entidad y te lo integra en la conversación. En DAW acabas viviendo entre pantallazos de profesores, y que el agente mire la misma pantalla que tú reduce a cero el "te lo copio a mano".

## Lo que me chirría

No todo son flores. Le pedí que añadiera una propiedad a una entidad de JPA y, aunque lo hizo bien, tardó más en decidir que el resto: el modo de confirmación por defecto pide permiso cada poco, y en tareas mecánicas de varias pasadas se hace pesado. Puedes aflojar la rienda con la bandera de modo de riesgo, pero entonces pierdes la supervisión que he alabado un párrafo arriba. Tú eliges.

El otro pero es la **constancia del proveedor**. Google ha cambiado el nombre y la arquitectura de sus productos de IA para desarrolladores varias veces en un año (te lo contaba en [antigravity y el fin de Code Assist](/articulos/listas/herramientas-ia-google-2026/)). Todo apunta a que Gemini CLI se queda, pero después de tantos cambios, me reservo el derecho a esperar un año antes de construir sobre ello mi rutina de clase.

## Cuándo elegirla de verdad

Comparada con [Claude Code](/articulos/reviews/claude-code-cli-review-2026/) y [Codex CLI](/articulos/reviews/codex-cli-openai-review-2026/), Gemini CLI no es la más bestia, pero es la mejor entrada si no pagas nada todavía: la clave de AI Studio te da un agente de terminal real sin cartera. Eso hoy no lo iguala ninguno de los otros dos, que o exigen un plan de pago o un plan gratuito con límites mucho más tacaños.

Si ya pagas ChatGPT, la cuenta te sale rentable con Codex. Si ya vives en el universo GitHub, mira el combate de [Copilot CLI vs Codex CLI](/articulos/comparativas/github-copilot-cli-vs-codex-cli-2026/). Y si tu vida ya es Google, Gemini CLI es el que cierra el círculo sin pedirte dinero.

**Lo recomiendo si** quieres probar un agente de terminal sin pagar, si te sientes cómodo en el ecosistema de Google y si te gusta que el agente te pida permiso. **No lo recomiendo si** ya pagas un plan de OpenAI y buscas la integración máxima, porque el dinero ya lo tienes en otro sitio. Y si no lo has probado aún, dime cómo te va instalándolo; el email sigue siendo ivan@codeandia.com.

## Sigue por aquí

- [Codex CLI de OpenAI en 2026: el agente de terminal gratis y abierto](/articulos/reviews/codex-cli-openai-review-2026/)
- [Las herramientas de IA de Google para programar en 2026](/articulos/listas/herramientas-ia-google-2026/)
- [GitHub Copilot CLI vs Codex CLI en 2026, cuál para tu curso](/articulos/comparativas/github-copilot-cli-vs-codex-cli-2026/)