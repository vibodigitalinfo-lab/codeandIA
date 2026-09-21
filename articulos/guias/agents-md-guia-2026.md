---
layout: article
title: "AGENTS.md: la guía de instrucciones para IA en tus proyectos (2026)"
description: "Guía de AGENTS.md, el estándar de instrucciones para IA en 2026: escribirlo, jerarquía por carpetas y compatibilidad con Cursor, Copilot, Codex y Claude Code."
category: "Guía"
date: 2026-09-12
readtime: 7
---

Me pasaba esto todas las semanas en prácticas: entraba Cursor, le pedía un cambio en mi `UserService.java`, y me devolvía código que no seguía ni el estilo de mis clases ni el patrón del proyecto. Separadores en inglés, `System.out.println` por todos lados, y refactorizaciones que no había pedido. Hasta que un compañero me enseñó una cosa que lo arregló en 30 minutos: **AGENTS.md**.

Lleva dos años acompañándome y hoy es, de largo, el fichero que más horas de correcciones me ha ahorrado. Te explico qué es, cómo escribirlo bien y por qué en 2026 deberías tenerlo en cada proyecto que toques, aunque seas estudiante de DAW.

## Qué es AGENTS.md en 30 segundos

**AGENTS.md es un fichero Markdown, en la raíz de tu repositorio, que le dice a las herramientas de IA cómo deben comportarse en TU proyecto concreto.**

Piensa en él como el manual de onboarding para un compañero nuevo: qué comandos construir y testear, qué formato de código usas, qué styleguide sigues y, sobre todo, qué NO debe hacer. La IA no lo lee siempre (depende de la herramienta y del contexto), pero cuando lo lee, tu trabajo mejora muchísimo.

No es un invento mío ni de una herramienta. Se estandarizó en agosto de 2025 de la mano de OpenAI, Google, Cursor y otros, y en diciembre de 2025 se donó a la **Linux Foundation (Agentic AI Foundation)**, la misma gobernanza que tiene MCP. Hoy lo usan más de 60.000 repositorios en GitHub.

## Qué le pones: las secciones que de verdad importan

No hay formato obligatorio. Un AGENTS.md mínimo y útil tiene esto:

```markdown
# Gestión De Cursos (prácticas DAW)

App Java 21 + Spring Boot 3 + Maven. BD MySQL local con docker compose up -d.

## Comandos
- Compilar: mvn -q compile
- Tests: mvn test
- Arrancar: mvn spring-boot:run

## Estilo
- Clases y métodos en español (código de prácticas).
- Un servicio por entidad, un repositorio por entidad (patrón del módulo).
- Logging con Logger, nunca System.out.println.

## No hacer
- No refactorices archivos que no tocan el cambio.
- No borres tests para que pasen: corrígelos.
- No abras un PR con mvn test en rojo.
```

Fíjate en la última sección, **"No hacer"**. Es la que más efecto tiene: los agentes de IA son demasiado serviciales, y poner límites explícitos es lo que evita los refactors de 400 líneas que nadie pidió.

## Jerarquía: funciona también en proyectos grandes

AGENTS.md soporta **ficheros anidados**. Tienes el de la raíz con las normas globales y puedes añadir más dentro de subcarpetas:

```
/repo/AGENTS.md              # normas comunes del repo
/repo/api/AGENTS.md          # reglas del backend (build, tests)
/repo/frontend/AGENTS.md     # reglas del front (format, linter)
```

La regla es simple: **el fichero más profundo gana sobre el más general**. Si trabajas con microservicios o en un proyecto con backend y frontend separados, esto te evita meter en la raíz matices que solo aplican a una parte.

## Quién lo lee de verdad (septiembre 2026)

Aquí está la parte que casi nadie cuenta bien:

| Herramienta | ¿Lee AGENTS.md? | Qué tienes que hacer |
|---|---|---|
| **Cursor** | ✅ Nativo | Nada |
| **OpenAI Codex CLI** | ✅ Nativo | Nada |
| **GitHub Copilot** | ✅ Nativo | Nada (desde 2025) |
| **Windsurf, Zed, Amp, Devon, Jules, Warp** | ✅ Nativo | Nada |
| **Claude Code** | ⚠️ No lo lee | Import o symlink (abajo) |
| **Gemini CLI** | ⚠️ No lo lee | Apunta a él en `.gemini/settings.json` |
| **Aider** | ⚙️ Configurable | `read: AGENTS.md` en `.aider.conf.yml` |

