---
layout: article
title: "Biome vs ESLint + Prettier en 2026: qué pongo en mis prácticas"
description: "Biome promete sustituir a ESLint y Prettier con un único binario en Rust. Comparo velocidad, cobertura de reglas, migración y qué te conviene."
category: "Comparativa"
date: 2026-09-27
readtime: 8
---

Tengo una carpeta con la configuración de las prácticas que cargo desde hace meses, con dos ficheros que se pelean entre ellos y un paquete cuyo único propósito es decirles que no se peleen. Es el kit de siempre: `eslint.config.js`, `.prettierrc`, `eslint-config-prettier` y, si usas TypeScript, un transformador aparte. Nada de eso está mal. Es simplemente mucho ruido para lo que hace. Biome es el que viene a prometer que todo eso cabe en un `biome.json` y un binario, y como en las últimas prácticas he estado comparando a ver si el cambio merece la pena, esta es mi conclusión honesta.

## Qué hace cada uno, de verdad

**ESLint** analiza tu código buscando errores y patrones viejos. Se inventó en 2013, cuando el mundo JavaScript usaba CommonJS y Babel. Funciona, sigue funcionando, y tiene el ecosistema de plugins más grande que existe.

**Prettier** no analiza: formatea. Le da a tu código un aspecto idéntico en todo el proyecto, con una decisión por fichero que tú no discutes.

**Biome** es un binario escrito en Rust que hace las dos cosas más una tercera que nadie te había dado: ordenar las importaciones. Todo en una pasada, en paralelo, con un solo fichero de configuración.

```bash
npm install --save-dev @biomejs/biome
npx biome check --write
```

Y se acabó. Eso reemplaza a cuatro dependencias en un proyecto de React o TypeScript normal.

## Criterio 1: la velocidad, que es donde se gana sin discusión

Aquí no hay debate. Biome formatea, analiza y ordena importaciones en paralelo, en un proceso, con un solo arranque. ESLint, por su parte, es mono-hilo por defecto y encima paga el arranque de Node.js y la carga de su cadena de plugins.

Medidas independientes que he visto de terceros, en un proyecto de unos 500 ficheros, dan entre **10 y 15 veces menos tiempo** con Biome. Las cifras que publica Biome en su web son bastante más altas, pero esas son de su propio banco de pruebas, así que las miro con desconfianza. Lo que sí puedo decirte con datos propios: la diferencia se nota en cuanto activas el guardado automático en el editor, porque el formateo al guardar deja de ser un tirón de un segundo.

Antes de que te lo vendas: **si tu configuración actual va bien, no vas a notar nada**. La velocidad importa en integración continua, en un *pre-commit* o si escribes con el modo de vigilancia activado todo el rato. Si nunca has sentido la lentitud, la velocidad no es un argumento para migrar.

## Criterio 2: la cobertura de reglas, que es donde la cosa se complica

Aquí sí que hay que ser adulto. Biome cubre bien el núcleo: equivalentes de `eslint:recommended`, un montón de reglas de TypeScript, reglas de React, orden de importaciones y accesibilidad básica. En un proyecto típico de React con TypeScript, la cobertura ronda el 80-85 % de lo que te daría un ESLint bien configurado.

El 15-20 % que falta no es tonto:

- **No hay equivalente a `import/no-cycle`**, que es la regla que detecta las dependencias circulares que luego se manifiestan como fallos en tiempo de ejecución que no sabes de dónde salen.
- **No hay reglas de Testing Library ni de Jest.** Te quedas sin los avisos sobre `await` olvidado en una aserción o sobre mal uso de `screen.queryBy*`.
- **No hay `eslint-plugin-security`.** Si trabajas en un repositorio con reglas de seguridad propias, ese es un punto de bloqueo claro.
- **La accesibilidad es más básica** que la de `eslint-plugin-jsx-a11y`. Si tu web es pública, eso se nota.
- **No analiza SCSS** (está en la hoja de ruta) ni tiene analizador propio para ficheros `.vue`, `.svelte` o `.mdx`.

Y las reglas con información de tipos existen desde Biome 2.0, pero su inferencia de tipos es propia y **no llega a la paridad total** con `no-floating-promises` ni `no-misused-promises` de `typescript-eslint`. Si tu proyecto es muy asíncrono y esas reglas son innegociables, ahí sigues necesitando ESLint.

