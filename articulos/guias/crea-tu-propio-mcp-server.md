---
layout: article
title: "Crea tu propio MCP server: conecta una API a tu editor"
description: "Crea un servidor MCP propio en Python para conectar tus APIs y datos al editor con IA. Guía paso a paso, con un servidor real y cómo probarlo."
category: "Guía"
date: 2026-09-22
readtime: 10
---

Si ya has leído lo que es el Model Context Protocol (te lo expliqué en [la guía de MCP para principiantes](/articulos/guias/mcp-para-principiantes-guia-2026/)), seguro que te ha pasado como a mí: te quedas con las ganas de conectarlo a *tus* cosas, no solo a las que otro ya publicó. ¿Y si tu lista de tareas del curso estuviera en una API? ¿Y si quisieras que la IA consultara tu base de datos de apuntes, o los datos de tu API de weather, sin copiar y pegar? Eso es justo lo que puedes hacer, y no es tan difícil como parece cuando te lo pongas. En esta guía montamos un servidor MCP propio, de principio a fin, en Python, y lo conectamos a un editor con IA. Es el paso natural después de entender qué es: dejar de consumir herramientas ajenas y empezar a exponer las tuyas.

## Qué vas a construir y para qué

Vamos a hacer algo concreto y útil: un servidor MCP que exponga **una API de tareas** (crear, listar y completar tareas) como herramientas que la IA pueda invocar. Cuando le escribas a tu editor "añade una tarea comprar café", la IA podrá llamar a tu servidor, que guardará la tarea en tu backend, y te lo confirmará. Sin que tengas que cambiar de ventana ni copiarte JSON.

La razón por la que esto me parece útil de verdad es que **conecta la IA con *tus* datos, no con datos genéricos de internet**. Los servidores MCP que ya existen te dan acceso a archivos, a bases de datos de ejemplo, a documentación. El tuyo te da acceso a *tu* proyecto, *tus* notas, *tu* API. Y una vez que tienes el primer servidor funcionando, el segundo es cambiar unas líneas.

## La Anatomía de un servidor MCP (lo mínimo)

Un servidor MCP no es más que un programa que habla un protocolo concreto para *exponer herramientas*. En la práctica, todo se reduce a tres cosas que el servidor declara:

1. **Nombre e instrucciones**: qué es y cómo usarlo.
2. **Herramientas (tools)**: las funciones que la IA puede llamar, cada una con sus parámetros.
3. **La ejecución**: cuando la IA llama a una herramienta, tu código la ejecuta y devuelve un resultado.

Si vienes de Python, te adelanto la buena noticia: existe un SDK oficial (`mcp`) que se encarga de todo el protocolo por ti. Tú solo escribes las funciones y las "decoras" con un decorador que dice cómo se llama y qué parámetros tiene. Es la misma idea que cuando expones una función para que otra cosa la use, pero con un estándar que los editores con IA ya saben entender.

## Paso 1: preparar el entorno

Crea una carpeta para el servidor y aísla el entorno. Python 3.10 o superior, y el SDK:

```bash
mkdir mcp-tareas
cd mcp-tareas
python -m venv .venv
# Activa el entorno (Windows: .venv\Scripts\activate | Linux/Mac: source .venv/bin/activate)
pip install mcp
```

Trabajar con un entorno virtual aquí es la misma buena práctica que te resumo en [la guía de docker para DAW](/articulos/guias/docker-para-daw-con-ia-2026/): aislar dependencias para que no se te rompa nada global. Si más adelante quieres llevarlo a otra máquina o compartirlo, dockerizarlo es el siguiente paso natural.

## Paso 2: tu primera herramienta

Vamos a escribir el servidor. Cada herramienta es una función async con un decorador `@mcp.tool()` que declara su nombre y descripción. La descripción es **clave**: es lo que la IA lee para saber cuándo usarla, así que tiene que estar escrita pensando en la IA, no en tu colega humano.

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mis-tareas")

# Nuestra "base de datos" en memoria (para el ejemplo; luego la conectamos a una API real)
TAREAS = []

@mcp.tool()
def listar_tareas() -> list[str]:
    """Devuelve la lista de tareas pendientes. Úsala cuando el usuario pregunte qué tiene pendiente."""
    return TAREAS

@mcp.tool()
def anadir_tarea(tarea: str) -> str:
    """Añade una nueva tarea a la lista. Úsala cuando el usuario quiera crear o apuntar una tarea."""
    TAREAS.append(tarea)
    return f"Tarea añadida: {tarea}"

@mcp.tool()
def completar_tarea(tarea: str) -> str:
    """Marca una tarea como completada. Úsala cuando el usuario diga que ya ha terminado algo."""
    if tarea in TAREAS:
        TAREAS.remove(tarea)
        return f"Tarea completada: {tarea}"
    return f"No encontré la tarea: {tarea}"

if __name__ == "__main__":
    mcp.run()
