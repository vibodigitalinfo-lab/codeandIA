---
layout: article
title: "Code review con IA: que no te suban código roto"
description: "Cómo revisar un pull request con IA sin sustos: preparar el diff, pedir hallazgos con severidad, automatizar con los revisores y saber qué no hace la IA."
category: "Guía"
date: 2026-09-24
readtime: 7
---

En DAW el primer susto de verdad no llega cuando tu código no compila, sino cuando te toca decir si **el código de otro** está listo para subirse. De repente eres tu propia disciplina: hay que mirar líneas que no has escrito, juzgar si algo va a romperse en producción y explicarlo sin picar a nadie. La tentación con la IA es la de siempre: "revísame este pull request". Y la IA, encantada, te suelta un vistazo genérico que nadie se lee. Este artículo es el método que acabé usando para que la revisión con IA sirva de verdad: qué pedir, en qué orden y, sobre todo, qué no delegar.

## Por qué "revísame el código" no funciona

Le pides a un agente que revise y te devuelve veinte puntos con la seguridad de quien acaba de mirar el código cinco minutos. El problema no es el modelo: es la **petición**. "Revísame" no lleva ni objetivo ni criterio, así que la IA rellena echando mano de lo genérico ("considera extraer esta lógica a una función", "añade un comentario"). Eso se llama ruido, y el ruido mata las revisiones porque al final nadie lee nada.

El patrón que funciona tiene tres ingredientes: un **diff pequeño**, un **contexto** y una **severidad**. Todo lo demás son señales.

## Paso 1: prepara el diff, no le pases el fichero entero

Si le pegas el fichero entero, el agente revisa cosas que no han cambiado y pierde la vista en lo que importa. Lo que quieres revisar es la **diferencia con la rama principal**, porque eso es lo que se va a romper, no todo el borrador.

```bash
git diff main...tu-compañero > /tmp/revision.txt
```

El rango de tres puntos compara tu rama con el punto en el que se separó, que es justo lo que un revisor de verdad miraría. Si no te suena, en [git con IA](/articulos/guias/git-con-ia-2026/) está el empujón para tenerlo dominado.

Y a partir de hoy, el que sube algo viene con el diff preparado. Preparar tú el diff del otro no es trabajo tuyo; lo que sí es tuyo es revisarlo con criterio.

## Paso 2: dáselo con objetivo y severidad

Ahora la petición. En vez de "revísame", algo así:

> Revisa el diff adjunto y dime solo los fallos que puedan romper el comportamiento esperado. Marca cada uno con [crítico], [mayor] o [menor], y para cada [crítico] o [mayor] explica en una línea por qué rompe. No comentes estilo.

Con ese prompt le quitas el botón de "revisión rellena" y le obligas a jerarquizar. La severidad es la pieza que te ahorra el ruido: un fallo [crítico] merece bloquear el pull request, un [mayor] merece conversación, y un [menor] es para anotar y continuar.

```text
[crítico] Lección 10: se filtra la nota suspendida igual que la aprobada.
[mayor]   No se valida que el array venga vacío antes de dividir (NaN).
[menor]   El nombre mensaje no describe que es una nota.
```

Ese formato lo entiende cualquiera, tu compañero incluido, y sube la barra de lo que significa "he revisado esto".

## Paso 3: deja que el agente revuelva y pregúntale la vuelta

La IA se queda corta diciéndote el qué de una vez. El truco está en la segunda pasada: tras el listado, pregúntale por el caso que no ha visto. "¿Qué pasaría si esta lista llega vacía?", "¿y si el precio de este plan cambia a mitad de mes?". Las buenas revisiones no son las que señalan lo que está mal delante, son las que descubren lo que se rompe en el borde.

Eso encaja con lo que ya vimos en [escribir tests con IA](/articulos/guias/escribir-tests-con-ia-2026/): los casos límite se piden, no se regalan. Igual que pides casos borde en los tests, pídelos en la revisión.

## Paso 4: automatiza lo repetitivo y reserva tu cabeza para lo importante

El siguiente nivel es que la revisión llegue **antes** de que tú la pidas, con un robot que comenta en cada pull request. Aquí hay dos caminos que ya hemos recorrido por aquí: los revisores automáticos como [CodeRabbit](/articulos/reviews/coderabbit-review-ai-code-review/) para señalar lo mecánico en el repositorio de GitHub, y los asistentes de testing como [Qodo o QA Wolf](/articulos/comparativas/qa-wolf-vs-qodo-ai-testing-estudiantes/) para que la cobertura no se olvide.

Lo que automatizas libera tu cabeza para lo que la IA no da: leer el **criterio del negocio**, mirar si la solución responde a lo que pedía la tarea y decidir si el código es mantenible dentro de un año. Eso no aparece en ningún diff.

## Qué se le escapa a la IA y tienes que mirar tú

Por muy bueno que sea el agente, hay un repertorio de cosas que casi siempre se le escapan y que son las que de verdad hunden un proyecto:

- **Lo que estaba antes.** La IA revisa el trozo que le das, pero no sabe si este trozo rompe medio mundo que no ha visto. Tú sí tienes el mapa mental del proyecto.
- **El diseño, no la forma.** Un agente detecta un bucle raro, pero no te dice que la arquitectura entera está pensada para el caso equivocado.
- **El tono de tu equipo.** La IA no sabe que en vuestro proyecto las funciones cortas son dogma o que estáis migrando a puerta cerrada. Eso son reglas que tú tienes que traducirle.

Y la trampa silenciosa: **si automatizas la revisión al 100 %, te quedas sin el hábito de leer**. La IA revisa cada vez mejor, pero el que decide si entra o no al proyecto sigues siendo tú. Leer un diff al día es el músculo que más te va a salvar en las prácticas, y no se deja delegar.

## El orden de operar en el grupo

Para cerrar, el flujo que funciona entre estudiantes sin que nadie se pique:

1. **Revisión automática** (robot) en cuanto se abre el pull request: mecánico, velocidad y primeros [críticos].
2. **Revisión con IA de tú a tú** (el prompt de arriba) para los [menores] y los casos límite.
3. **Tú lees el diff** mirando solo lo que la IA no ve: coherencia, criterio y si responde a la tarea.

Con eso, los pull requests pasan de "a ver si no se rompe" a "sabemos lo que entra". Los tres niveles no se saltan: el robot solo no basta, la IA sola no ve el negocio y tú solo te pierdes la mitad de los sustos mecánicos. Y si tu grupo no sabe por dónde empezar a trabajar en equipo, el punto de partida es [el primer proyecto publicado](/articulos/guias/primer-proyecto-web-con-ia/), donde el rival no es el código, es el miedo a tocar lo de otro.

## Sigue por aquí

- [Cómo revisar un pull request sin llorar: CodeRabbit analysis](/articulos/reviews/coderabbit-review-ai-code-review/)
- [Refactorizar código con IA sin romper nada](/articulos/guias/refactorizar-codigo-con-ia-sin-romper/)
- [Escribir tests con IA: qué funciona y qué falla](/articulos/guias/escribir-tests-con-ia-2026/)