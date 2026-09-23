---
layout: article
title: "MCP para principiantes: qué es y por qué está por todas partes"
description: "Guía de MCP en 2026 para estudiantes: qué es el Model Context Protocol, para qué sirve de verdad, cómo configurarlo en 5 minutos y qué puedes ignorar."
category: "Guía"
date: 2026-09-14
readtime: 7
---

Llevo semanas leyendo "MCP" en todas las notas de producto de mis herramientas de IA, y una cosa era segura: nadie lo explicaba de forma que entrara en diez líneas. Había probado Cursor, Copilot, una librería local… y cada vez que aparecía la palabra me venía el recuerdo de los días en que me perdía mirando una pila de errores. Pero MCP es más simple de lo que parece, y hoy lo vas a entender aunque sea tu primera vez con esto. Te lo cuento como me lo hubiera explicado a mí hace dos semanas.

## Qué es MCP de verdad

MCP significa **Model Context Protocol** y es un protocolo abierto que presentó Anthropic en noviembre de 2024. La metáfora que repiten todos desde entonces y que es útil: es **"el USB-C de la IA"**. Antes, para que un modelo pudiera leer tu base de datos o tus apuntes, cada herramienta necesitaba su propia integración hecha a medida. Había que enchufar un cable distinto a cada dispositivo. MCP estandariza ese enchufe: un modelo habla con un servidor a través de un protocolo común, y ese servidor sabe acceder a tus datos o a tus herramientas.

En la práctica, la arquitectura es:

- **Host**: la aplicación que usas (Cursor, Claude, tu editor).
- **Server**: un pequeño programa que expone "capacidades" (leer una tabla, buscar en GitHub, buscar en tu documentación).
- **Tools / Resources / Prompts**: las cosas que el servidor ofrece al modelo — funciones que ejecuta, datos que lee, plantillas.

El modelo decide cuándo usar esas capacidades y el servidor las ejecuta por él. Ya está. No hay magia: es "la IA pregunta, el servidor contesta".

Y de 2024 a hoy esto ha dejado de ser una novedad de Anthropic: OpenAI y Google lo soportan, y en diciembre de 2025 Anthropic lo **donó a la Agentic AI Foundation** (con la Linux Foundation) junto a OpenAI y Block, con apoyo de Microsoft, Amazon y Google. La especificación quedó estable en julio de 2026. Es decir: no es una moda pasajera, es el estándar.

## Para qué lo necesitas tú (estudiante de DAW)

Sé honesto: para **editar código no lo necesitas**. Cursor, VS Code y Copilot ya acceden a tus archivos sin MCP. Donde MCP te cambia el día es cuando le pides a la IA algo que está **fuera de los archivos**: una base de datos, la documentación de una librería, tu repositorio en GitHub.

El caso que a mí me enganchó: le dije a un servidor MCP que se conectara a una base SQLite que estaba preparando para el módulo de bases de datos y le pedí "dame los clientes que pidieron más de 3 veces este mes". La IA fue a buscar la estructura real, ejecutó la consulta y me explicó paso a paso qué tabla recorría. En vez de imaginarse la base, la leyó.

Otro uso tonto pero que suma: **Context7**, un servidor MCP que trae la documentación de las librerías. Cuando trasteo con una API de Java que no estoy tocando desde el trimestre pasado, le pido "explícame cómo se instala esto según la doc oficial" y me responde con la doc actual, no con lo que recuerda de su entrenamiento.

## Cómo configurarlo en 5 minutos

No necesitas pensar en "arquitectura". En todos los clientes modernos lo que cambias es un bloque JSON llamado `mcpServers`. La idea es la misma en todos:

- **Cursor**: archivo `.cursor/mcp.json` (del proyecto) o `~/.cursor/mcp.json` (para todos tus proyectos).
- **VS Code + Copilot**: archivo `.vscode/mcp.json` del proyecto.
- **Claude Desktop**: en Windows, `%APPDATA%\Claude\claude_desktop_config.json`.

Un ejemplo real de servidor para una base de datos de prácticas:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@microsoft/postgres-mcp", "postgresql://localhost/tu_base"]
    }
  }
}
```

Si estás en Windows, a veces hay que envolver el comando con `cmd /c`. Y si usas Supabase (como el proyecto que montamos en el curso), su servidor es una URL: `https://mcp.supabase.com/mcp`. Guardas el JSON, reinicias el cliente (o recargas), y listo: aparece una herramienta nueva en el chat.

## Lo que puedes ignorar (los 5 filtros)

Cuando busques tutoriales de MCP te van a asustar con SDK, transportes y OAuth. Como estudiante, puedes ignorar casi todo al principio:

1. **Crear tu propio servidor**: no. Primero usa los que ya existen.
2. **Distinguir versiones de la especificación** (2024-11-05, 2026-07-28…): no, tú no tocas la spec.
3. **Transportes (stdio, HTTP, SSE)**: no, el cliente lo gestiona por ti.
4. **OAuth y autenticación avanzada**: no hasta que toques datos de verdad.
5. **Publicar en el registro oficial**: no, a menos que quieras compartir algo.

Tu trabajo es elegir qué servidor conectas — y no conectarlo a todo.

## El riesgo que no te cuentan en los titulares

Ojo, que no todo es gratis. Conectar servidores MCP **expande el acceso del modelo**, y un modelo engañado es un problema con los datos correctos. En 2026 ya hay casos reales de **injection de instrucciones a través de las descripciones de las herramientas** ("tool poisoning") y de servidores que exfiltran credenciales. Las reglas que sigo yo:

- Solo servidores **oficiales o muy conocidos** (los de tu base, GitHub, Supabase, Context7).
- **Permisos mínimos**: si solo quiero leer la base de prácticas, que el servidor sea read-only.
- Nunca credenciales reales en ejercicios o proyectos de clase.
- Si un servidor tiene mala fama, no lo conecto — ya te conté que este tema (injection y credenciales) es la parte que más me preocupa del desarrollo con LLM en [esta guía que escribí sobre seguridad](/articulos/guias/prompt-injection-seguridad-apps-ia-2026/).

## Mi veredicto

**MCP para un estudiante se reduce a una frase: conéctalo cuando quieras que la IA lea algo que no está en tus archivos, y no lo conectes a todo lo demás.**

Lo uso para dos cosas y con eso me basta: leer bases de datos reales en ejercicios de SQL y tirar de documentación actualizada con Context7. Para escribir código, mi editor ya tiene acceso a los archivos y MCP no me aporta nada. Si estás empezando, prueba el de PostgreSQL/SQLite con una base de prácticas un viernes por la tarde; cuando lo veas ejecutar una query real a tus datos, lo entiendes todo.

Y si quieres el contexto de dónde encaja esto con las instrucciones que le das a la IA, este protocolo convive a diario con ficheros como **AGENTS.md, de los que te hablé [en esta guía](/articulos/guias/agents-md-guia-2026/)**. Si te atascas configurando un servidor concreto de tu módulo, escríbeme a ivan@codeandia.com y te lo dejo montado por pasos.