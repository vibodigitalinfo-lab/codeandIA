---
layout: article
title: "Zed: el editor en Rust con IA integrada, ¿alternativa a VS Code?"
description: "Review honesta de Zed: rendimiento en Rust, IA nativa (Anthropic + modelos locales), colaboración en tiempo real, y si merece la pena para un estudiante de DAW."
category: "Review"
date: 2026-07-11
readtime: 10
version: "Zed (Rust) con claves propias y modelos locales; en Windows ya hay build estable"
tiempo: "tres semanas de uso"
proyecto: "prácticas Spring Boot + React (un monolito de ~3k archivos) y un bug del frontend en pareja"
limites: "no trae terminal propia ni edita varios archivos él solo; el ecosistema de extensiones es pequeño"
affiliate_text: "Prueba Zed gratis y decide si te cambia el flujo de edición"
affiliate_url: "https://zed.dev"
affiliate_label: "Descargar Zed"
updated: 2026-10-02
last_modified_at: 2026-10-02
---

Llevo meses viendo a gente en Twitter (y en clase) que jura que **Zed les ha cambiado la vida**. "Es VS Code pero rápido", "la IA está integrada de forma nativa", "colaboración en tiempo real sin plugins". Suena bien, pero también suena a marketing. Me lo bajé hace tres semanas para un proyecto de prácticas (Spring Boot + React, el típico de DAW) y esto es lo que he encontrado.

---

## Qué es Zed y por qué no es "otro fork de VS Code"

Zed **no es Electron**. Está escrito en **Rust** y usa **GPUI**, su propio framework de UI que renderiza con la GPU (Metal en Mac, Vulkan/DX12 en Windows/Linux). Eso significa:

- Arranque en **< 500 ms** en frío (en mi portátil de 2021 con 16 GB RAM).
- Scroll a 120 fps sin pestañear, incluso en archivos de 10k líneas.
- Memoria base ~150 MB (VS Code con extensiones fáciles se pone en 600-800 MB).

La IA **viene de serie**, pero aquí hay que separar el editor de los modelos: el plan Personal de Zed ya no trae los modelos alojados de Zed. Te logueas con tu cuenta de GitHub y tienes 2.000 predicciones de edición aceptadas. Para hablar con un modelo te hace falta una de estas tres: tu propia clave (Anthropic, OpenAI, etc.), un agente externo como Claude Agent o Codex CLI, o el plan Pro de pago. También sigue soportando **modelos locales vía Ollama** (llama3.2, qwen2.5-coder, etc.), que es la vía gratis si no quieres que tu código salga de la máquina.

La **colaboración en tiempo real** (Zed Channels) es nativa: creas un canal, invitas a alguien con un link, y los dos editáis el mismo buffer a la vez. Sin Git, sin Live Share, sin configurar nada. Para prácticas en pareja o revisar código con un compañero, es **brutal**.

---

## Experiencia real: tres semanas en proyectos de clase

### 1. El rendimiento se nota (y mucho)

En clase trabajamos con un monolito Spring Boot de ~3k archivos Java + un frontend React. En VS Code, `Cmd+P` (quick open) a veces tarda 1-2 segundos en aparecer. En Zed, **instantáneo**. El índice semántico (para "ir a definición", "buscar referencias") se construye en segundo plano y no bloquea la UI.

Lo que más me flipó: **abrir el mismo proyecto en Zed y en VS Code a la vez**. Zed usa ~200 MB, VS Code ~700 MB. En batería, Zed me dura ~45 min más en mi portátil.

### 2. La IA: buena, pero con matices

El panel de chat (`Ctrl+>`) entiende el contexto del repo si le das acceso (arrastras la carpeta o usas `@workspace`). Le pedí:

- "Genera un test JUnit 5 para `UserService` con Mockito y AssertJ" → salió correcto a la primera, usando los patrones del proyecto.
- "Refactoriza este `UserController` para usar DTOs y validación con Jakarta Bean Validation" → hizo el 80% bien, tuve que ajustar imports y un `@Valid` que se le olvidó.
- "Explícame por qué esta query JPA hace N+1" → me dio la explicación y la solución (`@EntityGraph` / `JOIN FETCH`).

**Lo que NO hace (todavía):**
- No ejecuta comandos en terminal por ti (no hay "agent mode" tipo Cursor/Copilot Agent).
- No edita varios archivos en una sola pasada autónoma (tienes que aceptar cambio a cambio).
- El autocompletado inline (Zed Predictions) es **bueno para patrones repetitivos**, pero no razona como Copilot/Claude Code.

Para mí, que uso IA sobre todo para **explicar, generar tests y refactors puntuales**, me sobra. Si buscas "dime qué hacer y hazlo todo tú", Zed se queda corto.

### 3. Colaboración real: probada en prácticas

Mi compañero y yo teníamos que arreglar un bug en el frontend React (un useEffect que provocaba bucle infinito). Abrí un Channel, le mandé el link por Discord, y en **10 segundos** los dos estábamos editando el mismo `Dashboard.tsx`. Vimos el cursor del otro, los cambios aplicados al instante, y lo arreglamos en 5 min sin Git ni pushes. Para **programación en pareja remota**, es el mejor flujo que he probado.

