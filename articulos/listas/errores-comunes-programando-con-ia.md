---
layout: article
title: "7 errores programando con IA (y cómo evitarlos)"
description: "Errores reales usando Copilot, ChatGPT y Claude Code en mi primer año de DAW: confiar a ciegas, no leer el código generado, perder contexto. Con soluciones."
category: "Lista"
date: 2026-09-01
readtime: 8
---

Hace un año pensé que programar con IA era "le doy el prompt y me genera todo". Después de meses usando Copilot, ChatGPT y Claude Code en proyectos reales de DAW, me di cuenta de que **la IA amplifica tanto lo bueno como lo malo**. Si eres desordenado, la IA te ayuda a ser desordenado más rápido. Si eres metódico, la IA te multiplica la productividad x10. Aquí van los 7 errores que más me dolieron — y que veo que cometen otros estudiantes constantemente.

---

## 1. Confiar ciegamente en el código generado

**Lo que me pasó**: Pedí a Copilot que generara una función de validación de email en Java. Funcionaba... hasta que un usuario puso `test@test` (sin TLD). La regex no lo bloqueó. En producción, un usuario creó una cuenta con email inválido y las notificaciones fallaron silenciosamente.

**La raíz del problema**: Copilot generó una regex que cubría el 90% de casos, pero no validaba edge cases. Yo la pegué sin leer ni testear.

**La solución**:
- **Lee cada línea que la IA genera**. Si no entiendes por qué funciona, no la uses.
- **Escribe tests antes** (TDD): define qué debe fallar antes de que la IA genere el código.
- **Pregunta a la IA**: "¿Qué edge cases no cubre esta regex?" — y luego vérificalos.

```java
// Lo que Copilot generó (incompleto):
public static boolean isValidEmail(String email) {
    return email != null && email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$");
}

// Lo que debí pedirle explícitamente:
public static boolean isValidEmail(String email) {
    if (email == null || email.isBlank()) return false;
    if (email.length() > 254) return false; // RFC 5321
    String[] parts = email.split("@", -1);
    if (parts.length != 2) return false;
    if (parts[0].isEmpty() || parts[1].isEmpty()) return false;
    if (!parts[1].contains(".")) return false; // Sin TLD
    return email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$");
}
```

---

## 2. No entender el contexto completo del repo

**Lo que me pasó**: Le pedí a ChatGPT que refactorizara un servicio de autenticación. Generó código bonito... que rompió 12 tests en otro módulo porque no sabía que `UserService` se usaba también en el microservicio de notificaciones (no estaba en el contexto que le di).

**La raíz del problema**: La IA solo ve lo que le das. Si no le das el contexto completo, genera soluciones parciales que rompen otras partes.

**La solución**:
- **Usa herramientas con contexto del repo**: Claude Code o Cursor (que indexan el workspace) ven más que un chat aislado.
- **Antes de refactorizar**: busca todas las referencias (`Ctrl+Shift+F` en VS Code) y dáselas a la IA.
- **Pregunta**: "¿Qué archivos afecta este cambio? ¿Qué dependencias tiene esta clase?"

---

## 3. Dejar que la IA me haga "todo de una"

**Lo que me pasó**: En un examen práctico de DWES, le pedí a ChatGPT que me generara un CRUD completo en Spring Boot. Funcionó... en mi portátil. Pero no entendía qué hacía cada anotación, por qué el `@Transactional` estaba en el servicio y no en el controlador, ni cómo conectaba con la base de datos. Cuando el profesor me preguntó "¿por qué usas `Optional` aquí?", me quedé en blanco.

**La raíz del problema**: Pedir "todo de una" te da el resultado sin el aprendizaje. Es como copiar los apuntes de un compañero sin leerlos.

**La solución**:
- **Divide en pasos pequeños**: "Primero explica la entidad", "Luego el repositorio", "Ahora el servicio con lógica", "Después el controlador".
- **Después de cada paso**: lee el código, entiéndelo, explica con tus palabras qué hace.
- **Regla personal**: si no puedo explicar cada línea, no la presento.

---

## 4. Perder horas por no cambiar de herramienta

**Lo que me pasó**: Luché 3 horas con Copilot para resolver un problema de deployment en Docker. Copilot me daba soluciones que no funcionaban (imágenes base incompatibles, puertos mal configurados). Cuando finalmente le pregunté a Claude (con el error completo + logs), lo resolvió en 2 minutos.

