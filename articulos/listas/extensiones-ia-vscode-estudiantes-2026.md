---
layout: article
title: "7 extensiones de IA para VS Code que uso a diario siendo estudiante (y una que quité)"
description: "Las extensiones de IA que de verdad me ahorran tiempo en prácticas DAW: Copilot, Codeium, Continue, Error Lens, y más. Qué hace cada una, cuánto cuesta, y mi combo real."
category: "Lista"
date: 2026-08-27
readtime: 7
---

El marketplace de VS Code tiene **cientos** de extensiones con "AI" en el nombre. La mayoría son envolturas alrededor de la misma API, te piden clave, y al final no usan. Yo he probado unas 20 este curso. Estas 7 son las que **siguen instaladas** y las que uso de verdad cada semana en prácticas. La octava la quité y te cuento por qué.

---

## 1. GitHub Copilot (la base de todo)

**Qué hace:** Autocompletado inline, chat lateral (`Ctrl+I`), explicación de código, generación de tests, fix de errores.
**Coste:** **Gratis para estudiantes** (ver [cómo activarlo](/articulos/reviews/github-copilot-gratis-estudiantes/)), $10/mes Individual.
**Por qué está aquí:** Es la que más uso. El autocompletado en Java (mi día a día en DAW) acierta ~80% de lo que voy a escribir. El chat (`Ctrl+I`) me evita ir al navegador: "explícame este NullPointer", "genera test JUnit para UserService", "refactoriza a Stream API".

**Mi config real (`settings.json`):**
```json
"github.copilot.enable": {
  "*": true,
  "yaml": false,
  "markdown": false
},
"github.copilot.chat.locale": "es",
"editor.inlineSuggest.enabled": true
```
Desactivo en YAML/Markdown porque alucina claves y frontmatter.

---

## 2. Codeium (la alternativa gratis sin cuenta estudiante)

**Qué hace:** Autocompletado + chat, **gratis ilimitado** para uso individual. Modelos propios + GPT-3.5/4 opcional.
**Coste:** **Gratis** (Individual), $15/mes Teams.
**Por qué está aquí:** La tengo **como respaldo** cuando Copilot se queda sin cuota (raro en plan estudiante, pero pasa) o cuando quiero una segunda opinión. El autocompletado es ligeramente menos preciso en Java, pero en **Python/JS/TS va muy bien**. El chat (`Ctrl+Shift+P` → Codeium Chat) entiende contexto de repo.

**Cuándo la uso:** Proyectos personales en Python/React, o cuando Copilot falla en un patrón raro de Spring Boot.

---

## 3. Continue (tu "Cursor" open source dentro de VS Code)

**Qué hace:** Trae **modelos locales (Ollama) o remotos (Anthropic, OpenAI, Gemini)** a un panel lateral tipo Cursor. Edita múltiples archivos, ejecuta comandos, indexa tu codebase.
**Coste:** **Gratis** (open source, MIT). Pagás solo la API del modelo que elijas (o nada si usas Ollama local).
**Por qué está aquí:** Es lo más cerca a **Cursor sin pagar $20/mes**. Con `qwen2.5-coder:7b` en Ollama local, tengo **agent mode offline**: "refactoriza todo el módulo auth a DTOs", "añade tests a todos los controllers". Tarda más que Claude Code, pero **cero coste, cero red**.

**Setup 2 min:**
```bash
# 1. Instala Ollama y baja modelo
ollama pull qwen2.5-coder:7b

# 2. Extensión Continue en VS Code
# 3. Configura en Continue: "Local (Ollama)" → qwen2.5-coder:7b
```

**Ojo:** En portátil de 16 GB RAM, `qwen2.5-coder:7b` va fluido. `13b` empieza a hacer swap. No intentes `32b` salvo que tengas 32+ GB.

---

## 4. Error Lens (no es IA, pero parece magia)

**Qué hace:** Muestra **errores, warnings e hints de diagnóstico inline** en la línea exacta, con color y mensaje. No tienes que mirar la pestaña "Problems" ni pasar el ratón.
**Coste:** **Gratis**.
**Por qué está aquí:** Ahorra **minutos por sesión**. En Java con Spring Boot, un `@Autowired` que falla, un `import` que falta, un tipo incompatible — lo ves **en la línea**, en rojo, sin mover el cursor. Combina con Copilot: ves el error, `Ctrl+I` → "arregla esto", listo.

