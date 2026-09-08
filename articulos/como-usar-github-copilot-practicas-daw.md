---
layout: article
title: "Cómo usar GitHub Copilot para hacer tus prácticas de DAW más rápido"
description: "Te cuento cómo uso github copilot para prácticas DAW en clase y en casa, con ejemplos reales de proyectos del ciclo."
category: "Guía"
date: 2026-09-08
readtime: 7
affiliate_text: "Si quieres probarlo tú mismo, GitHub Copilot tiene plan gratuito para estudiantes"
affiliate_url: "https://github.com/features/copilot"
affiliate_label: "Consigue GitHub Copilot gratis con GitHub Student Pack"
---

Lo primero que tengo que decir es que no empecé usando Copilot porque me lo recomendara nadie del instituto. Lo instalé un domingo por la tarde porque llevaba tres horas atascado con un ejercicio de Programación que tenía que entregar el lunes, y un compañero de clase me dijo por Discord "tío, prueba github copilot para prácticas DAW, a mí me salva la vida con Java". Le hice caso más por desesperación que por fe, y la verdad es que desde entonces no he vuelto a programar sin él abierto en el VS Code.

No voy a venderte que Copilot te hace el ciclo por ti, porque no es así y si alguien te dice eso te está mintiendo. Pero sí te acorta muchísimo el tiempo que pierdes en cosas mecánicas, que en DAW son bastantes: getters y setters, consultas SQL repetitivas, formularios en Angular que se parecen todos entre sí. Ahí es donde de verdad marca la diferencia.

## Cómo empecé a usar Copilot en mis prácticas de DAW

Cuando lo instalé por primera vez, lo hice con el plan de estudiante, que es gratis si tienes el correo del instituto verificado o usas el GitHub Student Pack. Eso ya te digo que es un puntazo, porque de normal Copilot cuesta una mensualidad y siendo estudiante no tiene sentido pagarlo.

La primera vez que lo probé en serio fue con un ejercicio de Acceso a Datos, concretamente un CRUD contra una base de datos MySQL con JDBC. Escribí el nombre del método `insertarUsuario` y antes de terminar la primera línea ya me estaba sugiriendo prácticamente todo el bloque try-catch con el PreparedStatement montado. Me sorprendió, la verdad, porque esperaba algo más torpe. No estaba perfecto, cambié un par de nombres de variables y añadí una validación que él no había puesto, pero me ahorró fácilmente diez minutos de escribir código que ya me sabía de memoria de tanto repetirlo.

### El día que casi me la juega en un examen práctico

Tengo que contar esto porque creo que es importante no idealizar la herramienta. En un examen práctico de Desarrollo Web en Entorno Servidor nos dejaban usar el ordenador con conexión, así que tenía Copilot activo. Le pedí que me generara la lógica de paginación para una lista de productos y me soltó una solución que compilaba perfectamente pero que tenía un error de índices fuera de rango en el último caso límite. Si no hubiera repasado el código línea por línea antes de entregar, me habría comido un fallo tonto en la nota. Desde ese día reviso todo lo que sugiere, especialmente en bucles y condiciones límite, porque ahí es donde más se equivoca.

## Github Copilot para prácticas DAW: en qué asignaturas rinde más

No todas las asignaturas se benefician igual. En Bases de Datos y en Acceso a Datos es donde noto más el ahorro de tiempo, porque hay mucho código de conexión, consultas y mapeo de resultados que se repite curso tras curso. En Programación también ayuda bastante, sobre todo con estructuras de datos y algoritmos clásicos que Copilot conoce de sobra.

Donde menos me ha convencido es en Diseño de Interfaces Web, específicamente con maquetación CSS un poco más creativa. Ahí las sugerencias suelen ser genéricas, del estilo "caja azul con sombra", y al final acabo escribiendo yo mismo los detalles finos porque quiero que mi proyecto se vea distinto al de mis compañeros y no como sacado de un tutorial de YouTube.

## Trucos que aprendí usando Copilot en el día a día del ciclo

Uno de los cambios que más noté fue empezar a escribir comentarios antes del código en lugar de después, algo que en clase casi nadie hace. Si pongo `// función que valida que el DNI tenga el formato correcto con letra` antes de escribir la función, Copilot entiende mucho mejor lo que quiero y las sugerencias mejoran una barbaridad. Es un poco raro acostumbrarse a explicar lo que vas a hacer antes de hacerlo, pero funciona.

Otra cosa que hago, y que recomiendo a cualquiera que empiece con github copilot para prácticas DAW, es no aceptar nunca la primera sugerencia a ciegas. Le doy al tabulador para ver qué propone, pero antes de aceptar leo la línea completa. Al principio aceptaba todo por pereza y luego me encontraba con nombres de variables en inglés mezclados con mi código en español, que quedaba raro y además el profesor de Programación una vez me lo comentó en una corrección.

## ¿Merece la pena para alguien de DAW?

Después de un año usándolo casi a diario, mi opinión es que sí merece la pena, pero con matices. Si estás en primero de DAW y todavía no tienes soltura con la sintaxis básica, te diría que lo uses con cuidado, porque puede volverte dependiente antes de que hayas entendido de verdad por qué funciona algo. A mí me pasó al principio con los bucles anidados: los usaba porque Copilot los generaba bien, pero si me preguntaban en un examen sin ordenador me costaba reproducirlos solo.

Ahora que estoy en segundo lo veo de otra forma. Ya tengo la base y lo uso más como lo que es, un compañero que te propone cosas y tú decides si las aceptas, las cambias o las tiras a la basura. Para las prácticas de clase, para los proyectos de módulo y sobre todo para cuando se te acumulan tres entregas la misma semana, Copilot es de las pocas herramientas de IA que realmente he integrado en mi rutina de estudio y no he abandonado a los dos meses como me pasó con otras.
