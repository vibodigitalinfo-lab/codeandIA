---
layout: article
title: "Configuración de VS Code para IA en 2026: lo que uso de verdad"
description: "Configuración de VS Code con IA en 2026: extensiones que siguen vivas, AGENTS.md, settings útiles, modelos propios y el flujo real de un estudiante de DAW."
category: "Lista"
date: 2026-09-06
readtime: 7
---

Cada dos semanas sale una lista de "las 7 extensiones de IA que necesitas" y todas recomiendan lo mismo de hace un año. El problema no es la lista, es que **la IA no se configura con extensiones, se configura con flujo**: qué herramienta hace cada cosa, qué reglas le das, y cómo revisas lo que te propone. Esto es lo que de verdad tengo montado a mediados de 2026, tras probar de más y quedarme con menos.

## El panorama real de 2026

Antes de hablar de mi configuración, el contexto, porque el ecosistema se consolidó de golpe:

- **Continue**, la extensión open-source con la que todos empezamos, **fue adquirida por Cursor** en 2026. Sigue funcionando, pero ya no tiene desarrollo activo. Si la usas, no esperes novedades.
- **Roo Code**, el fork de Cline, está archivado.
- El resultado es que en VS Code el agente libre de referencia que queda es **Cline**: autónomo, open source, leyendo y editando tus archivos, con tu propia API key.

Esta consolidación es buena para elegir: ya no hay 10 opciones, hay tres claras (Copilot, Cline y el chat nativo), y por eso lo que importa ya no es "cuál instalo" sino "cómo lo configuro".

## Mi configuración actual

**1. GitHub Copilot (el copiloto del día a día).** Inline suggestions al escribir, chat para dudas y el modo agente para tareas multi-archivo. Para estudiante, el plan se consigue gratis con el Student Pack (aunque los programas de estudiante han tenido pausas raras en 2026 — mira el estado de tu pack antes de elegir). Es la integración más pulida que hay con VS Code.

**2. Cline (el agente libre, con tu API).** Cuando Copilot no me deja hacer algo o simplemente no tengo créditos, uso Cline con mi propia API key. Es Apache-2.0 y pagas los tokens que gastas; si usas un modelo local o barato, el coste es risible. Para tareas largas ("refactoriza esto y ejecuta los tests") es mi herramienta.

**3. No uso Trae como extensión.** Ojo con esto: Trae no es una extensión de VS Code, es un IDE aparte (un fork de VS Code). Si te gusta su estilo, lo ves en [mi review de Trae AI IDE](/articulos/reviews/trae-ai-ide-review-2026/); aquí hablo de VS Code de verdad.

## El fichero que lo cambia todo: AGENTS.md

La pieza más infravalorada. **AGENTS.md** es un fichero en la raíz de tu proyecto donde le dices a la IA cómo trabaja con ESE proyecto: qué comandos se usan para build y tests, qué convenciones de código sigues, qué no debe tocar. Y desde 2025 lo soporta de forma nativa el agente de Copilot (y lee también `.github/copilot-instructions.md`). En 2026, además, los servidores de Claude y el fichero `.cursorrules` evolucionaron hacia este estándar: los `.cursorrules` están deprecados, ahora se usa AGENTS.md.

No es marketing: es el mayor salto en calidad de lo que te propone la IA. Normalmente lo explico con detalle en [esta guía de AGENTS.md](/articulos/guias/agents-md-guia-2026/) y en la de [cursor rules y `.mdc`](/articulos/guias/cursor-rules-configuracion-mdc-guia/), pero la idea cabe en tres líneas:

```markdown
# Convenciones
- Estilo: indentación 2 espacios, sin semicolons, tests en /test.
# Comandos
- npm test   → ejecuta la suite
- npm run dev → servidor local
```

Con eso, la IA deja de adivinar cómo se trabaja en tu proyecto.

## settings.json que de verdad importan

Lo que toco en la configuración (todo desde Configuración > JSON, `settings.json`):

