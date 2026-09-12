---
layout: article
title: "Claude Code CLI 2026: terminal-first, agentes paralelos y el precio de la autonomía"
description: "Review honesta de Claude Code: qué hace distinto a Cursor/Copilot, Dynamic Workflows, MCP nativo, hooks, pricing por tokens, y si merece la pena para un estudiante."
category: "Review"
date: 2026-09-05
readtime: 8
affiliate_text: "Prueba Claude Pro y accede a Claude Code desde la terminal"
affiliate_url: "https://claude.com/pricing"
affiliate_label: "Ver planes Claude"
---

La primera vez que vi a un senior usar Claude Code en directo, pensé: "esto es trampa". Escribió en la terminal: `claude "refactoriza todo el módulo de pagos a arquitectura hexagonal, añade tests, y actualiza la doc"`. **Y lo hizo**. En 20 minutos. Lo que a mí me habría llevado dos días.

Claude Code no es un autocompletado, no es un chat en el IDE, **es un agente autónomo que vive en tu terminal**. Lee tu repo entero, edita múltiples archivos, ejecuta comandos, corre tests, y itera hasta que todo pasa. Y lo que es más loco: puede lanzar **decenas de sub-agentes en paralelo** para verificar su propio trabajo (Dynamic Workflows).

Te cuento qué es, cómo se diferencia de Cursor y Copilot, qué cuesta realmente (ojo: tokens), y si tiene sentido para un estudiante de DAW.

## Qué es Claude Code y en qué se diferencia

| | **Claude Code** | **Cursor** | **Copilot** |
|---|-----------------|------------|-------------|
| **UI principal** | **Terminal (CLI)** | IDE (fork VS Code) | Extensiones IDE |
| **Modelo** | Solo Claude (Opus/Sonnet/Haiku/Fable) | Multi-modelo (Grok, Composer, Sonnet, etc.) | Multi-modelo |
| **Contexto** | **Lee repo entero a demanda** | Índice propio (potente) | Índice semántico VS Code |
| **MCP** | ✅ **Nativo, first-class** | ⚠️ Limitado | ❌ |
| **Dynamic Workflows** | ✅ **10-100s sub-agentes paralelos** | ❌ | ❌ |
| **Hooks** | ✅ Deterministas (pre-tool, post-tool, etc.) | ❌ | ❌ |
| **Agent SDK** | ✅ Construye tus propios agentes | ❌ | ❌ |
| **Git/PRs** | ✅ Nativo (`git`, `gh`) | ✅ | ✅ |
| **Computer Use** | ✅ Abre apps, navega, ejecuta herramientas | ❌ | ❌ |

**La diferencia filosófica**: Cursor y Copilot son **"IA dentro del editor"**. Claude Code es **"IA que usa el editor (y la terminal, y el navegador, y lo que haga falta) como herramientas"**.

---

## Características únicas 2026

### Dynamic Workflows (mayo 2026) — lo más diferencial
Claude escribe **harnesses en JavaScript** que lanzan sub-agentes en paralelo. Ejemplos reales:
- **Adversarial verification**: un agente escribe código, **otros 5 intentan romperlo** (fuzzing, edge cases, security, performance, correctness). Solo pasa si todos fallan.
- **Tournament**: 3 agentes proponen soluciones distintas al mismo problema → un juez elige la mejor.
- **Fan-out verification**: 50 agentes revisan 50 archivos en paralelo para encontrar bugs.

Esto no es "prompt engineering". Es **orquestación programática de agentes**. Tú escribes el harness una vez, lo reusas siempre.

### Routines (abril 2026)
Tareas programadas o disparadas por API: "cada noche a las 3am, revisa dependencias obsoletas y abre PRs". Corre en la nube de Anthropic, no en tu máquina.

### Computer Use (marzo 2026)
Claude Code **abre el navegador, navega a la doc de una API, lee la especificación, vuelve a la terminal y escribe el cliente**. O abre Postman, prueba un endpoint, y genera el código. Es "Computer Use" de Anthropic expuesto en CLI.

### Agent View (mayo 2026)
Gestión multi-sesión: ves todas tus sesiones activas, su estado, coste en tokens, y puedes saltar entre ellas.

