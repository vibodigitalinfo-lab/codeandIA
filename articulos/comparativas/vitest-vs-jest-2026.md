---
layout: article
title: "Jest vs Vitest en 2026: qué runner de tests elijo en DAW"
description: "Jest y Vitest ejecutan los mismos tests, pero no se parecen en nada por dentro. Comparo velocidad, ESM, TypeScript, mocks y cuándo conviene migrar en DAW."
category: "Comparativa"
date: 2026-09-10
readtime: 9
---

Llego al proyecto de prácticas con el síntoma de siempre: el test pasa en mi portátil y falla en el de mi compañero. No es su código, es la configuración. Resulta que uno usa Jest con su transformador de TypeScript y el otro Vitest, y los dos ejecutan lo mismo de dos maneras distintas. Eso me dejó con una pregunta que me ha acompañado todo el trimestre: si los tests se escriben igual, ¿por qué tengo dos configuraciones distintas para lo mismo? Lo que sigue es lo que comparé, porque en 2026 la respuesta corta es que Vitest ya es el valor por defecto y Jest sigue teniendo un hueco real.

## El problema de fondo: dos herramientas dentro de tu proyecto

Para entender por qué importa la elección, hay que ver de dónde sale la fricción. Tu proyecto tiene **dos procesos de compilación**: el que construye tu aplicación y el que ejecuta tus tests. Si el primero es Vite y el segundo es Jest, tienes dos configuraciones resolviendo lo mismo: los alias de rutas, los plugins, la resolución de módulos, las variables de entorno. Y cuando una funciona y la otra no, te pasas una tarde entera descubriendo por qué el test no encuentra el mismo fichero que la aplicación sí encuentra.

**Vitest ataca eso por dentro**: reutiliza la configuración de Vite. Mismos alias, mismos plugins, misma resolución. No es una integración añadida después; es la razón de ser de la herramienta. Añades un bloque `test` a tu `vite.config.ts` y listo.

**Jest**, en cambio, se diseñó en la era de CommonJS y Babel. Funciona bien, pero necesita un transformador aparte y su propio `moduleNameMapper` para duplicar los alias que ya tienes en Vite.

## Velocidad

Las diferencias de arranque en frío y de vigilancia salen de mediciones de terceros y no las he reproducido yo. Lo que sale consistente en los informes es que **el modo de vigilancia de Vitest se nota más rápido**, porque solo vuelve a ejecutar los tests de los ficheros que dependen del que has tocado. Jest tiende a ser más conservador y reejecuta más.

Si escribes con TDD, eso se convierte en un bucle de realimentación más corto, y se nota en horas, no en milisegundos. En integración continua, varios segundos por ejecución se suman. Pero insisto: si tu suite tarda dos segundos y no te molesta, esto no es un motivo para migrar.

## Módulos ESM: aquí ya no es velocidad, es que funciona

Este es el argumento de peso, y no es un matiz.

Jest soporta ESM de forma experimental. Necesitas el flag `--experimental-vm-modules` de Node.js, además de `extensionsToTreatAsEsm` en el `package.json` y bastante cuidado con los paquetes que solo publican ESM. El propio equipo de Jest lo reconoce: la experiencia sigue siendo más áspera.

**Vitest trata ESM como el caso normal**, sin banderas de la línea de órdenes y sin configuración extra. `import.meta`, el `await` en el nivel superior, los `import()` dinámicos y los paquetes con `"type": "module"` funcionan a la primera.

Esto importa cada año porque el ecosistema de npm se mueve en esa dirección. Cada dependencia que llega solo en ESM es una más que te va a doler con Jest y que no te va a doler con Vitest.

## TypeScript: cero configuración frente a una cadena de montajes

Con Vitest, TypeScript funciona sin configuración porque usa la transformación de esbuild que ya usa Vite. No hay transformador que mantener, ni cadena de plugins que ajustar.

Con Jest necesitas una dependencia aparte, cargar el compilador de TypeScript y sincronizar su configuración con la del proyecto. He perdido horas con esto, y lo interesante es que los errores que salen no dicen "tu transformador está mal": dicen cosas como "no se encuentra el módulo", que te mandan a otro sitio. Con [depurar con IA](/articulos/guias/depurar-codigo-con-ia-guia-2026/) se va más rápido, pero es tiempo que no gastas en la parte interesante.

## Requisitos de versión, que aquí se complica

Si te decides por Vitest, mira antes qué versión tienes:

