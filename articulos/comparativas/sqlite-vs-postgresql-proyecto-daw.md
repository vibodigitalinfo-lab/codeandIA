---
layout: article
title: "SQLite vs PostgreSQL para tu proyecto de DAW"
description: "SQLite o PostgreSQL para un proyecto de DAW: cuándo aguanta SQLite, cuándo peta y cómo hacer la migración con IA sin perder los datos que ya tenías."
category: "Comparativa"
date: 2026-09-24
readtime: 10
---

Esta decisión se toma sola en casi todos los proyectos de DAW, y casi siempre por inercia: el profesor dijo SQLite, o el tutorial que seguiste usaba SQLite, así que ahí se queda. Y para un proyecto de primero puede ser perfecto. El problema aparece en marzo, cuando tres personas escriben a la vez y tu archivo se bloquea.

Lo que sigue es la comparación que hago cuando alguien me pregunta qué usar, con los límites reales: dónde se rompe SQLite, qué te cuesta cambiarla, y por qué la respuesta a veces es "las dos cosas" (y eso no es una evasiva).

## La diferencia que lo explica todo

No es "una es mejor que otra". Es que los dos resuelven problemas distintos y, durante un tiempo, el problema de SQLite es invisible.

SQLite guarda **todo en un archivo**. No hay servidor, no hay proceso corriendo, no hay que instalar nada. Abres el archivo y ya tienes la base de datos. Eso es BPBD en tu portátil, en una práctica de clase y en un proyecto que aún no tiene usuarios.

PostgreSQL es un **servicio**. Tienes que arrancarlo, escribir un usuario, una contraseña y un puerto. Ese coste de arranque es real, pero es exactamente lo que te paga cuando necesitas que varias cosas pasen a la vez.

La frase corta: SQLite es un archivo que habla SQL, PostgreSQL es un programa que habla SQL. Elegir es elegir qué problema quieres tener.

## Dónde aguanta SQLite (de verdad)

Esto no es marketing de PostgreSQL, SQLite aguanta más de lo que la gente cree:

- **Proyectos personales o en solitario.** Sin discusión.
- **Prácticas y trabajos de clase.** Donde el professor va a mirar el código, no a auditar la concurrencia.
- **Apps de escritorio o scripts.** Una herramienta local que abre un archivo es el caso de uso nativo.
- **Unit tests y pruebas automatizadas.** En memoria (`:memory:`) cada test arranca limpio y va rapidísimo. Para esto es mejor que PostgreSQL, y no por poco.
- **Prototipos que van a durar tres semanas.** El coste de montar un servidor no se amortiza.

Hasta unos cientos de miles de registros, con lectura mayoritaria, SQLite va sobrado. El límite no es el volumen, es quién escribe a la vez.

## Dónde peta SQLite

**Escrituras simultáneas.** Este es el punto de no retorno y hay que entenderlo bien. SQLite serializa las escrituras: dos operaciones de escritura no ocurren a la vez, se hacen por turnos. Si tienes varios usuarios guardando, se produces un cuello de botella que no se ve hasta que se ve: la app se ralentiza con dos usuarios y con cinco se queda colgada.

**La base de datos bloqueada.** Cuando dos procesos intentan escribir a la vez y el segundo no puede esperar, aparece el famoso `database is locked`. Es la señal de que has pasado de "aplicación" a "servicio compartido" sin haber planeado la migración.

**Base de datos en red.** Y aquí va la advertencia seria: **nunca pongas el archivo SQLite en una carpeta de red compartida** (NAS, carpeta de la empresa, un disco sincronizado tipo OneDrive o Dropbox). Es la peor decisión posible y no funciona de forma sutil: SQLite necesita bloqueos de archivo que los sistemas de archivos en red no coordinan bien. El resultado es corrupción. Si has leído esto y tienes el `.db` en OneDrive, muévelo hoy.

**Una imagen de contenedor que necesita datos.** Si metes tu base de datos dentro de un contenedor, cada vez que lo recreas te llevas los datos. Esto es un problema de arquitectura, no del motor, pero la respuesta sigue siendo la misma.

## Dónde PostgreSQL gana sin discusión

- **Varios usuarios escribiendo a la vez.** Es el caso para el que existe.
- **Necesitas transacciones complejas.** PostgreSQL tiene un sistema transaccional de verdad; SQLite también, pero con limitaciones que aparecen justo cuando empiezas a hacer cosas interesante.
- **Tipos más ricos.** JSONB, arrays, tipos propios. En SQLite puedes guardar JSON como texto y ya.
- **Búsquedas y consultas complejas.** `JSONB` con índices, `full-text search`, `pgvector` si en algún momento quieres guardar embeddings. Esto último, para lo que me preguntan bastante, es la razón número uno para saltar a PostgreSQL: buscar en documentos por significado, no por palabras.
- **Autenticación y permisos finos.** Roles por tabla y por columna. SQLite no tiene usuarios de verdad.

## La tabla, que es lo que se recuerda

