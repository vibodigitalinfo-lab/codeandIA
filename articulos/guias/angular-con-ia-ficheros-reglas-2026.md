---
layout: article
title: "Angular con IA: los ficheros de reglas que te da el framework"
description: "Angular 22 trae un fichero de reglas para cada editor con IA, llms.txt y un servidor MCP. Cómo configurarlos para que el copiloto no te dé código de 2019."
category: "Guía"
date: 2026-10-01
last_modified_at: 2026-10-01
readtime: 9
---

El problema de Angular con la IA no es que el modelo sea tonto. Es que el framework **se movió** y el modelo se quedó en su sitio. Cada vez que le pido un componente, me devuelve `standalone: true`, inyección por constructor, `*ngIf` y un `ChangeDetectionStrategy.OnPush` puesto a mano. Todo eso estaba bien en 2019. En Angular 22 es exactamente lo contrario de lo que hay que escribir.

Lo bueno es que el equipo de Angular ya no lo deja a tu suerte: publica un fichero de reglas para cada editor con IA, un prompt de buenas prácticas actualizado, dos versiones de `llms.txt` y un servidor MCP en la CLI. Ninguna de las herramientas de esta guía es un invento mío.

## Qué cambió de verdad (octubre de 2026)

Antes de configurar nada, esto es lo que tienes que saber. La línea **v22 es la activa** y es la que te genera `ng new` hoy:

| Cambio | Desde cuándo | Qué implica para ti |
|---|---|---|
| `OnPush` como estrategia por defecto | v22 | **No lo pongas a mano**, ya está |
| Componentes standalone por defecto | v20 | **No escribas `standalone: true`** |
| Sin `zone.js` en proyectos nuevos | v21 | Zoneless es el punto de partida |
| Signal Forms (`@angular/forms/signals`) estables | v22 | El sustituto de los formularios reactivos |
| `resource()`, `rxResource()`, `httpResource()` estables | v22 | Menos tuberías de RxJS |
| `@Service` para servicios singleton | v22 | Ya no hace falta `@Injectable({providedIn: 'root'})` |
| Vitest como runner por defecto | v21 | Karma y Jest siguen, pero Vitest es el camino |
| Servidor MCP en la CLI | v22 | **Experimental**, de momento |

Y un aviso de soporte que te va a doler si te quedas quieto: **v17 a v19 ya no tienen soporte**, y la rama 20 entra en el final de soporte el 28 de noviembre de 2026. Entre junio y agosto de 2026 se publicaron varios avisos de seguridad que afectaban a la rama 21. Si tu práctica usa v20 o v21, actualizar no es opcional.

## La solución 1: el fichero de reglas oficial de tu editor

Esto es lo primero que montaría. Cada asistente lee un fichero de contexto distinto, y Angular publica el suyo para todos:

| Editor con IA | Fichero que debes crear | Dónde va |
|---|---|---|
| Cursor | `cursorrules.md` | raíz del proyecto |
| VS Code (Copilot) | `.instructions.md` | raíz del proyecto |
| JetBrains IDEs | `AGENTS.md` | raíz del proyecto |
| Gemini / Antigravity | `GEMINI.md` | raíz del proyecto |
| Windsurf | `guidelines.md` | raíz del proyecto |

La diferencia con lo que suele decirte la gente es que **no tienes que escribirlo tú**: te lo descargas de la sección *Build with AI* de la documentación y lo copias. El equipo de Angular lo mantiene actualizado con cada versión, así que deja de ser tu problema.

Si solo vas a hacer una cosa hoy: **crea `AGENTS.md`**. Es el estándar que, además, ya te expliqué en detalle en [mi guía de AGENTS.md](/articulos/guias/agents-md-guia-2026/), y JetBrains lo lee de forma nativa.

## La solución 2: el prompt de buenas prácticas del propio equipo

El prompt oficial que publica Angular es una lista de instrucciones concretas, y hay partes que contradicen lo que la mayoría de tutoriales te enseñan. Estas son las que más te van a cambiar el código que te escupe:

- **No uses `@HostBinding` ni `@HostListener`**: pon los bindings dentro del objeto `host` del decorador.
- **No uses `ngClass` ni `ngStyle`**: usa los bindings `class` y `style`.
- **No importes `CommonModule`**: importa solo las directiva que la plantilla usa, como `AsyncPipe` o `DatePipe`.
- **No asumas globales como `new Date()`** en la plantilla.
- **No uses `mutate` en signals**: usa `update` o `set`.
- **Usa `NgOptimizedImage`** para todas las imágenes estáticas.

Y dos que te ahorran más de lo que parecen: `model()` para propiedades de doble binding en vez de emparejar `input()` con `output()`, y `linkedSignal()` cuando el estado derivado depende de varias fuentes reactivas que tienen que quedar sincronizadas.

El truco para conseguir todo esto es que funciona como instrucción de sistema de tu editor, así que el modelo deja de inventarse convenciones.