- **Vitest 5** exige **Vite 6.4 o superior** y **Node 22.12 o superior**. Si tu proyecto tiene un Vite antiguo o un Node antiguo, actualiza antes o quédate en la rama anterior.
- **Jest 30** dejó atrás Node 14, 16, 19 y 21, usa `jsdom` 26 y sube el mínimo de TypeScript a 5.4.

Los dos han dado un salto de requisitos, pero Vitest se apoya en un ecosistema que ya tienes si usas Vite, así que el salto te sale gratis.

## Mocks: la parte que más se te va de las manos

Las dos herramientas comparten casi toda la API: `describe`, `test`, `expect`, `beforeEach`, y los espías son `vi.fn()` frente a `jest.fn()`. Con `globals: true` en la configuración de Vitest, incluso los imports desaparecen. **La migración se reduce a buscar y reemplazar `jest.` por `vi.`.**

Donde sí se pica es en los módulos:

- En Jest, la fábrica de `jest.mock` devuelve directamente la exportación por defecto. En Vitest, la fábrica **debe devolver un objeto con cada exportación explícita**, y `default` va dentro de sus llaves. Si no, se rompe de forma confusa.
- `jest.requireActual()` es síncrono; su equivalente, `vi.importActual()`, **es asíncrono**. Si te lo saltas, acabas repartiendo un objeto `Promise` en lugar del módulo real. Es el error más común en una migración.
- Por el izado de los `import`, Vitest es más estricto: no puedes referenciar variables externas dentro de la fábrica sin envolverlas con `vi.hoisted()`.
- La cobertura funciona en los dos, con el proveedor `v8` o con Istanbul. Jest usa Istanbul por defecto y Vitest tira de `v8`, que va más rápido.

## La prueba práctica antes de decidir

Lo mejor que puedes hacer, en una copia de tu proyecto y sin tocar `package.json`, es esto:

```bash
npx vitest --run --globals
```

Si la mayoría de tus tests pasan sin tocar una línea, ya sabes que la migración es barata. Si falla la mitad, mira por qué: casi seguro son `jest.mock` con lo de las exportaciones por defecto. Ese test concreto es el que te va a costar más, y conviene saberlo antes de tocar nada.

## El navegador de verdad

Vitest 4 graduó su modo de navegador a estable: en vez de simular el DOM con `jsdom` o `happy-dom`, ejecuta los tests en un Chromium de verdad. Eso elimina una categoría entera de falsos negativos, porque `jsdom` no implementa el layout real, ni `getBoundingClientRect`, ni buena parte de las APIs modernas de CSS. Si tus tests van sobre interacciones que dependen del layout, es una diferencia de fondo. Jest no tiene nada equivalente integrado.

## Mi veredicto

**Empieza con Vitest si** tu proyecto usa Vite, SvelteKit, Nuxt o Astro, usas TypeScript, o quieres escribir tests en ESM sin pelearte con las opciones de la línea de órdenes. En 2026 es el valor por defecto razonable para proyectos nuevos: Angular ya lo usa desde Angular 21 y Nuxt, SvelteKit y Astro lo integran en sus plantillas.

**Quédate con Jest si** trabajas en **React Native**, donde su ecosistema de tests está construido sobre Jest, si tienes un proyecto grande con configuración madura y cientos de tests que funcionan sin fricción, o si dependes de plugins de Jest sin equivalente en Vitest. Ahí migrar no es ganar nada, es perder tiempo.

**Y migra por dolor, no por moda.** Si tu configuración de Jest te está costando más tiempo de ingeniería del que te costaría cambiarla, entonces sí. Si va bien, déjala quieta. El que la API de Vitest sea compatible con la de Jest es precisamente lo que te permite decidir más adelante.

Antes de nada, eso sí, la pregunta previa es si los tests automáticos te sirven de algo: eso está en [escribir tests con IA](/articulos/guias/escribir-tests-con-ia-2026/). Y el orden de las herramientas importa, así que si aún no has decidido el bundler, mira primero [Vite vs Next.js vs Astro](/articulos/comparativas/vite-vs-nextjs-vs-astro-primer-proyecto-ia/). ¿Tu proyecto ya usa Jest y te va bien? Cuéntamelo a ivan@codeandia.com y te digo si migrar te conviene.

## Sigue por aquí

- [Escribir tests con IA en 2026: qué funciona, qué falla](/articulos/guias/escribir-tests-con-ia-2026/)
- [Vite vs Next.js vs Astro para tu primer proyecto con IA](/articulos/comparativas/vite-vs-nextjs-vs-astro-primer-proyecto-ia/)
- [QA Wolf vs Qodo: testing con IA para estudiantes](/articulos/comparativas/qa-wolf-vs-qodo-ai-testing-estudiantes/)
