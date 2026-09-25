---
layout: article
title: "Escribir tests con IA en 2026: qué funciona, qué falla"
description: "Guía para escribir tests con IA en 2026: pedir casos borde en vez de cobertura, revisar aserciones, y usar mutation testing gratis con Stryker y PIT."
category: "Guía"
date: 2026-09-18
readtime: 7
---

En el ciclo nadie te enseña a escribir tests bien; se dan por hechos, y la frase típica es *"ya los haré con la IA"*. Pues bien: la IA para escribir tests es una herramienta fantástica... y un poco mentirosa. Escribo esto con una semana de pruebas por medio y con datos de 2026 que me dejaron de piedra: en repositorios reales, **el 16,4% de los commits que añaden tests ya los escribe una IA** de forma detectable, y los humanos siguen escribiendo aserciones más estables que los modelos. Lo bueno es que con un método concreto, esa debilidad se convierte en tu ventaja. Te explico cómo lo hago.

## Lo primero: qué hace bien y qué hace mal la IA con los tests

Esto no es opinión, hay mediciones recientes de 2026 y me cuadran con lo que veo en clase:

- **Le sobran las ideas de casos borde.** En el último estudio que leí (y del que hablo con cautela porque hay que leerlo fino), los agentes de IA encontraban más casos límite que un humano medio: una puntuación de variedad de **0,62 frente a 0,32** del humano. Ese es su superpoder: se le ocurren el array vacío, la nota clara, el usuario sin apuntes… eso es tuyo para aprovecharlo.
- **Sus aserciones son flojas.** Las revisiones siguen encontrando en los tests generados ~11 veces más aserciones ambiguas (que vale casi cualquier cosa) que las humanas: ronda el 11,6 % frente al 1,5 % de un humano. Traducción: la IA escribe código de test que *pasa*, y un test que siempre pasa no comprueba nada.
- **Son más inestables a veces.** Los tests creados por modelos tienden a ser un pelín más frágiles (miden más cosas de las necesarias, dependen de un orden interno…). En una base de código hecha de piezas, eso muerde.

## La estrategia: pídele casos límite, no cobertura

Mi mayor error era pedir *"escribe tests con cobertura total para esta función"*. Resultado: decenas de tests que pasaban y no detectaban el bug real. Ahora lo hago al revés: **la IA me da los casos límite y yo (o un humano) decidimos cuáles importan.**

La plantilla que uso: *"Aquí tienes la función. Lista 10 casos límite que podrían romperla (valores vacíos, nulos, muy grandes, repetidos, dependientes de fecha u hora). No escribas tests: solo los casos, de más importante a menos."*

Con esa lista en la mano, elijo los 4-5 que de verdad importan para el dominio y le pido: *"escribe un test para exactamente este caso: entrada X, resultado esperado Y"*. Cada test es pequeño, explica UNA cosa y tú sabes si esa condición es la correcta. Si quieres afinar la técnica de "pensar en límites", también te sirve la mentalidad de [prompts para los módulos de DAW](/articulos/listas/8-prompts-programacion-daw-2026/).

## El arte de la aserción (o cómo que el test no mienta)

La vice de la IA no es escribir el test; es escribir la **aserción** que no comprueba nada. Tres reglas que a mí me funcionan:

1. **Una aserción con significado por test.** Si la IA te pone un test con diez `expect`, desconfía: el test entero puede estar pasando porque una aserción se cumple de casualidad. Pídele *"un test, una condición, y si hay más, un test por cada una"*.
2. **Aserción sobre el resultado, no sobre el cómo.** Que compruebe la salida/efecto final, no que "se llame la función" ni detalles internos que hoy pasan y mañana rompen.
3. **Hazlos fallar una vez antes de dejarlos.** Antes de cantar victoria, cambio un valor a propósito, corro los tests y verifico que **fallan**. Un test que no has visto fallar no te ha demostrado nada. Es el mismo instinto que en [depurar con IA](/articulos/guias/depurar-codigo-con-ia-guia-2026/): ver el rojo antes que el verde.

## El truco que me dejó enganchado: mutation testing gratis

La mejor forma de saber si tus tests sirven no es ver cuánto código cubren, sino **romper el código a propósito y ver si tus tests se dan cuenta**. Eso es el *mutation testing*, y hay versiones gratuitas perfectas para estudiantes:

- **Stryker** para JavaScript/TypeScript: muta tu código, tira tus tests y te dice qué "mutantes sobrevivieron" (es decir, qué partes no comprueba nadie).
- **PIT** para Java: el equivalente si andas con Spring y Maven como en el grado.

Lo uso así: termino la tanda de tests con la IA, corro Stryker/PIT y le pregunto al modelo *"estos mutantes han sobrevivido; ¿qué casos límite me faltan?"*. Y la IA brilla ahí: le das el resultado, te propone los tests que faltan. Es lo mejor de ambos mundos: él encuentra los huecos, tú decides si importan. Es muy del palo de [hacer que la IA refactorice sin romper](/articulos/guias/refactorizar-codigo-con-ia-sin-romper/) pero a la inversa: ahora no proteges a la IA, la IA protege tus tests.

## Integrarlo en tu rutina real

Los tests solo sirven si los ejecutas siempre. En mis proyectos de módulo, cuando un proyecto se va complicando, meto un paso en `package.json` y un `npm test` en CI (los hooks de git o un GitHub Action van perfectos). La IA me escribe ese "andamiaje" sin problema, porque es una tarea corta y bien definida: *"aquí tienes el repositorio, crea un workflow que ejecute los tests en cada push"*. Para el trabajo en grupo de fin de curso esto es oro, y se engancha con [git y el trabajo en equipo con IA](/articulos/guias/git-con-ia-2026/).

Y una cosa de cobertura: **tirar de "100% de cobertura" como meta es una trampa**; yo prefiero correr Stryker/PIT y ver que los mutantes clave mueren, que perseguir el porcentaje. La IA te puede llevar a una cobertura inflada y sin valor; los mutantes te llevan a la verdad. Si quieres comparar herramientas de testing de pago contra las gratuitas, en [QA Wolf vs Qodo](/articulos/comparativas/qa-wolf-vs-qodo-ai-testing-estudiantes/) doy mi lectura, aunque mi respuesta corta para DAW es: empieza gratis.

## Mi veredicto

**Escribir tests con IA funciona de maravilla si no le pides cobertura, sino casos límite, y si revisas sus aserciones como revisarías a un compañero flojo en el grupo.** Mi rutina: lista de casos borde con la IA, tests uno a uno con aserción única, confirmar que fallan antes de que pasen, y mutation testing con Stryker o PIT para que me diga dónde me queda débil. Con eso, la IA pasa de "tramposa que escribe tests que pasan de cualquier forma" a "detective de casos raros". Y lo mejor: los [estudios y tendencias de 2026](/articulos/listas/tendencias-ia-para-devs-2026/) apuntan a que esto solo va a mejorar, así que aprender el hábito hoy te deja en buen sitio. Si quieres que te mire una función de tu módulo y te diga qué casos límite le faltan, escríbeme a ivan@codeandia.com.