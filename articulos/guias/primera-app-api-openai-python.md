---
layout: article
title: "Tu primera app con la API de OpenAI en Python, paso a paso"
description: "Guía para crear tu primera app con la API de OpenAI en Python: API key, SDK, un asistente de terminal que explica errores y controlar el gasto."
category: "Guía"
date: 2026-09-17
readtime: 8
---

Usar ChatGPT en la web es gratis y muy cómodo. Pero hay una frontera que se nota mucho cuando la cruzas: **llamar a la API de OpenAI directamente y construir tu propia herramienta**. Es la diferencia entre que la IA te ayude y que tú le digas a la IA qué hacer con tus datos.

En este artículo te cuento cómo hice mi primera app con la API de OpenAI en Python: crear la clave, instalar el SDK, una primera llamada, una app de terminal que explica errores y, lo más importante para un estudiante sin presupuesto, **cuánto cuesta de verdad**.

## Qué necesitas antes de empezar

- Una cuenta en **platform.openai.com** (distinta de la cuenta de ChatGPT normal).
- Una **API key** en `platform.openai.com/api-keys`. Al crear la cuenta suelen darte unos créditos de regalo; verifícalo tú al registrarte porque cambia con el tiempo.
- **Python 3.10 o superior** y `pip`.
- Nunca, nunca, subas tu key a GitHub. En la sección de errores te cuento cómo la lié yo la primera vez.

Seguridad de la clave: la guardo en un fichero `.env` que tengo en `.gitignore`, y la leo con `python-dotenv`. Así no se cuela en tus repositorios de prácticas.

## La primera llamada (en serio)

Instala el SDK oficial:

```bash
pip install openai python-dotenv
```

Crea un `.env` en la raíz de tu proyecto:

```bash
OPENAI_API_KEY=sk-...
```

Y el programa más pequeño que funciona:

```python
from openai import OpenAI
client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": "Explicas errores de Java a estudiantes de DAW en español y de forma sencilla."},
        {"role": "user", "content": "¿Qué significa NullPointerException?"},
    ],
)
print(resp.choices[0].message.content)
```

Ejecutas con `python app.py` y tienes tu primer LLM de verdad. La llamada `chat.completions.create` es la más estable de la API: `model` vale por el nombres de acceso del modelo (en septiembre de 2026, `gpt-5-mini` es mi opción por defecto) y `messages` es la lista de turnos. El `system` fija el comportamiento; el resto son el historial.

Un apunte: OpenAI tiene ahora también la **Responses API**, más nueva y pensada para agentes con herramientas. Si comes de `chat.completions`, vas bien; sepas que existe y que `responses.create` es lo que usa todo lo nuevo en 2026.

## Tu primera app útil: un asistente que explica errores

La web de ChatGPT te vale si pegas y copias a mano. El salto es cuando automatizas. Mi primera app real fue un pequeño script que recibe un log o un error por `stdin`, lo manda al modelo y te lo explica sin que tengas que abrir el navegador:

```python
import sys
from openai import OpenAI

client = OpenAI()
error = sys.stdin.read()[:4000]  # trunco para no mandar logs kilométricos

resp = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": "Explicas errores de programación a estudiantes en español. Si te falta contexto, pregúntalo. No inventes."},
        {"role": "user", "content": f"Estoy haciendo mis prácticas de DAW y me sale este error:\n\n{error}"},
    ],
)
print(resp.choices[0].message.content)
```

El uso es tan cómodo como:

```bash
cat log.txt | python explica_error.py
```

Detalles que aprendí con el uso:

- **Trunca la entrada.** Límite de 4.000 caracteres me basta y evito mandar medio log de Spring por token.
- **Pídele que pregunte si falta contexto.** Con un `system` así, deja de darte respuestas genéricas.
- **Manda solo la traza relevante.** Filtrar antes de llamar a la API baja el coste y sube la calidad.

## Cuánto cuesta de verdad (septiembre 2026)

