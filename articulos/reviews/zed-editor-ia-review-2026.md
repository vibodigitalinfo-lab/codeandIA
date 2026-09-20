---
layout: article
title: "Zed: el editor en Rust con IA integrada, ¿alternativa a VS Code?"
description: "Review honesta de Zed: rendimiento en Rust, IA nativa (Anthropic + modelos locales), colaboración en tiempo real, y si merece la pena para un estudiante de DAW."
category: "Review"
date: 2026-08-25
readtime: 7
affiliate_text: "Prueba Zed gratis y decide si te cambia el flujo de edición"
affiliate_url: "https://zed.dev"
affiliate_label: "Descargar Zed"
---

Llevo meses viendo a gente en Twitter (y en clase) que jura que **Zed les ha cambiado la vida**. "Es VS Code pero rápido", "la IA está integrada de forma nativa", "colaboración en tiempo real sin plugins". Suena bien, pero también suena a marketing. Me lo bajé hace tres semanas para un proyecto de prácticas (Spring Boot + React, el típico de DAW) y esto es lo que he encontrado.

---

## Qué es Zed y por qué no es "otro fork de VS Code"

Zed **no es Electron**. Está escrito en **Rust** y usa **GPUI**, su propio framework de UI que renderiza con la GPU (Metal en Mac, Vulkan/DX12 en Windows/Linux). Eso significa:

- Arranque en **< 500 ms** en frío (en mi portátil de 2021 con 16 GB RAM).
- Scroll a 120 fps sin pestañear, incluso en archivos de 10k líneas.
- Memoria base ~150 MB (VS Code con extensiones fáciles se pone en 600-800 MB).

La IA **no es un plugin**: viene de serie. Tienes un panel lateral (`Cmd/Ctrl + >`) donde hablas con **Claude 3.5 Sonnet** (por defecto, gratis con límites) o conectas tu propia clave de Anthropic/OpenAI. También soporta **modelos locales vía Ollama** (llama3.2, qwen2.5-coder, etc.) — clave si no quieres que tu código salga de la máquina.

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
| **Solo macOS y Linux nativo** (Windows en preview, agosto 2026) | Alta si usas Windows | WSL2 + Zed Linux (funciona bien, pero no nativo) |
| **Ecosistema de extensiones minúsculo** | Media | Configuras todo en JSON/TOML; LSP nativo para Java, TS, Python, Rust, Go |
| **Sin marketplace de temas** | Baja | Temas base + importas `.tmTheme` / VS Code themes manualmente |
| **Curva de atajos distinta** | Media | Modo "Vim" nativo bueno; keymap VS Code importable |
| **IA gratuita con límites diarios** | Media | Trae tu propia API key (Anthropic/OpenAI) o usa Ollama local |

**El tema Windows** es el elefante en la sala. A septiembre 2026, la build de Windows está en **preview pública** (descargable desde zed.dev). Funciona, pero a veces peta el GPU renderer y tienes que lanzar `zed --disable-gpu`. Si tu día a día es Windows nativo sin WSL, **espera a la 1.0 estable**.

### El precio (esto no lo cuentan en Twitter)

Zed es **gratis hoy**: te logueas con tu cuenta de GitHub y listo. No hay plan de pago para el editor individual a septiembre 2026 — monetizan con cosas para empresas (Zed Office) que aún no me interesan como estudiante. La IA trae un límite diario de peticiones con Claude; cuando lo gasto, conecto mi API key de Anthropic o uso **Ollama local** y sigo sin pagar. **En mi caso: cero euros al mes.**

---

## Para estudiante DAW: ¿merece la pena?

**Sí, si:**
- Usas macOS o Linux (o WSL2 en Windows) y valoras **rendimiento real**.
- Quieres **IA integrada sin configurar plugins, claves, MCP, nada**.
- Haces **programación en pareja** remota con frecuencia.
- Te gusta la idea de **configuración en archivos (JSON/TOML)** en vez de GUI infinita.

**No, si:**
- Necesitas **Windows nativo estable ya**.
- Dependes de extensiones muy específicas de VS Code (ej. algún linter raro, plugin de framework legacy).
- Buscas **agent mode autónomo** que edite 10 archivos y ejecute tests solo.
- Tu flujo actual en VS Code + Copilot + extensiones te va perfecto y no quieres reaprender.

---

## Mi veredicto personal

Me quedo con **Zed como editor principal** para proyectos propios y prácticas donde controlo el stack. El salto de "esperar a que VS Code indexe" a "abro y trabajo" me ahorra fricción diaria. La IA nativa cubre mis casos de uso (explicar, testear, refactor puntual) y la colaboración nativa es un superpoder para trabajos en grupo.

Para el **proyecto final de curso** (donde el profe exige IntelliJ para Java y a veces Windows nativo), sigo usando IntelliJ + Copilot. No es religión: es usar la herramienta que menos fricción pone ese día.

En Windows sigue siendo promesa, pero la dirección está clara. Lo probaré a fondo el día que su versión para Windows deje de llamarse preview; hasta entonces, VS Code e IntelliJ no corren peligro en mi máquina.