### CLAUDE.md + Auto-memory
- **CLAUDE.md** en la raíz del repo = instrucciones persistentes para TODAS las sesiones (estilo proyecto, convenciones, comandos útiles).
- **Auto-memory**: aprende de tus correcciones entre sesiones ("la próxima vez usa `MapStruct` no mapping manual") y lo aplica solo.

---

## Pricing real (septiembre 2026) — el elefante en la habitación

Claude Code **no tiene precio fijo mensual por uso ilimitado**. Usa **API pay-as-you-go** (consola Anthropic) o planes Pro/Max/Team que incluyen "uso moderado/alto" de Claude Code.

### Planes de suscripción (incluyen acceso a Claude Code)

| Plan | Mensual | Anual | Acceso Claude Code | Para quién |
|------|---------|-------|-------------------|------------|
| **Free** | $0 | — | ❌ **No incluido** | Chat web solo |
| **Pro** | $20 | $17/mes ($200) | ✅ Uso moderado | Uso diario ligero-medio |
| **Max 5x** | $100 | — | ✅ Uso diario codebases grandes | Power users |
| **Max 20x** | $200 | — | ✅ Intensivo | Heavy users |
| **Team Standard** | $25/seat | $20/seat | ✅ 2-150 seats | Equipos |
| **Team Premium** | $125/seat | $100/seat | ✅ 5× Pro | Equipos intensivos |
| **Enterprise** | $20/seat+API | Anual | ✅ API rates | Enterprise |

### API Pay-as-you-go (consola) — si te pasas del plan

| Modelo | Input $/MTok | Output $/MTok |
|--------|--------------|---------------|
| **Opus 5** | $5 | $25 |
| **Sonnet 5** | $2 | $10 |
| **Haiku 4.5** | $1 | $5 |
| **Fable 5.1** | $10 | $50 |

**Estimación real de coste**: una sesión Agent de 30 min en repo mediano (~50 archivos, tests, builds) gasta **$1-5 en Opus/Sonnet**. Un día intenso (4-5 sesiones) = **$10-25**. Un mes = **$200-500** si lo usas a diario para tareas gordas.

**Para estudiante**: **Pro ($20/mes o $200/año)** es la entrada. Incluye "uso moderado" de Claude Code. Si te pasas, pagas API rates. **No hay descuento estudiante**. ¿Merece la pena? Solo si vas a usarlo **diariamente para tareas complejas** (migraciones, arquitectura, debugging profundo). Para autocompletado y chat, Copilot Pro ($10, gratis Student) o Cursor Hobby (gratis) salen más a cuenta.

---

## Mi experiencia real: migración real en prácticas

**Proyecto**: monolito Spring Boot 2.7 → 3.3 + Java 17 → 21 + JUnit 4 → 5 + Micrometer + OpenTelemetry + Kubernetes manifests. ~80 archivos.

**Prompt**: `claude "migra este proyecto a Spring Boot 3.3 y Java 21. Actualiza todas las dependencias, fixa breaking changes, actualiza tests, y genera Kubernetes manifests listos para ArgoCD"`.

**Qué pasó**:
1. **Leyó todo el repo** (pom.xml, 40+ clases Java, 30+ tests, Dockerfile, docker-compose, GitHub Actions). 2 min.
2. **Planificó** 12 pasos (output en terminal con checkboxes).
3. **Ejecutó en bucle**: editó pom.xml → `./mvnw compile` → fix errors → editó código → `./mvnw test` → fix tests → generó K8s manifests → `kubectl apply --dry-run`.
4. **Duración total**: 22 minutos. **Coste**: ~$3.50 (Opus 4.7 en ese momento).
5. **Resultado**: build passed, tests passed (247/247), manifests validados. Tuve que ajustar 2 configs de OpenTelemetry a mano.

**Lo que NO hizo bien**:
- En un test de integración complejo, mockó mal un `WebClient` y tardó 4 iteraciones en arreglarlo.
- Generó un `application.yml` con propiedades deprecated de Spring Boot 3.1 (las quitó en siguiente iteración).
- **No sabe tu lógica de negocio**. Si el algoritmo de pricing tiene un bug de redondeo, no lo pilla salvo que se lo digas.

---

## Claude Code vs Cursor vs Copilot: benchmarks comunidad 2026 H1

