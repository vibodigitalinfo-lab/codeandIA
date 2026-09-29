---
layout: article
title: "Codex CLI de OpenAI en 2026: el agente que uso en la terminal"
description: "Codex CLI de OpenAI es el agente en terminal, gratis y abierto: instalación, AGENTS.md, modos de sandbox, codex exec y qué tal se comporta programando."
category: "Review"
date: 2026-09-24
readtime: 9
---

Llego a la terminal con una pregunta que llevo semanas arrastrando desde clase: ¿por qué hago que una IA piense en un chat aparte si puedo tenerla aquí, leyendo de verdad mis ficheros? Esa es la promesa de Codex CLI, el agente de OpenAI que corre en tu máquina, en tu terminal, sobre tu repositorio. No es un chat con un botón de "copiar": lee, edita y ejecuta. Y como ya pago el Plus para lo de las prácticas, la pregunta era si me aporta algo o si es simplemente más sitio donde perder la tarde.

## Qué es exactamente (y qué no)

Codex CLI es el agente de programación de OpenAI que se ejecuta en local. El repositorio es público, con licencia Apache-2.0 y escrito en Rust. Eso significa dos cosas prácticas: puedes leer qué hace antes de instalarlo, y puedes aportar tú mismo si algo falla. La instalación es de las más cortas que he visto en una herramienta de terminal seria:

```bash
npm install -g @openai/codex
# o en macOS
brew install --cask codex
```

En Windows va por WSL, que es lo que te dirá el propio instalador. A partir de ahí escribes `codex` y te pregunta cómo quieres entrar. Aquí está la decisión que importa: **con tu cuenta de ChatGPT o con una clave de API**. Si eliges la cuenta, el consumo sale de la cuota de tu plan. Si eliges clave, pagas por tokens con la tabla de precios de la API. Yo uso la cuenta, porque ya estaba pagando Plus y me parecía absurdo pagar dos veces por lo mismo.

## Qué modelos te da y cuánto cuesta

Con la cuenta de ChatGPT, Codex va incluido en los planes Free, Go, Plus, Pro, Business, Edu y Enterprise. Los que importan de verdad:

- **Plus (20 $/mes)**: incluye Codex en la web, en la CLI, en la extensión del editor y en iOS, con la familia GPT-5.6 y la opción de añadir créditos.
- **Pro**: hay dos escalones, 100 $/mes con unas cinco veces más uso que Plus y 200 $/mes con unas veinte. El de 100 también desbloquea GPT-5.3-Codex-Spark, que va en vista previa.
- **Clave de API**: si prefieres separar el gasto, pagas por uso. Los créditos van por millón de tokens, el precio depende del modelo y la entrada ya cacheada se factura bastante más barata que la normal.

Dentro de una sesión, `status` te dice lo que te queda. Detalle importante: **Plus no son sesiones ilimitadas**. Hay límites por ventana de tiempo, no un número fijo de mensajes, y OpenAI los ajusta según la carga. Me he topado con el aviso un par de veces haciendo refactors largos una tarde, y la sensación es la de un asistente que te dice "tómatela". Si tu uso es de varias horas al día, el escalón de Pro es casi seguro tu suelo.

## Lo que de verdad lo hace bueno: AGENTS.md y el sandbox

Si lo único que le pido es que me escriba código en un chat, cualquier modelo vale. Lo que me hizo quedarme fue otra cosa, y tiene mucho que ver con [AGENTS.md](/articulos/guias/agents-md-guia-2026/).

Codex lee un fichero `AGENTS.md` antes de tocar nada. Y no solo el de la raíz: mira primero en tu carpeta global (`~/.codex`) y luego va bajando desde la raíz del proyecto hasta el directorio en el que estás, de modo que **los ficheros más cercanos pisan a los lejanos**. Es una cadena de instrucciones, no un archivo suelto. En la práctica es como tener las reglas de la asignatura escritas justo donde la IA las va a leer: cómo se forman los commits, qué framework usamos, qué convención de nombres hay que respetar.

Lo segundo es el modelo de permisos, que es lo que más me tranquilidad viniendo de un agente de terminal:

- Por defecto, `codex exec` corre en **sandbox de solo lectura**. Puede leer y explicar, pero no escribir.
- Para editar hay que pedirlo explícitamente con `--sandbox workspace-write`.
- `--sandbox danger-full-access` existe, y la propia documentación lo reserva para entornos controlados tipo contenedor o runner de integración continua.

