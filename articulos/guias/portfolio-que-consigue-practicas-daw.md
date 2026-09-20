---
layout: article
title: "Portfolio de programador con IA que consigue prácticas"
description: "Cómo montar un portfolio que te consiga prácticas de DAW con IA: estructura, proyectos, el texto de candidatura y los fallos que me costaron entrevistas."
category: "Guía"
date: 2026-09-20
readtime: 7
---

## Mi primer portfolio era un cajón desordenado

Cuando empecé segundo de DAW, monté un portfolio en un fin de semana: tema oscuro, un ramo de proyectos con nombres en inglés y un "sobre mí" que decía que me apasionaba la programación. Sonaba genial hasta que lo enseñé en clase y un profesor tuvo la honestidad de preguntarme: "¿y esto, en qué priorizas?" No supe responder. El cajón desordenado, a la vista, era yo.

Tres entrevistas de prácticas (dos falladas, una conseguida) después, entiendo el error de fondo: un portfolio no es una galería de código bonito, es un argumento que responde a "¿por qué elegirte?". Y la parte buena de 2026 es que la IA te permite montarlo con calidad de alguien con experiencia… si sabes qué argumentar. Esto es lo que haría hoy, con IA, para que un portfolio de DAW sí consiga prácticas.

## Primero el argumento, luego el código

Antes de abrir un editor, hay una pregunta que la gente se salta: ¿qué quieres que vean? Las prácticas las suele elegir alguien que ha visto 50 portfolios del mismo módulo. Tu ventaja no es "sé hacer una calculadora", es "sé resolver esto mejor que el resto de candidatos".

Mi enfoque ahora: elegir **un tema** y construirlo alrededor. Por ejemplo, si lo tuyo son las bases de datos, tu portfolio entero habla de datos: consultas optimizadas, normalización, un proyecto de informe con SQL. Si te gustó Desarrollo Web, tu portfolio es una tienda o una app con backend real. La IA te ayuda a descubrir ese hilo: pásale la lista de lo que has hecho en el curso y pídele que te diga "qué 3 temas se repiten y cuál sería tu ángulo más convincente para unas prácticas".

## Los proyectos que cuentan una historia

La segunda pata: los proyectos. En DAW tienes dos o tres proyectos por módulo, y no todos valen para un portfolio. La regla que sigo es la de "el proyecto que puedes explicar en una frase": si te preguntan qué hace y tardas más de diez segundos en contestar, no está claro.

Usar la IA para construirlos está bien, siempre que la entiendas (lo repito en la [lista de errores comunes programando con IA](/articulos/listas/errores-comunes-programando-con-ia/)). Pero el truco que me cambió la entrevista no fue el código, fue el **README**: ahora trato cada proyecto como si lo leyera un jefe de proyecto, no un compañero de clase. Le pido a la IA que lo escriba así, con capturas de pantalla de verdad y un párrafo de decision-making ("por qué elegí SQLite aquí en vez de MySQL", aunque sea una decisión de dos líneas). Eso comunica más que mil commits.

En la [lista de proyectos para portfolio](/articulos/listas/5-proyectos-portfolio-desarrollador-ia-fin-de-semana/) tienes cinco ideas que en realidad sí te obligan a aprender, no a copiar. Con dos de esos, bien pulidos, tienes suficiente para unas prácticas de primer año.

## La parte que más se cuela: la estructura

No importa el motor (static site, React, WordPress): importa que en 10 segundos alguien encuentre:

- **Quién eres y qué edificas**: tu nombre y el foco en una línea.
- **Proyectos con su explicación**: minimalista, 3 máximo con capturas y el porqué.
- **Cómo contactarte**: correo visible, un LinkedIn, repo de GitHub por proyecto.
- **Carga en móvil**: que se lea bien con el dedo, porque lo verán desde el teléfono.

La IA acelera esto de dos formas: te revisa la jerarquía ("¿qué le dice esto a un desconocido en 10 segundos?") y te corrige el texto. Sí, genera textos que suenan bien, pero el error que cometí es aceptar el primero: un about escrito por IA se nota nada más leerlo. Ahora uso dos prompts: uno para que *pregunte* (qué me gusta, qué he hecho, cómo hablo) y otro para que *escriba con mi tono*, y aun así lo reescribo a mano. Como contaba al construir el [portfolio en la guía de desarrollo web con IA](/articulos/guias/crear-portfolio-desarrollador-web-con-ia/), la IA es un editor brutal pero mal autor con tu voz.

## Deploy: que el enlace esté vivo

Nada mata una candidatura como un portfolio que "está en local". Subirlo gratis es hoy más fácil que nunca; en la [comparativa de Vercel, Netlify y GitHub Pages](/articulos/comparativas/vercel-vs-netlify-vs-github-pages-2026/) te dejo cuál me convence según el caso. Lo único no negociable: el enlace tiene que abrirse en el móvil, rápido, sin "Oops".

Y una cosa que aprendí por las malas: el dominio. Un enlace `usuario.github.io/practicas-2026` no dice nada; en la guía de [qué dominio comprar para tu primer proyecto](/articulos/guias/que-dominio-comprar-primer-proyecto-web/) explico por qué gastarse una vez 10 euros en tu apellido cambia la percepción entera. Las prácticas se consiguen antes con un dominio propio que con tres proyectos más en el cajón.

## El texto que te abre la puerta (la IA de redactor jefe)

Cuando tienes portfolio nuevo, toca la parte que a nadie se le da bien: pedir las prácticas. El email o el currículum. Aquí la IA es la herramienta más rentable que existe si la usas para *estructurar* tu propia experiencia, no para inventarla.

El truco que funciona:

```text
Redacta una carta de presentación corta para unas prácticas de DAW
a partir de estos hechos reales: [lista de lo que has hecho]. No inventes
nada que no esté en la lista. Debe tener un parrafo breve y terminar
pidiendo una primera conversacion.
```

Luego le quitas todo el relleno que suene a plantilla (la IA adora las frases tipo "me encantaría aportar mis conocimientos"). Lo que queda es un email de seis líneas que dice lo que hiciste y pide café. Ese formato, junto con el flujo de la [guía de prácticas al primer curro con IA](/articulos/guias/de-practicas-a-primer-curro-con-ia/), es lo que me consiguió la entrevista que acabó en contrato de prácticas.

## Checklist antes de enviar

Te dejo el mío, que imprimo mentalmente cada vez que actualizo el portfolio:

- El enlace funciona y carga en móvil.
- Una idea clara del tema (datos, web, juegos…) sin mezclar.
- 3 proyectos como mucho, cada uno con captura y un "por qué".
- El about suena a mí (compruébalo en voz alta).
- Email visible y respuesta rápida a quien escriba.
- Texto de presentación de 6 líneas listo para cada oferta.

La clave de todo esto es que la IA te ha dado la *velocidad* para ir de cero a un portfolio digno en días, pero el argumento (qué eres y por qué te eligen) sigue siendo tuyo. Cuando lo entiendes así, el portfolio deja de ser estrés y se convierte en lo que debería haber sido desde el principio: una herramienta de venta, no un diario de código.

Si quieres que te revise el flujo entero (portfolio + texto + email de candidatura) y te dé ideas para tu caso concreto, escríbeme a ivan@codeandia.com y lo vemos.