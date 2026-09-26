---
layout: article
title: "De prácticas a tu primer curro con IA: preparar entrevistas técnicas"
description: "Guía DAW para buscar tu primer trabajo: usar IA en entrevistas técnicas, challenges de código y un portfolio que impresione. Sin trampas, con estrategia real."
category: "Guía"
date: 2026-08-10
readtime: 10
---

Cuando empecé a buscar prácticas de DAW, me encontré con una realidad que nadie me había contado: **saber programar no es suficiente**. Necesitas pasar entrevistas técnicas donde te ponen a resolver problemas en tiempo real, made un challenge de código en 45 minutos, y demostrar que sabes más que "lo que vimos en clase". Aquí es donde la IA se convierte en tu mejor aliada — no para que haga el trabajo por ti, sino para que **te entrene como un coach personalizado** que nunca se cansa de explicarte las mismas cosas.

---

## La realidad de las entrevistas técnicas para juniors

Antes de hablar de IA, hay que ser honesto sobre qué te esperan:

| Tipo de entrevista | Qué evalúan | Duración típica |
|---|---|---|
| **Live coding** | Resolución de problemas, lenguaje, razonamiento | 45-60 min |
| **Code review** | Entender código ajeno, detectar bugs, sugerir mejoras | 30-45 min |
| **System design básico** | Arquitectura de una app simple, decisiones técnicas | 45-60 min |
| **Culture fit / behavioral** | Comunicación, trabajo en equipo, cómo resuelves conflictos | 30-45 min |
| **Take-home project** | Código completo, tests, documentación, deploy | 3-7 días |

Lo que descubrí: **el 80% de las empresas junior hacen live coding + una pregunta de system design sencillo**. Y aquí es donde la IA te puede entrenar mejor que cualquier libro.

---

## Estrategia 1: Entrenamiento de live coding con Copilot

El truco no es que Copilot resuelva el problema por ti (eso lo detectan al instante), sino que **uses su explicación para entender el patrón**.

### Flujo de estudio real

1. **Busca un problema en LeetCode Easy/Medium** (o neetcode.io, que tiene los 150 esenciales)
2. **Intenta resolverlo sin IA** (15-20 min máximo)
3. **Si no lo sacas**, abre Copilot Chat y pregunta: "Explica el enfoque para resolver este problema sin darme el código completo"
4. **Lee la explicación**, entiende el patrón, intenta de nuevo
5. **Una vez resuelto**, pide a Copilot: "¿Qué complejidad tiene? ¿Hay una forma más óptima?"

