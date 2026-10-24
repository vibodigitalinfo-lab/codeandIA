---
layout: article
title: "Ejercicios Java para principiantes: 8 prácticas con soluciones"
description: "Ocho ejercicios de Java para principiantes con su solución explicada: del Scanner a dos clases que se relacionan. Un regalo para facilitar tu estudio."
category: "Guía"
date: 2026-10-23
updated: 2026-10-23
readtime: 10
last_modified_at: 2026-10-23
---

## Un regalo para que practiques Java sin complicaciones

Estudio primero de DAW, el ciclo de FP de desarrollo de aplicaciones web en España, y Java es mi primera asignatura de programación. Si algo he aprendido con mi primer examen es que Java no se aprende leyendo, se aprende escribiendo código. Yo empecé tarde por pereza y me costó más de lo necesario.

Lo que más me costó al principio fue la sintaxis del `Scanner`: me liaba con `nextInt()`, `nextLine()` y compañía, y casi siempre los ponía mal. Después se me atascaron los ejercicios en los que un objeto depende de otro, porque no conseguía entender cómo se relacionaban. Cuando lo ves, todo se vuelve mucho más sencillo.

Por eso te dejo **8 ejercicios de Java básicos** con su solución. Empiezan por el `Scanner` y acaban con dos clases que se relacionan, que es justo donde yo me atascaba. Cada uno lleva su enunciado, el código completo y una explicación de lo que hace. Los he preparado con ayuda de una IA y no son los del profesor. Cópialos, pruébalos en Eclipse (o en el IDE que uses) y modifícalos a tu gusto.

Los ofrezco como regalo para facilitarte el estudio. No necesitas registrarte ni dar ningún dato.

---

### Ejercicio 1: Datos del alumno

**Enunciado:** Crea un programa que pida por teclado el nombre del alumno, su edad y la nota de un examen, y los muestre por pantalla.

**Código:**

{% raw %}
```java
import java.util.Scanner;

public class DatosAlumno {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Nombre del alumno: ");
        String nombre = sc.nextLine();
        
        System.out.print("Edad: ");
        int edad = sc.nextInt();
        
        System.out.print("Nota del examen: ");
        double nota = sc.nextDouble();
        
        System.out.println("\n--- Datos del alumno ---");
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Nota: " + nota);
        
        sc.close();
    }
}
```
{% endraw %}

**Qué hace:** Usa `Scanner` para leer datos por teclado, guarda los valores en variables y los imprime con `System.out.println`.

---

### Ejercicio 2: Calculadora simple

**Enunciado:** Pide dos números por teclado y muestra la suma, resta, multiplicación y división.

**Código:**

{% raw %}
```java
import java.util.Scanner;

public class CalculadoraSimple {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Primer número: ");
        double a = sc.nextDouble();
        
        System.out.print("Segundo número: ");
        double b = sc.nextDouble();
        
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        
        if (b != 0) {
            System.out.println("División: " + (a / b));
        } else {
            System.out.println("División: no se puede dividir entre cero");
        }
        
        sc.close();
    }
}
```
{% endraw %}

**Qué hace:** Realiza las cuatro operaciones básicas y comprueba que el divisor no sea cero antes de dividir.

---

### Ejercicio 3: ¿Par o impar?

**Enunciado:** Pide un número entero y di si es par o impar.

**Código:**

{% raw %}
```java
import java.util.Scanner;

public class ParOImpar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Introduce un número entero: ");
        int numero = sc.nextInt();
        
        if (numero % 2 == 0) {
            System.out.println("Es par");
        } else {
            System.out.println("Es impar");
        }
        
        sc.close();
    }
}
```
{% endraw %}

**Qué hace:** Usa el operador módulo `%` para saber si el resto de dividir entre 2 es cero.

---

### Ejercicio 4: Números del 1 al 10

**Enunciado:** Muestra por pantalla los números del 1 al 10, uno por línea.

**Código:**

{% raw %}
```java
public class Numeros1al10 {
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
        }
    }
}
```
{% endraw %}

**Qué hace:** Un bucle `for` que comienza en 1 y termina cuando `i` llega a 10.

---

### Ejercicio 5: Tabla de multiplicar

**Enunciado:** Pide un número por teclado y muestra su tabla de multiplicar del 1 al 10.

**Código:**

{% raw %}
```java
import java.util.Scanner;

public class TablaMultiplicar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("¿Tabla de qué número quieres ver? ");
        int n = sc.nextInt();
        
        for (int i = 1; i <= 10; i++) {
            System.out.println(n + " x " + i + " = " + (n * i));
        }
        
        sc.close();
    }
}
```
{% endraw %}

