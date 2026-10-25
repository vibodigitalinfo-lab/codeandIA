---
layout: article
title: "Mis ejercicios de Java de primero: aciertos, fallos y alguno a medias"
description: "Un mes de ejercicios de Java en Eclipse, con mi código tal cual: los que funcionan, el fallo del Scanner, un main que no compila y los que dejé a medias."
category: "Guía"
date: 2026-10-23
updated: 2026-10-25
readtime: 9
last_modified_at: 2026-10-25
---

## Un mes de ejercicios, tal cual los tengo en Eclipse

Estudio primero de DAW, el ciclo de FP de desarrollo de aplicaciones web en España, y Java es mi primera asignatura de programación. Entre el 23 de septiembre y el 23 de octubre he ido llenando mi carpeta de Eclipse con 16 proyectos de práctica. Algunos son ejercicios de clase. Otros los buscaba yo o se los pedía a Claude, basándome en los que nos daba el profesor y en cómo trabaja él (lo cuento en [cómo aprendo Java con IA](/articulos/guias/aprender-java-con-ia-daw/)).

Antes aquí tenía ocho ejercicios con soluciones perfectas. Los he quitado: eran correctos, pero no eran míos, y hay miles iguales en internet. Lo que te enseño ahora es **mi código, tal cual me salió**: algunos bien, otros con fallos y alguno a medias porque me agobiaba. Los enunciados no los copio, porque muchos son del profesor; solo cuento de qué iba cada uno.

## El primero: un cocinero que hace masa

Mi primer proyecto, del 23 de septiembre. Una clase con dos atributos, un constructor y unos métodos para consultar y cambiar el nombre:

```java
public class Cocinero {

	private String nombre;
	private int edad;

	public Cocinero(String nombreCocinero, int edadCocinero) {
		nombre=nombreCocinero;
		edad=edadCocinero;
	}

	public int hacerMasa(int grHarina, int grAgua, int grAceite) {
		int grMasa=grHarina+grAgua+grAceite;
		return grMasa;
	}

	public String consultarNombre() {
		return nombre;
	}

	public void establecerNombre(String nuevoNombre) {
		nombre=nuevoNombre;
	}
}
```

Visto ahora es muy simple, pero aquí entendí lo básico: la clase es el molde, el objeto es lo que creas con `new`, y los métodos son lo que ese objeto sabe hacer. Fíjate en que `edad` se guarda y nunca se usa. Cosas de primer día.

## Cuando empezó a encajar: una linterna con su batería

Tres semanas después, el 18 de octubre, ya hacía cosas como esta: una `Bateria` que no puede bajar de 0 ni pasar de su capacidad, y una `Linterna` que tiene una batería dentro.

```java
public class Bateria {

	private int capacidadBat, cargaActual;

	public Bateria(int capacidad) {
		capacidadBat=capacidad;
		cargaActual=capacidadBat;
	}

	public Bateria() {
		this(2000);
	}

	public void gastar (int bateriaGastada) {
		cargaActual=cargaActual-bateriaGastada;
		if (cargaActual < 0) {
			cargaActual=0;
		}
	}

	public void cargar (int bateriaRecargada) {
		cargaActual=cargaActual+bateriaRecargada;
		if (cargaActual > capacidadBat) {
			cargaActual=capacidadBat;
		}
	}

	public int getCarga() {
		return cargaActual;
	}
}
```

```java
public class Linterna {

	private Bateria bateria;

	public Linterna() {
		bateria = new Bateria();
	}

	public Linterna(int capacidad) {
		bateria = new Bateria(capacidad);
	}

	public void encender(int minutos) {
		bateria.gastar(10*minutos);
		System.out.println("La carga restante es: "+bateria.getCarga());
	}

	public void cargar(int minutos) {
		bateria.cargar(40*minutos);
		System.out.println("La carga restante es: "+bateria.getCarga());
	}
}
```

Así salía en la consola de Eclipse al ejecutarlo:

![Consola de Eclipse con la salida de la linterna: 1900, 1980, 0, 200 y 500 de carga restante](/assets/img/java-linterna-consola.png){: width="460" height="205"}

La primera linterna gasta 100 en 10 minutos y recupera 80 al cargar. La segunda, de 500, se queda en 0 tras una hora encendida (no baja a negativo) y, aunque la cargue 20 minutos, se queda en 500 (no pasa de su capacidad).

Aquí hay tres cosas que al principio no tenía claras:

- **`this(2000)`**: un constructor que llama a otro. Si creas la batería sin decir la capacidad, tiene 2000.
- **Los límites con `if`**: la carga nunca baja de 0 ni pasa del máximo, la gastes o la cargues lo que quieras.
- **Un objeto dentro de otro**: la linterna no sabe cuánta carga hay; se lo pregunta a su batería. Esto es lo que más me costaba entender, y cuando lo ves, todo se vuelve mucho más sencillo.

El mismo día hice una cuenta bancaria con la misma idea: `retirar()` comprueba primero si hay saldo suficiente y, si no, avisa con un «Saldo insuficiente» en vez de dejar el saldo en negativo.

