---
layout: article
title: "ChatGPT vs Claude vs Gemini para programar en 2026"
description: "Comparativa real de ChatGPT, Claude y Gemini para programar en 2026: precios, contexto, modo agente y cuál te conviene según tu bolsillo y tus proyectos."
category: "Comparativa"
date: 2026-09-16
readtime: 6
---

En clase la pregunta es semanal: *"¿tú qué usas, ChatGPT, Claude o Gemini?"*. Cada uno defiende su bando como si fuese un equipo de fútbol, y la verdad es que casi todos copiamos del que le funcionó el primer día y no miramos atrás. El problema es que eso era razonable en 2024, pero en 2026 las tres opciones han cambiado muchísimo: precios, límites y sobre todo el **modo agente**, que se ha vuelto la diferencia real. Me he pasado dos semanas probando las tres con ejercicios de los módulos y esto es lo que he encontrado. Y aviso: hablo de precios y límites de septiembre de 2026, que en este sector cambian cada pocos meses.

## Lo primero: qué piden de tu bolsillo

**ChatGPT** (OpenAI):
- **Gratis**: sí, con límites de uso por ventana (en la práctica, unas horas). Suficiente para preguntas sueltas.
- **Go**: 8 €/mes (el antiguo "Plus básico" que lanzaron en 2025).
- **Plus**: 20 €/mes, el clásico; te da contextos largos y acceso a modelos de razonamiento.
- **Pro**: 100 a 200 €/mes, para uso intensivo de investigación.
- Lo interesante: los planes de pago incluyen **Codex**, el agente de código, y que pagues 20 € al mes te da esto sin sorpresas. Además, desde 2025 el límite de la versión gratis abarca ChatGPT, o sea que lo usas también para imágenes y búsqueda.

**Claude** (Anthropic):
- **Gratis**: sí, con una **ventana de uso de 5 horas** en la que se agota pronto (según el día, entre 5 y 10 mensajes para programación pesada).
- **Pro**: 20 $/mes. Aquí sí que notas la diferencia: contexto amplísimo en Claude Code y ventanas de uso mucho mayores.
- **Max**: 100 $ (5x) o 200 $ (20x) al mes, para quien vive del modelo.
- El detalle que afecta a estudiantes: **no hay descuento oficial de estudiante**, algo que ya comenté en [si merece la pena pagar por una IA](/articulos/comparativas/merece-la-pena-pagar-ia-2026/).

**Gemini** (Google):
- **Gratis**: sí, con límites diarios y ventana de 5 horas igual que Claude. A mí se me agota con un proyecto de tarde.
- **AI Plus**: entre 4,99 y 7,99 €/mes según región.
- **AI Pro**: 19,99 €/mes.
- **AI Ultra**: 99,99 a 199,99 €/mes.
- Ojo, estudiantes: en EE. UU. hay promos de un año gratis del plan superior, pero **en España no aparecen**; no te fíes de los clips de TikTok que lo pintan como universal.

## El contexto: de cuánta ventana hablamos

Sinceramente, para DAW la mayoría de ejercicios caben en cualquier ventana. La diferencia aparece cuando arrastras un **proyecto de varias páginas**: ahí el orden es más o menos Claude > ChatGPT > Gemini. Claude Pro con su contexto enorme es el que antes te acaba replicando un proyecto entero de un sitio. ChatGPT Plus con Codex también se defiende muy bien y da pasos en tu repositorio. Gemini en su plan gratis se ahoga antes en proyectos grandes, pero para fragmentos va tan fino como los otros.

## El modo agente: la verdadera diferencia en 2026

Esto es lo que yo miraría antes que nada. En 2026 "chatear con la IA" es la parte fácil; lo que marca la diferencia es si el modelo puede **tocar tu repositorio, ejecutar comandos y proponerte cambios que tú apruebas**:

- **Claude Code**: el más cómodo de arrancar con Claude de fondo. Te lee el proyecto, te propone diffs y hasta deja tareas trabajando. Para proyectos de DAW largos es una gozada.
- **Codex (ChatGPT)**: integrado en el IDE y con una lógica de "ejecuta, falla, corrige" que con ejercicios de clase funciona muy bien. La velocidad es lo que mejor valoro.
- **Gemini** en versión móvil/web es más conversacional, pero su salto agente es **Antigravity** (antes Gemini Code Assist): gratis en su plan individual con 6.000 peticiones de código al día, y desde junio de 2026 las extensiones de Gemini Code Assist se han ido moviendo ahí. Si tu proyecto es GitHub, **Jules** (el agente de tareas en segundo plano de Google) también es una opción tremenda para "mándame un PR que arregle este issue".

Esto lo cuento con más detalle en [la lista de herramientas IA de Google](/articulos/listas/herramientas-ia-google-2026/), porque Google pierde la batalla del "chat de moda" pero gana la de darte cosas gratis.

## Veredicto según tu caso

No hay un ganador absoluto; lo digo siempre, y también lo dije cuando [comparé GPT-5 con Claude](/articulos/comparativas/gpt-5-vs-claude-para-programar-2026/) o [los gratuitos entre sí](/articulos/comparativas/deepseek-vs-chatgpt-gratuitos-para-programar/). La decisión es tuya según tu bolsillo y tu proyecto:

- **Si no vas a pagar nada**: Gemini gratis aguanta más que ChatGPT gratis si eres constante (los 6.000 de código al día de Antigravity son la mejor lotería gratis del sector), y Claude gratis es el que más cómodo te deja cuando el modelo está "iluminado". Yo iría primero a Gemini para probar y a ChatGPT para respuestas de una tanda corta.
- **Si puedes pagar 8-10 €/mes**: ChatGPT Go o Google AI Plus. Para estudiantes, el salto de precio-no-cambio suele decepcionar; lo he visto con [ChatGPT Plus](/articulos/reviews/chatgpt-plus-para-programadores/) y el diferencial real está en los agentes.
- **Si puedes pagar 20 €/mes**: aquí me inclino por **Claude Pro si trabajas en proyectos grandes** y por **ChatGPT Plus si quieres rapidez y Codex**. Es el empate más igualado de la lista.
- **Si quieres un agente que trabaje mientras tú estás en clase**: Codex o Claude Code según la IA que ya uses; de JavaScript no te juzgo, que [cada uno tiene su manía](/articulos/comparativas/cursor-vs-claude-code-2026/).

## Mi veredicto

**ChatGPT gana en comodidad y velocidad, Claude gana en contexto y calidad de razonamiento, y Gemini gana en precio gratis.** Para un estudiante de DAW en España en 2026, mi combinación es: Gemini/Antigravity para el día a día gratis, y cuando un proyecto se me atraganta, tiro de Claude o ChatGPT de pago solo ese mes. Y recuerda que la IA no te sustituye: [programar con ellas de apoyo](/articulos/guias/aprender-java-con-ia-daw/) es la forma en que de verdad se aprende. Si quieres que te oriente con tu caso concreto (qué módulo estás haciendo, cuánto quieres gastar), escríbeme a ivan@codeandia.com.