## La solución 3: llms.txt

Angular publica dos ficheros para que los LLM entiendan el framework: `llms.txt` (un índice de ficheros y recursos clave) y `llms-full.txt` (un conjunto compilado y mucho más extenso de cómo funciona Angular).

No es un estándar cerrado todavía, pero es la vía más barata: si tu herramienta admite adjuntar ficheros de contexto, esto ya te da el manual del framework en el contexto sin que tengas que pegarlo a mano en el chat.

## La solución 4: el servidor MCP de la CLI

Angular incluye un servidor **Model Context Protocol** en su CLI, y la propia documentación lo marca como experimental. Ojo con eso: úsalo para trastear, no para depender de él en una entrega.

Cuando lo montas, tu asistente gana tres herramientas:

- `get_best_practices`: le pregunta al framework cuál es la forma correcta de hacer algo, con la versión de Angular que tienes instalada.
- `ai_tutor`: un tutor con el contexto del framework.
- `find_examples`: busca ejemplos reales de la API.

El valor real no es la herramienta en sí: es que **el asistente deja de responder con lo que recuerda de 2023 y empieza a preguntar**. Si ya lees sobre MCP en el blog, esta es la parte donde se ve por qué importa.

## Los seis errores que verás en el código de la IA

Para que puedas reconocerlos en un pull request sin buscar la guía, estos son los que más se repiten:

1. **`standalone: true`** en cada componente. Ya es el defecto desde v20; sobra.
2. **`ChangeDetectionStrategy.OnPush`** explícito. En v22 es el defecto, así que ponerlo es ruido.
3. **`*ngIf` y `*ngFor`** en lugar de `@if` y `@for`, que son el flujo de control nativo.
4. **Inyección por constructor** en vez de la función `inject()`.
5. **Formularios reactivos clásicos** cuando lo indicado son Signal Forms.
6. **`@Injectable({providedIn: 'root'})`** en un servicio singleton, cuando v22 ya tiene `@Service` para eso.

## Angular en el temario de DAW

## Cómo montarlo en tu práctica, en cuatro pasos

Lo de arriba es la teoría. Esto es lo que hago yo en un proyecto de clase:

```markdown
<!-- AGENTS.md, en la raiz del repo Angular -->
App Angular 22, standalone y zoneless. Sin zone.js en polyfills.
API en Spring Boot aparte, en /api.

## Comandos
- Instalar: npm ci
- Arrancar en dev: npm start
- Tests: npm test
- Compilar: npm run build

## Estilo
- Componentes standalone con selector, una responsabilidad por componente.
- Signals para el estado local y computed() para lo derivado. Nada de setTimeout.
- Plantillas con @if y @for, nunca *ngIf ni *ngFor.
- Formularios con Signal Forms, no con los reactivos antiguos.

## No hacer
- No pongas standalone: true ni ChangeDetectionStrategy.OnPush: ya son el defecto.
- No refactorices componentes que no toquen el cambio.
- No borres un test para que pase: arréglalo.
```

1. **Descarga** el fichero de reglas de tu editor desde la sección *Build with AI* y cópialo en la raíz como punto de partida.
2. **Fusiona** con esas reglas tuyas: los comandos, tu estilo y la sección "No hacer", que es la que más efecto tiene.
3. **Prueba**: pide un componente con formulario y compara el resultado con lo que te daba antes.
4. **Actualiza** cuando cambies de versión de Angular. Si el fichero se queda viejo, es peor que no tener ninguno.

Para el resto del temario tienes artículos específicos:

- [React vs Vue con IA para tu proyecto de DAW](/articulos/comparativas/react-vs-vue-con-ia-daw-2026/)
- [TypeScript para estudiantes: los 6 tipos que te ahorran depurar](/articulos/guias/typescript-para-estudiantes-con-ia/)
- [Conectar tu frontend al API con IA](/articulos/guias/conectar-frontend-api-con-ia-2026/)

## Veredicto

Angular con IA no es un caso especial: es el ejemplo perfecto de por qué un framework moderno publica sus propias reglas para IA. Mientras tu asistente iba con lo que aprendió antes de tu framework, vas a recibir código heredado. Con el fichero de reglas en la raíz, dejas de escribir Angular de 2019.

Empieza por lo gratuito: descarga el fichero de reglas de tu editor, ponlo en la raíz y pide un componente. Compara. Si la diferencia se nota, ya tienes la respuesta.

## Sigue por aquí

- [AGENTS.md: la guía de instrucciones para IA en tus proyectos](/articulos/guias/agents-md-guia-2026/)
- [MCP (Model Context Protocol): qué es y por qué deberías conocerlo](/articulos/guias/mcp-model-context-protocol-guia-desarrolladores/)
- [TypeScript para estudiantes: los 6 tipos que te ahorran depurar](/articulos/guias/typescript-para-estudiantes-con-ia/)