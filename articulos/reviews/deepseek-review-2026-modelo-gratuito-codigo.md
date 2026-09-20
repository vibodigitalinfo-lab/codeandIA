---
layout: article
title: "DeepSeek review 2026: el modelo gratuito que sigue dando guerra"
description: "Mi review honesta de DeepSeek en 2026: qué incluye el plan gratis, cómo programa de verdad, precios de la API y la letra pequeña de la privacidad."
category: "Review"
date: 2026-09-08
readtime: 8
---

Empecé a usar DeepSeek a principios de 2025, cuando todo el mundo hablaba del R1 gratis que rivalizaba con modelos de pago. Lo curioso es que un año y medio después sigo usándolo casi a diario, y sigue siendo gratis. Antes de escribir esto me he releído su documentación con fecha de hoy para no contarte humo: te cuento qué hay de verdad detrás del modelo chino, cómo programa para un estudiante de DAW y qué letra pequeña no te van a contar en las noticias.

## Qué es DeepSeek hoy (septiembre 2026)

DeepSeek es el laboratorio chino que se hizo famoso en enero de 2025 cuando el modelo R1 dejó a medio sector con el culo al aire: rendimiento de los grandes a una fracción del coste y con los pesos abiertos. En 2026 la cosa ha evolucionado bastante y el modelo actual ya no es el R1.

Desde el 10 de septiembre de 2026 el modelo por defecto del chat es **DeepSeek-V4.1-Flash**: 552 mil millones de parámetros con arquitectura MoE (8 mil millones activos en entrada), contexto de 1 millón de tokens, visión multimodal nativa y pesos abiertos con licencia MIT. O sea: puedes bajártelo y correrlo tú, como con los modelos de Ollama que ya te conté en [mi guía de modelos locales](/articulos/reviews/ollama-modelos-ia-local-review-2026/).

Lo más gordo: DeepSeek entró en una guerra de precios tan fuerte que OpenAI recortó precios de su modelo barato un 80% en julio de 2026 para intentar competir. Eso beneficia a todos, vayas a usar DeepSeek o no.

## El plan gratis: sigue siendo gratis, pero con matices

Aquí va lo importante: en 2026 **el chat web y las apps de DeepSeek siguen siendo gratuitos**. No hay "plan Pro" que te venda la versión buena: el gratis es el único plan de consumo. Eso ya lo diferencia de ChatGPT o Claude, donde el modelo bueno de verdad está detrás de 20€ al mes.

Qué te llevas sin pagar:

- Chat con el V4.1-Flash, incluido el modo de razonamiento.
- Subida de archivos (PDF, Word, Excel, imágenes) y búsqueda web integrada.
- Entrada de voz en la app.
- Contexto de 1 millón de tokens, que es bestial: puedes pegarle un proyecto entero.

Ahora, los matices que nadie te cuenta. No hay una cuota de mensajes publicada: DeepSeek aplica throttling dinámico, y en horas punta te aparece el aviso de "servidor ocupado" y las respuestas van más lentas. A mí me pasa a última hora de la tarde español con bastante más frecuencia de lo que me gustaría. Y deja claro que "gratis" se refiere al chat: **la API es de pago por token**, no hay plan gratis de API y, de hecho, varias fuentes apuntan a que ya no regalan créditos al crear cuenta. No lo he verificado al 100% porque no he recargado saldo; si necesitas la API, míralo tu antes de dar de alta.

## DeepSeek programando: qué dice la experiencia real

Aquí seré honesto y te separo el hype de lo que se ve en el día a día. La mayoría de reviews técnicas de 2026 hablan del V4-Flash y el V4-Pro de abril-julio, porque el V4.1-Flash acaba de salir y aún no tiene masa crítica de opiniones. Con esa salvedad:

