---
layout: article
title: "Claude Code CLI: la terminal manda, agentes en paralelo y su precio"
description: "Review honesta de Claude Code: qué lo hace distinto, los sub-agentes en paralelo, MCP nativo, hooks, el precio por tokens y si compensa."
category: "Review"
date: 2026-06-28
updated: 2026-09-30
readtime: 14
version: "Claude Code CLI con Opus 4.7 (plan Pro, 20 $/mes). Probado en junio de 2026; desde entonces hay versiones más nuevas, así que lo que sigue describe esa versión concreta"
tiempo: "una sesión intensiva de 22 minutos sobre ~80 archivos"
proyecto: "migración Spring Boot 2.7→3.3 y Java 17→21 en las prácticas"
limites: "el coste va por tokens y sube sin aviso; los límites de uso de los planes los cambia Anthropic cuando quiere"
affiliate_text: "Prueba Claude Pro y accede a Claude Code desde la terminal"
affiliate_url: "https://claude.com/pricing"
affiliate_label: "Ver planes Claude"
last_modified_at: 2026-09-30
---

La primera vez que vi a alguien con experiencia usando Claude Code en directo, pensé: "esto es trampa". Escribió en la terminal: `claude "refactoriza todo el módulo de pagos a arquitectura hexagonal, añade tests y actualiza la documentación"`. **Y lo hizo**. En 20 minutos. Lo que a mí me habría llevado dos días.

Claude Code no es un autocompletado, no es un chat en el IDE, **es un agente autónomo que vive en tu terminal**. Lee tu repo entero, edita varios archivos, ejecuta comandos, corre los tests e itera hasta que todo pasa. Y lo que más llama la atención: puede lanzar **decenas de sub-agentes en paralelo** para verificar su propio trabajo.

Te cuento qué es, cómo se diferencia de Cursor y Copilot, qué cuesta realmente (ojo: tokens), y si tiene sentido para un estudiante de DAW.

## Qué es Claude Code y en qué se diferencia

| | **Claude Code** | **Cursor** | **Copilot** |
|---|-----------------|------------|-------------|
| **UI principal** | **Terminal (CLI)** | IDE (fork VS Code) | Extensiones IDE |
| **Modelo** | Solo Claude | Multi-modelo | Multi-modelo |
| **Contexto** | **Lee repo entero a demanda** | Índice propio (potente) | Índice semántico VS Code |
| **MCP** | Nativo, de serie | Cliente MCP | Cliente MCP (`.vscode/mcp.json`) |
| **Dynamic Workflows** | Sí, script de orquestación con sub-agentes en paralelo | Sub-agentes (`/multitask`) | `'/fleet'` en la CLI |
| **Hooks** | Sí, deterministas (pre-tool, post-tool) | No | No |
| **Agent SDK** | Sí, construyes tus propios agentes | No | No |
| **Git/PRs** | Nativo (`git`, `gh`) | Sí | Sí |
| **Computer Use** | Sí, abre apps y navegador | No | No |

**La diferencia filosófica**: Cursor y Copilot son **"IA dentro del editor"**. Claude Code es **"IA que usa el editor (y la terminal, y el navegador, y lo que haga falta) como herramientas"**.

---

## Lo más diferencial: sub-agentes en paralelo
Claude escribe **andamiajes en JavaScript** (*harnesses*) que lanzan sub-agentes en paralelo. Ejemplos:
- **Verificación adversarial**: un agente escribe código y **otros cinco intentan romperlo** (casos límite, seguridad, rendimiento, corrección). Solo pasa si todos fallan.
- **Torneo**: tres agentes proponen soluciones distintas al mismo problema y un juez elige la mejor.
- **Revisión en abanico**: 50 agentes revisan 50 archivos en paralelo para buscar fallos.

Esto no es "ingeniería de prompts". Es **orquestación programática de agentes**: escribes el andamiaje una vez y lo reutilizas.

> **Aviso sobre la versión (actualizado el 30/09/2026).** La Dynamic Workflows que describo aquí es real y sigue vigente, pero mi prueba es de **junio de 2026 con Opus 4.7**. Desde entonces Anthropic ha sacado versiones nuevas y ha cambiado algún detalle de cómo se lanza (la palabra activadora y el comando de esfuerzo cambiaron de nombre). Lo que no cambia es el patrón: el script decide el reparto de los subagentes, no el modelo turno a turno.

### Tareas programadas (Routines)
Trabajos que se lanzan solos o desde una API: "cada noche a las 3, revisa dependencias obsoletas y abre PRs". Corre en la nube de Anthropic, no en tu máquina.

### Computer Use
Claude Code **abre el navegador, navega a la documentación de una API, lee la especificación, vuelve a la terminal y escribe el cliente**. O abre Postman, prueba un endpoint y genera el código.

### Agent View
Gestión de varias sesiones a la vez: ves cuáles están activas, su estado, el coste en tokens y saltas entre ellas.

