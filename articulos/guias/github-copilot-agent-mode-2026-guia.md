---
layout: article
title: "GitHub Copilot Agent Mode 2026: qué es, cómo se usa y si merece la pena el salto desde Chat/Edit"
description: "Guía completa del modo Agent de Copilot: modo autónomo multi-archivo, terminal, auto-corrección, precios con créditos IA, y comparativa con Cursor y Claude Code."
category: "Guía"
date: 2026-09-07
readtime: 8
affiliate_text: "Activa Copilot Pro y prueba Agent Mode en VS Code hoy"
affiliate_url: "https://github.com/features/copilot/plans"
affiliate_label: "Ver planes Copilot"
---

Hasta abril 2025, GitHub Copilot era "autocompletado en esteroides" (modo Chat) o "edita varios archivos si se los seleccionas" (modo Edit). **Agent Mode cambió las reglas**: ahora Copilot **planifica, edita múltiples archivos, ejecuta comandos en terminal, ve los errores, y se corrige solo en bucle** hasta que la tarea funciona.

Lo probé en un proyecto real de prácticas (microservicios Spring Boot + React, tests, Docker, CI/CD). Te cuento cómo funciona, qué cambió en 2026, cuánto cuesta realmente con el sistema de créditos, y si compensa frente a Cursor o Claude Code.

---

## Qué es Agent Mode y en qué se diferencia de Chat/Edit

Tres modos en VS Code (y JetBrains, VS, Neovim, CLI, Web, Mobile):

| | **Chat** | **Edit** | **Agent** |
|--|----------|----------|-----------|
| **Archivos** | Manual (tú los abres) | Multi-archivo (tú los seleccionas) | **Autónomo (elige él los archivos)** |
| **Terminal** | ❌ | ❌ | ✅ **Ejecuta comandos** |
| **Auto-corrección** | ❌ | ❌ | ✅ **Itera en fallos** |
| **Contexto** | Historial chat | Archivos seleccionados | **Codebase entero (indexado)** |
| **Casos de uso** | Preguntas, explicaciones, snippets | Refactors conocidos, cambios multi-archivo guiados | **Features completas, debugging, scaffolding, migraciones** |

**En palabras simples**: Chat = "pregúntame". Edit = "cambia estos archivos". Agent = **"haz esta feature completa, yo me encargo"**.

---

## Cómo funciona el bucle autónomo

Le das una instrucción en lenguaje natural:
> "Añade autenticación JWT al microservicio `users`: endpoint login, registro, middleware de validación, tests de integración, y actualiza el Dockerfile para copiar el keystore."

Agent Mode hace:
1. **Explora** el codebase (usa índice semántico, no solo grep)
2. **Planifica** internamente: qué archivos tocar, en qué orden
3. **Edita** `UserController.java`, `JwtConfig.java`, `SecurityConfig.java`, `application.yml`, `Dockerfile`, `UserControllerTest.java`...
4. **Ejecuta** `./mvnw test` en terminal integrada
5. **Si falla**: lee el error, modifica el código, **vuelve a ejecutar**
6. **Repite** hasta que tests pasan o pide ayuda

**Tú ves todo en tiempo real**: archivos modificados (diff), comandos ejecutados, output de tests. Puedes parar en cualquier momento (`Esc`) o dejar que termine.

---

## Novedades 2025-2026 que importan

### Agent Mode GA (abril 2025, VS Code 1.99)
Salió de preview. Estable en VS Code, JetBrains (2025.2+), Visual Studio, Neovim, GitHub CLI, GitHub Mobile, GitHub Web.

### Copilot Coding Agent (mayo 2025)
**Agente en la nube**: le asignas un *issue* en GitHub → el agente clona el repo, trabaja en una rama, abre PR. **No necesitas tener VS Code abierto**. Útil para "arregla este bug" mientras estás en clase.

### Project HydraFusion (sep 4, 2026)
**Orquestación multi-modelo**: Copilot elige el mejor modelo para cada subtarea (Claude para reasoning, GPT-5 para código, Gemini para contexto largo). Transparente para el usuario.

