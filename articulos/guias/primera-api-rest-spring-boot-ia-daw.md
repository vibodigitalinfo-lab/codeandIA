---
layout: article
title: "Cómo hacer tu primer API REST con Spring Boot e IA"
description: "Guía para DAW: crea tu primer API REST con Spring Boot usando IA desde el pom hasta el deploy, con los errores reales que me costó depurar."
category: "Guía"
date: 2026-09-01
readtime: 8
---

El primer día que tuvimos que entregar una API REST en la asignatura de servidor, me pasé toda la tarde viendo el esqueleto de Spring Boot sin saber por dónde empezar. Luego dejé que la IA escribiera el código por mí y las cosas empeoraron: me daba endpoints que no compilaban, dependencias que no existían y ningún contexto de lo que se pedía. Ahora, con un par de proyectos a mis espaldas, esta guía es exactamente lo que me habría gustado tener ese día. No es "copia y pega y ya": es el orden en el que usar la IA para que te enseñe, no para que decida por ti.

## Antes de escribir una sola línea

Necesitas tres cosas: un JDK decente (Java 21 o superior), IntelliJ IDEA gratis o VS Code con la extensión de Java, y acceso a una IA (Copilot en el editor, ChatGPT o Claude en el navegador). Nada de esto requiere pagar. Si vas a usar Copilot dentro de IntelliJ, tengo una [guía para configurarlo paso a paso](/articulos/guias/github-copilot-intellij-java-daw/) que te ahorra los típicos veinte minutos peleándote con el login.

La clave de esta parte es saber qué pides. Spring Boot tiene cientos de dependencias; la IA te va a sugerir las típicas, pero tú decides cuáles entran. Para el clásico ejercicio de DAW (gestionar una lista de alumnos), con tres basta: **Spring Web** para los endpoints, **Spring Data JPA** para la persistencia y **H2** para la base de datos en memoria. Eso es lo mínimo, y lo aprendí porque Spring Initializr genera el proyecto con un par de clicks y te añade el `.pom` correspondiente. Pídeselo a la IA si quieres, pero échale un vistazo y verás que son exactamente esas tres.

## El primer endpoint: que te lo explique, no que te lo escriba

Mi error de la primera tarde fue pedir "dame el código de un CRUD completo". Me lo dio, claro, y no entendía nada. Lo que funciona es pedirlo en pasos pequeños con una condición: cada vez que la IA genere una clase, preguntar "¿qué hace aquí `@RestController`?" o "¿por qué la entidad lleva `@Entity`?". La IA es un profesor increíblemente paciente; deja que lo sea.

El primer paso real es el controlador. Empieza con un único `GET` que devuelva una lista vacía. Debe quedar algo así, aunque no hace falta que sea idéntico:

```java
@RestController
@RequestMapping("/api/alumnos")
public class AlumnoController {
    @GetMapping
    public List<Alumno> listar() {
        return List.of();
    }
}
```

Te adelanto el primer problema que vas a encontrar: devuelves la entidad directamente y, en cuanto añadas una relación entre clases, Jackson se atraganta al convertirla a JSON. Aquí la IA te va a responder "añade un DTO", y tendrá razón, pero esa respuesta vale el doble si antes lo has visto fallar tú con tus propios ojos.

## Entidad, repositorio y el momento en que algo "cliquea"

Con la base del controlador funcionando, toca la entidad. Una clase `Alumno` con `id`, `nombre`, `email` y `curso`. Aquí la IA brilla para enseñarte las anotaciones: `@Entity`, `@Id`, `@GeneratedValue`. La meto en su sitio, le doy al compile, y hasta aquí todo en orden.

El repositorio es donde mejor se ve la diferencia entre copiar y entender:

```java
public interface AlumnoRepository extends JpaRepository<Alumno, Long> {}
```

