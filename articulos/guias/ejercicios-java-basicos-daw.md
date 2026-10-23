---
layout: article
title: "Ejercicios Java básicos para principiantes: 7 prácticas con soluciones"
description: "Siete ejercicios de Java para principiantes, con código y soluciones explicadas paso a paso. Un regalo para facilitar tu estudio."
category: "Guía"
date: 2026-10-23
updated: 2026-10-23
readtime: 7
last_modified_at: 2026-10-23
---

## Un regalo para que practiques Java sin complicaciones

Si algo he aprendido esta semana con mi primer examen de programación es que Java no se aprende leyendo, se aprende escribiendo código. Yo empecé tarde por pereza y me costó más de lo necesario, así que no quiero que te pase lo mismo.

A continuación te dejo **7 ejercicios de Java básicos**, pensados para primero de DAW, cada uno con su enunciado, el código completo y una explicación sencilla de lo que hace. Los puedes copiar, probar en Eclipse (o en el IDE que uses en clase) y modificar a tu gusto.

Los ofrezco como regalo para facilitarte el estudio. No necesitas registrarte ni dar ningún dato: cópialos, pruébalos y úsalos.

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

## Errores comunes al empezar con Java

- **Olvidar `import java.util.Scanner;`**: sin él, el programa no sabe leer datos por teclado.
- **No cerrar el `Scanner`**: no rompe el programa, pero es buena costumbre hacer `sc.close()` al final.
- **Confundir `nextInt()` con `nextLine()`**: si lees un número con `nextInt()` y luego intentas leer texto con `nextLine()`, el programa se salta la lectura. Es uno de los fallos más típicos al principio.
- **Dividir entre cero**: siempre comprueba que el divisor no sea cero antes de hacer una división.

## Lo que haría diferente

Si pudiera volver atrás, empezaría a hacer ejercicios desde el primer día del curso, no solo cuando se acerca el examen. Con Java, como con casi todo en programación, lo importante no es memorizar sino practicar. Cuanto antes empieces a escribir código tú mismo, menos te costará el examen.

Si te sirven estos ejercicios o quieres contarme cómo te va con ellos, puedes escribirme a ivan@codeandia.com.