| Métrica | Claude Code | Cursor | Copilot Agent |
|---------|-------------|--------|---------------|
| **Calidad código complejo** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Reasoning multi-paso** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Control contexto** | ⭐⭐⭐⭐⭐ (lee todo) | ⭐⭐⭐⭐ (índice) | ⭐⭐⭐ (selección) |
| **Velocidad** | ⭐⭐⭐ (más lento, piensa más) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Coste predecible** | ⭐ (tokens) | ⭐⭐⭐⭐ (flat) | ⭐⭐⭐ (créditos) |
| **Integración enterprise** | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Extensibilidad (MCP, hooks, SDK)** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐ |

**Consenso Reddit/HN 2026**: **Claude Code gana en tareas "senior" (arquitectura, migraciones, debugging profundo, refactors transversales). Cursor gana en día a día (velocidad, UX, precio plano). Copilot gana en enterprise (SSO, IP indemnity, Knowledge Bases, ecosistema GitHub).**

---

## Lo que la comunidad critica (y yo confirmo)

| Crítica | Realidad |
|---------|----------|
| **Coste impredecible / alto** | ✅ Real. Un mes intenso = $200-500. No hay hard cap en Pro/Max. |
| **Calidad inconsistente** | ✅ A veces brillante, a veces alucina librerías. Requiere supervisión. |
| **Trust erosion** | ✅ Casos documentados: steganographic tracking en outputs, source map leaks, bloqueo a terceros (claude-code-router). Forced auto-updates. |
| **Solo Claude** | ✅ No puedes usar GPT-5, Grok, Gemini. Si Claude falla en tu stack, no hay fallback. |
| **Curva de aprendizaje** | ✅ Requiere pensar en "agentes y workflows", no en "prompts". |

---

## Setup mínimo para empezar hoy (5 min)

```bash
# 1. Instala (macOS/Linux/Windows via winget)
brew install claude-code  # o: curl -fsSL https://claude.ai/install.sh | sh

# 2. Autentica (necesitas cuenta Pro/Max/Team)
claude auth login

# 3. En tu repo, crea CLAUDE.md con tus convenciones
cat > CLAUDE.md << 'EOF'
# Instrucciones para Claude Code
- Stack: Java 21, Spring Boot 3.3, Gradle Kotlin DSL
- Testing: JUnit 5 + Mockito + AssertJ + Testcontainers
- Arquitectura: Hexagonal (domain, application, infrastructure)
- Commits: Conventional Commits
- Comandos útiles:
  - Build: ./mvnw compile
  - Tests: ./mvnw test
  - Lint: ./mvnw checkstyle:check
EOF

# 4. Lanza tu primera tarea
claude "añade health check endpoint en /actuator/health con detalles de BD y Kafka"
```

---

## Conclusión: ¿Claude Code o no?

**Sí, si**:
- Eres senior / lead / arquitecto y haces tareas complejas a diario (migraciones, refactors gordos, debugging de producción).
- Valoras **MCP nativo, Dynamic Workflows, hooks, Agent SDK** para automatizar tu flujo.
- Aceptas coste variable por tokens y sabes estimar/controlar uso.
- Vives en terminal y odias cambiar de ventana.

**No, si**:
- Eres estudiante / junior y buscas **autocompletado + chat barato**. Copilot Pro ($10, gratis Student) o Cursor Hobby (gratis) te dan 90% del valor por 10% del coste.
- Necesitas **precio plano mensual** sin sorpresas.
- Tu stack principal no encaja bien con Claude (ej. mucho C++ legacy, embedded, lenguajes niche donde GPT-5/Grok rinden mejor).
- Te importa **privacidad/confianza** y los episodios de tracking/leaks te echan para atrás.

**Mi setup actual**: **Copilot Pro (gratis Student)** para día a día en VS Code. **Claude Code Pro ($20/mes)** para las 2-3 tareas gordas por semana donde la autonomía real me ahorra horas. **Cursor** instalado pero en desuso.

Si tienes $20/mes y curiosidad, **prueba Claude Code una semana**. Si no te cambia el flujo, cancela. Si te lo cambia, ya sabes el coste real.

¿Lo has probado? Comparte en comentarios tu tarea más loca con Dynamic Workflows.