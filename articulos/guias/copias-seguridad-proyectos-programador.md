---
layout: article
title: "Copias de seguridad de tus proyectos: no pierdas las prácticas"
description: "Cómo hacer copias de seguridad de tus proyectos de DAW sin depender de la suerte: Git con GitHub, la nube con cabeza y una copia local, con la rutina que uso."
category: "Guía"
date: 2026-10-01
readtime: 8
last_modified_at: 2026-10-01
---

He visto entregas rehacerse la noche antes de la fecha límite por un portátil que no arranca, y carpetas de proyecto desaparecer al sincronizar en la nube. No es mala suerte: es que nadie monta las copias de seguridad hasta que pierde algo, y para entonces el proyecto ya incluye tres semanas que no vas a recordar cómo se hicieron.

Tener copias no es de gente paranoica ni de informáticos veteranos. Para un estudiante es aún más importante, porque tu proyecto del trimestre es tu nota y no hay una segunda versión guardada en ninguna parte. Esto es el sistema que uso, en el orden en que importa.

## La regla que basta: 3 copias, 2 sitios, 1 fuera

La norma clásica de copias de seguridad se resume en 3-2-1: **tres copias** de tus datos, en **dos medios distintos**, y al menos **una fuera de tu casa**. Suena a empresa, y aplica igual a tus prácticas:

1. **Tu ordenador** (la copia de trabajo, la que editas).
2. **GitHub** (una copia remota, versionada, en otro sitio).
3. **Un disco externo o un ZIP** (una copia que no dependa de internet ni de ninguna cuenta).

Si se te cae cualquiera de las tres, las otras dos te salvan. Con eso ya estás por delante del 90 % de la clase.

## Git y GitHub: tu copia principal

Git no es solo para trabajar en equipo: es la mejor herramienta de copias que tienes. Cada commit es una foto de tu proyecto a la que puedes volver.

- **Haz commit a menudo, no cada día.** Un commit por "cosa que funciona" (añadir el formulario, corregir el login) te deja un historial útil. Un commit por semana es una copia mala y un historial inservible.
- **Sube con `push` antes de cerrar el portátil.** El commit es local; hasta que no haces `push`, tu proyecto solo existe en tu ordenador.
- **Los repositorios privados son gratis.** No haya excusa para no subir el proyecto por miedo a que te lo copien. En GitHub puedes tener repos privados sin pagar.
- **Usa `.gitignore` desde el primer día.** No subas `node_modules/`, `target/`, `venv/`, `.env` ni ficheros temporales del editor. Una carpeta de dependencias infla el repo y no aporta nada.

Un truco que ahorra disgustos: haz una rama antes de tocar algo que funciona. `git switch -c probando-login` cuesta un segundo, y si la lías, borras la rama y sigues con la principal intacta.

## Git no es Copilot

Un apunte que sorprende a mucha gente: **Git no es una herramienta de IA y no lo va a ser**. No te genera código ni te corrige; solo guarda tu historia. Tiene una curva de aprendizaje y hay comandos que dan miedo (`rebase`, `reset --hard`), pero aquí solo necesitas cuatro: `add`, `commit`, `push` y `pull`. Con esos y una rama de pruebas vives tranquilo el curso entero.

## La nube, con cabeza

Guardar la carpeta del proyecto en OneDrive, Google Drive o Dropbox parece la copia más fácil, y es donde más gente se ha cargado un proyecto. El problema es la carpeta `.git` y las carpetas de dependencias: si la nube las sincroniza a la vez que tu editor las toca, aparecen conflictos, ficheros duplicados como `proyecto (1).java` y repositorios corruptos que dejan de reconocer tu historial.

Si quieres usar la nube, sigue estas dos reglas:

- **Nunca sincronices la carpeta del proyecto con `.git` dentro.** Si lo haces, pon `.git` en la lista de exclusiones de la carpeta.
- **Usa la nube para cosas que no cambian a todas horas.** Apuntes, PDFs, capturas, informes sí; el código en vivo, no.

Para el código, la copia en la nube que funciona es GitHub, no el disco sincronizado.

## Una copia local de verdad

El último eslabón es el que todo el mundo se salta: una copia que no dependa de internet ni de una cuenta de nadie. Dos formas simples:

- **Un disco externo o un pendrive grande.** Copa la carpeta entera del proyecto una vez al mes, o al cerrar cada hito. Se tarda un minuto.
- **Un ZIP por hito.** Antes de entregar una práctica, comprímela con la fecha en el nombre: `proyecto-daw-2026-10-09.zip`. Ocupa poquísimo y es una foto que no se corrompe sola.

Lo importante no es el método, es que **no sea el mismo disco que tu portátil**. Una copia en la misma máquina no es una copia: es un segundo sitio donde perderlo todo a la vez.

## Lo que no debe ir en una copia en la nube

Hay una excepción que vale la pena repetir: los secretos. Nunca subas un `.env` con claves, ni un token de GitHub, ni contraseñas de base de datos, ni a un repo privado. Si el día de mañana ese repo se hace público o se filtra la cuenta, la clave deja de ser secreta.

La regla es la misma que cuando le pides ayuda a la IA: **sube la forma, no el valor**. Un `.env.example` con los nombres de las variables es lo que va al repo; el `.env` con las claves se queda en tu máquina y se añade al `.gitignore`. Lo tienes desarrollado en [claves API y `.env`: lo que no debes pegar en la IA](/articulos/guias/no-pegues-claves-api-en-la-ia/).

## Cómo recuperar cuando ya la has liado

La buena noticia es que Git está diseñado para deshacer. Estos son los rescates que más se usan:

- **Borraste un fichero sin querer:** `git restore ruta/del/fichero` te lo devuelve desde el último commit.
- **Un commit rompió algo y quieres deshacerlo sin borrar la historia:** `git revert <commit>` crea un commit nuevo que deshace el anterior. Es la forma segura de "deshacer" en un proyecto que ya has subido.
- **Hiciste un `reset --hard` y crees que perdiste commits:** `git reflog` lista todo lo que ha pasado por tu rama, incluidos commits que ya no ves. Casi siempre están ahí y los puedes recuperar.
- **El repo se ha vuelto raro (commits fantasma, conflictos sin sentido):** muchas veces es el disco sincronizado metiendo mano en `.git`. Restaura desde GitHub con `git clone` en una carpeta nueva y quédate con esa.

## La rutina mínima

Todo esto cabe en cinco costumbres que no tardan nada:

1. `commit` cuando algo funciona, con un mensaje que entiendas dentro de un mes.
2. `push` antes de cerrar el portátil.
3. Una rama para probar cosas que puedan romper lo que ya va.
4. Un ZIP con fecha en cada entrega.
5. Una vez al mes, copia la carpeta entera a un disco externo.

Y una que casi nadie hace y es la que de verdad valida el sistema: **prueba una restauración**. Alguna vez, borra un fichero a propósito y recupéralo. Un sistema de copias que nunca has probado es una creencia, no una copia.

## Sigue por aquí

- [Claves API y .env: lo que no debes pegar en la IA](/articulos/guias/no-pegues-claves-api-en-la-ia/)
- [Secrets y variables en GitHub Actions sin morir en el intento](/articulos/guias/github-actions-secrets-variables-entorno-guia/)
- [Documentar tu proyecto con IA: README y código que se entienden](/articulos/guias/documentar-proyecto-con-ia-2026/)
