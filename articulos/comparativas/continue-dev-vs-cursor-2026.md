---
layout: article
title: "Continue.dev vs Cursor vs Copilot: comparativa para estudiantes"
description: "Continue.dev, Cursor y GitHub Copilot cara a cara: precios, privacidad, modelos (Claude, GPT, Ollama local) y cuál uso yo en prácticas de DAW."
category: "Comparativa"
date: 2026-08-20
readtime: 9
---

Llevo años usando GitHub Copilot en el editor, Cursor me lo instalé este curso, y hace dos meses me metí Continue.dev (open source, MIT) con Ollama local para no mandar código a la nube. Tres formas de "IA que te ayuda a programar", tres precios, tres filosofías. Te las comparo **con números reales y experiencia de prácticas DAW**, no con el marketing de cada uno.

---

## Por qué comparar justo estos tres

- **GitHub Copilot (Individual)**: el estándar en VS Code/JetBrains/Vim. Autocompletado + chat, $10/mes, gratis para estudiantes.
- **Cursor**: fork de VS Code (Electron) con chat, Composer (multi-archivo), agent mode, MCP. $20/mes, algo free.
- **Continue.dev**: extensión para VS Code/JetBrains que te trae modelos remotos (Anthropic, OpenAI) o locales (Ollama) + chat + agent + index de codebase. Gratis, open source.

Un estudiante me preguntó: "¿Instalo Cursor o sigo con Copilot?" Otro: "¿Continue con Ollama sirve para exámenes sin red?" Vamos a responder.

---

## Criterios reales que miro (no el de la web oficial)

| Criterio | Qué miro yo |
|---|---|
| **Coste real estudiante** | Gratis DAW, Individual, Pro — sin engañar con "desde $..." |
| **Privacidad** | ¿Tu código sale de la máquina? Crítico en prácticas con NDA o sin red. |
| **Modelos disponibles** | ¿Solo su modelo? ¿Multi-modelo? ¿Local? |
| **Autocompletado** | Velocidad, precisión en Java/Spring (mi día a día), sin conflictos. |
| **Chat / Agent** | Edición multi-archivo, ejecutar terminal, MCP, hooks. |
| **Index / Context del repo** | ¿Entiende todo mi proyecto? ¿O solo el archivo abierto? |
| **Offline** | ¿Sin red / en examen funciona? |
| **DX / Estabilidad** | ¿Se cuelga? ¿Atajos cómodos? ¿Importar config? |

---

## Ronda 1: Coste (lo que más duele a comienzo de curso)

| Plan | Copilot Individual | Cursor (Hobby → Pro) | Continue.dev |
|---|---|---|---|
| **Gratis** | **Gratis vía Students Pack** (2 años) | **Free** (2k completions + 50 agent chat/mes) | **Gratis ILIMITADO** (open source, MIT) |
| **Pago base** | $10/mes | $20/mes (Pro, 500 fast requests/mes) | Pagás APISep usado (Anthropic, OpenAI, Gemini) o nada con Ollama local |
| **Para estudiante** | **$0** | **$20/mes** (sin descuento estudiante salvo Education Pro $0 en 2026 limitado) | **$0** (local) / ~$5-15/mes (API remota según uso) |
| **Hard cap** | Sin cap (rate limit suave) | 500 fast → luego lento (queue) | Sin cap (tu API / tu hardware) |

**Ganador coste:** **Empate: Copilot (gratis estudiante) y Continue (gratis local)**. Cursor es el único que no es $0 en tu caso DAW (salvo promo Education Pro puntual).

---

## Ronda 2: Privacidad y offline (el que nadie mira hasta que te hace falta)

| | Copilot | Cursor | Continue |
|---|---|---|---|
| **Datos de código** | Telemetry ON (opt-out) → va a GitHub/MS | Telemetry + index propio → va a Cursor/AWS | **Tú decides**: Ollama local = nada sale; API remota = al proveedor que elijas |
| **Self-host / local** | ❌ | ❌ | ✅ **Ollama local (qwen2.5-coder, llama3.2, etc.)** |
| **Funciona sin red** | ❌ | ❌ | ✅ Con Ollama local (tras `ollama pull`) |
| **Compliance org/NDA** | ⚠️ (policy org) | ⚠️ | ✅ **Local = máximo control** |

**Ganador privacidad/offline:** **Continue.dev + Ollama** por goleada. Si tienes examen práctico sin red o prácticas con datos sensibles, es la única que sigue funcionando.

---

## Ronda 3: Autocompletado (el día a día real)

| | Copilot | Cursor (Tab) | Continue (local qwen2.5-coder:7b) |
|---|---|---|---|
| **Latencia** | ~70 ms (cloud) | ~80 ms (cloud) | **~150-300 ms** (local 7b) en portátil 16 GB |
| **Precisión Java/Spring** | ⭐⭐⭐⭐⭐ (entrenado con tu repo) | ⭐⭐⭐⭐⭐ (Composer/tab igual) | ⭐⭐⭐⭐ (bueno, conecta peor el repo) |
| **Precisión Python/JS/TS** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Conflictos con otras extensiones** | Base — nadie pelea con él | Compite con Copilot (desactivar uno) | Compite con ambos (elige uno para tab) |
| **Inline vs suggestions** | Inline ghost + panel lateral | Ghost + Composer (reemplaza selección) | Ghost (Continue tab) + panel chat |