Esto es justo lo contrario de un agente que te pide permiso veinte veces. El valor por defecto es el seguro y tú subes el nivel cuando sabes lo que haces. Con un proyecto de clase, que es donde menos atención tienes a las once de la noche, eso vale mucho.

Y para lo que ya tengas automatizado está `codex exec` sin interacción: escribe el progreso por `stderr`, el mensaje final por `stdout` y acepta `--json` para devolver líneas JSON. Es el modo que metería en un script si quisiera, aunque de momento solo lo he usado en local, no en integración continua. También hay soporte de MCP, que ya expliqué por aquí en [MCP para principiantes](/articulos/guias/mcp-para-principiantes-guia-2026/), y skills locales en `.codex/skills`.

## Mi experiencia real con el proyecto de clase

Lo probé sobre la API REST que estoy haciendo con Spring Boot, la misma que conté en [tu primer API REST](/articulos/guias/primera-api-rest-spring-boot-ia-daw/). El flujo que acabé usando es este:

1. Le pido primero que **lea y explique**, en solo lectura: "dime qué hace este controlador y dónde está el problema".
2. Le pido que **planifique** los cambios sin tocar nada: "enumera los ficheros que tocarías para añadir un campo y por qué".
3. Solo entonces le dejo escribir, con un `AGENTS.md` ya escrito por mí con las reglas del proyecto.

Ese orden me ha ahorrado la mitad de los sustos. En modo escritura directa te mete cambios que no habías pedido y encima los aplica con absoluta confianza; en lectura primero te enteras de lo que va a hacer antes de que lo haga. Y como tengo git, antes de cada ronda hago *commit*, que es la lección que me tracé en [git con IA](/articulos/guias/git-con-ia-2026/).

Lo que **no** me ha ido bien: el frontend. Pedí que rehíciera un componente de React con estilos y el resultado fue más o menos el que me da cualquier chat: bonito, genérico y con cuarenta clases dentro de un `div`. En la comunidad se coincide bastante en que Codex brilla en terminal, scripts, infraestructura y todo lo que se parece a DevOps, y que se queda corto en interfaz. No lo he medido yo, así que me lo quedo como rumor razonable.

La otra cosa que me ha pasado: **no cumple literalmente lo que pides**. Le escribí "no toques el nombre de la función" y me lo cambió en un fichero. Con Claude Code me pasa bastante menos. Contexto, instrucciones claras y commits, y se arregla.

## Precio: lo que te cuesta de verdad

Aquí no hay sorpresas, que es la gracia. Si ya pagas Plus, **Codex CLI te sale a coste cero**: la herramienta es abierta y el consumo va con la cuota que ya estás pagando. Si entras con clave de API, entonces sí pagas por token, y una sesión larga con un modelo grande se nota en la factura.

Para comparar con la alternativa tienes [Cursor vs Claude Code](/articulos/comparativas/cursor-vs-claude-code-2026/) y el panorama completo de terminales está en [IA en la terminal para estudiantes](/articulos/guias/ia-en-terminal-estudiantes-daw/). El veredicto corto es este: si ya pagas un plan de ChatGPT, la CLI de OpenAI es la forma más barata de tener un agente de terminal serio, porque no te pide una suscripción nueva.

## Mi veredicto

**Lo recomiendo si ya pagas ChatGPT y te gusta la terminal.** Es abierto, el sandbox por defecto es de solo lectura, lee `AGENTS.md` de verdad y la cuenta de Plus te cubre sin pagar nada extra. Que el código sea público te deja auditar lo que hace con tus ficheros, y en un agente que ejecuta comandos eso no es un detalle menor.

**No lo recomiendo si** quieres un agente dentro del editor y que la interfaz sea el sitio donde piensas; para eso sigo viendo mejor a Cursor. Tampoco si esperas que te resuelva la maquetación sin que tengas que pelearte con el resultado, porque ahí flojea.

**Y no lo uses sin git y sin `AGENTS.md`.** Un agente que ejecuta comandos en tu máquina es un desastre esperando a pasarle la noche, pero con un commit antes de empezar y un fichero de instrucciones, mi problema se convirtió en productividad. Si te animas y te atascas con la instalación, escríbeme a ivan@codeandia.com y lo vemos.

## Sigue por aquí

- [IA en la terminal para estudiantes: Claude Code, Copilot CLI y Ollama](/articulos/guias/ia-en-terminal-estudiantes-daw/)
- [AGENTS.md: la guía de instrucciones para IA en tus proyectos](/articulos/guias/agents-md-guia-2026/)
- [Claude Code CLI: terminal-first, agentes paralelos y su precio](/articulos/reviews/claude-code-cli-review-2026/)
