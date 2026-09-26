---
layout: article
title: "TypeScript para estudiantes: los 6 tipos que te ahorran depurar con IA"
description: "Los tipos de TypeScript que más te ahorran errores cuando programas con IA: any, unknown, interfaces y tipos unión. Con ejemplos para tu primer proyecto."
category: "Guía"
date: 2026-09-20
readtime: 8
---

Si programas con IA y te has encontrado con esta línea en el código que te genera el modelo, no eres el único: `function procesar(dato: any)`. Cualquier cosa cabe dentro de un `any`, incluida la que no debería. El resultado es que la IA escribe rápido, TypeScript no te avisa de nada y el error aparece tres archivos más allá, donde ya no entiendes ni qué hizo la IA. La buena noticia es que no necesitas la mitad de TypeScript para ser peligroso: te bastan **seis tipos** para que la IA pase de generar errores invisibles a errores que te avisa el editor antes de ejecutar nada.

## Por qué `any` es la peor decisión que puedes tomar

Empiezo por el culpable. `any` le dice a TypeScript "confía en mí, no compruebes nada". Es cómodo porque nunca falla... hasta que falla de verdad, y entonces falla en runtime, con un `undefined is not a function` que no señala la línea real. Es el equivalente en código a decirle a la IA "hazlo como quieras".

Si la IA te genera funciones con `any` en todas partes, tienes dos salidas. La rápida: pasarle el archivo y decirle *"sustituye todos los `any` por tipos reales, y explícame cada uno"*. Y la buena: entender por qué están ahí. Casi siempre, un `any` es un tipo que aún no sabes nombrar, y obligarte a nombrarlo es exactamente el trabajo de aprender.

## `unknown`: el `any` que sí te protege

Si un valor llega de fuera y todavía no sabes qué es (un `JSON.parse`, la respuesta de una API, un `localStorage`), el tipo correcto no es `any` sino `unknown`. La diferencia parece académica pero no lo es: con `unknown` te **obligas** a comprobar el tipo antes de usarlo, y el editor te señala cada uso peligroso en rojo. Con `any`, el compilador se calla y el error salta en producción.

En la práctica es un check de una línea antes de tocar nada:

```ts
const respuesta = await fetch("/api/notas");
const datos: unknown = await respuesta.json();

if (Array.isArray(datos)) {
  // aquí TypeScript ya sabe que es un array
  console.log(datos.length);
} else {
  console.error("La API no devolvió una lista");
}
```

Ese `Array.isArray` es todo. Es la diferencia entre "esto puede ser cualquier cosa y rezo" y "esto es una lista o no lo es, y lo compruebo". Cuando la IA te traiga un JSON de una API, dale esta instrucción: *"los datos externos son `unknown`, compruébalos antes de usarlos"*. Verás que en la mayoría de apps la lista es la que te ahorra el crash.

## La interface: tus componentes y tus datos

Si vienes de JavaScript, lo más cercano a "describir mis datos" es una `interface`. Sirve para decir qué campos tiene un objeto, con qué tipo. Cuando la IA construye un formulario o una tarjeta de usuario, en vez de dejar los campos sueltos, yo le pido que defina la forma una vez:

```ts
interface Nota {
  id: number;
  titulo: string;
  hecha: boolean;
}

const nueva: Nota = {
  id: 1,
  titulo: "Repasar apuntes",
  hecha: false
};
```

A partir de aquí, si mañana añades un campo `etiqueta: string` a la `interface`, el editor te marca **todos** los sitios donde falte, sin que tengas que probarlo. Ese es el superpoder de los tipos, y es lo que a una IA le cuesta hacer bien sola. Instrucciones que me funcionan: *"crea una interface `Nota` con estos campos, y actualiza todos los objetos que la usan"*. Es una petición concreta, y la IA la resuelve sin que tengas que controlar cada archivo.

## Los tipos unión: cuando son "o A o B"

Un tipo unión es una `|` entre opciones, y modela el caso más común del mundo real: un estado que puede ser una cosa u otra, pero nunca las dos. El ejemplo canónico es una carga de datos que todavía no ha llegado:

```ts
type Estado = "cargando" | "listo" | "error";

function mostrar(estado: Estado, total?: number) {
  if (estado === "listo") {
    console.log("Tienes " + total + " notas");
  } else {
    console.log(estado);
  }
}
```

Por qué mola: si escribes `mostrar("cargando", ...)` mal escrito, el editor te lo subraya al instante porque no es ninguno de los tres valores permitidos. Ese error tonto, que antes solo aparecía al ejecutar, ahora lo ves mientras escribes. Y con la IA es aún mejor: cuando le pido estados para una pantalla, si le insisto en que use un tipo unión en vez de un `string` suelto, el bug de los estados inventados desaparece.

## `never`, el quinto útil y el que nadie te explica

`never` significa "esto no debería existir, y si existe es un error". Se usa en dos sitios, y los dos te ahorran dolor:

- **En el `default` de un `switch`**: si más adelante añades un estado nuevo al tipo unión y no lo manejas, TypeScript te fuerza a ocuparlo. Es un "`switch` que se rompe solo cuando lo extiendes", que es justo lo contrario de lo que quieres.
- **En funciones que nunca devuelven**: una que solo lanza errores, como un `parse` que revienta con la entrada inválida. Le dices que su retorno es `never` y el editor entiende que no hay nada que esperar.

```ts
function parseId(valor: string): number {
  const n = Number(valor);
  if (Number.isNaN(n)) {
    throw new Error("No es un id válido");
  }
  return n;
}
```

El `default` que nunca debería ejecutarse es justo donde va un `never`.

## Reglas de oro y cómo las aplico yo

Después de trabajar con esto ya tengo la rutina. Te la dejo como lista para copiar:

1. **Nunca `any` en la superficie.** Si un valor viene de fuera, es `unknown` y se comprueba.
2. **Los datos que describes, van en una `interface`.** Usuario, Nota, Producto: una vez, y se reutiliza.
3. **Los estados van en tipos unión.** Nunca el string `"cargando"` suelto por ahí.
4. **`never` en el `default` de los `switch`.** Para que crecer duela lo mínimo.
5. **La IA escribe, TypeScript corrige.** Cuando te traiga código, el trabajo tuyo es leer los tipos, no el cuerpo. Son la parte que la IA suele clavar y que menos cambia.

La pista práctica que más me ha servido: cuando pidas código a la IA, **pídele también los tipos**. El prompt que uso es: *"dame la función con los tipos TypeScript definidos y un `unknown` con comprobación donde sea datos externos"*. Con eso, de cada cinco fragmentos que me da la IA, uno llega ya sin `any` y listo para no romperse.

## Mi veredicto

TypeScript parece un añadido de Symfony cuando llevas tres meses con JavaScript, y durante un tiempo lo es. Pero en cuanto la IA te genera veinte archivos, los tipos pasan a ser lo único que te dice qué está pasando, y sin ellos estás leyendo código a ciegas. No aprendas todo el lenguaje: aprende estos seis tipos, pídele a la IA que los use, y deja que el editor haga de policía. El día que este tutorial te sirva, ya será porque los estás usando sin pensar.

Si quieres ver estos tipos aplicados a algo real, el mejor sitio es un proyecto pequeño con formulario y API, como el que monto en [tu primer proyecto web con IA](/articulos/guias/primer-proyecto-web-con-ia/) o cuando [conectas un frontend a una API](/articulos/guias/conectar-frontend-api-con-ia-2026/). Y si te atascas con un error que no sabes leer, mándamelo a ivan@codeandia.com y lo miramos juntos.