**Ganador autocompletado:** **Copilot (gratis estudiante) en Java/Spring**. En Python/JS, empate con Cursor. Continue local queda por detrás en latencia, pero sorprende en calidad con `qwen2.5-coder:7b`.

**Regla:** **Solo un autocompletado activo**. Yo dejo Copilot para tab y Continue solo para chat/agent. Tener Copilot + Cursor tab + Continue tab a la vez = parpadeo y locura.

---

## Ronda 4: Chat y Agent (editar varios archivos, ejecutar comandos, MCP)

| | Copilot Agent | Cursor Agent | Continue (agent + Ollama) |
|---|---|---|---|
| **Multi-archivo** | ✅ (crea/edita varios, pregunta antes) | ✅ (Composer) | ✅ (via chat → apply) |
| **Terminal** | ✅ Copilot Agent ejecuta comandos | ✅ Cursor terminal tool | ⚠️ Continue no ejecuta terminal (copias y pegas) |
| **MCP / Tools** | ✅ (filesystem, GitHub, Postgres, etc.) | ✅ (MCP nativo, 100/scope) | ⚠️ No nativo; via config JSON manual |
| **Modelo recomendado** | Claude Sonnet 4 (gratis en plan), GPT-5 (Pro+) | Claude Sonnet/Grok Build, Composer | Tú eliges: Sonnet/GPT vía API, o Ollama local |
| **Teleprompter / contexto** | Índice semántico VS Code | Índice propio (potentísimo) | Índice local + `@file`/`@codebase` manual |

**Ganador agent:** **Empate técnico: Copilot Agent y Cursor Agent**. Ambos son autónomos, ejecutan comandos, usan MCP, editan 10 archivos y reintentan en fallos. Continue agent (con Ollama) es más "chat que aplica cambios", no autónomo total.

Hablando de esto, si quieres el detalle de lo nuevo: [GitHub Copilot Agent Mode 2026: qué es y si merece la pena el salto](/articulos/guias/github-copilot-agent-mode-2026-guia/) y [Cursor Rules (.mdc) para que la IA programe como tú quieres](/articulos/guias/cursor-rules-configuracion-mdc-guia/).

---

## Ronda 5: Modelos y coste por token (el detalle que nadie mira)

| Proveedor | Claude Sonnet 4 | GPT-5 | DeepSeek V3 | Ollama local |
|---|---|---|---|---|
| **$ / MTok input** | ~$3 | ~$5 | ~$0.55 | **$0 (tu RAM)** |
| **$ / MTok output** | ~$15 | ~$15 | ~$2.19 | **$0** |
| **Context window** | 200k (Copilot/Cursor), 128k (Ollama 7b) | 128k | 64k | 32k-128k según modelo |
| **Vía Copilot** | Precio plano ($10/mes) — te olvidas | Idem (credits sep 2026) | No | No |
| **Vía Cursor** | Credits (500 fast) | Credits | No | No |
| **Vía Continue** | Tu API key / local | Tu API key | Tu API key | Offlin |

**Para estudiante:** Copilot te abstrae el coste (flat). Continue local = gratis total. Continue remoto = pagás uso real (en mis pruebas DAW: ~$8-12/mes con Sonnet si usas agent diario).

---

## Mi veredicto honesto por caso de uso

| Caso | Uso | Por qué |
|---|---|---|
| **Estudiante DAW con Pack Estudiante** | **Copilot Individual ($0)** | Gratis 2 años, mejor autocompletado Java, Agent autónomo, zero config |
| **Proyecto Java / Spring en IntelliJ** | **Copilot en JetBrains** | Agent + chat dentro de IntelliJ (ver [Copilot en IntelliJ](/articulos/guias/github-copilot-intellij-java-daw/)) |
| **Privacidad total / offline / examen sin red** | **Continue.dev + qwen2.5-coder:7b (Ollama)** | Gratis, nada sale, funciona sin red, sorprendentemente bueno |
| **Side project React/Next.js + IA agente autónomo** | **Cursor Pro ($20)** | Autonomía real, Composer, MCP, preview deployment cercano |
| **Portfolio / SaaS serio / presupuesto cero** | **Continue.dev + API Sonnet/GPT** | Gratis + pagás consumo real, eliges modelo, control total |

**Mi setup real (hoy):**
- **Día a día (clase, prácticas Java):** Copilot Individual (estudiante gratis) como autocompletado + Copilot Agent para tareas gordas.
- **Código sensible / sin red:** Continue.dev + `qwen2.5-coder:7b` local (alias `ai` en terminal).
- **Side projects serios (React/Next.js, auth + DB):** Cursor Pro ($20) cuando necesito agent que ejecute 20 archivos y no quiero babysitting.

No es religión: es **usar la herramienta que menos fricción pone ese día**. Copilot te cubre el 80% gratis. Continue te salva el 10% offline/privado. Cursor es el 10% donde necesitas autonomía total.

---

Al final esta comparativa se reduce a una pregunta: ¿prefieres gratis, abierto y laborioso, o de pago, pulido y que te deja trabajar? Mi respuesta cambió con el presupuesto, y no me avergüenza admitirlo. La tuya dependerá del momento del curso en el que estés, y eso también es perfectamente válido.
