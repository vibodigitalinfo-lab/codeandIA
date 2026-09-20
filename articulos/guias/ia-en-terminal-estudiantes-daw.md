---
layout: article
title: "IA en la terminal para estudiantes: Claude Code, Copilot CLI y Ollama"
description: "Guía para integrar IA en tu terminal: instalar y configurar Claude Code, GitHub Copilot CLI y modelos locales con Ollama. Casos reales de prácticas DAW."
category: "Guía"
date: 2026-08-24
readtime: 7
---

El año pasado mi terminal era solo `cd`, `ls`, `git add .` y `npm run dev`. Este curso, la IA se ha colado en la línea de comandos y **ha cambiado cómo hago las prácticas de DAW**: desde generar un `Dockerfile` multi-stage hasta depurar un `NullPointerException` en Spring Boot sin abrir el navegador. Te cuento cómo lo tengo montado yo, qué uso cada herramienta y los errores que cometí al principio.

---

## Por qué IA en terminal (y no solo en el editor)

En el editor (VS Code, IntelliJ) la IA está a un `Tab` o `Cmd+I`. Pero en la terminal pasas tiempo **entre comandos**: buscando en `history`, armando `find`/`grep` complejos, leyendo logs, editando `docker-compose.yml` a mano. Ahí la IA del editor no llega.

Las tres que uso yo:

| Herramienta | Qué hace | Coste | Mejor para |
|---|---|---|---|
| **Claude Code** | Agente autónomo en CLI, lee repo entero, ejecuta comandos | $20/mes (Pro) o $100/mes (Max) | Refactors grandes, migraciones, debugging profundo |
| **GitHub Copilot CLI** | `gh copilot suggest/explain` — comandos y explicaciones | Incluido en Copilot Individual ($10/mes) | "¿Cómo hago X en bash?", explicar errores de build |
| **Ollama + shell** | Modelos locales (qwen2.5-coder, codellama) vía CLI | Gratis (tu hardware) | Privacidad total, offline, sin límites de cuota |

No necesitas las tres. Empieza por **una** según tu caso.

---

## Paso 1: GitHub Copilot CLI (la más fácil, ya la tienes si eres estudiante)

Si tienes **GitHub Copilot gratis de estudiante** (ver [mi review](/articulos/reviews/github-copilot-gratis-estudiantes/)), el CLI viene incluido.

```bash
# 1. Instala GitHub CLI si no la tienes
brew install gh          # macOS
winget install GitHub.cli  # Windows
sudo apt install gh      # Linux

# 2. Autentica
gh auth login

# 3. Activa la extensión Copilot
gh extension install github/gh-copilot
```

**Úsalo así en tu día a día:**

```bash
# "¿Cómo hago un find que busque archivos .java modificados hoy?"
gh copilot suggest "buscar archivos java modificados hoy"

# "Explícame este error de Maven"
gh copilot explain "Could not find artifact com.example:lib:1.0.0"

# "Dame un comando para limpiar contenedores Docker parados hace >24h"
gh copilot suggest "limpiar contenedores docker parados hace mas de 24 horas"
```

**Mi truco:** pongo un alias en `.zshrc` / `.bashrc`:
```bash
alias ??='gh copilot suggest'
alias ???='gh copilot explain'
```
Ahora `?? "backup bd postgresql"` me da el comando al instante.

---

## Paso 2: Claude Code (para cuando la tarea "pesa")

Claude Code es distinto: **es un agente que vive en tu terminal**, lee todo tu repo, y **ejecuta comandos por ti** (pregunta antes de los peligrosos). Lo uso para tareas que en el editor serían tediosas:

- "Migra este servicio de Spring Boot 2 a 3.2"
- "Añade tests de integración con Testcontainers para todo el módulo `user`"
- "Configura CI/CD en GitHub Actions para build, test, y deploy a Railway"

**Instalación (macOS/Linux/Windows via winget):**
```bash
# macOS
brew install claude-code

# Windows
winget install Anthropic.ClaudeCode

# O universal (curl)
curl -fsSL https://claude.ai/install.sh | sh
```

**Autenticación:**
```bash
claude auth login
# Te abre el navegador, inicias sesión con tu cuenta Anthropic (Pro/Max/Team)
```

**Primer uso real en prácticas DAW:**
```bash
cd mi-proyecto-spring-boot
claude
> Añade tests de integración con Testcontainers para UserRepository.
> Usa JUnit 5, @SpringBootTest, y base de datos PostgreSQL real.
```
Claude Code:
1. Escanea el repo (`@codebase` implícito)
2. Te muestra el plan: "Voy a crear `UserRepositoryIntegrationTest.java`, añadir dependencia Testcontainers al `build.gradle`, configurar `@Container PostgreSQLContainer`..."
3. Pregunta: "¿Ejecutar `./gradlew test` para verificarlos?" → `yes`
4. Si fallan, itera solo.

