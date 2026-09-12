---
layout: article
title: "Ollama: mi review corriendo modelos de IA en local con un portátil de estudiante"
description: "Probé Ollama durante un mes para correr modelos de IA en mi propio portátil sin pagar API: instalación, modelos que merecen la pena, límites reales y veredicto."
category: "Review"
date: 2026-09-07
readtime: 7
---

A finales del curso pasado me di cuenta de que estaba pagando tres cosas a la vez: ChatGPT Plus, GitHub Copilot Pro y Cursor. No era que las usara todas a todas horas, era más bien el miedo a quedarme sin ellas el día que hicieran falta. Y un día, mirando las facturas juntas, pensé: esto no tiene sentido para un estudiante de DAW.

Fue mi compañero de la última fila, el del portátil lleno de pegatinas, el que me soltó la idea: "¿por qué no pruebas a correr un modelo en local con Ollama? Es gratis, y tan tonto no es."

Así que lo probé. Configuré Ollama, bajé modelos, lo usé un mes en mi flujo real de clase y de proyecto personal. Esto es lo que encontré, sin humo.

## Qué es Ollama, en una frase

Ollama es una herramienta de terminal que descarga modelos de lenguaje y los ejecuta en tu propia máquina. No mandas tus preguntas a un servidor de OpenAI ni de nadie. El modelo se instala en tu disco, se carga en tu RAM y responde con tu CPU o tu tarjeta gráfica.

Lo de "correrlo tú mismo" tiene una pinta más técnica de lo que en realidad es. El comando básico no puede ser más simple: `ollama run llama3.2:3b`. En el momento en que lo ejecutas, Ollama se descarga el modelo que le pidas (la primera vez tarda un rato) y te deja yo con una terminal interactiva donde puedes escribir normal.

## Instalación y primera impresión

En Windows instalé Ollama con el instalador oficial, que es una aplicación que se queda en la bandeja del sistema. En Linux la historia es un comando: `curl -fsSL https://ollama.com/install.sh | sh`. La verdad es que no le di ninguna pega: bajé el instalador de la web, lo abrí, y en dos minutos estaba yo descargándome el primer modelo.

Mi portátil es uno normal de los de clase: 16 GB de RAM, tarjeta gráfica integrada, nada de GPU gamer. Con eso pensé que el modelo iba a tardar treinta segundos en contestarme. No fue tan mal.

Empecé con `llama3.2:3b`, que es pequeñito. Respuestas casi instantáneas. Después subí a `qwen2.5:7b` para tareas de código, y ahí ya noté que el portátil se calentaba y las respuestas tardaban unos segundos, pero seguían siendo manejables. Con modelos más grandes como `deepseek-r1:8b` empecé a ver la RAM al límite y el equipo haciendo ruido de aspiradora. Ahí está el primer límite, y conviene enterarse pronto.

## Qué modelos uso de verdad

Esto es lo que aprendí después de un mes: la etiqueta no lo es todo, el tamaño sí.

- **`llama3.2:3b`**: lo dejé para cosas rapiditas de texto, redactar un mensaje, resumir una clase, explicarme un concepto sin darle mucha caña. Va fino incluso en máquinas normales.
- **`qwen2.5:7b`**: mi favorito para preguntas de código. Entiende lo suficiente de Java, SQL y JavaScript como para ayudarme con ejercicios de DAW. Es el equilibrio que busqué durante días.
- **`phi4:14b`**: lo probé por las ganas de ver más "inteligencia", pero en mi portátil se arrastraba. Si tienes una GPU decente, seguro que rinde más; yo no.
- **`deepseek-r1:8b`**: el que más me gustó como compañero de razonamiento, cuando le pides que piense paso a paso. Es lento en mi máquina, pero cuando le das una función de Java y le pides "encuentra el fallo", se nota que razona en voz alta.

No me líes con las versiones exactas porque en esto salen modelos nuevos cada pocos meses. La idea que te tienes que llevar: los modelos de 3B no son tontos, los de 7B ya se defienden, y a partir de 8-14B en un portátil sin gráfica buena empiezas a depender de la paciencia.

## Para qué me ha servido de verdad

Lo que menos esperaba es que Ollama se convirtiera en mi herramienta para lo que no quiero meter en la nube. En DAW trabajamos con datos del instituto, exámenes, ejercicios con las soluciones, y a mí no me gusta trolear que eso esté en un chat de una empresa americana. Con Ollama, el historial se queda en mi disco. Punto.

También le saqué partido cuando se me acababa el balance gratis de las APIs o cuando estaba sin cobertura. En el tren de vuelta a casa, sin red, pude seguir explorando "por qué me da error esta query de MySQL" con un modelo local. Eso no lo ofrece ninguna web.

Y hay una cosa que no aparece en ninguna review: **aprender cómo funciona un LLM**. Instalar Ollama, medir cuánto tarda cada modelo, ver cómo se calienta el equipo y por qué un modelo de 7B alucina más que uno de 70B te obliga a entender de qué va esto, y eso en una asignatura técnica vale más que mil prompts.

## Los límites, sin adornos

Ahora la parte que nadie te cuenta cuando te dicen "Ollama es gratis y listo".

Primero, **los modelos pequeños alucinan más**. Muchas veces me devolvió código Java que no existe, bibliotecas inventadas o sintaxis de una versión distinta. Si no sabes ya lo que estás haciendo, Ollama te puede liar tanto como ayudarte.

Segundo, **es lento para la talla que maneja un estudiante normal**. Lo mío no es correr modelos en local para escribir una aplicación de 20 archivos; eso es para gente con gráfica dedicada. En mi portátil, para tareas largas, prefería pegar el problema en ChatGPT y que me respondiera en dos segundos.

Tercero, **no sustituye a Copilot ni a Cursor**. Los modelos que uso con Ollama no están integrados en el editor como el autocompletado de GitHub Copilot. Ollama te da una terminal donde hablar con un modelo; el resto del flujo —que el código se autocomplete mientras escribes, que te haga tab a tab— eso no lo tienes, o para montarlo necesitas plugins de terceros que al final te dan más guerra que otra cosa.

## Veredicto: para quién es y para quién no

¿Merece la pena Ollama para un estudiante de DAW en 2026? Sí, pero con matices.

- **Sí**, si quieres privacidad, si te gusta aprender cómo funcionan estas herramientas, o si un día te quedas sin conexión.
- **Sí**, como complemento gratuito, para preguntas donde no importa esperar cuatro segundos.
- **No**, como sustituto de tu asistente de código en el editor. Ahí sigo usando Cursor para lo gordo y las [7 herramientas de IA gratuitas](/articulos/listas/7-herramientas-ia-gratuitas-estudiantes-desarrollo-web-2026/) para el resto.
- **No**, si lo que buscas es la remota inteligencia de un modelo grande. En tu portátil no cabe un GPT-5, y si no tienes gráfica, lo que corre en local se queda corto.

Un mes después, Ollama sigue instalado en mi máquina, pero lo uso de forma puntual: privacidad, sin red, o curiosidad. Es una herramienta que vale la pena tener, no una que vaya a cambiar tu vida. Y eso, a mí, ya me parece bastante.

Si te está enganchando esto de las herramientas nuevas de IA, te recomiendo echar un vistazo a [mi review de Claude Code](/articulos/reviews/claude-code-cli-review-2026/) (otra que corre desde terminal, pero con modelos en la nube) o a la [guía de MCP](/articulos/guias/mcp-model-context-protocol-guia-desarrolladores/), que es el protocolo que permite que estos modelos se conecten con tus proyectos.