---
layout: article
title: "Claves API y .env: lo que no debes pegar en la IA"
description: "Guía para no filtrar claves de API, contraseñas ni tokens al usar ChatGPT, Claude o Cursor: qué pegar en su lugar y qué hacer si ya has enviado el secreto."
category: "Guía"
date: 2026-10-04
readtime: 9
last_modified_at: 2026-10-04
---

He visto a más de un estudiante pegarle a ChatGPT un `application.yml` entero para preguntarle por qué le falla la conexión a la base de datos. El archivo tenía la contraseña de producción escrita dentro. En ese momento la clave dejó de ser secreta.

No es un error de novato tonto, es un error de diseño: la IA te resulta útil porque ve tu código entero, y tu código entero incluye la parte que no debes mostrarle a nadie. La buena noticia es que **la IA no necesita el valor de tu clave para ayudarte**. Necesita la forma.

## Qué se filtra exactamente

No solo son las claves de OpenAI. Cuando pegas un archivo de configuración o un fragmento de código, lo que sale hacia fuera es todo lo que tenga un valor secreto. En proyectos de DAW me he encontrado esto:

- Claves de API de OpenAI, Anthropic, Gemini o Replicate.
- Contraseñas de MySQL, PostgreSQL o MongoDB en `application.yml` o `.env`.
- Tokens de GitHub y claves de despliegue de Netlify, Vercel o Hostinger.
- El campo `secretKey` de la cookie de sesión en un proyecto con Spring Security.
- Correos de_instance y correos de administrador en pruebas de JWT firmados.

El detalle que sorprende: los tokens de GitHub son los más delicados porque duran meses. Una clave de OpenAI la puedes revocar en cuanto te avisas; un token con permisos de repositorio sigue dando acceso a tu código hasta que lo revoques tú.

## Por qué "solo lo usé para preguntar" sí importa

Puedes pensar que tu conversación es privada, y en parte lo es. Pero hay tres motivos por los que una clave pegada en un chat deja de estar a salvo:

1. **Los historiales se conservan y se pueden volver a leer.** Nada de esto es una cuenta hackeada: es simplemente que dentro de seis meses puedes buscar tu propia conversación y ahí está tu clave.
2. **Las claves se filtran por error humano.** Si copias un fragmento de un hilo para pegarlo en otro, se lleva la clave con él. Y un canal de Discord de clase no es un sitio privado.
3. **Los planes de empresa entrenan con tu contenido según el acuerdo.** Cambia la pregunta de "me lo están robando" a "no sé quién puede leerlo", que es peor.

Por eso la regla no es "no uses IA con secretos", sino "usa IA sin secretos dentro". Es una diferencia de mentalidad que se aprende una vez y ya no se olvida.

## El método: pega la forma, no el valor

La solución es tener siempre a mano un archivo de ejemplo. Es el `.env.example` que many proyectos ya usan, y su único trabajo es describir las variables sin los valores:

{% raw %}
```bash
# .env.example — esto sí puedes pegarlo en el chat
OPENAI_API_KEY=sk-aqui-va-tu-clave
DB_HOST=localhost
DB_PORT=3306
DB_NAME=mi_proyecto
DB_USER=estudiante
DB_PASSWORD=cambia-esto
JWT_SECRET=cadena-larga-aleatoria
```
{% endraw %}

Cuando preguntes, pegas eso y añades una línea explicando qué falla. El modelo ve los nombres de las variables, los puertos, los tipos de dato y la estructura, que es justo lo que necesita para diagnosticarlo. Lo único que no ve es el valor, y el valor no le sirve de nada.

Si necesitas que pruebe algo, dale un valor inventado:

{% raw %}
```bash
DB_PASSWORD=clave-falsa-para-pruebas
```
{% endraw %}

Nunca falla, y nadie puede iniciar sesión con `clave-falsa-para-pruebas`.

### Para cuando el problema está en el código y no en la configuración

A veces lo que pega el estudiante no es el archivo de configuración sino un fragmento de código que leyó de un tutorial o de un foro. Ahí el patrón es el mismo: sustituye las constantes por marcadores y deja el nombre de la constante.

{% raw %}
```java
private static final String SECRET = "pega-aqui-tu-secreto";
```
{% endraw %}

Esto no es un detalle menor de estilo. Si el mismo objeto `SecretKey` está hardcodeado en tu clase de configuración, no hace falta que pegues nada para que un escáner lo encuentre.

## La lista antes de pegar