**La raíz del problema**: Copilot es genial para completado de código, pero para debugging complejo con múltiples archivos de configuración, Claude (o ChatGPT con GPT-4o) rinde mejor por su ventana de contexto más grande.

**La solución**:
- **Copilot**: completado de líneas, snippets, código repetitivo.
- **ChatGPT/GPT-4o**: explicaciones, debugging con contexto pequeño, queries SQL.
- **Claude**: debugging complejo, análisis de código grande, arquitectura.
- **Ollama local**: cuando no hay WiFi o el código es sensible.
- **No uses una sola herramienta**. Cada una tiene su sweet spot.

---

## 5. No versionar los prompts que funcionan

**Lo que me pasó**: Tenía un prompt perfecto para generar tests de integración con Testcontainers. Lo perdí cuando limpié el historial de ChatGPT. Ahora no lo recuerdo y cada vez que intento recrearlo, sale diferente.

**La raíz del problema**: Tus prompts exitosos son una herramienta de trabajo. Si no los guardas, los pierdes.

**La solución**:
- **Crea un archivo `PROMPTS.md`** en tu repo (o en Notion) con tus prompts efectivos.
- **Etiquétalos**: `#tests-integracion`, `#code-review`, `#examen-daw`.
- **Versiona**: si un prompt mejora, guarda la versión anterior y la nueva.

```markdown
# Mis prompts efectivos

## Test de integración (Spring Boot + Testcontainers)
Prompt: "Genera tests de integración para este servicio usando Testcontainers.
Usa @DataJpaTest, incluye test para happy path, empty result, y exception.
El test debe ser self-contained con H2 en modo PostgreSQL."

## Code review
Prompt: "Haz code review de este archivo. Clasifica por severidad:
crítico > alto > medio > bajo. Focus: bugs, security, performance, readability.
No sugieras cambios de estilo, solo lógica."
```

---

## 6. Ignorar la privacidad del código

**Lo que me pasó**: Pegué una configuración de base de datos (con la contraseña real) en ChatGPT para que me ayudara a diagnosticar un error de conexión. La contraseña quedó en el historial de OpenAI.

**La raíz del problemas**: Olvidé que ChatGPT/Claude son servicios en la nube. Todo lo que pegas se envía a sus servidores.

**La solución**:
- **Nunca pegues credenciales reales**: reemplázalas con `YOUR_PASSWORD_HERE` antes de preguntar.
- **Si el código es sensible** (proyecto de empresa, NDA): usa Ollama local (100% offline).
- **Revisa la política de datos**: OpenAI no entrena con datos de API (Business), sí con datos de ChatGPT free. Anthropic tampoco entrena con datos de API.
- **Regla simple**: si no lo publicarías en GitHub público, no lo pegues en un chat de IA.

---

## 7. Olvidar que tú eres el que programa

**Lo que me pasó**: Durante un mes, mi flujo era: "abrir ChatGPT → copiar código → pegar en VS Code → compilar → si funciona, siguiente". No estaba programando. Estaba copiando. Y cuando llegué al examen sin IA, mi nivel real era más bajo del que pensaba.

**La raíz del problema**: La IA te da la ilusión de competencia. Si no practicas sin ella, nunca desarrollas tu propio criterio.

**La solución**:
- **Sesiones "sin IA"**: dedica 1-2 horas/día a programar sin Copilot/ChatGPT. Los primeros días cuestan, pero es la única forma de realmente aprender.
- **Aprende los fundamentos PRIMERO**: antes de pedir a la IA que genere un DTO, entiende qué es un DTO y por qué existe.
- **Usa la IA como junior que necesita supervisión**, no como senior que te da la solución perfecta.

---

## Resumen: reglas que sigo hoy

1. **Leo cada línea** que la IA genera antes de pegarla.
2. **Entiendo el contexto completo** del repo antes de pedir refactorizaciones.
3. **Divido en pasos pequeños** en lugar de pedir "todo de una".
4. **Cambio de herramienta** cuando una no rinde para la tarea.
5. **Guardo mis prompts efectivos** en un archivo versionado.
6. **Nunca pego credenciales** o código sensible en chats de IA.
7. **Programo sin IA** al menos 1 hora al día para mantener mi nivel real.

**La IA es una herramienta brutal**. Pero como toda herramienta, depende de quién la use. Un buen programador con IA es imparable. Un programador flojo con IA solo se equivoca más rápido.

---

De todos estos, el que más me costó fue el primero: la confianza ciega. El resto vino solo. Si te reconoces en cualquiera de ellos, ya estás a medio camino de no cometerlo.
