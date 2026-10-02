---
layout: article
title: "Cuánto cuesta la IA para programar: 0 €, 10 € o 20 € al mes"
description: "Precios de IA para programar en octubre de 2026: Copilot, Claude, ChatGPT Plus, Cursor, Zed, Warp, Gemini CLI y DeepSeek, con tres presupuestos reales."
category: "Comparativa"
date: 2026-10-02
readtime: 11
last_modified_at: 2026-10-02
---

Hay una pregunta que me llega por el grupo de clase cada pocas semanas y que siempre acaba en la misma discusión: **¿cuánto os gastáis vosotros en IA al mes?** El que lo tiene claro responde con veinte dólares, el que no lo tiene claro contesta "gratis" sin saber si su límite de peticiones se le acaba a media tarde, y casi nadie ha hecho la cuenta de lo que realmente consume un trimestre de prácticas.

La he hecho. Y la respuesta corta es que **con 0 euros llegas al 80 %**, que con 10 euros vas sobrado y que los veinte dólares solo tienen sentido si el agente de la terminal es parte de tu flujo de trabajo, no un extra.

> **Aviso de fechas**: todos los precios de esta comparativa están comprobados el 2 de octubre de 2026 contra las páginas oficiales de cada producto, porque en este sector un artículo de hace dos meses ya no vale nada. Están en **dólares**; en España hay que sumarle el 21 % de IVA, así que 20 $ se te van a 24 $ en la factura.

## La tabla corta

| Herramienta | Plan | Precio al mes | Para qué te sirve |
|---|---|---|---|
| **Gemini CLI** | Gratis con cuenta Google | **0 $** | Agente de terminal: 60 peticiones por minuto y 1.000 al día |
| **DeepSeek** | Chat web | **0 $** | Preguntar, entender errores y revisar código |
| **Ollama / LM Studio** | Modelos en local | **0 $** | Modelo propio en tu portátil, sin enviar una línea de código |
| **CodeRabbit** | Repositorios públicos | **0 $** | Revisión de código en abierto: 5 revisiones por hora |
| **GitHub Copilot** | Estudiante verificado | **0 $** | Autocompletado ilimitado; chat y agentes, limitados |
| **GitHub Copilot** | Pro | **10 $** | Autocompletado y agentes en el IDE, la CLI y GitHub.com |
| **Zed** | Pro | **10 $** | Modelos alojados en el editor y predicciones ilimitadas |
| **Claude** | Pro | **17 $ con pago anual / 20 $ al mes** | Claude Code en la terminal, entre otras cosas |
| **Warp** | Build | **18 $ con pago anual / 20 $ al mes** | Terminal con bloques y 1.500 créditos de IA |
| **ChatGPT** | Plus | **20 $** | Razonamiento avanzado y más límites (la API va aparte) |
| **Cursor** | Pro | **20 $** | El editor con el modo agente más pulido del mercado |
| **Claude** | Max | **desde 100 $** | Cinco o veinte veces más uso de Claude Code |
| **Cursor** | Pro+ / Ultra | **60 $ / 200 $** | Cuando los 20 $ de uso se quedan cortos |

## La ruta de 0 euros: la que suele dar mejor resultado

Empiezo por aquí porque es la que casi nadie hace bien. **No es que uses un juguete**: es que combinas cuatro cosas que no compiten entre sí.

1. **Gemini CLI, agente de terminal gratis.** Con una clave gratuita de AI Studio tienes 60 peticiones por minuto y 1.000 al día. Para una tarde de prácticas eso de sobra. Está explicado en [la review de Gemini CLI](/articulos/reviews/gemini-cli-review-2026/).
2. **DeepSeek en el chat, sin límite y sin pagar.** Es lo que uso para entender por qué falla un `NullPointerException` cuando ya he mirado veinte minutos. La review cuenta también lo que no debes mandarle: el código de la empresa.
3. **Un modelo local con Ollama**, si tu portátil aguanta. Cuesta 0 €, es privado y va lento, pero para tareas pequeñas funciona. Los tres modelos que uso están en [la guía de Ollama](/articulos/reviews/ollama-modelos-ia-local-review-2026/).
4. **Copilot gratis para estudiantes verificados.** El autocompletado no tiene límite de peticiones; lo que sí está limitado es el chat y el modo agente. Está en [la review de Copilot para estudiantes](/articulos/reviews/github-copilot-gratis-estudiantes/).

Con esa combinación llegas hasta mayo sin pagar nada. La calidad no es la de un plan de veinte dólares, pero para prácticas de DAW, para explicaros y para la parte del proyecto final donde lo que necesitas es que alguien te diga qué está mal, sí es suficiente.

## El escalón de 10 dólares: el punto dulce

Si vas a pagar una sola cosa, que sea una de estas dos.

- **GitHub Copilot Pro, 10 $ al mes.** Es el plan más redondo que hay ahora mismo: funciona igual en VS Code, en JetBrains, en la CLI y en la web de GitHub, y por el mismo precio te da los agentes donde los necesitas. Si estudias Java en IntelliJ, este es el que te va a servir.
- **Zed Pro, 10 $ al mes.** El plan Personal de Zed es gratis pero **sin modelos alojados**: si no gastas esos 10 $, escribes con tus propias claves o con modelos locales. Lo que compras aquí son los modelos dentro del editor y las predicciones de edición sin techo.