Antes de enviar cualquier cosa al chat, comprueba estas cuatro cosas:

- ¿Hay algún `password`, `secret`, `token` o `apiKey` con un valor de más de diez caracteres? Fuera.
- ¿Aparecen cadenas largas de caracteres aleatorios? Son claves. Fuera.
- ¿He pegado la salida de un comando que imprime el entorno? Esa salida puede contener URLs firmadas. Fuera.
- ¿Estoy pegando un `.env` en lugar de un `.env.example`? Casi seguro. Fuera.

## Si ya lo has pegado: qué hacer ahora

Esto es lo que más gente se salta, y es la parte que de verdad importa. Una clave pegada en un chat no se queda invalidada sola.

1. **Revoca la clave, no la borres.** En el panel del proveedor hay una opción de revocar y regenerar. Borrar el mensaje no sirve de nada: la clave sigue viva en el historial del chat y en los registros del proveedor.
2. **Comprueba el uso antes y después.** Las APIs cobran por uso, así que un_commit con una clave filtrada se ve en el gráfico de gasto a los pocos minutos. Si ves un pico que no reconoces, alguien más la está usando.
3. **Rota también las de GitHub y del hosting.** Si el token que pegaste tenía permisos de repositorio, revócalo y crea uno nuevo con el mínimo alcance.
4. **Si el secreto estaba en un commit**, remember que `git rm` no lo borra del historial. Sigue ahí, y basta con que alguien clone el repo para recuperarlo. La rotación de la clave es la única solución; reescribir el historial solo elimina el síntoma si ya la clave está en manos ajenas.

Y un apunte de sentido común: una clave que vive en un repositorio público no la puedes proteger con un `.gitignore` si ya está en la historia. Por eso el paso 1 va primero.

## Lo que sí puedes pegar

Para que quede claro qué es aceptable:

- Código fuente que has escrito tú, sin valores dentro.
- Mensajes de error y stack traces completos, incluidos los de tu framework. Son los más útiles de todo lo que puedes enviar.
- Esquemas de base de datos, migraciones y consultas SQL.
- Archivos de configuración con los valores sustituidos por marcadores.
- Salidas de `npm list`, `pip freeze` o `mvn dependency:tree`. Son nombres de paquetes, no secretos.

Y un matiz: las capturas de tu navegador pueden llevar la cookie de sesión en la barra de direcciones. Si subes una, recórtala.

## Cómo montarlo para que no se te olvide

Esto no va de memorizar una lista, va de tener el hábito montado. Dos cosas que hago yo:

- Un archivo `.env.example` en la raíz de cada proyecto, y la regla de que **el `.env` nunca se copia**. Se escribe a mano.
- Un `script` que enumere las variables que tu proyecto necesita, para que el `.env.example` no se quede viejo. En cuatro líneas de Python sale, y te ahorra el susto de subir una variable nueva a GitHub sin darte cuenta.

Si tu proyecto llega a producción, la cosa ya no es solo el chat: revisa el artículo de [secrets y variables en GitHub Actions](/articulos/guias/github-actions-secrets-variables-entorno-guia/) para cómo dejarlo bien montado desde el principio.

## Veredicto

La regla cabe en una línea: **la IA ve tu código, no tus claves**. Cuando te pidas un archivo de configuración, pásalo con los valores cambiados por `sk-aqui-va-tu-clave`, y el diagnóstico va a ser igual de bueno.

Si ya has pegado algo, no te castigues: revoca, comprueba el gasto y sigue. Lo que no sirve de nada es dejar la clave ahí esperando que nadie la lea, porque eso ya no depende de ti.

Para cerrar el círculo, dos lecturas que van justo al revés: [prompt injection y seguridad en tus apps con IA](/articulos/guias/prompt-injection-seguridad-apps-ia-2026/) trata de proteger tu aplicación de quien la usa, y [programar con IA sin volverte dependiente](/articulos/guias/aprender-programar-con-ia-sin-volverse-dependiente/) trata de que el modelo no termine decidiendo por ti. Esta va de la tercera persona en la habitación: la IA.

## Sigue por aquí

- [Secrets y variables en GitHub Actions sin morir en el intento](/articulos/guias/github-actions-secrets-variables-entorno-guia/)
- [Prompt injection 2026: qué es y cómo proteger tu app con IA](/articulos/guias/prompt-injection-seguridad-apps-ia-2026/)
- [AGENTS.md: la guía de instrucciones para IA en tus proyectos](/articulos/guias/agents-md-guia-2026/)