```python
# Ejemplo: problema de "Two Sum"
# Tu intento inicial (fuerza bruta, O(n²)):
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Después de preguntar a Copilot, aprendes el patrón hash map (O(n)):
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

**Lo que ganas**: no memorizas la solución, aprendes el **patrón** (hash map para busquedas de pares). Cuando en la entrevista te pongan "Two Sum II" o "Three Sum", ya sabes qué patrón aplicar.

---

## Estrategia 2: Simulación de entrevista con ChatGPT/Claude

ChatGPT y Claude son excelentes para hacer de "entrevistador". Prompt que funciona:

```
Actúa como un entrevistador técnico de una empresa que contrata developers junior.
Hazme una pregunta de live coding de dificultad media.
Solo dame el enfoque general, no el código.
Si me equivoco, explícame por qué.
Cuando lo resuelva, dame feedback de calidad del código y sugerencias.
Empezamos ahora:
```

**Lo que esto simula**: el ritmo de una entrevista real. Tienes que articular tu razonamiento en voz alta (o escribiendo), recibir feedback inmediato, y ajustar. Es como un mock interview pero sin la presión social.

### Qué preguntar después de cada ejercicio

- "¿Esto es lo que esperarían en una entrevista junior?"
- "¿Cómo explicaría esta solución a un senior que me hace follow-up?"
- "¿Qué errores comunes cometería aquí y cómo los evitaría?"
- "¿Qué preguntas de seguimiento me haría el entrevistador?"

---

## Estrategia 3: Code review real con Claude Code o Copilot

Las empresas quieren ver que **entiendes código ajeno**, no solo que escribes el tuyo. Ejercicio que hago semanalmente:

1. Busca un repo open source pequeño (1k-5k líneas) en Python/Java/TypeScript
2. Lee un PR abierto o un archivo complejo
3. **Sin mirar comentarios ni reviews previos**, intenta hacer tu propio code review
4. Usa Claude Code o Copilot para que revise lo mismo: `claude "Revisa este archivo y dame 5 problemas de calidad, seguridad y rendimiento"`
5. Compara tu review con la de la IA

```bash
# Ejemplo con Claude Code
claude "Haz code review de src/services/payment.ts:
- Bugs potenciales
- Problemas de seguridad
- Code smells
- Mejoras de rendimiento
Da prioridad: crítico > alto > medio > bajo"
```

**Lo que ganas**: aprendes a **ver problemas que un junior no ve**. Los reviewers de la empresa esperan que detectes al menos bugs obvios (null checks, error handling, SQL injection). Si tu review es mejor que el de Copilot, vas por buen camino.

---

## Estrategia 4: Preparar el portfolio con IA (sin que parezca hecho por IA)

Tu portfolio es lo primero que ven. Si huele a "lo hizo ChatGPT", pierdes puntos. Usa la IA para:

| Qué | Cómo usar IA | Qué NO hacer |
|---|---|---|
| **Estructurar el proyecto** | "Diseña la arquitectura de un e-commerce con Spring Boot" | Copiar la arquitectura completa sin entenderla |
| **Resolver bugs** | "¿Por qué falla esta query N+1 en JPA?" | Pedir que te escriba toda la lógica |
| **Tests** | "Genera tests de edge cases para este método" | Usar los tests sin leerlos ni entenderlos |
| **Documentación** | "Revisa mi README y sugiere mejoras" | Dejar que escriba todo el README |
| **Deploy** | "Configura GitHub Actions para deploy en Vercel" | Copiar sin entender el workflow |

**Mi truco personal**: después de que la IA me ayuda con algo, **me lo explico a mí mismo**. Si no puedo explicar por qué funciona, no lo entiendo y no lo incluyo en mi portfolio. El entrevistador va a preguntar "¿por qué hiciste esto así?" y necesitas saber responder.

---

## Estrategia 5: System design para juniors (la parte que nadie te enseña)

En DAW no te enseñan system design. En las entrevistas te preguntan: "¿Cómo diseñarías un sistema de reservas de cine?" Y tú piensas: "¿Eso no lo vimos?"

**Prompt para practicar**:

```
Estoy preparando entrevistas junior de software.
Pregúntame un system design sencillo (nivel junior, no microservicios masivos).
Solo dame el enfoque: qué preguntaría al entrevistador, qué componentes dibujaría,
y qué tecnologías elegiría y por qué.
Después damelo a mí para que lo intente.
```

**Framework que te salva** (aprende esto y cubres el 90% de system design junior):

1. **Aclara requisitos**: "¿Cuántos usuarios? ¿Geo-restricción? ¿Real-time o batch?"
2. **Dibuja los bloques**: Frontend → API Gateway → Backend → DB + Cache
3. **Escoge tecnologías y justifica**: "PostgreSQL por transaccionalidad, Redis por caché de sesiones"
4. **Habla de escalabilidad**: "Si crece, separo reads de writes con réplica DB"
5. **Habla de trade-offs**: "Elegí SQL sobre NoSQL por consistencia, pero si crece mucho, migraría a DynamoDB"

---

## Herramientas IA específicas para cada fase de la búsqueda

| F Herramienta | Qué hace | Cuándo usarla |
|---|---|---|
| **GitHub Copilot** | Completado en vivo, explicaciones de código | Practicar live coding, entender soluciones |
| **ChatGPT / Claude** | Mock interviews, system design, feedback | Preparación general, behavioral questions |
| **Ollama + qwen2.5-coder** | Entrenamiento offline, sin límites | Sin WiFi, exámenes, prácticas con NDA |
| **Claude Code** | Code review profundo, arquitectura | Revisar tu portfolio, mejorar código existente |
| **Notion AI** | Organizar preguntas, trackear progreso | Llevar registro de qué temas dominas |

---

## Plan de 4 semanas para pasar una entrevista junior

**Semana 1: Fundamentos**
- 3 problemas LeetCode Easy/día con Copilot (sin mirar solución)
- 1 system design question con ChatGPT
- Leer "Cracking the Coding Interview" capítulos 1-3 (o resúmenes en YouTube)

**Semana 2: Patrones**
- 2 problemas Medium/día (hash maps, two pointers, sliding window)
- Simular 1 entrevista completa con Claude (45 min, live coding + behavioral)
- Revisar tu portfolio con Claude Code: detectar code smells

**Semana 3: Proyectos**
- Mejorar 2-3 proyectos del portfolio con tests y documentación
- Deploy automático con GitHub Actions
- Grabarte resolviendo un problema (tu propio "mock interview" en video)

**Semana 4: Simulación**
- 2 mock interviews reales con amigo o mentor
- Preparar 5 stories STAR para behavioral (situación, tarea, acción, resultado)
- Repasar system design con un amigo usando el framework de 5 pasos

---

## Lo que no te dice nadie

1. **La IA no sustituye la práctica real**. Entrevistar se aprende entrevistando. Usa la IA para prepararte, pero busca mock interviews reales (amigos, comunidades, interviewing.io).
2. **Saber explicar es más importante que saber resolver**. Un senior prefiere ver tu razonamiento aunque tardes 10 min más. La IA te entrena para articular tu lógica.
3. **El 70% de las empresas junior valoran actitud sobre conocimiento**. "No sé, pero buscaría..." es mejor que intentar adivinar. La IA te da la base para decir eso con confianza.
4. **No mientas sobre el uso de IA**. Si te preguntan "¿usas IA en tu día a día?", la respuesta correcta es: "Sí, para code review y resolver bugs, pero entiendo el código que genero". Eso es una fortaleza, no una trampa.

---

Si me escribes a ivan@codeandia.com contándome qué parte de la entrevista te mete más miedo, te digo cómo la atacaría yo con lo de esta guía. Sin guion, con lo que de verdad me funcionó.