### Canvases, Parallel Agents, Stacked Sessions (H2 2026)
- **Canvases**: vista visual del plan de Agent (nodos = pasos, edges = dependencias)
- **Parallel Agents**: varios Agent Mode trabajando en ramas distintas del mismo issue
- **Stacked Sessions**: continuas una sesión Agent días después sin perder contexto

### NES (Next Edit Suggestions)
Predice **dónde** será tu próxima edición y pre-carga el diff. Ahorra keystrokes en refactors repetitivos.

### Modelos disponibles (sep 2026)
Claude Fable 5, Sonnet 4/5, Opus 4.7/5, GPT-5 family, Gemini 3.5-3.8, Grok 4.5/4.6, Kimi K2.7/3. **Auto-select** en planes básicos; **elección manual** en Pro+/Max.

---

## Precios reales: el sistema de créditos IA (septiembre 2026)

GitHub cambió a **créditos IA ($0.01/crédito)**. Cada plan incluye una cantidad base + "créditos premium" para modelos caros (Opus, GPT-5, etc.).

| Plan | Mensual | Anual | Créditos base/mes | Créditos premium/mes | Modelos premium | Agent Mode |
|------|---------|-------|-------------------|----------------------|-----------------|------------|
| **Free** | $0 | — | Limitado | ❌ | ❌ Auto-select | ❌ |
| **Pro** | **$10** | $100 | $15 ($10+$5) | Limitado | Limitado | ✅ |
| **Pro+** | **$39** | $390 | $70 ($39+$31) | ✅ | ✅ Opus, etc. | ✅ + 3rd party agents |
| **Max** | **$100** | $1,000 | $200 ($100+$100) | ✅ Priority | ✅ Priority | ✅ Todo |
| **Business** | $19/seat | — | $1,900 | ✅ | ✅ + IP indemnity, SSO | ✅ |
| **Enterprise** | $39/seat | — | $3,900 | ✅ | ✅ + Knowledge Bases, fine-tuning | ✅ |

**Claves que no te cuentan en la landing**:
- **Agent Mode está en TODOS los planes de pago** (Pro, Pro+, Max, Business, Enterprise). Free **no** lo tiene.
- **Agentes de terceros (Claude Code, Codex)**: solo **Pro+** ($39/mes) en adelante.
- **Créditos se consumen por**: requests a modelos premium, Tool calls (terminal, file ops), embedding/indexing.
- **Estimación real**: una sesión Agent de 30 min en repo mediano (~50 archivos) gasta ~$0.50-2.00 en créditos premium. Un mes intenso puede superar los $15-30 de créditos extra.

**Para estudiante**: **Copilot Pro ($10/mes o gratis con Student Pack)** te da Agent Mode con créditos limitados. Si usas modelos base (no Opus/GPT-5), te sobra. Si necesitas modelos premium a diario, **Pro+ ($39)** es el salto real. No hay descuento estudiante en Pro+.

---

## Mi experiencia real en prácticas DAW

**Proyecto**: migración de monolito Spring Boot a 3 microservicios (users, orders, notifications) + API Gateway + React frontend.

**Lo que Agent Mode hizo bien**:
1. **Scaffolding completo**: "Crea microservicio `orders` con Spring Boot 3.3, PostgreSQL, Kafka, OpenAPI, tests, Dockerfile, Kubernetes manifests" → 47 archivos creados/modificados en 8 min. Compiló a la primera.
2. **Debugging en bucle**: test de integración fallaba por configuración de testcontainers. Agent leyó el error, arregló `@DynamicPropertySource`, re-ejecutó, pasó. **3 iteraciones sin mi intervención**.
3. **Refactor transversal**: "Cambia todos los `ResponseEntity` por `ResponseEntity<ApiResponse<T>>` en todo el codebase" → 23 archivos, 0 roturas.

