---
layout: article
title: "Saqué un 10 en XML haciendo la práctica sin IA (y creo que fue por eso)"
description: "Cómo aprendí XML en mi primer trimestre: lo que me ayudó saber HTML, por qué hice las actividades sin IA y para qué sí la usé: tests de teoría."
category: "Guía"
date: 2026-11-06
publicar: 2026-11-06
readtime: 6
---

## La práctica que hice sin IA

Estudio primero de DAW, un ciclo de FP de desarrollo de aplicaciones web en España. En este blog hablo mucho de cómo uso la IA para aprender a programar: en Java le pido que me corrija los ejercicios y me dé feedback, y hasta me he hecho [mi propio corrector de Java](/articulos/guias/corrector-java-gratis/).

Pero hay una asignatura en la que la parte práctica la he hecho entera sin IA: Lenguajes de marcas, que en este primer trimestre ha sido XML. Ni las actividades ni la preparación de los ejercicios del examen. Y es justo la que mejor me ha salido. Las notas oficiales:

- **10** en el cuestionario tipo test.
- **10** en la parte práctica: tres ejercicios, uno de corregir la sintaxis de un XML que nos daban y dos de crear un XML desde cero a partir de un enunciado.
- **10** en todas las actividades entregables del trimestre.

No te lo cuento para presumir. Te lo cuento porque creo que una cosa tiene que ver con la otra, y porque en un blog que habla tanto de IA me parece honesto decir cuándo no la he necesitado. Para la teoría sí la usé, y también te cuento cómo.

## Por qué no la usé en la práctica

Al empezar el tema, el profesor nos dijo que hacer las actividades con IA sería engañarnos a nosotros mismos. Y tiene razón.

Si las actividades me las hubiera hecho la IA, habrían salido bien igual y me habrían puesto la misma nota en ellas. El problema habría llegado en el examen, que se hace sin ayuda. Estoy bastante seguro de que no me habría salido tan bien. Las actividades son el entrenamiento, y si otro entrena por ti, el día del partido no estás en forma.

Con Java me pasó al principio: copié código generado por la IA sin entenderlo y me di cuenta de que no servía. Lo conté en [cómo aprendo Java con IA sin volverme dependiente](/articulos/guias/aprender-java-con-ia-daw/). Con XML no quise repetir el error.

## Lo que me ayudó: ya sabía HTML

XML lo pillé desde el primer momento, y creo que la razón principal es que ya conocía HTML. Los dos se escriben con etiquetas que se abren y se cierran y que van unas dentro de otras, así que la estructura y la sintaxis me sonaban desde el primer ejercicio.

La diferencia es que en XML las etiquetas no vienen dadas: te las inventas tú según lo que quieras describir. Y XML es mucho más estricto que HTML. Un navegador te perdona casi todo en una página web; un XML con un solo fallo ya no está bien formado.

Si vienes de HTML, tienes medio camino hecho. Si no, no pasa nada: las reglas son pocas y muy claras, y en cuanto haces un par de ejercicios se quedan.

## Cómo hacía las actividades

En clase usamos XML Copy Editor, un editor gratuito que comprueba si tu XML está bien escrito. Mi forma de trabajar era siempre la misma:

1. Me ponía el ejercicio delante y empezaba a escribir el XML.
2. Si había algún detalle que no sabía, lo buscaba en los apuntes o en un ejercicio anterior que ya tenía hecho y corregido.
3. Lo comprobaba con el editor.
4. Cuando el editor me decía que estaba bien **y** además cumplía con lo que pedía el enunciado, lo daba por terminado.

El punto 4 tiene dos partes, y las dos importan. Que el editor no dé errores solo significa que la sintaxis es correcta. Que tenga sentido (que estén todos los datos que pide el enunciado y con una estructura lógica) eso lo tienes que mirar tú.

Lo bueno de XML es que esa comprobación te da una respuesta clara al momento: o está bien o te dice dónde falla. Por eso no sentí que necesitara a la IA para corregirme. Con Java es distinto: un programa puede compilar y aun así hacer algo mal, y ahí el feedback de la IA sí me ayuda.

## El error que más me salía: las mayúsculas

No todo fue perfecto. El fallo que más se me repetía al principio eran las mayúsculas. En XML, `<Nombre>` y `<nombre>` son etiquetas distintas, así que esto da error:

```xml
<alumno>
  <Nombre>Ana</nombre>
</alumno>
```

La etiqueta se abre como `Nombre` y se cierra como `nombre`, y para XML eso no cuadra. En HTML no pasaría nada, porque no distingue mayúsculas, y supongo que por eso me costó acostumbrarme.

Lo que hago ahora es decidir al principio cómo voy a escribir los nombres (yo los pongo todo en minúscula) y no salirme de ahí en todo el documento.

## Donde sí usé IA: la teoría

Para la parte teórica sí uso IA, en XML y en cualquier examen que tenga. Lo que hago es pasarle mis apuntes y pedirle que me haga tests sobre ellos, para comprobar si me sé la teoría antes del examen.

Uso dos herramientas según el tiempo que tenga:

- **Gemini**, cuando quiero algo rápido: unas cuantas preguntas tipo test para repasar en un rato.
- **NotebookLM**, cuando voy a estar estudiando varios días antes del examen. Le subo los apuntes y me hace las preguntas a partir de ellos, así que no se inventa temario que no hemos dado.

La diferencia con la práctica es que aquí la IA no hace el trabajo por mí: me pregunta y soy yo quien tiene que responder. Es como tener a alguien que te toma la lección. En el cuestionario tipo test también saqué un 10.

## Lo que viene: DTD y normalización

En el segundo tema de Lenguajes de marcas estamos empezando con DTD, que sirve para definir qué etiquetas puede tener un XML y en qué orden. Eso no entraba en el primer tema, así que todavía no te puedo contar qué tal me va.

Y en Bases de datos acabamos de empezar con la normalización. Ahí sí puede que use la IA para entenderla bien, porque falté a alguna clase y no quiero quedarme con huecos. La diferencia es que la usaría para que me lo explique, no para que me haga los ejercicios.

## Mi conclusión

La IA no es buena o mala para estudiar: depende de para qué la uses. Cuando algo te resulta sencillo y tienes una forma clara de saber si está bien, como el validador de XML, hacerlo tú solo es lo que más te enseña. Para repasar teoría, que te pregunte sobre tus apuntes funciona muy bien. Y cuando te atascas de verdad, que te lo expliquen está bien, mientras la parte de pensar siga siendo tuya.

Si estás empezando con XML y tienes dudas, o te preguntas si deberías usar IA en alguna asignatura, puedes escribirme a vibo@codeandia.com.
