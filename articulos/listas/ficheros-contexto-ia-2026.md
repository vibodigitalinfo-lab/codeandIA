---
layout: article
title: "5 ficheros de contexto que tu IA lee antes que tú"
description: "AGENTS.md, .cursorrules, .editorconfig, .gitignore y tus dotfiles: los ficheros con los que tu agente sabe qué hacer y por qué deberías repasarlos hoy."
category: "Lista"
date: 2026-09-13
readtime: 7
---

Cuando trabajas con un agente de estos que corren en tu repositorio, hay un momento que pasa desapercibido: nada más arrancar, la IA va a mirar una serie de ficheros de configuración para decidir cómo comportarse. Tú nunca los miras porque son invisibles, pero ella los lee como un contrato. Y lo que hay dentro de ellos, o lo que falta, decide si el agente respeta tus reglas o si hace lo que le da la gana con el proyecto. Esta es la lista de los cinco que más me han salvado, en el orden en que los revisaría hoy un estudiante de DAW que quiere que su IA trabaje con criterio.

## 1. AGENTS.md, las reglas de la casa

El primero y el más rentable de todos. Un fichero `AGENTS.md` en la raíz del proyecto le dice a la IA, en texto plano, cómo se trabaja aquí: qué framework se usa, cómo se llaman los commits, qué convenciones hay que respetar y qué partes no se tocan sin preguntar.

```markdown
# Reglas del proyecto

- API Spring Boot con gradle, Java 21.
- Los endpoints devuelven JSON con codigo, mensaje y datos.
- Formato de los commits: tipo(alcance): verbo.
- No tocar /src/main/resources sin preguntar.
```

No es otra forma de llamar a un README: distintos agentes de terminal (los que te contaba en [Codex CLI](/articulos/reviews/codex-cli-openai-review-2026/)) leen este fichero antes de tocar nada, y en la práctica significa que le presentas las normas al nuevo empleado antes de que empiece. La guía completa de qué meter está en [AGENTS.md para IA](/articulos/guias/agents-md-guia-2026/), y si vienes de las reglas por carpeta, [la configuración de Cursor con ficheros .mdc](/articulos/guias/cursor-rules-configuracion-mdc-guia/) es su prima hermana.

## 2. .cursorrules y sus herederos

Antes de que existiera AGENTS.md como estándar, los editores con IA usaban un fichero `.cursorrules` en la raíz para lo mismo: pinzas de estilo para la herramienta concretas y sin moraleja. Sigue funcionando en Cursor y en la mayoría de los derivados.

Mi consejo es que no dupliques: si ya tienes un AGENTS.md en la raíz, no reescribas las reglas en un `.cursorrules` que las contradiga. La IA junta ambas fuentes de contexto y, si se llevan mal, el que decide eres tú, pero sin enterarte. Una sola fuente de verdad por regla, y los agentes que leen la tuya la encontrarán.

## 3. .editorconfig, la paz entre editores

Cuando tres personas editan con tres editores distintos, el `prettierrc` y el `eslint.config` se pelean por la sangría. El `.editorconfig` es el árbitro que va por delante de todos: define sangrías, fin de línea y codificación para el fichero que se toca, y todos los editores serios lo respetan sin pedirte que configures nada.

```ini
root = true

[*]
charset = utf-8
indent_style = space
indent_size = 2
```

La IA, cuando edita, lee este fichero igual que tu editor. Si está, se acabaron los diffs de dos mil líneas porque cambió la sangría a mitad del proyecto. Lo que parecen minucias de higiene son las que evitan que una revisión se convierta en una discusión de tabuladores, y de eso ya hablamos en [la configuración de VS Code para IA](/articulos/listas/configuracion-vscode-ia-2026/).

## 4. .gitignore, lo que no forma parte del proyecto

El `.gitignore` es el fichero más hablador de la lista, aunque no lo parezca. Le dice a la IA qué cosas **no** intentar: las carpetas de dependencias, los ficheros generados, las claves que no deben entrar en el repositorio. Y lo importante es lo contrario de lo que suena: un buen `.gitignore` es la garantía de que la IA no intente editar `node_modules` ni se proponga hacer un commit de las bases de datos de desarrollo.

```gitignore
node_modules/
.env
target/
dist/
```

Sin él, un agente con buen corazón intenta "organizar" la carpeta y acaba tocando lo que no debe. Con él, se queda en el perímetro. Si del `.gitignore` viene el susto de las claves, tienes la parte de secretos en [GitHub Actions con variables de entorno](/articulos/guias/github-actions-secrets-variables-entorno-guia/) y las decisiones de despliegue en [Docker para DAW](/articulos/guias/docker-para-daw-con-ia-2026/).

## 5. El paquete de dependencias y sus scripts

El último de la lista es un fichero que no parece de contexto: el `package.json` (o el `pom.xml` si vives en Java). Es la tabla de mandos del proyecto para la IA: qué dependencias hay, qué versiones se mueven y, sobre todo, **los scripts** (`npm run build`, `npm test`, `gradle test`) que el agente va a querer ejecutar para comprobarlo todo.

Si esos scripts están limpios y con nombre claro, el agente puede construir y probar solo, y eso es lo que convierte una ayuda a medias en un asistente que se asegura de no romperte la práctica. Si los scripts son un puzle sin documentar, la IA inventa el comando y tú pagas la factura. Dale un nexo con nombre a tus tareas y el contexto se hace solo.

## La regla de oro

Todo fichero de configuración que la IA pueda leer es contexto, y el contexto malo es peor que el que falta: un `.editorconfig` que contradice al formateador, un AGENTS.md desactualizado con reglas que ya no son, un `.cursorrules` huérfano del proyecto anterior. Antes de darle a la IA más contexto, revisa el que ya tiene: si contradice a la realidad, el agente no lo va a adivinar.

Y si no sabes qué lecturas hace tu editor primero, la respuesta corta es la misma para todos: **el orden de prioridad suele ir de lo más específico a lo más general**, así que empieza por el fichero de la carpeta donde estés y sube hacia la raíz. Eso es lo que hace un profesional cuando hereda un proyecto: no pregunta qué pinta tiene el código, mira qué reglas van a gobernarlo. Que la IA te eche un cable con [MCP](/articulos/guias/mcp-para-principiantes-guia-2026/) o con el resto de la lista de [recursos gratuitos](/articulos/listas/recursos-gratuitos-aprender-programacion-con-ia/) no cambia ese primer paso: cuanto mejor le digas cómo se trabaja aquí, mejor te va a trabajar.

## Sigue por aquí

- [AGENTS.md: la guía de instrucciones para IA en tus proyectos](/articulos/guias/agents-md-guia-2026/)
- [Configuración de VS Code para IA en 2026](/articulos/listas/configuracion-vscode-ia-2026/)
- [Codex CLI de OpenAI en 2026, el agente que uso en la terminal](/articulos/reviews/codex-cli-openai-review-2026/)