Esa interfaz vacía parece magia, y la primera vez lo es. Pregúntale a la IA qué métodos te da *gratis* solo por heredar de `JpaRepository`: `findAll`, `findById`, `save`, `deleteById`. Cuando lo verbaliza y lo escribes tú, el CRUD deja de ser un concepto abstracto.

En este punto toca CORS, porque el lunes siguiente, cuando en el módulo de cliente intentes llamar a tu API desde el HTML de siempre, el navegador va a bloquear la petición. Un `@CrossOrigin` en el controlador y se acabó el susto. Es el aviso que la IA no te da por placer: lo olvidé yo, lo olvidarás tú.

## Probar de verdad: Postman, curl y el error que nadie te cuenta

La tentación es "ya compila, ya está". No lo está. Ábrelo en el navegador con `http://localhost:8080/api/alumnos` o lanza un `curl`. Y aquí aparece el fallo del que nadie habla en clase: si perdiste diez minutos buscando por qué no te da respuesta, y en el log no sale nada raro, revisa si el `server.port` está ocupado por otra instancia que dejaste abierta. Me pasó tres veces seguidas, y las tres fue eso.

Para el POST, recuerda que el cuerpo que envías debe tener exactamente los nombres de campo que espera el JSON. La IA te da el endpoint, pero los nombres los defines tú en la entidad. Un `alumno.json` con `{"nombre": "Ana", "curso": "2DAW"}` que no casa con tu clase te va a dar un 400 sin más explicación. Léelo dos veces antes de culpar al framework.

## El prompt que me funciona (y lo que la IA no debe decidir)

Después de mucho ensayo, el prompt que mejor me rinde es corto y con tres requisitos. Algo así: "Estoy en DAW, con Spring Boot 3 y Java 21. Dame solo el controlador para un GET que devuelva una lista de alumnos, explícame cada anotación y dime qué comando Maven uso para arrancarlo". Pidiendo el porqué y el comando, la respuesta deja de ser un bloque que no entiendes y pasa a ser una clase particular.

Dos cosas que la IA no debe decidir por ti. La primera: si te añade **Spring Security** el primer día, di que no. Te va a meter un login que rompe tus pruebas y que no toca ese módulo. La segunda: los números de versión de las dependencias. La IA los inventa de vez en cuando y el proyecto no arranca. Los copias del Spring Initializr y te quitas el problema.

Y una herramienta que casi nadie usa: la consola de H2 en `http://localhost:8080/h2-console`, con la URL `jdbc:h2:mem:testdb`. Ahí ves si tu `save()` guardó de verdad o si el POST devolvió 200 pero no persistió nada. Un vistazo y sabes si el fallo está en la entidad o en el controlador.

## El deploy: lo que diferencia un 5 de un 10

El profe no dijo "súbela", pero la diferencia entre enseñar el proyecto en local y enseñar una URL que abre en el móvil es abismal. Para un estático hay mil opciones gratis; para una API con JPA necesitas algo que ejecute Java. Aquí el socio más rápido para un estudiante es un hosting con Tomcat: subes el `.jar` generado por Maven, configuras la base y listo. Es el mismo Hostinger que analicé en mi [review de Hostinger](/articulos/reviews/hostinger-review-2026/) y que comparo con la alternativa gratis en la [guía de qué hosting elegir en DAW](/articulos/guias/que-hosting-elegir-estudiantes-daw-2026/), donde está la letra pequeña de los planes.

No hace falta que lo hagas el primer día. El veredicto real es el de siempre: la API entera la hiciste tú, con la IA ejerciendo de profesor y traductor, no de autómata. Mi consejo final para el módulo es que dediques la primera sesión a entender el `GET` que devuelve `List.of()`, porque cuando ese endpoint responde, ya tienes el 80% del camino andado. El 20% restante es variar los verbos HTTP y aguantar los CORS de la práctica siguiente. Si el tuyo se cuelga en el segundo endpoint, me lo cuentas cuando quieras y te digo por dónde tirar.