### CLAUDE.md y memoria automática
- **CLAUDE.md** en la raíz del repo = instrucciones que se aplican a TODAS las sesiones (estilo del proyecto, convenciones, comandos útiles).
- **Memoria automática**: aprende de tus correcciones entre sesiones ("la próxima vez usa `MapStruct`, no mapeo manual") y lo aplica solo.

---

## Precio: el elefante en la habitación

Claude Code **no tiene precio fijo mensual por uso ilimitado**. Vas por dos vías: la **API pay-as-you-go** (consola de Anthropic, se paga lo que consumas) o los **planes Pro/Max/Team**, que incluyen una cantidad de uso de Claude Code incluida.

**Aviso de fecha:** la tabla de abajo es la que Anthropic tenía publicada cuando escribí esto (junio de 2026). Este es el sector donde antes caducan los precios, así que **contrata siempre desde la [página oficial de precios](https://claude.com/pricing)** y no desde una tabla mía.

**Ojo con la moneda:** Anthropic factura en dólares (USD). Las cifras de abajo son las oficiales de su web; al pagar desde España se aplica el cambio del día y los impuestos, así que el cargo en euros sale algo distinto.

### Planes de suscripción (incluyen acceso a Claude Code)

| Plan | Mensual | Anual | Acceso a Claude Code | Para quién |
|------|---------|-------|----------------------|------------|
| **Free** | $0 | — | **No incluido** | Solo chat web |
| **Pro** | $20 | $17/mes ($200) | Sí, uso moderado | Uso diario ligero-medio |
| **Max 5x** | $100 | — | Sí, para codebases grandes | Uso intenso |
| **Max 20x** | $200 | — | Sí, uso intensivo | Uso muy intenso |
| **Team Standard** | $25/asiento | $20/asiento | Sí, 2-150 asientos | Equipos |
| **Team Premium** | $125/asiento | $100/asiento | Sí, 5× Pro | Equipos intensivos |
| **Enterprise** | $20/asiento+API | Anual | Sí, a precio API | Empresa |

### API Pay-as-you-go (consola) — si te pasas del plan

El precio por token cambia cada pocos meses y hay más modelos cada temporada, así que **no copio aquí la tabla**: se queda obsoleta y te haría pagar sobre datos míos. Los precios vigentes están en la [página oficial de precios de Anthropic](https://platform.claude.com/docs/pricing), desglosados por modelo en **dólares por millón de tokens de entrada y de salida**.

Lo que sí puedo decirte es la forma que tiene, porque es la que hace que el coste sea cambiante:

- **La entrada y la salida no cuestan lo mismo.** Los tokens de salida son bastante más caros que los de entrada, así que una respuesta larga y razonada cuesta bastante más que un prompt corto.
- **El modelo que elijas marca el precio.** No es lo mismo una sesión con el modelo más potente que con uno pequeño, y el coste se multiplica.
- **Los sub-agentes se multiplican.** Lanzas decenas de agentes en paralelo y cada uno lee parte del repo y responde: la factura también. Es la razón principal por la que el gasto mensual se dispara sin que se note en pantalla.

**Estimación de coste**: una sesión de agente de 30 min en un repo mediano (unos 50 archivos, con tests y build) se mueve en el orden de **1 a 5 dólares**; un día con 4 o 5 sesiones, del orden de **10 a 25**. **Esto es un orden de magnitud, no una factura**: te lo doy para que te hagas una idea de si el plan te compensa, no para que calcules lo que vas a pagar. La cifra real sale de la consola, que lleva el desglose token a token.

**Para estudiante**: **el plan Pro** es la entrada. Incluye una cantidad moderada de uso de Claude Code. Si te pasas, pagas a precio de API. **No hay descuento para estudiantes**. ¿Merece la pena? Solo si lo vas a usar **a diario para tareas complejas** (migraciones, arquitectura, debugging profundo). Para autocompletado y chat, [Copilot](/articulos/reviews/github-copilot-gratis-estudiantes/) con el Student Pack o el plan gratuito de Cursor salen mucho más a cuenta.

---

## Mi experiencia real: migración real en prácticas

**Proyecto**: un monolito de Spring Boot 2.7 a 3.3, con Java 17 a 21, JUnit 4 a 5, Micrometer, OpenTelemetry y manifiestos de Kubernetes. Unos 80 archivos.

**Instrucción**: `claude "migra este proyecto a Spring Boot 3.3 y Java 21. Actualiza todas las dependencias, corrige lo que rompa, actualiza los tests y genera los manifiestos de Kubernetes listos para ArgoCD"`.

**Qué pasó**:
1. **Leyó todo el repo** (pom.xml, más de 40 clases Java, 30 tests, Dockerfile, docker-compose, GitHub Actions). 2 min.
2. **Planificó** 12 pasos (los muestra en la terminal con casillas).
3. **Executó en bucle**: editó pom.xml → `./mvnw compile` → corrigió errores → editó código → `./mvnw test` → corrigió tests → generó los manifiestos de K8s → `kubectl apply --dry-run`.
4. **Duración total**: 22 minutos.
5. **Resultado**: compilación correcta, los 247 tests en verde y manifiestos validados. Tuve que ajustar a mano dos configuraciones de OpenTelemetry.

**Lo que NO hizo bien**:
- En un test de integración complejo, simuló mal un `WebClient` y tardó cuatro intentos en arreglarlo.
- Generó un `application.yml` con propiedades que Spring Boot 3.1 ya había marcado como obsoletas (las quitó en la iteración siguiente).
- **No conoce tu lógica de negocio**. Si el algoritmo de cálculo de precios tiene un fallo de redondeo, no lo pilla salvo que se lo digas.

---

## Cómo lo valoro

**Aviso sobre la tabla siguiente:** es mi impresión de un estudiante que ha usado las tres en clase. **No he medido nada con tests automáticos ni con tiempos**, así que tómatela como criterio personal y no como una medición. Si lo que necesitas es un dato duro, aquí no lo tienes.

| Criterio | Claude Code | Cursor | Copilot Agent |
|---------|-------------|--------|---------------|
| **Calidad en código complejo** | La mejor de las tres para mí | Buena | Irregular |
| **Razonamiento multi-paso** | La mejor de las tres para mí | Buena | Irregular |
| **Control del contexto** | Lee todo el repo | Índice | Selección |
| **Velocidad** | Más lento: piensa antes de escribir | Rápido | El más rápido |
| **Coste predecible** | El peor: va por tokens | Plano, cuota fija | A créditos |
| **Integración en empresa** | Pobre | Pobre | La mejor |
| **Extensibilidad (MCP, hooks, SDK)** | La mejor | Pobre | Pobre |

**Mi valoración**: **Claude Code gana en tareas "senior" (arquitectura, migraciones, debugging profundo, refactors transversales). Cursor gana en el día a día (velocidad, UX, precio plano). Copilot gana en lo que no es código (licencias, SSO, ecosistema de GitHub).**

---

## Lo que critico

| Crítica | Mi lectura |
|---------|----------|
| **Coste impredecible / alto** | Real. El gasto va por tokens y sube sin que se note. Si te importa el techo, ponlo tú en la consola antes de empezar. |
| **Calidad inconsistente** | Real. A veces brillante, a veces se inventa librerías. Hay que supervisar. |
| **Cambios de condiciones** | Real. Anthropic mueve a menudo los límites de uso, los modelos disponibles y las condiciones de los planes. Antes de pagar, mira su página de precios. |
| **Solo Claude** | Real. No puedes usar GPT-5, Grok ni Gemini. Si Claude falla con tu stack, no hay plan B. |
| **Curva de aprendizaje** | Real. Hay que pensar en "agentes y flujos de trabajo", no en "prompts". |

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
- Valoras **MCP nativo, los sub-agentes en paralelo, los hooks y el Agent SDK** para automatizar tu flujo.
- Aceptas un coste variable por tokens y sabes vigilarlo.
- Vives en la terminal y odias cambiar de ventana.

**No, si**:
- Eres estudiante o junior y buscas **autocompletado y chat baratos**. [Copilot Pro](/articulos/reviews/github-copilot-gratis-estudiantes/) (gratis con el Student Pack) o el plan gratuito de Cursor te dan casi todo el valor por una fracción del coste.
- Necesitas **precio plano mensual** sin sorpresas.
- Tu stack principal no encaja bien con Claude (ej. mucho C++ legacy, embedded, lenguajes niche donde GPT-5/Grok rinden mejor).
- Te importa la privacidad y prefieres una herramienta donde el código no salga de tu máquina. Ojo: eso descarta Claude Code, porque es un servicio en la nube y no se puede ejecutar en local. Para eso está [Ollama](/articulos/reviews/ollama-modelos-ia-local-review-2026/).

**Mi setup actual**: **Copilot Pro** (gratis con el Student Pack) para el día a día en VS Code. **Claude Code Pro** para las dos o tres tareas gordas de la semana, donde la autonomía real me ahorra horas. **Cursor** instalado, pero en desuso.

Si tienes $20 al mes y curiosidad, **prueba Claude Code una semana**. Si no te cambia el flujo, cancelas. Si te lo cambia, ya sabes lo que cuesta.

Al final, Claude Code me convence por lo que casi nadie destaca: trabaja en silencio, sin ventanas ni rostro. Y eso, para concentrarse, vale su peso en oro.

## Sigue por aquí

- [Warp terminal: IA en la línea de comandos, ¿cambiar de iTerm/WSL?](/articulos/reviews/warp-terminal-ai-review-2026/)
- [IA en la terminal para estudiantes: Claude Code, Copilot CLI y Ollama](/articulos/guias/ia-en-terminal-estudiantes-daw/)
- [Cursor vs Claude Code en 2026: ¿IDE con agente o agente en terminal?](/articulos/comparativas/cursor-vs-claude-code-2026/)
