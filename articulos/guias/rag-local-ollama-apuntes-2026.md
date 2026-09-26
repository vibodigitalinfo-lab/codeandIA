---
layout: article
title: "RAG local con Ollama: respuestas a tus apuntes con IA sin pagar"
description: "Guía de RAG local con Ollama para estudiantes de DAW: embeddings con nomic-embed-text, ChromaDB y un chat 100% local con tus apuntes, gratis y offline."
category: "Guía"
date: 2026-08-27
readtime: 7
---

Cuando empecé DAW, mi sistema de estudio era una pesadilla: apuntes de MySQL por aquí, PDFs de Java por allá, y media docena de tabs de apuntes abiertas. Preguntarle algo a ChatGPT funcionaba, pero la respuesta era genérica: no conocía MIS apuntes, ni el guion de MI profesor, ni los ejercicios que hacíamos en clase.

La solución que llevo usando desde entonces es **RAG local**: que un modelo de IA lea "mis" documentos y responda con base en ellos, todo en mi portátil, sin pagar ni subir mis apuntes a la nube. No es una cosa rara de infraestructura: es un script de Python con dos librerías. Te enseño a montarlo en una tarde.

## Qué es RAG (en 30 segundos)

RAG (*Retrieval-Augmented Generation*) es el truco que hace que una IA "sepa" cosas que no entró en su entrenamiento: **antes de responder, busca en tus documentos los trozos más relevantes y se los pasa como contexto.**

El flujo completo es este:

1. Troceas tus apuntes en pedazos pequeños.
2. Cada trozo se convierte en un **embedding** (una lista de números que representa su significado) con un modelo específico.
3. Los guardas en una **base de datos vectorial** (ChromaDB es la más fácil).
4. Cuando preguntas, tu pregunta también se convierte en embedding y se busca "los trozos más parecidos".
5. Esos trozos + tu pregunta se mandan al modelo, que responde apoyándose en ellos.

La magia es que el modelo ya no alucina "de memoria": **responde con tus documentos delante**. Y si montas todo con Ollama, nada sale de tu equipo.

## Por qué local y no la web

Por tres motivos que a mí me decidieron:

- **Privacidad gratis**: tus apuntes de prácticas, tus notas de exámenes y tu código no se suben a ningún sitio. Para datos de empresa o del TFG de alguien, esto es oro.
- **Cero coste por uso**: una vez instalado, puedes preguntar lo que quieras sin mirar el contador. Ideal para cuando estudias y preguntas sin parar.
- **Es exactamente lo que se hace en producción**: las empresas montan RAG sobre sus documentaciones con las mismas piezas. Lo aprendes hoy en prácticas y te lo piden mañana en una entrevista.

Si no tienes Ollama instalado, en mi [review de Ollama](/articulos/reviews/ollama-modelos-ia-local-review-2026/) te explico cómo bajarlo y por qué corre hasta en portátiles de estudiante.

## El montaje paso a paso

### 1. Instala modelos

Ollama en marcha (arranca en `http://localhost:11434`), y dos modelos: uno de **embeddings** (nomic-embed-text, el estándar de facto, con casi 85 millones de descargas) y uno de chat ligero:

```bash
ollama pull nomic-embed-text
ollama pull qwen3:4b
```

Fíjate en la separación: el modelo de embeddings es SOLO para convertir texto en vectores; el de chat es el que responde. Usar el mismo para ambas cosas da peores resultados. Es uno de los detalles que encuentra todo el que prueba.

### 2. Instala Python y ChromaDB

```bash
pip install chromadb ollama
```

### 3. Indexa tus apuntes

Este script lee tus notas Markdown (también vale `.txt`), las trocea y las guarda con sus embeddings:

```python
import os
import ollama
import chromadb

cliente = chromadb.PersistentClient(path="./apuntes_db")
coleccion = cliente.get_or_create_collection(name="apuntes")

chunks = []
for raiz, _, archivos in os.walk("apuntes"):
    for archivo in archivos:
        if archivo.endswith(".md"):
            texto = open(os.path.join(raiz, archivo), encoding="utf-8").read()
            chunks += [texto[i:i + 1000] for i in range(0, len(texto), 1000)]

embeddings = []
for chunk in chunks:
    r = ollama.embed(model="nomic-embed-text", input="search_document: " + chunk)
    embeddings.append(r["embeddings"][0])

coleccion.add(ids=[str(i) for i in range(len(chunks))],
              embeddings=embeddings, documents=chunks)
print("Indexadas", len(chunks), "secciones")
```

