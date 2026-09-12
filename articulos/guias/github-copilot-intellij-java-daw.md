---
layout: article
title: "Cómo configurar GitHub Copilot en IntelliJ IDEA para tus proyectos de DAW"
description: "Configura GitHub Copilot en IntelliJ IDEA paso a paso: instalación del plugin, autocompletado en Java, chat inline, generar tests JUnit y los límites."
category: "Guía"
date: 2026-09-11
readtime: 7
---

Casi todos los tutoriales de Copilot que encuentras usan VS Code. Y casi todos nosotros, en el módulo de programación de DAW, estamos obligados a trabajar con Java en **IntelliJ IDEA** (en mi caso la Community, que es gratis) o en NetBeans. Cuando llegué a clase con Copilot configurado en IntelliJ, mis compañeros me preguntaron si estaba usando un truco. No es ningún truco: es el mismo GitHub Copilot, instalado en un IDE diferente.

El caso es que nadie te lo explica, y configurarlo tiene su cosa. Te lo dejo por escrito para que no pierdas la tarde que perdí yo.

## Por qué quieres Copilot dentro de IntelliJ y no en la web

Lo primero: si estás en DAW, en los módulos de Java (programación, y los que tocan Spring y las APIs) vas a escribir bastante código dentro de IntelliJ. Tener la IA *dentro* del editor marca la diferencia: el autocompletado se basa en tu propio proyecto (los nombres de tus variables, tus métodos de tu clase `GestionAlumnos`), no en un chat genérico donde le pegas el texto y ya.

En [la guía de Copilot para las prácticas](/articulos/guias/como-usar-github-copilot-practicas-daw/) expliqué el concepto más a fondo; aquí me centro en lo práctico: cómo montarlo en IntelliJ, que es donde se atasca la gente.

## Instalación del plugin, paso a paso

1. Abre IntelliJ IDEA y ve a **File > Settings** (o **Ctrl+Alt+S**).
2. Entra en **Plugins** y pincha en la pestaña **Marketplace** (no en "Installed").
3. Escribe en el buscador `github copilot`. Debería salir un plugin de JetBrains llamado **GitHub Copilot**. Pincha en **Install**.
4. Te pedirá reiniciar el IDE. Acepta.

Esto es lo único que cuesta de instalar, en serio. Lo que viene después es lo que liaba de verdad.

## Iniciar sesión: el paso que me daba la lata

En mi caso, la cuenta de GitHub ya la tenía del [plan gratuito para estudiantes](/articulos/reviews/github-copilot-gratis-estudiantes/). Pero igualmente hay que darle el OK desde IntelliJ:

1. Al reiniciar, o nada más instalar, al lado del nombre del IDE aparece un icono pequeño de Copilot (una especie de pluma). Tócalo y elige **Sign in to GitHub Copilot**.
2. Se abre una pestaña con un código de verificación. Si te sale en el navegador, pega el código ahí; si es del IDE, copia el código y pégalo en la web que te indica.
3. Autoriza la aplicación y listo. Un rato después el icono del plugin se pone en verde y ya está operativo.

Si el icono no aparece, revisa que el plugin está habilitado en la pestaña Plugins > Installed (a veces se instala deshabilitado si el IDE estaba abierto).

## El autocompletado en Java: la primera prueba

Lo primero que hago con cualquiera que me lo pide es esta prueba: escribe en una clase de Java:

```java
for (Student student : students
```

En el instante en que escribes los dos puntos, Copilot te sugiere la parte de la derecha (`){ System.out.println(student.getNombre()); }` o lo que toque según tu proyecto). Acepta con **Tab** y sigue: la siguiente línea también te sale sugerida.

Lo que me enganchó no fue lo típico (los `getter` y `setter`, que ya los escribe el IDE solo). Fueron los patrones repetitivos de mis ejercicios: montar un `ArrayList`, filtrar por una condición, comprobar si un elemento existe, hacer un `INSERT` en `PreparedStatement`. Copilot se da cuenta del patrón y te lo completa. Como escribe sobre tu propio código, las variables las pone tal cual las llamas tú, no inventa nombres raros.

## El chat inline: preguntar sobre código concreto

A partir de 2025, el plugin de Copilot en los IDE de JetBrains trae chat integrado (la pestaña de **Copilot** en el panel de la derecha). Ahí le puedes pegar un método entero y preguntarle "¿por qué esto no compila?" o "cómo harías esto más limpio".

El atajo que más uso es el chat *inline*: selecciono unas líneas de código, lo abro y le pregunto justo sobre esa selección. No tienes que explicarle el contexto: ya lo ve. Para mí esto ha sido la forma de entender en vez de copiar, que es la filosofía que cuento en [los 8 prompts que me salvan el curso](/articulos/listas/8-prompts-programacion-daw-2026/).

El consejo que te doy: úsalo para que te explique, no para que haga. "¿Qué está haciendo este método?" te enseña mucho más que "reescríbemelo más corto".

## Generar tests de JUnit: lo más rentable

Otra de las grandes: dentro del método que quieras probar, pídele a Copilot (por el chat o por la acción "Generar tests" del plugin) que te cree el test de **JUnit**. En DAW los tests no suelen ser obligatorios, pero cuando un ejercicio pedía comprobar casos raros (arrays vacíos, un solo elemento, una búsqueda que no encuentra nada), me generaba los casos de prueba y me ahorraba un montón de tecleo.

Eso sí: **revisa lo que genera**. Copilot a veces te hace un test que valida el caso feliz y se olvida de los casos raros que a ti de verdad te iban a puntuar. El test lo usa como plantilla, pero el criterio de qué casos probar sigue siendo tuyo.

## Los límites, para no llevarte un chasco

- **En el plan gratuito el autocompletado va fino, pero el chat y las acciones más potentes tienen límite de uso.** Cuando se acaba, el plugin se vuelve tímido hasta que se resetee el contador.
- **Sugiere, no razona.** Para ejercicios donde la lógica importa (un algoritmo de las clásicas torres de Hanoi, una recursión rara), Copilot te da algo que compila, no necesariamente algo que *entiendes*. Si el examen pide que expliques tu código, tendrás que saber qué hiciste.
- **Versiones de Java.** A veces me sugería API de Java 17 cuando en clase usamos Java 11, o el código no compilaba con la versión del proyecto. Antes de copiar, mira con qué versión estás compilando.

## Mi flujo real

Escribo la lógica del ejercicio **primero**, con Copilot como acelerador del tecleo, y dejo el chat para cuando estoy atascado o para que me genere los tests al final. Raro. Suena raro, pero me va mejor que dejar que la IA haga todo de golpe: llego al examen con criterio, no con ejercicios copiados.

Si al final quieres algo más potente que el autocompletado, te recomiendo leer si te merece la pena [Cursor sobre VS Code con IA](/articulos/comparativas/cursor-vs-vscode-con-ia-2026/), y si tu proyecto crece, la [guía del modo agente](/articulos/guias/github-copilot-agent-mode-2026-guia/) para tareas de varios archivos.