- `github.copilot.enable` — actívalo o desactívalo por lenguaje. Lo dejo en Java/JS/Python y SQL, y lo apago en YAML para que no me invente config.
- `editor.inlineSuggest.enabled` — los atajos: **Tab** acepta la sugerencia, **Esc** la descarta. Parece tonto, pero decidir rápido entre aceptar o descartar es el 80% de usar bien la IA.
- `github.copilot.nextEditSuggestions.enabled` — las "siguientes ediciones" que te adelantan el cambio repetitivo. Útil en prácticas con patrones (un CRUD).
- `chat.tools.autoApprove` — con cuidado. Cuando lo activo, el agente ejecuta comandos con permiso automático; mejor dejarlo en "pedir" hasta que confíes en el proyecto.

Y lo que más juego me da: **modelos propios en VS Code**. Desde finales de 2025, VS Code te deja enchufar tus propios modelos por API (`chatLanguageModels.json`). Para tareas baratas (explicaciones, dudas puntuales) conecto un modelo económico tipo DeepSeek y me ahorro los créditos de pago; para lo importante dejo el modelo bueno. Es gratis o casi, y no depende de ninguna suscripción.

## El flujo que uso a diario

Esto es lo que de verdad importa, más que cualquier extensión:

1. **Escribir**: Copilot me completa inline; Tab acepto, Esc descarto. Nunca dejo que "escriba por mí" sin mirar.
2. **Tarea grande**: abro el modo agente (con AGENTS.md cargado) y le pido el plan antes de que toque nada: "explícame qué vas a cambiar y en qué archivos".
3. **Reviso**: cada cambio suyo es un diff. No "lo apruebo todo". Si no entiendo una parte, la deshago. Con `git diff` y `git checkout` me curo en salud.
4. **Coste**: para las tareas tontas, soluciones baratas; para las difíciles, el modelo de pago. No gasto créditos en "explícame qué es un HashMap".

## Los errores que yo cometí configurando

Para que no repitas mis fallos de novato:

**1. Instalarlo todo.** Empecé con varios copilotos a la vez (Copilot, Cline, Continue, y dos más cuyos nombres ya he olvidado) y el editor era una selva de sugerencias que se pisaban entre ellas. Se configura mejor con dos, no con siete.

**2. Activar el permiso automático el primer día.** Con `autoApprove` activado desde el inicio, el agente ejecutó un comando que recorría todo el proyecto sin preguntarme. El susto me enseñó que el permiso se pide "hasta que entiendas qué va a hacer".

**3. No enlazar las reglas del repositorio.** Mientras no tuve AGENTS.md, la IA me proponía un estilo distinto en cada archivo (unos con puntos y coma, otros sin). Las reglas del proyecto son las que te salvan de que la IA "adivine tu estilo".

**4. Confundir "lo propone" con "está bien".** Al principio aceptaba todo lo que venía del agente. Ahora leo cada diff: si no lo entiendo, no lo firmo.

## Mi combinación real (y el veredicto)

Si te quedas con algo, esto es: **Copilot para el día a día, Cline (con tu API) para el agente libre, AGENTS.md en cada proyecto de prácticas, y modelos propios para no gastar de más.**

No necesitas las 20 extensiones. Necesitas elegir dos (copiloto + agente), darle a la IA las reglas de tu proyecto y aprender a revisar lo que te devuelve. Si quieres ver el otro lado del péndulo —todo gratuito sin pagar una suscripción—, en [esta comparativa de copilotos](/articulos/comparativas/cursor-vs-github-copilot-para-aprender/) y en la de [alternativas gratis a Cursor](/articulos/listas/alternativas-gratis-a-cursor-2026/) tienes cómo montar el mismo flujo sin gastar un céntimo. Y si me preguntas qué extensión conservaría si solo pudiera tener una: AGENTS.md ni siquiera es una extensión, y es la que más ha mejorado mi código con IA. Escríbeme a ivan@codeandia.com si quieres que te comparta mi `settings.json` completo.

## Sigue por aquí

- [15 atajos de VS Code que te ahorrarán horas cada día](/articulos/listas/atajos-vscode-ahorrar-horas-ia/)