El `search_document:` delante de cada texto es un prefijo que los modelos de embeddings esperan para distinguir documentos de preguntas. Para preguntar se usa `search_query:`. Es un detalle tonto que si te lo saltas, baja bastante la calidad de las búsquedas.

### 4. Pregunta

```python
import ollama
import chromadb

cliente = chromadb.PersistentClient(path="./apuntes_db")
coleccion = cliente.get_collection(name="apuntes")

pregunta = "¿Qué es un INNER JOIN?"
r = ollama.embed(model="nomic-embed-text", input="search_query: " + pregunta)
resultados = coleccion.query(query_embeddings=[r["embeddings"][0]], n_results=3)

contexto = "\n---\n".join(resultados["documents"][0])

resp = ollama.chat(model="qwen3:4b", messages=[
    {"role": "system", "content": "Responde SOLO con lo que diga el contexto. Si no está, dilo sin inventar."},
    {"role": "user", "content": f"Pregunta: {pregunta}\n\nContexto:\n{contexto}"},
])
print(resp["message"]["content"])
```

En cuatro bloques de código tienes tu primer RAG. Si tu portátil va justo, `qwen3:4b` responde bien; si tienes más memoria, sube a una variante de 7b-8b.

## Mejoras rápidas cuando ya funcione

- **Tamaño de trozos**: yo uso ~250 palabras por trozo. Trozos gigantes bajan la precisión; mini-trozos pierden contexto. Empieza ahí y ajústalo.
- **Canta las fuentes**: pide al modelo que cite el nombre del documento de donde saca la respuesta. Te enseña cuándo tus apuntes están incompletos.
- **Búsqueda híbrida**: el embedding sólito falla con palabras exactas (códigos, términos de la pregunta del examen). Mezclarlo con una búsqueda léxica (BM25) es lo que hacen las herramientas serias cuando quieren precisión.
- **Aísla el contexto**: lo que mete en el prompt es **contenido no confiable** (puede traer instrucciones ocultas dentro de un PDF con copiar-pegar). Sepáralo del estilo de la defensa nº1 que te dejé en el [guía de prompt injection](/articulos/guias/prompt-injection-seguridad-apps-ia-2026/), o el día que indexes un documento raro, tu "IA" hará lo que le mande el documento.

## Los fallos que cometí (para que no se repitan)

- **Mezclar el modelo**: al principio usaba `qwen3` para embeddings "para no descargar otro modelo". Los resultados eran decepcionantes; el embedding va a otro modelo, y punto.
- **No trocear**: metí un PDF de 200 páginas entero en una fila de Chroma. La búsqueda devolvía basura y el prompt reventaba de contexto. Trocea siempre.
- **Omitir los prefijos**: `search_document:` / `search_query:` no son optional. Sin ellos, las búsquedas pierden bastante calidad.
- **Guardar secretos junto a las notas**: no metas documentos con contraseñas o claves; el RAG los repetirá encantado en cuanto le preguntes bien.

## Conclusión

Mi veredicto: **todos los estudiantes de DAW deberían montar esto al menos una vez.** No porque lo vayas a usar cada día (apuntes en Markdown + preguntas de exámenes = tocado en una tarde), sino porque RAG es la habilidad estrella de 2026 para perfiles con IA, y lo aprendes sin pagar ni exponer tus datos.

Es además el complemento perfecto al flujo que ya te enseñé: en el [guía de la API de OpenAI](/articulos/guias/primera-app-api-openai-python/) montábamos la llamada al modelo; ahora el modelo tiene *memoria real de tus apuntes*. Si le añades el resto de herramientas de Ollama de la [comparativa que te dejé](/articulos/comparativas/ollama-vs-lm-studio-vs-jan-2026/), tienes todo un laboratorio de IA local.

Y si algún día te piden en prácticas "dar contexto de la documentación a un chat interno", ya sabes exactamente qué piezas usa.

El día que le pregunté a mi RAG por un apunte de Java y me respondió mejor que yo, decidí que este proyecto venía para quedarse. Que te parezca poco secreto es buena señal de que funciona.
