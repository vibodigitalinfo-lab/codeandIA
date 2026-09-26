---
layout: article
title: "Docker para estudiantes DAW: cómo usarlo con IA sin morir"
description: "Guía de Docker para DAW: qué son los contenedores, tu primer Dockerfile y docker-compose, con la IA de copiloto y los errores reales que te vas a encontrar."
category: "Guía"
date: 2026-09-07
readtime: 6
---

La tarde que decidí probar Docker me la pasé entera persiguiendo un mensaje de "port is already allocated". No sabía qué era un contenedor, por qué necesitaba el "docker-compose up" y, sobre todo, por qué la IA me seguía dando YAML que no funcionaba. Cuando por fin lo entendí, me di cuenta de que Docker no es difícil: es distinto, y la IA no te lo explica si no se lo pides bien. Esto es lo que me habría ahorrado esa tarde.

## Qué es un contenedor (en cinco líneas)

Un contenedor es tu aplicación empaquetada con todo lo que necesita para funcionar, aislada del resto de tu ordenador. Piensa en un contenedor como una minipc que se crea a partir de una plantilla: tiene su propio sistema de archivos, sus propias versiones de todo, y se enciende y se apaga con un comando. No es una máquina virtual (no arranca un sistema operativo completo), por eso es rápido y ligero.

La ventaja que te va a salvar la vida en prácticas: "en mi ordenador funciona" deja de ser un problema. Si el proyecto corre en un contenedor, corre igual en el tuyo, en el del profe y en el servidor.

## Antes de nada: pon a punto el entorno

En Windows, lo normal es **Docker Desktop** con WSL2. Y aquí está el primer consejo real: cuando la IA te diga "instala Docker Desktop y listo", no te confíes — WSL2 se activa con un comando en PowerShell (`wsl --install`) y si tu Windows está desactualizado, Docker te va a dar guerra hasta que lo actualices. Mejor que te lea mi guía de la terminal para Windows si vas justo de base.

Cuando arranques Docker Desktop y veas el icono del ballena fijo en la bandeja, ya estás listo.

## Tu primer contenedor sin escribir un Dockerfile

Para entender de qué va todo antes de complicarte, corre una imagen oficial del registro de Docker (toda esta parte de registros la explora mi artículo de la terminal):

```
docker run -d -p 8080:80 nginx
```

Ese comando descarga la imagen `nginx`, la arranca en segundo plano (`-d`) y mapea el puerto 8080 de tu ordenador al 80 del contenedor. Abre `http://localhost:8080` y ahí tienes un servidor web funcionando sin instalar nada. El puerto lo defines tú (derecha), y es el error más típico del mundo: si el 8080 está ocupado, falla con el dichoso "port is already allocated" que me persiguió la tarde entera.

## El Dockerfile: pídele la explicación, no el archivo

Cuando ya entiendes el `run`, toca empaquetar tu propia aplicación. Un Dockerfile es una receta con pasos: `FROM` (la imagen base), `COPY` (tus archivos), `RUN` (lo que se instala) y `CMD` (lo que se ejecuta). Para una API de Node, algo mínimamente decente queda así:

```dockerfile
FROM node:22-alpine
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "index.js"]
```

Mi regla de oro es la misma que en el resto del blog: que la IA **te explique cada línea** antes de pegarla. Y ojo con los números de versión: la IA tiene la costumbre de inventar `node:39` o un tag que no existe. Usa siempre versiones que puedas confirmar en el registro oficial, o el Dockerfile fallará en `pull`.

## docker-compose: cuando tu proyecto tiene varias piezas

Tu proyecto de DAW rara vez es una sola cosa: una API, una base de datos y quizá un frontend. `docker-compose.yml` te permite arrancarlas todas juntas con un comando. Un ejemplo clásico: la API de Spring Boot que monté en mi guía del módulo de servidor, con su base de datos al lado.

```yaml
services:
  db:
    image: postgres:17
    environment:
      POSTGRES_PASSWORD: prueba
    ports:
      - "5432:5432"
```

Aquí la IA sí es una ayuda enorme para generarte el YAML, porque es verboso y fácil de descolocar. Pero le pasa lo mismo que con las versiones: te pone `POSTGRES_PASSWORD` con contraseñas que copiarás a tu código y luego no entenderás por qué tu API no conecta. Los nombres de variables y de volumen los defines tú; la IA solo los rellena.

## Los comandos que te van a salvar (y el error de volúmenes)

La vida con Docker es un rosario de cuatro comandos: `docker compose up -d` para arrancar, `docker compose logs` para ver errores, `docker compose ps` para ver qué está vivo y `docker compose down` para apagar. Aprenderte esos cuatro te evita el 90% del dolor.

El error que más tiempo me comió fue el de los **volúmenes**: la base de datos perdía todos los datos cada vez que hacía `down`. Resulta que había "creado" el volumen con una línea que no encajaba y Postgres arrancaba limpio en cada `up`. La pista que me dio la IA fue buena, pero el fallo estaba en algo que ella había escrito mal en el YAML y yo había pegado sin leer. Regla: lee siempre el `compose` entero antes del primer `up`.

## El momento en que te da la paz

Cuando tu API de Spring, tu base de datos y tu frontend arrancan con un solo `docker compose up -d`, y el profe dice "ponlo en marcha" y lo ves funcionar en su portátil, te das cuenta de que el esfuerzo valió la pena. Docker no es obligatorio en DAW, pero en las prácticas de empresa te lo encontrarás sí o sí, y llegar sabiendo leer (y arreglar) un compose te separa de la mitad de la clase.

Mi consejo: no empieces con el Dockerfile de tu proyecto real. Empieza por el `nginx` suelto de arriba, luego un contenedor Node, y el día siguiente ya con compose. Ve en pasos pequeños, pídele a la IA las explicaciones, y si te quedas atascado con un puerto o un volumen, me lo cuentas cuando quieras y te digo por dónde tirar.