Para **Claude Code**, que es el que más uso, hay dos trucos:

1. **Import (recomendado, funciona también en Windows):** crea un `CLAUDE.md` que empiece con `@AGENTS.md` y añade debajo las reglas solo de Claude:

```markdown
@AGENTS.md
# Reglas extra solo para Claude Code
- Antes de editar, ejecuta mvn test.
```

2. **Symlink** si quieres el mínimo absoluto: `ln -s AGENTS.md CLAUDE.md` (en Windows necesitas permisos de administrador, así que yo me quedo con el import).

En mi flujo real mantengo **un solo fichero canónico** (`AGENTS.md`) y todos mis agentes leen lo mismo. Acabé con él después de probar la vía de mantener `CLAUDE.md`, `.cursorrules` y `.github/copilot-instructions.md` a la vez: era mantener tres documentos que se contradecían.

## Cómo NO escribir el fichero (lo que aprendí a la mala)

Estos son los errores que yo cometí y que he visto repetirse:

- **Hacerlo gigante.** Si pasas de ~150 líneas, los agentes empiezan a ignorar partes. Guarda los procedimientos largos en documentos sueltos y referencia la ruta, no copies el contenido completo.
- **Poner prompts que se pegan en el chat.** "Actúa como un experto senior" en AGENTS.md no aporta nada. Aquí van instrucciones de proyecto, no un rol de chatbot.
- **Repetir el README.** El README explica qué hace el proyecto; AGENTS.md explica cómo debe comportarse la IA dentro. Si se parecen, algo falla.
- **Olvidar la sección "No hacer".** Es la que más diferencia nota en el resultado.
- **No actualizarlo.** Si cambias de base de datos o de framework y el fichero queda obsoleto, las respuestas se degradan. Mi regla: cada vez que toco el `pom.xml`, reviso AGENTS.md.

## Y con esto, cómo diferenciarlo de Cursor Rules y CLAUDE.md

Este es el punto que más me preguntan: **¿no es esto lo mismo que los `.mdc` de Cursor o que `CLAUDE.md`?**

- **AGENTS.md** es el estándar universal: funciona en Cursor, Copilot, Codex y casi todo lo demás. Es tu capa base.
- **Las reglas `.mdc` de Cursor** son específicas de Cursor y permiten activarlas solo cuando tocas ciertos archivos (con `globs`). Cuando las pruebas bien, te dejan afinar un paso más.
- **CLAUDE.md** es solo de Claude Code; con el truco del import, puedes convertirlo en un reflejo de tu AGENTS.md en vez de duplicarlo.

Mi recomendación práctica: **empieza por AGENTS.md y añade reglas `.mdc` solo cuando necesites comportamientos distintos por ruta**. Si aún no has leído mi guía de Cursor Rules, es la pieza que le falta a esto.

## Conclusión: 30 minutos que rentan todos los días

AGENTS.md no es hype ni "otra cosa que aprender". Es la diferencia entre una IA que adivina tu código y una que ya conoce tu proyecto. Para un estudiante que da sus primeras prácticas, es además un gran ejercicio: te obliga a formalizar tus propias reglas de código, que es exactamente lo que te piden en las entrevistas técnicas.

Mi veredicto: **recomiendo crearlo en el primer commit de cualquier proyecto**, aunque sea la primera versión de 20 líneas. Luego crece solo.

Empieza hoy:
1. Crea `AGENTS.md` con comandos, estilo y "No hacer".
2. Si usas Claude Code, añade `CLAUDE.md` con `@AGENTS.md` al principio.
3. Prueba: pide a Cursor un cambio y compara con lo que hacía antes.
4. Actualízalo cada vez que cambie algo de tu setup.

Si en tu equipo el AGENTS.md molesta más de lo que ayuda, es normal: estos ficheros se escriben cuando algo se rompe, no antes. Empieza con dos reglas y ve añadiendo cuando sangre.
