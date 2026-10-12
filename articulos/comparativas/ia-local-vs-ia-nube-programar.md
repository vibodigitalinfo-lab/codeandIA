---
layout: article
title: "IA local o en la nube para programar: cuál te conviene"
description: "IA local (Ollama, LM Studio) frente a la IA en la nube para programar: privacidad, coste, hardware y cuándo merece la pena cada una, sin humo."
category: "Comparativa"
date: 2026-10-07
readtime: 7
last_modified_at: 2026-10-07
---

Cada vez que alguien monta Ollama en su portátil sale la misma discusión en el grupo de clase: "¿entonces para qué pagar nada, si tengo un modelo en casa?". Y al revés: quien paga veinte dólares al mes mira a los de local como si estuvieran jugando. Los dos tienen razón a medias, porque **local y nube no compiten: resuelven problemas distintos**.

La pregunta de fondo no es cuál es mejor. Es dónde acaba tu código y qué necesitas en cada momento. Vamos por partes.

## Qué significa "local" y qué significa "nube"

- **IA local:** el modelo se descarga y se ejecuta en tu ordenador. Tus datos no salen de tu máquina. Herramientas habituales: **Ollama** y **LM Studio**, con modelos abiertos de distintos tamaños.
- **IA en la nube:** el modelo vive en los servidores del proveedor y tú le envías las peticiones por internet. Es el caso de Copilot, ChatGPT, Claude, Cursor y compañía.

La diferencia técnica se traduce en cuatro cosas que sí notas: privacidad, coste, calidad y tu hardware.

## La tabla rápida

| | IA local | IA en la nube |
|---|---|---|
| **Dónde van tus datos** | Se quedan en tu máquina | Salen a los servidores del proveedor |
| **Coste** | 0 € (pero necesitas equipo) | Suscripción o pago por uso |
| **Calidad del modelo** | Limitada por lo que aguanta tu PC | Estado del arte |
| **Velocidad** | Depende de tu CPU/GPU | Alta y estable |
| **Sin internet** | Funciona | No funciona |
| **Contexto (cuánto lee de golpe)** | Corto, según memoria | Muy grande |
| **Tareas de agente** | Flojas | Buenas |
| **Montaje** | Hay que instalarlo | Entras y ya |

## Privacidad: la diferencia que de verdad importa

Es el argumento fuerte de lo local, y no es paranoia. Si programas para una empresa, o tocas datos personales de usuarios, o simplemente no quieres que tu código acabe en el entrenamiento de nadie, un modelo local te da una tranquilidad que la nube no te puede dar por contrato que firmes.

Dicho esto, para un estudiante que practica con los apuntes de clase, mandar código a un chat no es un drama **si no va con secretos dentro**. La frontera la marca lo que pegas, no la herramienta: claves, tokens y contraseñas no se pegan en ningún sitio, ni local ni en la nube, como cuento en [claves API y `.env`](/articulos/guias/no-pegues-claves-api-en-la-ia/).

## Coste: gratis no quiere decir barato

Aquí está la trampa. La IA local es gratis de usar, pero **necesitas un equipo que la mueva**, y ese equipo cuesta dinero. Y no hablamos de un portátil de 400 €.

- **Un modelo de 7-8B** (el tamaño más razonable para empezar) en cuantización Q4 ocupa unos 4-5 GB y va cómodo con 8 GB de RAM. En un portátil normal funciona, lento.
- **Uno de 14B** pide cerca de 8-9 GB solo para los pesos: necesitas 16 GB de RAM para ir sin sudar.
- **Uno de 30-34B** se va a 18-20 GB: eso son 32 GB de RAM, o una GPU con esa memoria, y ya no es un portátil de estudiante.

La nube, en cambio, te da un modelo enorme sin mover nada. El coste lo trasladas: en vez de pagar hardware, pagas suscripción. Y como ves en [cuánto cuesta la IA para programar](/articulos/comparativas/cuanto-cuesta-ia-programar-mes/), con la nube puedes arrancar a 0 €.

## Tu hardware manda

Este es el punto que la mayoría de tutoriales de IA local se salta. **El tamaño del modelo que puedes usar lo decide tu RAM (y tu GPU), no tu voluntad.** Si tienes 8 GB de RAM, olvídate de los modelos grandes: puedes correr uno pequeño y ya está. Y si tienes una GPU con poca VRAM, el modelo se ejecuta en la CPU, que es mucho más lento.

Antes de invertir tiempo en montar IA local, mira tus números: cuánta RAM tienes, si tienes GPU dedicada y cuánta VRAM. Si el resultado es "8 GB de RAM y gráfica integrada", lo local te va a servir para tareas pequeñas y como experimento, no como tu herramienta principal.

## Cuándo gana lo local

- **Cuando el código es sensible** (proyecto de empresa, datos de usuarios, algo que no puedes subir).
- **Cuando no hay internet o no quieres depender de él.**
- **Para tareas mecánicas y repetitivas:** reformatear, explicar un fragmento, generar datos de ejemplo, resumir un texto largo que no quieres mandar fuera.
- **Para aprender cómo funcionan los modelos**, que es un buen motivo para tenerlo aunque no lo uses a diario.

## Cuándo gana la nube

- **Cuando el problema es difícil.** Un modelo de nube razona mejor y se equivoca menos en código complejo.
- **Cuando necesitas contexto grande.** Leer un proyecto entero de golpe es cosa de la nube, no de un modelo local pequeño.
- **Cuando quieres un agente que ejecute comandos, edite varios ficheros y corra tests.** Los agentes de verdad hoy viven en la nube.
- **Cuando no tienes el equipo.** Si tu portátil es básico, la nube simplemente te da más por menos.

## El enfoque híbrido (el que uso)

No hay que elegir. La combinación que funciona es:

- **Local para lo privado y lo repetitivo.** Datos de ejemplo, reformateos, explicaciones de fragmentos sin secretos.
- **Nube para lo difícil y lo agéntico.** Depurar un error raro, refactorizar, montar un test, entender una librería nueva.
- **Secreto, en ninguno de los dos.** Ni local ni nube: los valores de tus claves no se pegan en un chat.

Así aprovechas lo mejor de cada uno sin pagar de más y sin exponer lo que no toca. Si quieres montar la parte local, lo tienes paso a paso en [Ollama: modelos de IA en tu propio ordenador](/articulos/reviews/ollama-modelos-ia-local-review-2026/) y, si vas más allá, en [montar un RAG local con Ollama](/articulos/guias/rag-local-ollama-apuntes-2026/).

## Veredicto

Si estás empezando y tu portátil es normal: **quédate en la nube** (con el plan gratuito de turno, que da para el curso) y no pierdas tardes peleándote con modelos locales. Si tienes 16 GB de RAM o más y te interesa la privacidad, **monta Ollama** como complemento, no como sustituto. Y si el código que tocas es sensible, entonces lo local deja de ser un capricho y pasa a ser lo correcto.

La pregunta no es "local o nube", es "¿esta tarea concreta dónde la haría mejor?". Casi siempre la respuesta es: la difícil, en la nube; la privada, en tu máquina.

## Sigue por aquí

- [Ollama: modelos de IA en local, review](/articulos/reviews/ollama-modelos-ia-local-review-2026/) — cómo montar la parte local y qué esperar de ella.
- [Montar un RAG local con Ollama](/articulos/guias/rag-local-ollama-apuntes-2026/) — llevar tus apuntes a un modelo que corre en tu PC.
- [Cuánto cuesta la IA para programar al mes](/articulos/comparativas/cuanto-cuesta-ia-programar-mes/) — la factura de la nube, plan por plan.