- **Precio-rendimiento sin rival.** Es la frase que más se repite en r/DeepSeek. El modelo no es el mejor del mundo, pero por lo que cuesta (nada) rinde muchísimo.
- **En tareas cotidianas no notas el bajón.** Refactorizar, escribir tests, explicarte un error de Java, generar un CRUD de prácticas: va sobrado. Yo lo uso bastante acoplado a GitHub Copilot y a mí me cubre el flujo normal de DAW sin quejarme.
- **En problemas duros se nota la diferencia.** Proyectos muy grandes, bugs raros de lógica o código con mil restricciones se le atascan antes que a un GPT-5 o un Claude de pago. A veces se pone a "razonar en círculos" y gasta muchísimos tokens sin avanzar. La regla que uso: tareas medias → DeepSeek; rompecabezas retorcido → me paso al modelo de pago que tenga el día.

Para el estudiante de DAW, el resumen es claro: para aprender, refactorizar y depurar sin gastar un euro es de lo mejor que hay. Con una condición: **hay que revisar el código que te da**, porque las alucinaciones y las referencias inventadas no han desaparecido. Eso es válido para cualquier IA y con DeepSeek es urgente, porque no tiene el filtro de calidad de un proveedor con más recursos.

## La API: la más barata del mercado, con truco

Si algún día montas algo que consuma IA por código (un asistente propio, un bot, automatizaciones), la API de DeepSeek es brutalmente barata. El modelo `deepseek-flash` (V4.1-Flash) está en torno a **0,15 dólares por millón de tokens de entrada y 0,60 por millón de salida**, y tiene la gracia del descuento off-peak: fuera de horas punta la tarifa baja a la mitad (en los fines de semana, todo el día). Además usa el mismo formato de API que OpenAI: cambias la `base_url` y tu código que llamaba a OpenAI funciona casi sin tocarlo.

Si te parece que mola para un proyecto de clase, ojo con una cosa: esa economía la paga alguien. Y ese alguien eres tú leyendo sus condiciones de uso.

## La letra pequeña: privacidad

Aquí no me voy a andar con medias tintas, que es lo que más me molesta de los videos de "DeepSeek es increíble y gratis". **Tu código se guarda en servidores en China continental.** La política de privacidad lo dice sin rodeos: recolectan, procesan y almacenan tus datos personales en la República Popular China. Están sujetos a la ley china, y varios reguladores europeos (Italia, Francia, Alemania, Bélgica, Portugal) les han abierto investigaciones.

Traducción para tu vida real: **nunca subas a DeepSeek código de las prácticas de empresa, credenciales, ni datos personales reales de clientes.** Para un proyecto de clase inventado, sin problema. Para la FCT con datos de una empresa de verdad, no lo toques. En ese caso usa un modelo local (los pesos del V4.1-Flash son MIT) o un proveedor con residencia de datos en la UE. No es paranoia: es leer la letra pequeña dos minutos.

## Veredicto honesto

¿Lo recomiendo? Depende de para qué.

- **Para aprender y practicar código sin pagar: sí, sin dudarlo.** Es la mejor opción gratuita sin límites que he probado, con un rendimiento muy cerca de modelos de pago en el día a día de DAW.
- **Para proyectos sensibles o datos de empresa: no.** Ahí la privacidad lo descalifica y punto.
- **Para la API barata: sí**, con el ojo puesto en el descuento off-peak, que te deja la entrada a mitad de precio.

La parte de "está cambiando todo" del titular... hasta cierto punto. El impacto real es que ha forzado la guerra de precios que te ha bajado las tarifas hasta a los modelos americanos, y eso sí lo notas. Pero ni es perfecto ni va a sustituir el que aprendas a programar: te da respuestas gratis, y tú sigues teniendo la obligación de entenderlas. Si quieres poner la IA al servicio del curso sin volverte dependiente, te dejo el método que uso yo para [preparar exámenes prácticos con IA](/articulos/guias/preparar-examenes-practicos-daw-con-ia/) sin convertirme en copión.