| Situación | Elige |
|---|---|
| Práctica de clase, en solitario | SQLite |
| Proyecto personal sin usuarios | SQLite |
| Tests automatizados | SQLite en memoria |
| Script o herramienta local | SQLite |
| Tu primero proyecto web con otros usuarios | PostgreSQL |
| Varias personas guardando a la vez | PostgreSQL |
| Base de datos en red o disco sincronizado | Ninguna: rethink |
| Embeddings o búsqueda por significado | PostgreSQL con `pgvector` |
| Ya tienes PostgreSQL y el proyecto es pequeño | PostgreSQL, no lo toques |

La penúltima fila es PostgreSQL pero con una extensión, así que es un "casi" que se queda corto en la tabla y se explica en el texto. Lo importante: si vas a guardar embeddings, esa decisión se toma al principio del proyecto, no en junio.

## Cómo hacer la migración con IA (la parte que nadie explica)

Si empezaste con SQLite y ahora necesitas PostgreSQL, la buena noticia es que **SQL es SQL**. La migración no es reescribir tu aplicación, es cambiar cuatro cosas. Y aquí es donde la IA es útil, porque los errores de esto son silenciosos.

Los cuatro sitios que cambian:

**El tipo de `AUTOINCREMENT`.** SQLite usa `INTEGER PRIMARY KEY AUTOINCREMENT`, PostgreSQL usa `SERIAL` o `IDENTITY`. Este es el cambio que más se olvida y el que rompe la primera inserción.

**Los booleanos.** SQLite usa `0` y `1`, PostgreSQL usa `true` y `false` de verdad. Las consultas que comparan con `= 1` dejan de funcionar.

**ElConcatenar y los tipos de fecha.** Menor, pero `||` se comporta distinto con `NULL` en los dos.

**El `INSERT OR REPLACE`.** SQLite lo tiene. PostgreSQL usa `INSERT ... ON CONFLICT (clave) DO UPDATE`. No es el mismo lenguaje.

Y aquí viene la trampa: **casi todo esto sigue funcionando en SQLite aunque sea incorrecto en PostgreSQL**, y al revés. Tu código puede parecer que migra bien y fallar en producción con un `NOT NULL` que no se puso. Por eso el prompt tiene que ser explícito:

> "Voy a migrar este proyecto de SQLite a PostgreSQL. Necesito el esquema equivalente, no que traduzcas el SQL sin más. Presta atención a: autoincremento de claves primarias, tipos booleanos reales, y la sintaxis de inserción con conflicto. Dame el DDL de PostgreSQL y avísame de cualquier cosa que en SQLite funcionaba pero aquí no, aunque parezca equivalente."

Esa última frase es la que vale. Una IA con buen criterio te avisa de los tres o cuatro sitios donde la migración es una trampa, aunque no se lo hayas pedido.

## Cómo lo hago yo: empezar en SQLite, migrar pronto

Para un proyecto web de DAW, mi recomendación por defecto es **PostgreSQL desde el primer día**, y lo digo siendo consciente de que es lo contrario de lo que se enseña.

El motivo es el coste del error. Empezar en SQLite cuesta treinta segundos. Migrar en diciembre, cuando ya tienes datos de prueba de tres personas y las consultas están escritas, cuesta un día. El coste no es el SQL, es todo lo que rodeas al SQL.

Si tienes claro que el proyecto es de una persona y no va a salir del portátil, SQLite es la elección correcta y no te voy a convencer de lo contrario. Pero si hay una duda, elige el motor que te permite seguir diciendo que no, que es PostgreSQL.

Y en cualquier caso, en tu `.gitignore` el `.db` fuera. La base de datos de tu proyecto no va a GitHub, y eso incluye la de SQLite.

## Resumen

- SQLite es un archivo, PostgreSQL es un servicio. Elige cuál problema quieres tener.
- SQLite aguanta de sobra proyectos en solitario, prácticas, scripts y tests.
- El límite es la **escritura simultánea**, no el volumen de datos.
- Nunca pongas un archivo SQLite en red ni en una carpeta sincronizada: se corrompe.
- Migrar es cambiar autoincremento, booleanos y dos o tres sintaxis más.
- Si hay duda entre los dos, PostgreSQL: el coste de migrar después es mayor que el de empezar bien.

La IA te va a traducir el esquema sin avisarte de los tres puntos donde la equivalencia es falsa. Si le pides que te señale las trampas, te las señala todas. Y un `database is locked` a las dos de la mañana, con cuatro personas usando la práctica, es la forma más rápida de aprender por qué los servidores existen.

*Si lo que quieres es conectar la base de datos con una interfaz web, en [conectar el frontend con una API usando IA](/articulos/guias/conectar-frontend-api-con-ia-2026/) lo vemos; y si la quieres desplegar, [cómo publicar tu primera web por poco con IA](/articulos/guias/como-publicar-primera-web-internet-barato-ia/) cubre la parte de hosting.*

## Sigue por aquí

La siguiente decisión después del motor de datos es dónde vive la aplicación.

- [Conectar el frontend con una API usando IA](/articulos/guias/conectar-frontend-api-con-ia-2026/)
- [Crear tu primera API REST con Spring Boot e IA](/articulos/guias/primera-api-rest-spring-boot-ia-daw/)
- [Aprender SQL con IA paso a paso](/articulos/guias/aprender-sql-con-ia-daw-2026/)
