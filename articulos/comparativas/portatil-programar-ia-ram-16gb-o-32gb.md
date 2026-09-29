---
layout: article
title: "Portátil para programar con IA: 16 GB o 32 GB de RAM"
description: "Por qué la memoria es la característica que decide si un portátil aguanta dos años de desarrollo, y qué ocurre de verdad cuando te quedas sin ella."
category: "Comparativa"
date: 2026-09-15
readtime: 7
affiliate_text: "Mira el portátil con 16 GB que te recomiendo en la guía"
affiliate_url: "https://www.amazon.es/dp/B0DHRQ18G1?tag=codeandia-21"
affiliate_label: "Ver en Amazon"
---

Pregunté en cuatro foros cuál era la característica que más condicionaba de un portátil para programar. Cuatro respuestas distintas, y ninguna fue la pantalla, la tarjeta gráfica ni el procesador. Todas fueron la memoria.

No es una coincidencia. Es la única característica del portátil que no puedes cambiar nunca y de la que depende, literalmente, cuántas pestañas de VS Code puedes dejar abiertas.

## Por qué la RAM es diferente a todo lo demás

Un disco lo puedes cambiar. La pantalla, la placa base y el procesador, no. Eso lo convierte todo en un problema de presupuesto, porque siempre puedes añadir almacenamiento más adelante.

La RAM es diferente porque en la mayoría de portátiles va soldada a la placa. Y con las versiones de 8 GB soldadas, la decisión se toma una vez, en la tienda, y dura toda la vida del equipo.

Pero el motivo real por el que la RAM se agota antes de lo que esperas no es la cantidad de programas abiertos. Es lo que hace el sistema operativo y las extensiones que no te imaginas.

## Lo que se come la RAM sin que lo cuentes

Un proyecto de DAW típico, con un stack de React y Node:

| Qué | RAM aproximada |
| --- | --- |
| Windows (o macOS) | 3-4 GB |
| Navegador con 15 pestañas | 2-3 GB |
| VS Code con 12 extensiones | 1-1,5 GB |
| Servidor de desarrollo de Node | 0,5-1 GB |
| Docker (si lo usas) | 1-2 GB |
| **Total realista** | **9-12 GB** |

Fíjate en que el editor y tus proyectos, que es lo que te importa, son la parte pequeña. El sistema operativo y el navegador se llevan casi tanto como tu trabajo.

Y luego están los procesos que no recuerdas tener abiertos:

- **El antivirus.** En Windows, el Defender con análisis en tiempo real se lleva 500 MB a 1 GB de forma permanente.
- **La telemetría de los editores.** Los IDE modernos con funciones de IA integradas lanzan procesos en segundo plano aunque no los estés usando.
- **Las versiones web de Teams o Slack**, que son en la práctica un segundo navegador consumiendo memoria.

Con 8 GB, el equipo empieza a escribir en el disco para compensar la falta de memoria. Y cuando eso pasa, todo se ralentiza: los ventiladores se aceleran, la batería dura menos y la respuesta al teclado se nota.

## 16 GB: el mínimo razonable en 2026

Si compras hoy un portátil para programar, **16 GB es el suelo, no la aspiración**. Cualquier recomendación de 8 GB en 2026 para desarrollo web es un consejo de 2020.

Con 16 GB vas sobrado si:

- Tienes un solo proyecto abierto.
- Usas un número razonable de pestañas del navegador.
- No convives con Docker con varios contenedores.

Y te va justo si:

- Tienes abierto un proyecto **y el servidor de desarrollo a la vez** (Angular y Node, por ejemplo).
- Sueles dejar muchas pestañas de documentación.
- Trabajas con vídeo, diseño o algún proceso pesado.

## 32 GB: cuándo compensa de verdad

Los 32 GB son 100€ o 150€ más en el momento de comprar. La pregunta es si ese dinero te va a devolver tiempo.

**Sí compensa si** estás en alguno de estos casos:

- **Docker de verdad.** Si levantas contenedores con dependencias, un arranque puede comerse 3 GB y pico.
- **Modelos locales.** Si pruebas Ollama con un modelo de 7.000 millones de parámetros en tu máquina, necesitas 8 GB solo para el modelo.
- **Bases de datos locales.** Una instancia de PostgreSQL o MongoDB junto a la aplicación.
- **Cuatro años de vida útil.** Un portátil de 2027 debería llegar a 2031 con un proyecto de DAW ya montado. Si para entonces corre Docker o IA local, 16 GB te van a frenar.

**No compensa si** vas a hacer desarrollo web básico con un proyecto a la vez y no has tocado Docker. Ahí es dinero que no te va a volver.

## Los gráficos no son lo que crees

Mucha gente quiere pagar más por una tarjeta gráfica dedicada "por si acaso". Si no vas a programar gráficos ni a jugar, la GPU integrada de un procesador moderno te sobra para desarrollo web.

La GPU dedicada tiene sentido para: aprendizaje automático con vídeo, diseño 3D, o si el portátil es también tu máquina de juego. Para el 90% de un alumno de DAW, es un gasto que no te va a mejorar el tiempo de desarrollo.

## Cómo leer la ficha técnica sin que te vendan humo

Cuando mires un portátil, fíjate en este orden:

1. **RAM y si es ampliable o soldada.** Antes de nada, antes de mirar el procesador. Si es soldada, es tu decisión definitiva.
2. **SSD y su velocidad.** 512 GB es el mínimo; 1 TB si vas a meter herramientas pesadas y modelos de IA.
3. **Pantalla.** Que no sea una TN; para programar, IPS.
4. **Teclado.** Suena obvio, pero se pasan meses tecleando en él. Si te queda el ángulo torcido, te va a doler el hombro.
5. **Procesador y RAM de vídeo.** Lo último. Y de última, la marca importa bastante menos que lo que te cobran por ella.

## Mi conclusión

Si compras con 16 GB **y** tienes margen para ampliar después, es una decisión tranquila: pagas algo más ahora y te ahorras la frustración de quedarte corto a mitad de un proyecto. Si no puedes ampliar, 16 GB es 16 GB y no vas a notar diferencia en el 90% del trabajo.

El error caro aquí no es comprar 8 GB, es comprar 8 GB pensando que "si me quedo corto, ya veré". Con la RAM no hay "ya veré": está soldada, y para entonces el portátil lleva dos años.

Si quieres el resto del puesto de trabajo, la [guía para elegir monitor](/articulos/guias/como-elegir-monitor-programar-2026/) y la [que va sobre el setup por 500 euros](/articulos/guias/setup-completo-programar-500-euros/) cubren las otras piezas con precios comprobados.

## Sigue por aquí

- [Qué portátil comprar para estudiar DAW](/articulos/guias/que-portatil-comprar-estudiar-daw-2026/) — el resto de la ficha técnica, con los modelos que he revisado.
- [Cómo elegir monitor para programar](/articulos/guias/como-elegir-monitor-programar-2026/) — la otra mitad del puesto de trabajo, y la que más afecta a tu vista.
- [Setup completo por 500 euros](/articulos/guias/setup-completo-programar-500-euros/) — por dónde empezar cuando el presupuesto manda sobre el modelo.
