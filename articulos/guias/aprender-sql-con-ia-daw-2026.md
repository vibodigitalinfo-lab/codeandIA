---
layout: article
title: "SQL y bases de datos con IA: aprende practicando en 2026"
description: "Guía de SQL con IA para estudiantes de DAW: laboratorio gratis, prompts que enseñan de verdad, cómo practicar sin copiar y errores que te delatan."
category: "Guía"
date: 2026-09-14
readtime: 7
---

SQL tiene fama injusta. En DAW nadie le da miedo al principio —tres `SELECT` para aprobar el módulo y a otra cosa— y luego resulta que es, de lejos, la habilidad que más se pide en las ofertas junior que miran los estudiantes. Es feo de asumir, pero es así: no hay stack moderno sin base de datos.

La buena noticia es que SQL es seguramente **la asignatura más fácil de aprender con IA en 2026**: los errores son crípticos pero los modelos los pillan de una, el feedback es inmediato y el terreno de prácticas es gratis. La mala noticia: la IA también permite estudiar fatal si la usas como ChatGPT para copiar en vez de como profesor particular. Te explico el sistema que a mí me funcionó.

## Por qué la IA es perfecta para aprender SQL

- **Feedback inmediato que ningún profesor te da a las 11 de la noche**: le pegas tu query rota y te dice en dos líneas dónde falla.
- **Explica el "por qué"**: puedes pedirle que te cuente *por qué* un `LEFT JOIN` te duplica filas, no solo qué pegaste mal.
- **Puedes tener base de datos y datos de prueba en segundos**: montar un entorno real de MySQL en prácticas es un deporte de riesgo; con SQLite lo tienes en un minuto.
- **No juzga**: el error de las 14:00 te lo corrige igual que el de las 9:00.

Pero con un requisito: **tú ejecutas, ella explica**. Si el modelo escribe y tú solo pegas el resultado, estás perdiendo el tiempo a máxima velocidad.

## Monta tu laboratorio (gratis, en 10 minutos)

Para practicar no necesitas el MySQL del instituto. Dos opciones según el momento:

- **SQLite + DB Browser for SQLite** (la que uso yo para estudiar): un solo archivo `.db`, sin servidor, sin configurar nada. Perfecta para hacer cien ejercicios mientras esperas el bus.
- **MySQL** (vía XAMPP o Docker) cuando quieras practicar con lo que de verdad usa tu centro y las ofertas: tipos más estrictos, usuarios, `mysqldump`. Los conceptos SQL son 90% iguales.

El truco que me enganchó: **pídele a la IA que genere la base de datos con datos de prueba realistas** para el tema que toque. ¿Estás estudiando `JOIN`? Pide un `alumnos`, `modulos`, `notas` con 30 filas que tengan alumnos sin matrícula y módulos sin notas. Practicar con datos raros (nulos, duplicados) es lo que de verdad enseña.

La forma más simple de tenerlo: genera el `.sql`, ejecútalo en el DB Browser... o directamente monta la base en Python memorizando nada:

```python
import sqlite3
conn = sqlite3.connect("practicas.db")   # crea el archivo si no existe
conn.executescript(script_sql_de_la_ia)
```

## Los prompts que de verdad enseñan

Estos son los cuatro que repito cada semana:

**1. "Explícame el error de esta query sin decirme la solución"** Este prompt es el mejor que existe: el modelo te apunta a la línea y el porqué, y la solución la buscas tú. Aprender del propio error es lo que más se queda.

**2. "Revisa mi query como un entrevistador senior: ¿hay N+1? ¿índices? ¿algo de rendimiento?"** Cuando ya sabes escribir consultas, este prompt te mete los conceptos profesionales que no estudiamos en el módulo: `EXPLAIN`, planes de ejecución, por qué un `SELECT *` en un `JOIN` de 5 tablas es un pecado.

**3. "Quiero practicar [tema]. Dame 5 ejercicios en orden de dificultad y corrígelos como un profesor"** Entrena el feedback en cadena: le dices tu solución, te la corrige y te da la siguiente. Es la experiencia profesor particular más barata que he encontrado.

**4. "Explica este plan de ejecución como si tuviera 12 años"** `EXPLAIN QUERY PLAN` o el equivalente de tu base te escupe cosas ilegibles; el modelo las traduce. Es como ver la respuesta del servidor, pero en español.

## Los 5 errores que te delatan

Esto es lo que hace que un examen o una entrevista te saquen del juego aunque hayas aprobado:

**1. No escribir SQL a mano.** Si solo copias lo que escupe la IA, el día que no escribas con fluidez de memoria (examen, entrevista, hora punta en producción) te quedas en blanco. Escribe cada query tú; que la IA la corrija, que no la teclee.

**2. No saber qué hace la query que "tú hiciste".** Regla de oro: *nunca entregues una query que no puedas explicar frase por frase.* Si te preguntan por el `HAVING` y no sabes por qué está, da igual quién la escribiera: eres tú quien la firma.

**3. Depender del copiar-pegar de datos.** Si pides datos de prueba otra vez, o te aprendes de memoria la salida de un ejercicio, no estás practicando el razonamiento. Cambia los datos cada vez.

**4. Saltarte los `JOIN`.** Encadenar tablas es el 60% de las preguntas de bases de datos en entrevistas junior. Practícalos hasta que el `LEFT JOIN` con datos nulos no te saque de quicio.

**5. Confundir "que funcione" con "que esté bien".** Una query que devuelve lo que toca pero con un `WHERE` mal pensado o un cartesiano escondido pasa el examen y explota en producción. Pide el prompt 2 (rendimiento) aunque no te lo pidan.

## Más allá del módulo: por qué esto te va pagando

SQL no es solo el módulo: es la columna vertebral de casi todo lo que usas cada día —pedirle al dashboard de una empresa "los clientes que más repiten" es SQL con otra ropa. Saber quitarle el miedo añade un filtro muy real en tu primer curro.

Y aquí está lo que nadie te dice: **la IA potencia esto, no lo sustituye.** Los datos se siguen simulando, consultando y defendiendo a mano. Yo usaría la IA como el compañero de prácticas que corrige tus ejercicios, no como la persona que te los hace. Cuando se trata de bases de datos, la diferencia entre "lo hice yo" y "lo hizo la IA" se nota al primer `SELECT` de una entrevista.

Esto encaja con la [preparación de entrevistas que ya te conté con IA](/articulos/guias/de-practicas-a-primer-curro-con-ia/), y con el paquete de prompts que te dejé en el artículo de [los 8 que me salvan el curso](/articulos/listas/8-prompts-programacion-daw-2026/). Si gestionas tus apuntes de bases de datos en Markdown, combínalo con un [RAG local](/articulos/guias/rag-local-ollama-apuntes-2026/) para preguntar "¿qué era inner join?" a tu propia documentación y tendrás el set completo.

## Conclusión

Mi veredicto: **aprender SQL con IA es la decisión más barata y rentable de tu año si lo haces bien.** Gratis para montar el laboratorio, gratis para entrenar, y con una regla que te enseñará a trabajar: la IA propone, tú decides.

Empieza esta tarde:
1. Abre el DB Browser, pide a una IA una base de datos de prácticas con datos feos (nulos, duplicados).
2. Resuelve 5 ejercicios SIN que la IA te dé la solución.
3. Cuando falles, usa el prompt 1 para entender el error.
4. El viernes, llama al prompt 2 y revisa tus consultas como "senior".

Cuando sepas qué módulo de bases de datos te toca, mándame un correo a ivan@codeandia.com con el temario y te devuelvo diez ejercicios por cada tipo de query que vayas a ver.