---

## 5. GitLens (Git + IA = superpoder)

**Qué hace:** Git blame, history, comparar ramas, autores, **y ahora "AI Commit Message"** (genera mensaje de commit con IA).
**Coste:** Gratis (core), $9/mes Pro para features de equipo.
**Por qué está aquí:** El **blame inline** (`git blame` en cada línea al pasar ratón) me dice quién tocó qué y cuándo. En prácticas grupales, "¿quién rompió esto?" se responde en segundos. La feature de **commit message con IA** (`GitLens: Commit` → botón ✨) escribe mensajes convencionales tipo `feat: add user authentication` basándose en tu diff. Ahorra el "fix stuff" de siempre.

---

## 6. Thunder Client (REST Client) + AI

**Qué hace:** Cliente HTTP dentro de VS Code (como Postman pero ligero). **Nueva feature IA**: "Generate request from description" → escribes "POST login con email y password, devuelve JWT" y te genera la request con headers, body, variables.
**Coste:** Gratis (core), Pro $30/año para sync/equipos.
**Por qué está aquí:** En DAW hacemos **REST APIs constante**. Thunder Client me evita abrir Postman. La IA genera la request base y yo la ajusto. Guarda colecciones en el repo (`.thunder-client/`) → todo en Git.

---

## 7. Better Comments (colorear comentarios, no IA pero esencial)

**Qué hace:** Colorea comentarios por tipo: `//!` rojo (importante), `//!` naranja (warning), `//?` azul (pregunta), `//!` verde (todo), `//*` gris (comentado).
**Coste:** **Gratis**.
**Por qué está aquí:** Cuando la IA me genera código, le pido "pon comentarios `//!` en lo crítico y `//?` en lo que no entiendo". Luego veo el archivo y **salto directo a lo importante**. Combo con Copilot: "genera servicio UserService con comentarios `//!` en validaciones y `//?` en lógica compleja".

---

## La que quité: Tabnine

**Por qué la instalé:** "Autocompletado IA gratis, modelos locales, privado".
**Por qué la quité:**
1. **Conflicto con Copilot/Codeium**: tres autocompletados peleando = sugerencias locas, parpadeo, lentitud.
2. **Modelo local lento**: en mi portátil, 2-3 seg por sugerencia. Copilot/Codeium son <100 ms (cloud).
3. **Menos preciso en Java/Spring**: Copilot entiende mejor los patrones de mi codebase.

**Lección:** **Una sola extensión de autocompletado a la vez**. Si usas Copilot (gratis estudiante), no necesitas Tabnine ni Codeium para autocompletado. Codeium/Continue solo para chat/agent mode.

---

## Mi combo real (lo que tengo activado HOY)

| Extensión | Rol | Cuándo la uso |
|---|---|---|
| **GitHub Copilot** | Autocompletado + chat principal | 90% del tiempo (Java, TS, config) |
| **Continue + Ollama (qwen2.5-coder:7b)** | Agent mode offline / privacidad | Código sensible, sin red, refactors gordos |
| **Codeium** | Backup / segunda opinión | Cuando Copilot falla o proyecto Python/JS |
| **Error Lens** | Ver errores inline | Siempre (no es IA, pero indispensable) |
| **GitLens** | Git blame + commit messages IA | Prácticas grupales, commits decentes |
| **Thunder Client** | REST API testing + IA generate | APIs de prácticas, side projects |
| **Better Comments** | Leer código generado por IA | Siempre (colorear `//!` `//?` `//*`) |

---

## Cómo no liarte (regla de oro)

**No instales todo a la vez.** Empieza por:
1. **GitHub Copilot** (gratis estudiante) → úsalo 2 semanas.
2. Si necesitas **offline/privacidad** → añade **Continue + Ollama**.
3. **Error Lens + GitLens + Better Comments** → instálalas ya, son gratis y zero config.
4. **Thunder Client** → cuando hagas tu primera API REST.

Las extensiones de IA **se pisan** si tienes varias haciendo autocompletado. Una para completar, una para chat/agent, y el resto para utilidades. Así el editor vuela y tú también.

---

¿Qué extensiones usas tú? ¿Has probado Continue con modelos locales? Cuéntame en comentarios tu setup.
