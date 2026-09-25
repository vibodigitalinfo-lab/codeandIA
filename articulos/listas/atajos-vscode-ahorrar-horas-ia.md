---
layout: article
title: "15 atajos de VS Code que te van a ahorrar horas (y ni sabías que existían)"
description: "Los atajos de teclado de VS Code que más uso para programar más rápido: navegación, edición, refactor y multitarea. Los que de verdad ahorran tiempo, no los sobrantes."
category: "Lista"
date: 2026-09-25
readtime: 7
---

Cuando empecé en DAW programaba con el ratón. Seleccionaba, copiar, pegar, guardar, abrir archivo. Me llevaba el doble de tiempo del necesario y ni lo notaba, porque es lo que haces cuando no sabes que hay atajos. Cuando empecé a usar IA para programar, descubrí que los atajos dejaron de ser un lujo: cuanto más rápido muevo el cursor y edito, más ventaja le doy al modelo para proponer cambios y más rápido los integro. No es broma, los atajos son de esas pocas cosas que te hacen el día a día más fluido sin cambiar una línea de tu proyecto. Esta es la lista de los que de verdad uso, no de los que aparecen en listas de veinte que nadie se lee.

## Los 5 de navegación (los que más cambiaron mi día)

Empiezo por estos porque son los que más vas a notar el primer día, y los que más rápido aprendes:

- **Ctrl/Cmd + P**: abre el buscador de archivos por nombre. Escribe tres letras y ya estás en el archivo. Sin ratón, sin pestañas infinitas.
- **Ctrl/Cmd + Shift + P**: la "paleta de comandos". Escribes lo que quieres hacer ("rename symbol", "format document") y lo ejecuta. Si solo aprendieras un atajo, que sea este.
- **Alt + flecha**: mueve la línea actual arriba o abajo. Para reordenar imports o bloques de código sin cortar y pegar.
- **Ctrl/Cmd + Shift + O**: salta a un símbolo (una función o variable) del archivo actual. Cuando un archivo tiene 500 líneas, esto vale oro.
- **Ctrl/Cmd + barra**: divide el editor en dos lado a lado. Ver el HTML y su CSS al mismo tiempo es otra velocidad.

Con solo estos cinco, y sin tocar el ratón, ya puedes moverte por un proyecto entero a una velocidad que sorprende.

## Los 5 de edición (donde la IA te ahorra tiempo)

Cuando la IA te propone un cambio, la mitad del trabajo es seleccionarlo y aplicarlo. Estos atajos lo hacen instantáneo:

- **Ctrl/Cmd + D**: selecciona la siguiente aparición de lo que tengas seleccionado. Si tienes un `id` repetido, pulsar esto tres veces lo selecciona todo. Luego escribes y cambias los tres de golpe.
- **Ctrl/Cmd + Shift + L**: selecciona todas las apariciones de lo que hay en el cursor. Igual que el anterior pero sin seleccionar una a una.
- **Alt + clic**: pone **múltiples cursores** donde hagas clic. Ideal para añadir comas o cerrar etiquetas en varios sitios a la vez.
- **Ctrl/Cmd + barra**: comenta o descomenta las líneas seleccionadas. Para desactivar temporalmente código que estás probando.
- **Shift + Alt + flecha abajo**: **duplica la línea actual**. Es el atajo más infravalorado que existe. Copiar un bloque de cinco líneas y pegarlo debajo ya no lo necesitas.

Los tres últimos son los que más uso yo, especialmente el de múltiplos cursores y el de duplicar línea. Cuando le pido un cambio a la IA y quiero mover esa función a otro sitio, duplico la línea, la muevo con Alt+flecha y la edito. Sin tocar el ratón.

## Los 5 de refactor y entre archivos (el salto de calidad)

Estos ya no son de velocidad, son de **calidad**. Son los que evitan que un pequeño cambio rompa tres cosas:

- **F2**: renombra un símbolo (variable, función, clase) en **todo** el proyecto, no solo donde lo escribiste. Este es de los que, cuando lo descubres, te preguntas por qué no lo sabías antes.
- **Ctrl/Cmd + Shift + R**: cambia el nombre de un archivo y actualiza solo todos los imports que lo referencian. Si mueves un archivo de sitio, esto te ahorra el dolor de cabeza de los imports rotos.
- **Ctrl/Cmd + G**: va a una línea concreta. Cuando la IA te dice "el error está en la línea 243", llegas en un segundo.
- **Alt + clic en una referencia**: abre la definición de una función o variable sin salir del archivo. Para entender qué hace una función que no es tuya.
- **Ctrl/Cmd + K, Ctrl/Cmd + S**: atajo de teclado para abrir las preferencias de teclado. Aquí es donde ves todos los atajos y los rebindas a tu gusto si los de por defecto no te encajan.

## Los bonus: 3 que no sabías que existían

- **Ctrl/Cmd + K, Ctrl/Cmd + X**: elimina una línea entera sin seleccionarla. El atajo equivalente a duplicar.
- **Ctrl/Cmd + Shift + V**: pega el texto sin formato. Si copias código de un sitio web y te pega con estilos raros, esto lo limpia.
- **Ctrl/Cmd + K, Z**: activa el "undo" de todo el archivo. Sí, se puede deshacer un archivo entero, no una letra. Me ha salvado más de una vez de un "replace all" que la IA hizo mal.

## Mi rutina y cómo aprenderlos sin ahogarte en el intento

No aprendas quince atajos de un día; te ahogas. Esta es la rutina que me funciona y que te recomiendo:

1. **Empieza por dos**: `Ctrl+P` (buscar archivo) y `Shift+P` (paleta de comandos). Con esos dos ya ganas mucho.
2. **Añade uno por semana**, y úsalo hasta que tu mano lo haga sola antes de que tu cerebro piense.
3. **El resto, cuando los necesites.** No se aprende un atajo que no te hace falta todavía; se aprende cuando te pilla desprevenido.

Y un truco que me costó años: cuando veas a alguien hacer algo en VS Code con el teclado, pídele el atajo. Y si no lo sabe, haz `Shift+P`, escribe "keyboard shortcuts" y busca el comando. Así dejas de depender de la memoria y empiezas a depender del propio editor, que nunca se equivoca.

La razón por la que esto va tan unido a la IA es que el flujo de trabajo con IA es de muchos cambios pequeños: corriges aquí, mueves allí, duplicas un bloque, cambias tres variable a la vez. Cada uno de esos pasos, con ratón, es un segundo; con atajo, es instantáneo. Multiplicado por veinte correcciones al día, son horas. Y esas horas son las que se van en el trabajo importante, que es entender el código, no en mover cursores.

## Mi veredicto

Los atajos de VS Code son, junto con saber usar git, la inversión de tiempo más rentable que puedes hacer cuando estás empezando. No es que los atajos te hagan mejor programador: es que te devuelven el tiempo y la atención que ibas a perder peleándote con el editor. Empieza por dos esta semana, y ve añadiendo uno cada vez que sientas que algo es lento. En dos meses los tendrás todos en la memoria muscular y no volverás a tener que pensar en cómo mover el cursor.

Personalmente, el que más me cambió fue `Shift+P` (la paleta de comandos), porque te da acceso a cosas que ni sabías que el editor podía hacer. Si quieres ir más allá y aprender a tocar el VS Code a fondo, te dejé una guía de [configuración de VS Code con IA](/articulos/listas/configuracion-vscode-ia-2026/) que va en esa misma línea. Y si quieres que te recomiende atajos para otro editor, escríbeme a ivan@codeandia.com y te digo. Porque al final, el mejor atajo es el que usas, y el que usas es el que te resulta natural.