**Lo que falló**:
1. **Alucinación de dependencias**: en un `pom.xml` añadió una librería que no existe (`spring-boot-starter-jwt-v2`). Lo pillé en el diff.
2. **Over-engineering**: para un DTO simple, generó Builder + Lombok + validación + mappers MapStruct. Tuve que decirle "solo record + @NotNull".
3. **Memoria de contexto**: en sesión larga (>2h), empezó a "olvidar" decisiones de arquitectura tomadas al principio. Reiniciar sesión ayuda.

---

## Copilot Agent vs Cursor vs Claude Code

| | Copilot Agent | Cursor Agent | Claude Code |
|--|---------------|--------------|-------------|
| **UI** | VS Code nativo (panel lateral) | VS Code fork (Composer panel) | Terminal (CLI) |
| **Modelos** | Multi (auto o manual Pro+) | Multi (Grok, Composer, Sonnet, etc.) | Solo Claude (Opus/Sonnet/Haiku/Fable) |
| **Contexto codebase** | Índice semántico VS Code | Índice propio (más potente) | **Lee repo entero a demanda** |
| **Terminal** | ✅ Integrada | ✅ Integrada | ✅ Nativa (es terminal) |
| **MCP** | ❌ | ⚠️ Limitado | ✅ **Nativo, first-class** |
| **Dynamic Workflows** | ❌ | ❌ | ✅ **Paralelismo masivo** |
| **Precio base** | $10/mes (Pro) | $20/mes (Pro) | $20/mes (Pro) |
| **Mejor para** | Usuarios VS Code,企业, GitHub ecosystem | Devs que quieren IDE IA-first | Seniors, terminal-first, workflows complejos |

**Benchmarks comunidad (2026 H1)**: Cursor y Claude Code **superan a Copilot** en calidad de código, reasoning, y completitud de tareas complejas. Copilot gana en **integración enterprise (SSO, IP indemnity, Knowledge Bases)** y **ecosistema GitHub nativo**.

---

## Guía rápida: activar y usar Agent Mode hoy

1. **VS Code**: `Ctrl+Shift+P` → "Copilot: Open Chat" → botón "Agent" (icono robot) en el panel de chat. O `Ctrl+Alt+A`.
2. **Prompt inicial**: sé específico. "Añade X" → malo. "Añade endpoint POST /api/orders con validación Bean Validation, test de integración con Testcontainers, y actualiza OpenAPI spec" → bueno.
3. **Controla el bucle**: `Esc` para pausar. Revisa diffs antes de aceptar (botón "Accept" en cada archivo).
4. **Dale contexto**: `@workspace` (codebase entero), `@file` (archivo concreto), `#terminal` (output anterior).
5. **Modelos**: en Pro+, click en selector de modelo → elige "Claude Sonnet 4" para reasoning, "GPT-5" para velocidad.

---

## Conclusión: ¿merezco la pena Agent Mode?

**Sí, si ya estás en el ecosistema GitHub/VS Code**. Agent Mode está **incluido en Pro ($10/mes, gratis con Student Pack)**. No hay coste extra para probarlo. Para tareas de "scaffolding + tests + fix", ahorra horas.

**No, si buscas la mejor calidad de código autónomo hoy**. **Cursor ($20) y Claude Code ($20)** entregan resultados superiores en tasks complejas, razonamiento multi-paso, y control de contexto. La diferencia se nota en proyectos >50 archivos, refactors arquitecturales, y debugging profundo.

**Mi setup actual**: Copilot Pro (gratis Student) para día a día en VS Code (autocompletado, Chat, Edit, Agent básico). **Claude Code ($20 Pro)** para tareas gordas: migraciones, arquitectura, debugging de 3 horas. **Cursor** lo tengo instalado pero apenas lo uso — me cuesta cambiar de IDE.

Si tienes Student Pack, **activa Copilot Pro y prueba Agent Mode esta tarde**. Cuesta $0 y en 30 min sabes si te cambia el flujo. Si no tienes Student Pack, $10/mes es bajo riesgo.

¿Lo has probado? Comparte en comentarios tu caso de uso más loco con Agent Mode.