## El fallo que más me ha pasado: el Scanner que se salta una pregunta

En uno de los ejercicios de la cafetería, del 21 de octubre, pedía tres datos por teclado:

```java
System.out.println("Introduce el nombre de un cliente: ");
String nombreCliente=s.nextLine();
System.out.println("Introduce el dinero inicial: ");
double dinero = s.nextDouble();
System.out.println("Introduce el nombre de un Barista: ");
String nombreBarista=s.nextLine();
```

Compila y arranca, pero el nombre del barista sale **vacío**: el programa no te deja escribirlo. El motivo es que `nextDouble()` lee el número, pero deja pendiente el salto de línea de cuando pulsas Intro. El `nextLine()` siguiente se encuentra ese salto y lo toma como una línea vacía.

La solución es poner un `s.nextLine();` suelto justo después de leer el número, para limpiar ese salto:

```java
double dinero = s.nextDouble();
s.nextLine(); // limpia el salto de línea que deja nextDouble()
String nombreBarista=s.nextLine();
```

En el ejercicio del taller, ese mismo día, ya lo hice así y funcionó. Otra cosa que se ve en ese código: leo el dinero inicial y luego nunca lo uso, porque el cliente se crea con el constructor que pone siempre 10 €. Compila, pero no hace lo que quería.

## Cuando cambio un método y se me olvida el main

Este es del 22 de octubre, un taller de bicis con un ciclista y dos mecánicos. Mientras lo hacía fui cambiando los métodos de `Ciclista` y `Mecanico`, pero el `main` se quedó llamándolos como estaban antes. Resultado: no compila, y Eclipse lo marca en rojo:

![Eclipse con taller_bicis abierto y la pestaña Problems: 5 errores, tres de métodos que no aceptan esos argumentos y dos de la variable paginas en Lector](/assets/img/java-taller-bicis-errores.png){: width="1587" height="780"}

El de `rodar()` dice:

```text
The method rodar(int) in the type Ciclista is not applicable for the arguments (int, Bicicleta)
```

Traducido: el método `rodar` ahora solo pide los kilómetros (`int`), porque el ciclista ya tiene su bicicleta dentro, pero yo le seguía pasando los kilómetros y la bici. Los otros dos son iguales, con `repararCiclistaPreferente` y `revisar`. Los dos de `paginas` son de la biblioteca, que te cuento más abajo. Y las 18 advertencias amarillas son variables que creo y luego no uso: no impiden ejecutar, pero dicen bastante de cómo dejo las cosas a medias. La solución es que la llamada coincida con lo que pide el método:

```java
ciclista.rodar(distanciaRecorridaCiclista);
mecanico1.repararCiclistaPreferente(3);
mecanico2.revisar(ciclista);
```

Lo bueno del error es que te dice exactamente qué pide el método, `rodar(int)`, y qué le has dado, `(int, Bicicleta)`. Un mensaje así en inglés asusta, pero la respuesta suele estar en esas dos líneas.

## Los que dejé a medias

Hay dos que no terminé, y no pasa nada por enseñarlos:

- **Libros** (15 de octubre): el libro sabe avanzar una página y calcular cuántas quedan, pero el `main` llama a `paginasRestantes()` y no hace nada con el resultado. Le falta un `System.out.println(...)` para que se vea algo por pantalla.
- **Biblioteca** (21 de octubre): no compila. En `Lector` escribí `paginas=paginas+1;`, pero `paginas` es un atributo de `Libro`, no de `Lector`. Debería ser algo como `l.leer();`, para que sea el libro el que avance. Además, `prestar()` de la biblioteca no termina de tener sentido, y los objetos que creo en el `main` nunca se usan. Ahí me agobié y lo dejé.

Los dejé así porque me agobié. Prefiero enseñarlos tal cual que esconderlos: también es parte de aprender.

## Si quieres practicar lo mismo

No te voy a dar soluciones copiables, pero sí el orden en que lo he ido haciendo yo:

1. **Una clase sola** con atributos, constructor y un par de métodos (como el cocinero).
2. **Límites con `if`**: que algo no pueda bajar de 0 o pasar de un máximo (como la batería o la cuenta).
3. **Un objeto dentro de otro** (como la linterna y su batería).
4. **Datos por teclado con `Scanner`**, vigilando el salto de línea después de leer números.
5. **Tres o cuatro clases que se relacionan**, como el taller o la cafetería.

Y si te sale un error que no entiendes, pégalo en el [corrector de Java](/herramientas/corrector-java/) que he montado: te explica qué falla y te devuelve el código corregido.

## Lo que me llevo

Al revisar todo junto se ve el avance en un mes, del cocinero a proyectos con cuatro clases. Y casi todos mis fallos se repiten: el `Scanner` con los números, y cambiar un método sin cambiar quien lo llama. La lección es sencilla: ejecutar el programa después de cada cambio, no al final, porque así el error aparece justo donde lo has metido.

Si estás empezando con Java y quieres contarme cómo te va, puedes escribirme a vibo@codeandia.com.
