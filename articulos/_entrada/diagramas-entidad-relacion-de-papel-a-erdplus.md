---
layout: article
title: "Diagramas entidad-relación: por qué ponía las cardinalidades al revés"
description: "Mi experiencia con los diagramas E-R en primero de DAW: el fallo de poner las cardinalidades en la entidad equivocada, cómo leerlas bien y qué tal erdplus."
category: "Guía"
date: 2026-11-03
publicar: 2026-11-03
readtime: 5
---

## Empezar las bases de datos dibujando

En bases de datos, en primero de DAW, empezamos por los diagramas entidad-relación y ahora estamos con los primeros pasos del modelo relacional, con las tablas. Hemos hecho un montón de ejercicios. Uno de ellos era una tienda con empleados, un dueño, un almacén, productos y clientes, algunos de los cuales podían ser socios. Te suena a ejercicio sencillo hasta que empiezas a pensar cómo se relaciona cada cosa con las demás.

En general no me está resultando difícil, salvo una cosa que me ha costado más que todo lo demás: **las cardinalidades**. Y no porque no entendiera qué significan, sino porque las ponía al revés, en la entidad equivocada. Te cuento el fallo y una forma de leerlas que evita caer en él.

## Primero a mano, luego en el ordenador

Al principio hacíamos los diagramas en papel. Después pasamos al ordenador con [erdplus.com](https://erdplus.com/), que es la herramienta que usamos en clase.

De erdplus no tengo quejas, la verdad. Es sencilla, se trabaja bien con ella y para lo que hacemos cumple perfectamente: pones las entidades, las relaciones y los atributos, lo mueves todo y queda ordenado. Es gratis y funciona en el navegador, así que no hay que instalar nada, algo que se agradece en un portátil de clase.

Aun así, creo que empezar a mano fue lo que más me sirvió. En el papel tienes que pensar la estructura antes de dibujarla, y ahí es donde salen las dudas de verdad. Erdplus te ayuda a dejarlo limpio, pero no piensa por ti dónde va cada cardinalidad.

## Mi fallo: la cardinalidad en la entidad equivocada

Una relación une dos entidades, y cada extremo lleva su cardinalidad. Mi problema era que entendía bien la frase («un almacén guarda muchos productos»), pero al dibujarla ponía el «muchos» al lado del almacén en vez de al lado del producto.

Pasa porque la intuición te dice que, si hablas del almacén, el número va al lado del almacén. Pero en la forma en que lo damos en clase, la cardinalidad se lee **desde la otra entidad, cruzando la relación**.

Con un ejemplo simplificado se ve mejor (no es el ejercicio de clase, solo una parte reducida para explicarlo):

![Diagrama entidad-relación de ejemplo: ALMACÉN (1,1) guarda (0,N) PRODUCTO](/assets/img/er-almacen-producto.svg){: width="640" height="220"}

- Pregunta: **un almacén, ¿cuántos productos guarda?** Puede que ninguno y puede que muchos: (0,N). Eso se escribe **al lado de PRODUCTO**, al otro extremo.
- Pregunta: **un producto, ¿en cuántos almacenes está?** En este ejemplo, en uno y solo uno: (1,1). Eso se escribe **al lado de ALMACÉN**.

Mi error era escribir cada respuesta junto a la entidad desde la que hacía la pregunta. Así, el diagrama decía justo lo contrario de lo que yo quería decir.

Un aviso: no todos los libros ni todos los profesores colocan las cardinalidades igual, porque hay varias notaciones. Si tienes dudas, mira un ejercicio corregido por tu profesor y fíjate en qué lado pone cada cosa. Lo que importa es que hagas siempre la pregunta desde una entidad y leas la respuesta en la otra.

## Una forma sencilla de no equivocarse

Antes de escribir ninguna cardinalidad, ayuda decir la frase completa (o escribirla al margen):

1. «Un **almacén** guarda **[mínimo, máximo]** **productos**.»
2. La respuesta va junto a la **última** entidad de la frase, la de los productos.
3. Le doy la vuelta: «Un **producto** está en **[mínimo, máximo]** **almacenes**.» Esa respuesta va junto a los almacenes.

Es lento las primeras veces, pero obliga a hacer las dos preguntas de cada relación en lugar de fiarse de la intuición, que es justo donde fallaba yo.

## Por qué importa tanto acertar

Al principio pensaba que era un detalle de dibujo, pero no lo es. Cuando pasas el diagrama al modelo relacional, las cardinalidades deciden cómo quedan las tablas: en una relación de uno a muchos, la clave del lado «uno» pasa como clave ajena al lado «muchos». Si las pones al revés, la clave ajena acaba en la tabla equivocada y todo el modelo se tuerce.

En el ejemplo, con las cardinalidades bien puestas, la tabla `PRODUCTO` lleva el código del almacén. Con ellas al revés, sería el almacén el que tendría que guardar un único producto, lo cual no tiene ningún sentido para una tienda.

## Lo que haría diferente

Si empezara otra vez, haría las dos preguntas de cada relación desde el primer ejercicio, en vez de fiarme de la intuición. Y repasaría los ejercicios corregidos fijándome solo en las cardinalidades, que es donde más fallaba.

Lo bueno es que es un error muy de principio: una vez que interiorizas que se lee cruzando la relación, es mucho más difícil que vuelva a pasar.

Si te pasa lo mismo con los diagramas E-R o estás con el modelo relacional, puedes escribirme a ivan@codeandia.com. También tengo una guía sobre [cómo estudio para los exámenes de programación con IA sin copiar código](/articulos/guias/estudiar-daw-con-ia-sin-copiar-codigo/), donde cuento cómo preparé el examen de bases de datos.