---

## Lo que NO me gusta (y debes saber)

| Problema | Gravedad | Workaround |
|---|---|---|
| **Windows sin soporte de primera** (build estable desde octubre 2026) | Baja | Instala la estable; si el renderer te da guerra, WSL2 + Zed Linux |
| **Modelos alojados solo en el plan Pro** | Media | Plan Personal gratis con tus claves, Ollama local o un agente externo |
| **Ecosistema de extensiones minúsculo** | Media | Configuras todo en JSON/TOML; LSP nativo para Java, TS, Python, Rust, Go |
| **Sin marketplace de temas** | Baja | Temas base + importas `.tmTheme` / VS Code themes manualmente |
| **Curva de atajos distinta** | Media | Modo "Vim" nativo bueno; keymap VS Code importable |
| **IA gratuita con límites diarios** | Media | Trae tu propia API key (Anthropic/OpenAI) o usa Ollama local |

**El tema Windows** ha cambiado desde que escribí esto: a 2 de octubre de 2026 zed.dev ya ofrece **build estable para Windows** además de la de preview. Cuando probé la build de preview se caía el renderer de GPU de vez en cuando y tocaba lanzar `zed --disable-gpu`; la estable ya no lleva esa instrucción en el camino normal. Si vas a instalarlo en Windows, coge la estable, no la de preview.

### El precio (esto no lo cuentan en Twitter)

Zed es **gratis hoy** para el editor, y conviene entender qué significa "gratis" porque a octubre de 2026 ya no incluye la IA alojada. La tabla oficial, comprobada el 2 de octubre de 2026, tiene tres planes:

| Plan | Precio | Qué te da |
| --- | --- | --- |
| **Personal** | **0 € para siempre** | El editor entero y 2.000 predicciones de edición aceptadas. Sin modelos alojados de Zed: usas tus claves o un agente externo |
| **Pro** | **10 $/mes** | Modelos alojados de Zed, predicciones ilimitadas y 5 $ de tokens incluidos al mes; a partir de ahí se cobra el uso a tasa API |
| **Business** | **30 $/asiento/mes** | Lo de Pro más controles de organización para equipos |

Pro tiene una **prueba de 14 días sin tarjeta**, con 5 $ de saldo y un único modelo alojado disponible durante la prueba. Si agotas el saldo, te cobran al final del mes o cada 10 $ que gastes, lo que ocurra antes, y se puede poner tope de gasto.

**En mi caso: cero euros al mes**, porque uso claves propias y modelos locales. Pero si lo que quieres es el modelo alojado sin claves propias, la respuesta corta es que hoy cuesta 10 dólares al mes, no cero. Y nada de eso es solo para empresas: lo que queda para las empresas es la capa de administración del plan Business.

---

## Para estudiante DAW: ¿merece la pena?

**Sí, si:**
- Usas macOS, Linux o Windows y valoras **rendimiento real**.
- Quieres **IA sin plugins ni configuración**, y ya asumes que los modelos alojados cuestan 10 $/mes.
- Haces **programación en pareja** remota con frecuencia.
- Te gusta la idea de **configuración en archivos (JSON/TOML)** en vez de GUI infinita.

**No, si:**
- No quieres pagar los 10 $/mes del plan Pro y ya tienes claves de Anthropic u OpenAI que te sirven.
- Dependes de extensiones muy específicas de VS Code (ej. algún linter raro, plugin de framework legacy).
- Buscas **agent mode autónomo** que edite 10 archivos y ejecute tests solo.
- Tu flujo actual en VS Code + Copilot + extensiones te va perfecto y no quieres reaprender.

---

## Mi veredicto personal

Me quedo con **Zed como editor principal** para proyectos propios y prácticas donde controlo el stack. El salto de "esperar a que VS Code indexe" a "abro y trabajo" me ahorra fricción diaria. La IA nativa cubre mis casos de uso (explicar, testear, refactor puntual) y la colaboración nativa es un superpoder para trabajos en grupo.

Para el **proyecto final de curso** (donde el profe exige IntelliJ para Java y a veces Windows nativo), sigo usando IntelliJ + Copilot. No es religión: es usar la herramienta que menos fricción pone ese día.

En Windows ya hay build estable, así que la excusa técnica se cae: lo que me frena no es el sistema, que en prácticas ya no uso, sino que mi máquina de pruebas es Linux. Ahí sigo con IntelliJ + Copilot porque es lo que pide el día a día en clase.

## Sigue por aquí

- [Trae AI IDE 2026: el editor que quiere comerse a Cursor](/articulos/reviews/trae-ai-ide-review-2026/)
- [Warp terminal: IA en la línea de comandos, ¿cambiar de iTerm/WSL?](/articulos/reviews/warp-terminal-ai-review-2026/)
- [Cursor vs Claude Code en 2026: ¿IDE con agente o agente en terminal?](/articulos/comparativas/cursor-vs-claude-code-2026/)