También hay un detalle de nomenclatura: ESLint escribe los nombres de regla en `kebab-case` y Biome en `camelCase`, y a veces le ha puesto un nombre distinto para la misma idea. Al buscar la regla equivalente por el nombre no la encuentras, y te toca buscarla por la intención.

## Criterio 3: la migración, que es donde se cae el entusiasmo

Aquí hay buenas noticias y una advertencia. Biome trae dos comandos que hacen el 90 % del trabajo:

```bash
npx biome migrate eslint --write
npx biome migrate prettier --write
```

Traducen tu configuración existente y te generan el `biome.json`. Con `--dry-run` ves el resultado antes de tocar nada.

Las buenas noticias: el formateador de Biome está diseñado para coincidir con Prettier, así que el formato final se parece muchísimo. Y `migrate eslint` mapea bastante bien las reglas comunes (`no-unused-vars` a `noUnusedVariables`, `eqeqeq` a `noDoubleEquals` y cosas así).

La advertencia: **se cae lo que no tiene equivalente**, en silencio, y no soporta configuración en YAML. Además hay una trampa de las gordas: **Biome usa tabuladores por defecto**, mientras que Prettier usa espacios. Si tu `.prettierrc` no tenía `useTabs: false` explícito, la migración te puede dejar el proyecto entero con tabs y un diff gigante. Ábrete el `biome.json` después de migrar y comprueba la sangría antes de hacer el *commit*.

También, al migrar se desactiva la opción `recommended` de Biome hasta que tú la vuelvas a activar. No es un fallo, pero te deja el linter más flojo de lo que creías si no te das cuenta.

Lo que nadie te dice: al cambiar de una pila a otra salen avisos nuevos que tu configuración anterior no detectaba. En un proyecto real de 80 000 líneas, la primera pasada de `biome check` puede soltar unos cientos de avisos nuevos, casi todos auto-corregibles, y auto-corregibles quiere decir que tienes que mirar el diff antes de aceptarlo. Cuenta con una tarde, no con diez minutos.

## Mi veredicto, por caso

**Empieza con Biome si** estás en un proyecto nuevo, usas React o TypeScript sin depender de plugins raros, y quieres una configuración que se entienda. Ahí la decisión es fácil y no duele.

**Quédate con ESLint + Prettier si** tu base de código ya funciona, dependes de plugins concretos, tienes reglas propias escritas a medida, o trabajas con Vue, Svelte o Astro con reglas de análisis específicas. La diferencia de velocidad no justifica un sprint de migración si no te está doliendo hoy.

**Y considera el término medio**, que es lo que acabé haciendo: dejar Biome solo para formatear, ordenar importaciones y el grueso de las reglas correctas, y conservar un ESLint reducido a esas pocas reglas de plugin que Biome no expresa. Es menos limpio que el todo o nada, pero es la opción pragmática y la que de verdad recommendaría a un compañero de clase.

La decisión real no es técnica, es de momento: **migra cuando el mantenimiento de tu configuración te esté costando más tiempo que la migración, no porque una gráfica de barras diga que hay una diferencia de diez veces.** Si quieres una guía para dejar Biome configurado en tu editor, está la de [configurar VS Code para IA](/articulos/listas/configuracion-vscode-ia-2026/). Si te interesa el otro lado del formateo, mira lo que cuesta mantener cuarenta clases de [Tailwind dentro de un `div`](/articulos/guias/tailwind-con-ia-guia-2026/). ¿Tu linter actual ya te está haciendo perder tiempo? Cuéntamelo a ivan@codeandia.com y te digo si migrar te va a salir gratis.

## Sigue por aquí

- [Configuración de VS Code para IA en 2026: lo que uso de verdad](/articulos/listas/configuracion-vscode-ia-2026/)
- [TypeScript para estudiantes: los 6 tipos que te ahorran depurar con IA](/articulos/guias/typescript-para-estudiantes-con-ia/)
- [GitHub Actions para DAW: automatiza tests y despliegues](/articulos/guias/github-actions-estudiantes-daw/)