Aquí va el mito que había que romper: **no, una app así no te va a arruinar.** OpenAI factura por tokens (palabras troceadas) y los precios son por millón de tokens:

| Modelo | Entrada (por 1M) | Salida (por 1M) | Para qué |
|---|---|---|---|
| **gpt-5-mini** | 0,25 $ | 2 $ | El equilibrio perfecto para tareas normales |
| **gpt-5** | 1,25 $ | 10 $ | Código complejo, agentes |
| **gpt-4o-mini** (legacy) | 0,15 $ | 60 cént. | Sigue vivo y barato |
| **gpt-5.6-luna** | 0,20 $ | 1,20 $ | Volumen alto, la familia nueva más tirada |

Con `gpt-5-mini`, explicar un error son unos 500-1.500 tokens en total. Eso son **fracciones de céntimo por llamada**: entre unas 70 y 300 llamadas por cada dólar. Si tus prácticas generan logs todo el día pero las consultas son puntuales, te sobra con 1 $ de saldo durante semanas.

Trucos para que el gasto ni se note:

- **Prompt caching**: OpenAI descuenta los prefijos repetidos (los `system` largos y constantes) hasta un 90 %.
- **Batch API**: un 50 % de descuento si el resultado no hace falta al momento (yo lo uso para análisis masivos de logs por la noche).
- **Limita de verdad**: en `platform.openai.com/settings/limits` fijas límites de gasto y avisos. Lo configuré el primer día y me ha salvado de un susto.

Facturan en dólares; al cambio, redondea y piensa en céntimos.

## Los 5 errores que cometí la primera vez

1. **Subí la key a GitHub.** En 20 minutos tenía un bot intentando cobrar con mi cuenta. Borra la key comprometida y rota por otra; nunca la vuelvas a commitear.
2. **No truncar la entrada.** Mandé un log de 80.000 caracteres: más lento y más caro. Mismo resultado que con 1.000 bien elegidos.
3. **Sin límite de gasto.** "Es que solo era una prueba" → 9 $ de prompts mal hechos. Configura los límites o te lo va a contar tu factura.
4. **Modelo equivocado.** Empecé con el más caro de la web (`gpt-5`) para cosas que resolvía `gpt-5-mini`. Revisa siempre si necesitas el caballo de carreras.
5. **Ignorar los rate limits.** Llamadas en bucle sin pausa dan errores `429`. Un `time.sleep` entre peticiones arregla el 90 % de los casos.

## Alternativas si quieres empezar en 0 €

Si tu preocupación es el coste, tienes otra puerta de entrada: **modelos locales con Ollama**, gratuitos y offline (te lo conté en mi review de Ollama y en la comparativa Ollama vs LM Studio vs Jan). La gracia de aprender a llamar a la API es que **el código es casi idéntico**: cambia el SDK, el model y la base URL, y tu lógica de la app se queda igual. Yo empecé con Ollama y saltar a OpenAI me costó cambiar tres líneas.

Y para guardar la clave sin liarla, uso el mismo patrón de variables de entorno que expliqué en la guía de GitHub Actions con secrets.

## Conclusión: es la diferencia que se ve en un portfolio

Mi veredicto: **recomiendo hacer esta app aunque sea solo para aprender.** No por la app en sí, sino porque un proyecto que "habla con una API de IA" demuestra que entiendes APIs, claves, entornos de variables y límites de coste. Es exactamente el perfil que se busca en las prácticas.

Si estás construyendo tu portfolio, esto encaja perfecto como idea de fin de semana, del mismo estilo que te dejé en mi lista de 5 proyectos con IA.

Empieza hoy:
1. Crea la cuenta, saca la key y ponla en `.env`.
2. Corre la primera llamada con `gpt-5-mini`.
3. Haz el script que explica errores y úsalo con tus logs de prácticas una semana.
4. Ponle límite de gasto antes de nada.

¿Qué app te gustaría construir tú con la API? Cuéntamelo por email (ivan@codeandia.com) y te doy mi opinión.