Los dos cuestan lo mismo, así que la decisión es de gusto: si quieres el asistente dentro del editor, Copilot; si quieres el editor entero, Zed.

## El escalón de 17-20 dólares: cuándo lo justifico

Aquí es donde la mayoría se equivoca, porque paga sin saber qué está comprando.

- **Claude Pro (17 $ al mes pagando el año, 20 $ pagando mes a mes) y ChatGPT Plus (20 $)**. Los dos traen el asistente de razonamiento potente y, en el caso de Claude, el acceso a Claude Code en la terminal. Si vas a usar agentes de verdad para escribir código y ejecutar pruebas, aquí es donde se nota. **Ojo con un detalle**: ChatGPT Plus **no** incluye uso de la API; eso se factura aparte en otra parte.
- **Warp Build (18 $ al año, 20 $ al mes)** son 1.500 créditos de IA al mes. Si lo que te gusta es la terminal y no el editor, tiene su sentido; si te gusta la terminal de VS Code, es un gasto de lujo.
- **Cursor Pro (20 $)** sigue siendo el editor con el agente más redondo del mercado, pero desde que le quitaron el año gratis a los estudiantes en junio de 2026, es el que más duele pagar.

Si te fijas en la etiqueta, Claude, ChatGPT y Cursor cuestan lo mismo. Si te fijas en lo que haces con ellos, **Claude es el único de los tres que te da un agente programador de verdad**; los otros dos te dan un asistente muy bueno dentro de una conversación.

## El salto a 100 dólares: por qué no

Claude Max empieza en **100 $ al mes** y da cinco o veinte veces más de uso de Claude Code; Cursor Pro+ y Ultra suben a 60 $ y 200 $. Son planes para gente que se pasa la vida con la herramienta: gente que factura por su tiempo, no gente que entrega prácticas en junio.

**Con 20 $ tienes la misma calidad en la práctica**, solo que si te pasas de uso esperas. Mi criterio es feo pero funciona: si un mes has llegado al límite de uso y has hecho un trabajo que te habría costado cuatro horas, el plan de 100 $ ya se ha pagado a sí mismo.

## Lo único que se paga por tokens: las APIs

Si lo tuyo es montar un bot, un asistente propio o automatizaciones, ya no eliges suscripción: eliges **tokens**. Y aquí la cosa se pone interesante, porque la API de DeepSeek es absurdamente barata frente a cualquier suscripción.

Por millón de tokens con V4.1-Flash, según la tabla oficial:

| | Fuera de punta | Hora punta |
|---|---|---|
| Entrada con caché | 0,003 $ | 0,006 $ |
| Entrada sin caché | 0,15 $ | 0,30 $ |
| Salida | 0,60 $ | 1,20 $ |

La hora punta son de 01:00 a 04:00 UTC y de 06:00 a 10:00 UTC, de lunes a viernes. Con una carga de trabajo de estudiante (unos 20 millones de tokens de entrada y 4 millones de salida al mes, escribiendo de madrugada) te sale **entre 3 y 5 dólares al mes**, no veinte.

## La cuenta de verdad: tres presupuestos

| Presupuesto | Qué contratas | Cuándo lo elijo |
|---|---|---|
| **0 €/mes** | Gemini CLI + DeepSeek + Copilot de estudiante + un modelo local | Estás aprendiendo: si ya controlas el tema, te quedas corto en cuanto empiece el proyecto de grupo |
| **10 €/mes** | Copilot Pro o Zed Pro, pero no los dos | Es el punto dulce de la mayoría de estudiantes |
| **30 €/mes** | Un plan de 20 $ más otro de 10 $ | Tienes que hacer dos cosas distintas: un editor con agente y un agente en la terminal |

**Mi veredicto**: con 0 euros haces el curso entero. Con 10 euros vas cómodo. Los veinte dólares tienen sentido solo si la IA es una parte de tu trabajo y no una ayuda puntual, y los cien euros no son para ti.

Y si lo que quieres decidir es si merece la pena pagar en absoluto, eso lo tienes desmontado punto por punto en [¿merece la pena pagar por IA en 2026?](/articulos/comparativas/merece-la-pena-pagar-ia-2026/). Si ya has decidido que sí y lo que quieres es la factura exacta, esta es tu tabla.

## Sigue por aquí

- [Claude Code CLI: la terminal manda](/articulos/reviews/claude-code-cli-review-2026/) — por qué es el único plan de veinte dólares que trae un agente programador de verdad.
- [Cursor vs Claude Code: dos formas de trabajar](/articulos/comparativas/cursor-vs-claude-code-2026/) — la comparación técnica de los dos agentes.
- [GitHub Copilot gratis para estudiantes](/articulos/reviews/github-copilot-gratis-estudiantes/) — cómo activar el plan gratuito y qué queda limitado.