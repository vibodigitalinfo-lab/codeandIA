---
layout: article
title: "Documentar tu proyecto con IA: README y código que se entienden"
description: "Cómo escribir documentación de tu proyecto con IA sin que parezca relleno: README que explican, comentarios útiles y por qué documentar te sube nota en DAW."
category: "Guía"
date: 2026-09-11
readtime: 5
---

Nadie te enseña a documentar en DAW. El profe te dice "sube el proyecto a GitHub en condiciones", y tú haces un README con el título y dos líneas de descripción copiadas del primer tutorial. Luego, el día de la entrega, te das cuenta de que quien mejor sabe qué hace tu proyecto eres tú a mediodía, pero a medianoche ya no. Documentar con la IA, bien hecho, te sube la nota y te ahorra explicarte a ti mismo.

## Por qué documentar no es perder tiempo

Documentar no es un favor al profe: es un favor a tu yo del futuro. Cuando vuelvas a un proyecto a las tres semanas de no tocarlo, el que te da la clave de todo es el README. Y en las prácticas de empresa, el código sin documentar es el primer signo de que el proyecto va a ser un dolor.

Además, documentar tiene un efecto raro que no esperaba: me obligó a entender mi propio código. No puedes explicar en dos frases qué hace una clase si no sabes qué hace. La IA puede robarte esa reflexión si la dejas, así que el truco está en que ordene tus ideas, no que las invente.

## Un README que de verdad funciona

El README no es un ensayo, es una cabecera de aeropuerto: la gente necesita saber en diez segundos qué hace el proyecto, cómo se pone en marcha y cómo se prueba. La estructura que me funciona:

- **Nombre y frase de qué hace** (una línea, no un párrafo).
- **Captura o demo** (un GIF o una imagen vale más que mil palabras).
- **Requisitos** (versiones de Java, Node, Docker...).
- **Cómo arrancar** (los comandos exactos, en orden y copiables).
- **Cómo probar** (qué URL abrir, qué esperar).
- **Estructura** breve de carpetas si el proyecto es grande.

Puedes pedirle a la IA que te genere el esqueleto con este prompt: "Esto es un proyecto Spring Boot para DAW que gestiona alumnos. Dime qué debe llevar un README claro en español, sección por sección, sin rellenar nada todavía". La clave es la última parte: que **no rellene**.

## El truco de la IA: que ordene, no que invente

Cuando generas documentación con IA, cometes el error de darle solo el nombre del archivo y decirle "docuéntamelo". Ella rellenará con funcionalidades que no existen: "ofrece autenticación con JWT" en un proyecto que no la tiene. Me pasó y entregué un README que mentía sobre mi propio trabajo, que es peor que no tener nada.

Lo que funciona es darle el contexto real y pedirle que sea honesta: "Aquí está la lista de endpoints que he implementado (dame la lista tú). Genera la sección de la API solo con estos, no inventes". Si el prompt incluye "no inventes nada que no esté en la lista", la calidad sube muchísimo.

## Documentar el código, no solo el proyecto

El siguiente nivel es documentar funciones y módulos. Aquí mi regla es la contraria: **escribes tú lo que hace y la IA lo pule**. No quiero que genere comentarios de cero porque entonces documento código que no sé que hace (misma trampa de siempre). Lo que hago es escribir a palo seco:

`// esta funcion filtra los alumnos del curso que aprobaron y devuelve solo nombres`

...y luego le pido: "ordena este comentario en JSDoc con parámetros y qué devuelve, sin añadir nada más". El resultado es una documentación profesional que sale de lo que yo entendí, no de lo que la IA supone. Ese matiz separa la documentación que apruebas de la que se nota.

## El README que te salva en la entrega

La entrega vale el doble cuando el que mira el repo es el profe con diez proyectos encima. Un README con los pasos copiables hace que pruebe tu proyecto en dos minutos; sin él, se queda en la cola y la nota lo nota. Si además tu proyecto usa Docker, incluye el `docker compose up -d` en el "Cómo arrancar" — es el camino que expliqué en la guía de Docker — y dejas el arranque en un solo comando.

Y para terminar, un detalle de git: documentar el proyecto también es tener un historial claro. Practicar el flujo de commits con mensajes que se entiendan es la mitad de la documentación, y es justo lo que toqué en la guía de git con IA.

## El veredicto

Documentar es el 10% del tiempo y el 30% de la percepción de tu trabajo. No hace falta volverse loco: un README claro, los endpoints reales listados y comentarios que expliquen el porqué ya te ponen por encima de la media de la clase. La IA es la mecanógrafa perfecta para esto — solo tienes que no dejar que sea la que piensa. Si quieres, me pasas el link de tu repo y te digo qué secciones del README le faltan para la entrega.

## Sigue por aquí

- [Cómo crear tu primer portfolio de desarrollador web con IA paso a paso](/articulos/guias/crear-portfolio-desarrollador-web-con-ia/)
- [Cómo leer código ajeno con IA: método de 4 pasos](/articulos/guias/leer-codigo-ajeno-con-ia/)
