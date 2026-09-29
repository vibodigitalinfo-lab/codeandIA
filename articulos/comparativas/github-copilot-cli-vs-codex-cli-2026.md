---
layout: article
title: "GitHub Copilot CLI vs Codex CLI en 2026: cuál para tu curso"
description: "Comparo la CLI de GitHub Copilot y la de Codex de OpenAI para programar en la terminal: cuenta, precio, permisos y cuál le gana al estudiante de DAW."
category: "Comparativa"
date: 2026-09-26
readtime: 7
---

En la review de [Codex CLI de OpenAI](/articulos/reviews/codex-cli-openai-review-2026/) terminé diciendo que era la forma más barata de tener un agente de terminal si ya pagas ChatGPT. Lo que no dije, porque me lo preguntasteis varios por correo, es qué pasa si lo comparas con la CLI del otro gigante: la de **GitHub Copilot**. Las dos corren en tu terminal, leen tu repositorio y editan ficheros por ti, pero la decisión entre una y otra no es técnica: es de cuenta, de dinero y de cómo te comporta la IA. Voy a contarte cómo las he usado en las prácticas este mes y qué haría un estudiante de DAW con cabeza.

## Qué es cada una, sin humo

**Codex CLI** es el agente de OpenAI que ya conté aquí: abierto, escrito en Rust, corre en local y se instala con un comando. Lee un `AGENTS.md` de forma nativa, su sandbox es de solo lectura por defecto y el consumo va con tu plan de ChatGPT o con una clave de API.

**GitHub Copilot CLI** es el agente de terminal de GitHub. Se instala como paquete de npm y se identifica con tu cuenta de GitHub, la misma que ya usas en el editor. Una vez dentro, tienes tres modos: uno para que te **explique** código, otro para que te **genere** piezas escribiendo en la terminal y un tercero para que **revise** un diff de camino a tu equipo (el método para aprovecharlo está en mi [guía de code review con IA](/articulos/guias/code-review-con-ia-2026/)).

```bash
npm install -g @openai/codex    # Codex CLI
npm install -g @github/copilot  # GitHub Copilot CLI
```

En Windows, las dos pasan por WSL. No hay atajo ahí.

## Criterio 1: qué cuenta necesitas y cuánto cuesta

Aquí se decide casi todo. **Codex CLI** funciona desde el plan Free de ChatGPT, aunque con límites, y si ya pagas el Plus entra sin coste añadido. Corrió en la máquina de mi primo sin un céntimo.

**Copilot CLI** pide una suscripción de GitHub Copilot. Y aquí está el matiz que cambió el panorama en 2026 y que ya conté en [merece la pena pagar por IA](/articulos/comparativas/merece-la-pena-pagar-ia-2026/): GitHub tuvo que hacer una pausa en el alta de nuevas cuentas durante meses, lo que dejó a muchos estudiantes intentando activar el plan gratis sin éxito. Si tu cuenta ya tiene Copilot (la que te da el [Student Pack](/articulos/listas/github-student-pack-que-incluye/)), la CLI te sale gratis; si no, tienes que esperar o pagar.

Veredicto de este criterio: **si ya pagas ChatGPT, Codex CLI gana; si ya tienes Copilot por el pack de GitHub, empatan.** El que empieza de cero lo tiene más fácil con Codex por el plan Free.

## Criterio 2: los permisos, que es donde te lesiones

Lo que separa a un agente divertido de uno que mete los dedos donde no debe es cómo te pide permiso.

**Codex CLI** trabaja por cajas: por defecto solo lee, y para escribir tienes que subir el nivel del sandbox de forma explícita. Yo lo dejo siempre en solo lectura hasta que le he leído el plan.

**Copilot CLI** pide confirmación comando a comando y te muestra cada acción antes de ejecutarla. Es más pesado en según qué tareas, pero es exactamente lo que necesitas a las once de la noche con una práctica que se va. Ninguna de las dos ejecuta nada sin que tú lo apruebes cuando la configuras bien.

Mi sensación tras usar ambas: Copilot CLI te trata como alguien que supervisa, Codex CLI te trata como alguien que decide cuándo dar el siguiente nivel. Para clase, prefiero la segunda con el sandbox en solo lectura: me obliga a entender el plan antes de dejarlo escribir.

## Criterio 3: cómo leen tu proyecto

Las dos leen el repositorio y te responden con el código de verdad delante, que es el salto enorme frente al chat de siempre.

**Codex CLI** monta una cascada de `AGENTS.md` (primero el de tu carpeta global y luego bajando por las carpetas), de modo que cada sitio tiene sus reglas. Eso lo hace ideal para un proyecto con varias partes, porque le pones el contexto justo donde lo va a leer.

**Copilot CLI** se apoya en la misma infraestructura que el editor: indexación del repositorio, historial de sesiones que puedes retomar con `sessions --resume` y un nivel de contexto muy cómodo si ya trabajas con Copilot en VS Code.

Si tu asignatura crece en ficheros y reglas por carpeta, la cascada de Codex se nota. Si trabajas a la manera de GitHub desde el día uno, Copilot CLI se siente como ampliar lo que ya haces.

## Criterio 4: qué modelos te deja y por qué importa

Copilot CLI te deja **elegir el modelo** entre los que copan tu suscripción, incluidos los de Anthropic y OpenAI. Eso es buena noticia si quieres cambiar de modelo por tarea sin cambiar de herramienta.

Codex CLI usa la familia de OpenAI y, si entras con clave de API o con un proxy de modelos, puedes enchufarle otras opciones (el punto de los proxies lo dejé en [MCP para principiantes](/articulos/guias/mcp-para-principiantes-guia-2026/)). Con la cuenta normal de ChatGPT no vas a cambiar de proveedor así como así.

Para el trabajo de DAW, la diferencia de modelos es de esas que suenan más de lo que pesan: con contexto bueno, las dos resuelven la práctica de programación. Donde sí noto a Copilot CLI es en tareas largas de edición: su flujo de vuelta con los agentes del editor es más adictivo.

## Mi veredicto, por caso

**Elige Codex CLI si** ya pagas un plan de ChatGPT, si quieres un agente abierto que puedas auditar y si te da confianza el sandbox de solo lectura por defecto.

**Elige GitHub Copilot CLI si** tu cuenta ya tiene Copilot (por el pack de estudiante o por un plan de pago), si quieres el mismo proveedor de contexto en editor y terminal, y si prefieres confirmar cada comando a que te lo den con niveles.

**Y si no pagas nada** es donde hay trampa: Codex con el plan Free te da un agente de terminal real sin abrir la cartera, lo que hoy no te da Copilot si su alta gratuita sigue parada. Eso, para un estudiante, manda.

La decisión real de un estudiante es esta: **usa el que ya tengas, y si no tienes ninguno, empieza por el que ya estás pagando sin saberlo.** La terminal no se gana por la herramienta, se gana por meterte y acostumbrarte. Empieza a leer tus propios ficheros con la IA en un proyecto de clase de verdad, el del trimestre, y deja la comparativa para cuando llegue la factura.

## Sigue por aquí

- [Codex CLI de OpenAI en 2026: el agente que uso en la terminal](/articulos/reviews/codex-cli-openai-review-2026/)
- [Claude Code CLI: terminal-first, agentes paralelos y su precio](/articulos/reviews/claude-code-cli-review-2026/)
- [AGENTS.md: la guía de instrucciones para IA en tus proyectos](/articulos/guias/agents-md-guia-2026/)