**Qué hace:** Combina un bucle `for` con la entrada de datos por teclado.

---

### Ejercicio 6: Nota media y aprobado

**Enunciado:** Pide las notas de tres exámenes, calcula la media y di si el alumno ha aprobado (media igual o superior a 5).

**Código:**

{% raw %}
```java
import java.util.Scanner;

public class NotaMedia {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Nota del primer examen: ");
        double n1 = sc.nextDouble();
        
        System.out.print("Nota del segundo examen: ");
        double n2 = sc.nextDouble();
        
        System.out.print("Nota del tercer examen: ");
        double n3 = sc.nextDouble();
        
        double media = (n1 + n2 + n3) / 3;
        
        System.out.println("Nota media: " + media);
        
        if (media >= 5) {
            System.out.println("Has aprobado");
        } else {
            System.out.println("Has suspendido");
        }
        
        sc.close();
    }
}
```
{% endraw %}

**Qué hace:** Calcula la media aritmética y usa un condicional para decidir si se aprueba.

---

### Ejercicio 7: Contar vocales

**Enunciado:** Pide una palabra por teclado y cuenta cuántas vocales tiene.

**Código:**

{% raw %}
```java
import java.util.Scanner;

public class ContarVocales {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Escribe una palabra: ");
        String palabra = sc.nextLine().toLowerCase();
        
        int contador = 0;
        
        for (int i = 0; i < palabra.length(); i++) {
            char letra = palabra.charAt(i);
            if (letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u') {
                contador++;
            }
        }
        
        System.out.println("La palabra tiene " + contador + " vocales");
        
        sc.close();
    }
}
```
{% endraw %}

**Qué hace:** Recorre la palabra letra a letra con un bucle y cuenta cuántas son vocales.

---

### Ejercicio 8: Un libro y su autor

**Enunciado:** Crea una clase `Autor` con nombre y país, y una clase `Libro` con título y un autor. Desde un `main`, crea un autor, crea un libro que lo use y muestra por pantalla los datos del libro junto con los de su autor. Cada clase va en su propio archivo.

**Código (`Autor.java`):**

{% raw %}
```java
public class Autor {
    String nombre;
    String pais;

    public Autor(String nombre, String pais) {
        this.nombre = nombre;
        this.pais = pais;
    }
}
```
{% endraw %}

**Código (`Libro.java`):**

{% raw %}
```java
public class Libro {
    String titulo;
    Autor autor;

    public Libro(String titulo, Autor autor) {
        this.titulo = titulo;
        this.autor = autor;
    }

    public void mostrar() {
        System.out.println(titulo + " - " + autor.nombre + " (" + autor.pais + ")");
    }
}
```
{% endraw %}

**Código (`Biblioteca.java`):**

{% raw %}
```java
public class Biblioteca {
    public static void main(String[] args) {
        Autor cervantes = new Autor("Miguel de Cervantes", "España");
        Libro quijote = new Libro("Don Quijote de la Mancha", cervantes);

        quijote.mostrar();
    }
}
```
{% endraw %}

**Qué hace:** El `Libro` guarda dentro un objeto `Autor`. Primero se crea el autor y después se le pasa al libro al construirlo. Desde el libro llegas a los datos del autor con `autor.nombre`. Esta idea de un objeto que contiene a otro es lo que a mí me costaba ver al principio.

---

## Dónde me atascaba yo

- **`nextInt()` y `nextLine()` juntos.** Es lo que más me fastidió con el `Scanner`. Si lees un número con `nextInt()` y justo después pides texto con `nextLine()`, el programa parece saltarse la pregunta: el número se lee, pero el salto de línea que escribiste al pulsar Intro se queda pendiente y `nextLine()` lo toma como una línea vacía. En el ejercicio 1 lo evito leyendo primero el texto, y si te hace falta el orden contrario, puedes poner un `sc.nextLine();` suelto después del número para limpiar ese salto de línea.
- **Objetos que dependen de otros.** Me atascaba porque no conseguía entender cómo se relacionaban. Lo que te puedo decir es que, una vez que lo ves, se hace muchísimo más sencillo. Si te pasa lo mismo, fíjate en el ejercicio 8: el autor tiene que existir antes de crear el libro, porque el libro lo recibe al construirse.

## Lo que haría diferente

Si pudiera volver atrás, empezaría a hacer ejercicios desde el primer día del curso, no solo cuando se acerca el examen. Con Java, como con casi todo en programación, lo importante no es memorizar sino practicar. Cuanto antes empieces a escribir código tú mismo, menos te costará el examen.

Si te sirven estos ejercicios o quieres contarme cómo te va con ellos, puedes escribirme a ivan@codeandia.com.