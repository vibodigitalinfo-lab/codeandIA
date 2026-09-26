---
layout: article
title: "Accesibilidad web con IA: cumplir sin inventarte reglas"
description: "Cómo usar IA para cumplir accesibilidad en tus prácticas de DAW sin inventarte las reglas: qué delegar, qué no, y el prompt que encuentra los fallos de verdad."
category: "Guía"
# PROVISIONAL: no es fecha de publicacion. Se cambia al mover el archivo
# fuera de _entrada/, a un dia libre y nunca posterior a hoy.
date: 2026-09-26
readtime: 7
---

La accesibilidad es de las pocas cosas donde la IA es casi tan buena como escribiendo código, y sin embargo casi nadie la usa. La razón es que exige un vocabulario que no te enseñan en primero de DAW: WCAG, ARIA, roles, foco, contraste. Es un tema donde la IA sabe mucho, tú no sabes ni qué preguntar, y ahí es donde se cuelan errores que no detectas porque no sabes leerlos.

El resultado típico es una web que "tiene accesibilidad" porque lleva `alt` en todas las imágenes y un `aria-label` suelto en un `div`. Eso no es accesibilidad, es decoración. Y lo peligroso es que pasa las comprobaciones automáticas que tienes configuradas, así que parece que está bien.

Te explico cómo uso la IA en esto sin que me invente estándares, qué partes delego y qué partes hago yo, y el prompt concreto que encuentra los problemas reales.

## Lo primero: pedirle los criterios, no las reglas

El fallo más caro es pedirle a la IA "¿este componente es accesible?". Recibes un sí rotundo y cinco frases genéricas, porque la pregunta se puede responder sin saber nada del tema. Ese sí no vale nada.

Lo que sí funciona es que la IA **repita el criterio oficial** mientras juzga tu código. Si te dice "no cumples 1.4.3 porque el contraste es 3.1:1 y necesita 4.5:1", estás ante algo verificable. Si te dice "el color podría ser más accesible", estás ante relleno.

> "Revisa este componente contra el criterio WCAG exacto que apliques. Para cada problema quiero tres cosas: el identificador del criterio (por ejemplo 1.4.3), el valor medido y el mínimo exigido. Si no puedes medirlo, dilo y no lo afirmes."

El "si no puedes medirlo, dilo" es la parte importante. Sin esa frase la IA rellena huecos con seguridad inventada, y el hueco típico aquí son los ratios de contraste, que se calculan con una fórmula que el modelo no hace mentalmente. Si te da un 3.1:1 sin explicar cómo lo ha medido, está suponiendo.

## Qué delegar y qué no

**Delega la revisión, no la decisión.** La IA es excelente para ver que un `div` hace de botón y que a un lector de pantalla no le queda claro. Ese barrido se hace en segundos y a una persona le lleva una hora.

**No delegues la declaración de semántica.** Aquí está la trampa seria: `aria-label` y `role` no son adornos, son promesas. Si pones `role="button"` en un `div` y no gestionas teclado ni foco, has creado un elemento que anuncia "botón" y luego no hace nada con el Enter. Para quien usa lector de pantalla eso es peor que no tener nada: es un control que engaña.

Mi regla: si un elemento puede ser `<button>` o `<a>`, es `<button>` o `<a>`. No me pongas `role` porque el modelo lo sugirió.

Para los `aria-label` hay una prueba rápida que no necesita la IA: si el texto visible ya dice lo mismo que el `aria-label`, sobra. Y si necesitas el `aria-label` para que suene bien, el problema es que el texto visible está mal, no que le falte una etiqueta.

## El prompt que encuentra los fallos de verdad

Este es el que uso, y funciona porque pide una prueba activa en vez de una inspección visual:

> "Soy estudiante de DAW y esta es una vista de mi proyecto. Haz un recorrido de accesibilidad como lo haría alguien que navega solo con teclado: empieza por el tab, dime el orden en el que llega a cada elemento y dónde se pierde. Después revisa los nombres accesibles: para cada control, ¿qué lee un lector de pantalla en voz alta? Si un nombre no es único en la página, dímelo. Al final dame una tabla con el fallo, el criterio WCAG y el cambio mínimo."

Lo de "navega solo con teclado" es lo que cambia el resultado. La IA deja de opinar sobre si está "bien hecho" y empieza a simular un recorrido, que es donde aparecen los problemas de orden de tabulación y de foco perdido. Esos son los que más se escapan y los que más penalizan.

## Tres fallos que aparecen siempre

En todos los proyectos de DAW que he revisado aparecen los mismos, y ninguno lo detecta un linter:

**El `div` que hace de botón.** El más común. Se arregla cambiando la etiqueta, no añadiendo ARIA.

**El modal que no devuelve el foco.** Al cerrarlo, el foco se va al principio del documento y la persona pierde el sitio. Es un fallo de JavaScript, no de HTML, y la IA lo encuentra rápido si le pides que lo compruebe.

**El contraste que falla solo en el estado hover.** El color base pasa el contraste y al pasar el ratón por encima baja a 2.8:1. Nadie lo ve porque solo aparece un instante, y una comprobación de color estático tampoco.

## Lo que hago yo siempre

Reviso con el teclado antes de leer una sola línea del informe. `Tab` y `Shift+Tab` desde el principio de la página, y compruebo tres cosas: que el orden tiene sentido, que siempre se ve dónde estás, y que `Escape` cierra lo que tiene que cerrarse. Es una prueba de dos minutos que encuentra más que cualquier análisis automático.

Después, si hay margen, paso el renderizador de Wave o el propio Lighthouse que trae Chrome en la pestaña de accesibilidad. Ojo con Lighthouse: solo evalúa una parte de los criterios y no cubre teclado. Sirve, no es la verdad.

Y por último, lo que más me costó aprender: la accesibilidad no es un apartado que se entrega al final, es un requisito más como el responsive. Trátalo así desde el principio, porque a mitad de camino es cuando cuesta el doble.

## Resumen

- Pide el identificador del criterio WCAG, no un "sí o no" bonito.
- Un `<button>` o un `<a>` de verdad, nunca un `div` con `role`.
- Prueba el recorrido con teclado antes de leer el informe.
- Mide el contraste de los estados, no solo del color base.
- El linter no ve el orden de tabulación. Tú sí, en dos minutos.

Es una de las pocas áreas donde delegar en la IA da un resultado netamente bueno, porque el trabajo real es el barrido y eso a una persona le lleva una hora. Lo único que tienes que hacer tú es no creerte el "está perfecto" y abrir el teclado.

*Si ya tienes clara la parte técnica, el siguiente paso es aplicarla en un proyecto real: [crear tu portfolio de desarrollador con IA](/articulos/guias/crear-portfolio-desarrollador-web-con-ia/) y [conectar el frontend con una API usando IA](/articulos/guias/conectar-frontend-api-con-ia-2026/).*

## Sigue por aquí

Lo que viene justo después es la parte de diseño visual del mismo proyecto.

- [V0 y las mejores herramientas de IA para generar interfaces](/articulos/listas/v0-vercel-ia-ui-generacion-lista-herramientas/)
- [Docker para DAW con IA](/articulos/guias/docker-para-daw-con-ia-2026/)
- [Los errores más comunes al programar con IA](/articulos/listas/errores-comunes-programando-con-ia/)