**Ojo:** gasta **tokens de tu plan Anthropic**. Un refactor gordo = $5-15. Yo uso el plan **Max 5x ($100/mes)** y me da para ~20 tareas gordas al mes. Si no quieres sorpresas, pon `export CLAUDE_CODE_MAX_COST=10` (para límite de $10/sesión).

---

## Paso 3: Ollama + modelos locales (privacidad total, gratis)

Si tu código **no puede salir de tu máquina** (prácticas con datos reales, NDA, o simplemente no quieres depender de la nube), Ollama es la respuesta.

```bash
# Instalar
brew install ollama        # macOS
winget install Ollama.Ollama  # Windows
curl -fsSL https://ollama.com/install.sh | sh  # Linux

# Arrancar servidor (background)
ollama serve &

# Bajar modelos de código (septiembre 2026)
ollama pull qwen2.5-coder:7b      # 4.7 GB — el mejor equilibrio calidad/velocidad
ollama pull codellama:13b         # 7.3 GB — fuerte en Python/Java
ollama pull llama3.2:3b           # 2.0 GB — rápido para explicaciones
```

**Úsalo desde terminal:**
```bash
# Chat interactivo
ollama run qwen2.5-coder:7b

# One-shot (pipe)
cat src/main/java/com/example/UserService.java | ollama run qwen2.5-coder:7b "Explica este código y sugiere 2 mejoras"

# Con contexto de varios archivos
ollama run qwen2.5-coder:7b "$(cat src/main/java/com/example/*.java) - Genera tests JUnit 5 para todos los servicios"
```

**Mi setup real para DAW (offline total):**
```bash
# En .zshrc - alias rápidos
alias ai='ollama run qwen2.5-coder:7b'
alias aiexplain='ollama run llama3.2:3b "Explica simple: "'
```

Uso `ai` para generar código/tests, `aiexplain` para entender errores de compilación raros. **Cero coste, cero red, cero límites.**

---

## Mi flujo real combinado (lo que hago cada día)

| Situación | Herramienta | Comando real |
|---|---|---|
| "¿Cómo hago X en bash/git/docker?" | Copilot CLI | `?? "backup postgresql a s3"` |
| Error de build raro (Maven/Gradle/npm) | Copilot CLI | `??? "error: could not find symbol UserDTO"` |
| Refactor gordo / migración / tests masivos | Claude Code | `claude` → "Añade tests integración para todo el módulo auth" |
| Código sensible / sin red / privacidad | Ollama local | `ai "Genera Dockerfile multi-stage para Spring Boot 3.3"` |
| Explicar concepto / debug rápido | Ollama local | `aiexplain "NullPointerException en UserService line 42"` |

---

## Errores que cometí (para que no los repitas)

1. **Intentar usar Claude Code para todo** → gasta tokens tontos. Úsalo solo para tareas que valgan >$2 de tu tiempo.
2. **No dar contexto a Copilot CLI** → `gh copilot suggest` sin más da respuestas genéricas. Añade contexto: `gh copilot suggest "en un proyecto Spring Boot con Gradle Kotlin DSL, cómo configuro Testcontainers"`.
3. **Ollama con modelo demasiado grande** → `codellama:34b` en 16 GB RAM = swap constante, 30 seg/respuesta. Quédate en **7b-13b** para portátil de estudiante.
4. **Olvidar `ollama serve`** → el comando peta con "connection refused". Pon `ollama serve &` en tu `.zshrc` o usa `brew services start ollama`.

---

## Lo que haría diferente si volviera a empezar

- **Empezaría solo con Copilot CLI** (gratis para estudiantes) y le sacaría jugo 2-3 semanas.
- **Después añadiría Ollama local** para privacidad y tareas offline.
- **Solo pagaría Claude Code** cuando de verdad necesite un agente autónomo que edite 20 archivos y ejecute tests solo.

La IA en terminal **no sustituye saber bash/git/docker**. Te quita la fricción de "cómo se hacía este comando" y te deja enfocar en la lógica. Sigue aprendiendo los comandos base; la IA es el copiloto, no el piloto.

---

La terminal ya no es el rincón al que bajas a sufrir: es donde pasas de pedir a hacer. Si todavía no le has pedido a una IA que te genere un alias para algo que repites cada semana, ese es tu proyecto de diez minutos.