```

Fíjate en lo poco que hay. Tres funciones, tres decoradores, y ya tienes un servidor MCP que expone tres herramientas. Lo bonito de esto es que la lógica de negocio (aquí, una lista en memoria) es independiente del protocolo: cuando quieras conectarlo a una base de datos real o a tu API del curso, solo cambias el cuerpo de las funciones. El andamiaje MCP no se toca.

Y un detalle que parece pequeño pero lo es todo: **las descripciones en las herramientas**. "Devuelve la lista de tareas pendientes" es mucho mejor que "lista tareas". La IA decide si llamar a una herramienta o no basándose en esas descripciones, así que escribirlas para la IA es parte del trabajo, no un adorno. Si te interesa el mindset de cómo escribir estas descripciones, es el mismo que uso en [la guía de agents.md](/articulos/guias/agents-md-guia-2026/), donde explico cómo darle a la IA contexto para que sepa qué hacer.

## Paso 3: conectarlo a tu editor

Ahora la parte que da miedo y que en realidad es copiar un JSON. Los editores con IA (Claude Desktop, Cursor, Windsurf) leen la configuración de servidores MCP desde un archivo. En Claude Desktop, por ejemplo, editas `claude_desktop_config.json` y le añades una entrada con el comando para arrancar tu servidor:

```json
{
  "mcpServers": {
    "mis-tareas": {
      "command": "python",
      "args": ["ruta/a/mcp-tareas/servidor.py"]
    }
  }
}
```

Guardas, reinicias el editor, y en el panel de herramientas (o en la conversación) debería aparecer tu servidor con sus tres herramientas. **Si usas Claude Desktop**, el atajo para probarlo sin editor es abrir una conversación y preguntarle directamente "¿qué tareas tengo pendientes?". Si usas Cursor o VS Code con Continue, el formato es parecido pero el archivo va en otro sitio; la documentación del MCP de cada editor te dice dónde.

**El truco de depuración:** si algo no aparece, casi siempre es que el comando o la ruta están mal, o que el entorno virtual no está activo desde donde se llama. Ejecuta `python servidor.py` a mano en una terminal: si arranca y se queda escuchando sin errores, tu servidor está bien y el problema es de configuración del editor. Este mismo método de "aislar para encontrar dónde está el fallo" es el que uso siempre, y lo detallo en [depurar código con IA](/articulos/guias/depurar-codigo-con-ia-guia-2026/).

## Paso 4: del prototipo a algo real

La lista en memoria es perfecta para aprender, pero se olvida al reiniciar. Cuando quieras algo de verdad, el cambio es pequeño: en lugar de tocar un `TAREAS.append(...)`, haces una llamada a tu API o a tu base de datos. Y aquí es donde este proyecto se vuelve realmente potente: si tus tareas están en la API de tu curso, o en una base de datos con tus apuntes, la IA puede consultarlas y escribirlas **sin que tengas que exportar nada**.

Para conectar una API real en Python, el flujo es:
1. **Leer**: haces un `GET` a tu endpoint y devuelves los datos como texto o JSON (el SDK se encarga de envolverlo).
2. **Escribir**: haces un `POST`/`PUT` con los datos que te pasa la IA.
3. **Errores**: si la API devuelve un error, devuelves un mensaje claro en lugar de reventar; la IA lo verá y puede corregir.

Ese "devolver errores claros en vez de reventar" es importantísimo, y aplica a todo lo que construyas con IA, no solo a MCP. Es la diferencia entre una herramienta que la IA usa bien y una con la que se frustra en bucle. Ya lo expliqué más a fondo cuando hablé de [conectar un frontend con una API](/articulos/guias/conectar-frontend-api-con-ia-2026/), y aplica igual aquí.

## Un consejo sobre seguridad antes de que publiques nada

Un servidor MCP da a la IA la capacidad de **ejecutar acciones** en tu sistema. Con la lista en memoria no pasa nada, pero en cuanto lo conectes a una API real o a ficheros, estás dándole a un modelo la capacidad de escribir en tus datos. Dos precauciones que me tomo siempre:

- **Empieza en modo lectura.** Conecta primero una herramienta que solo *lea*, comprueba que va bien, y solo después añade las que escriben.
- **No lo expongas a datos sensibles.** Nada de claves, contraseñas o datos personales en lo que la IA puede leer. Piensa en el servidor MCP como si le estuvieras dando las llaves de casa: Dale solo las habitaciones que necesite.

Esto no es paranoia, es sentido común. Si vas a montar algo que toque una base de datos real, dedicate un rato a [la guía de seguridad con IA](/articulos/guias/prompt-injection-seguridad-apps-ia-2026/), porque los mismos principios (qué puede tocar la IA, con qué datos, bajo qué condiciones) son los que te protegen aquí.

## Mi veredicto

Crear tu propio servidor MCP es de esas cosas que parecen de nivel avanzado y que en realidad son "escribir tres funciones y decorarlas". El protocolo se encarga de lo difícil, el SDK te quita la parte aburrida, y tú te quedas con la parte interesante: **exponer tus propios datos a la IA de una forma que ella entiende y puede usar**. Es el puente entre "hablar con un chatbot" y "programar con un asistente que de verdad toca tus cosas", y es la misma dirección en la que va todo el sector.

Mi recomendación: haz el ejemplo de la lista primero (es una tarde), luego conéctalo a una API real que tengas, y verás cómo la IA pasa de responderte a *hacerte* cosas. Si te animas y quieres ir más allá, el siguiente salto natural es escribir las descripciones de las herramientas con el mismo cuidado con el que escribes un buen prompt, porque en el fondo es eso: un prompt que la IA lee antes de actuar.

¿Lo pruebas y me cuentas? Si te atascas con la configuración del editor, con el JSON, o quieres que lo adaptemos a la API de tu proyecto, escríbeme a ivan@codeandia.com y lo montamos paso a paso. Y si te ha gustado la guía, no te olvides de la parte más aburrida pero imprescindible: un buen [git bien usado](/articulos/guias/git-con-ia-2026/) por si tocas algo y tienes que volver atrás.

## Sigue por aquí

- [Tu primera app con la API de OpenAI en Python, paso a paso](/articulos/guias/primera-app-api-openai-python/)
