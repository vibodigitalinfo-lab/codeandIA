---
layout: article
title: "Notion + IA para apuntes de DAW: mi sistema real (bases y plantillas)"
description: "Cómo uso Notion con IA para apuntes de DAW: bases por módulo, plantillas, resúmenes automáticos y sync con GitHub. Lo que funciona y lo que no."
category: "Guía"
date: 2026-08-07
readtime: 10
---

Empecé el curso con una carpeta de Google Drive llamada `DAW 2025-26` y dentro 40 PDFs sueltos, capturas de pizarra, y un `apuntes.txt` que nunca abrí. A noviembre ya no encontraba nada. Me pasé a Notion, le metí IA, y **ahora mi sistema de apuntes es lo único que me deja estudiar para los exámenes sin pánico**. Te lo enseño entero: bases de datos, plantillas, prompts que uso, y los errores que cometí.

---

## Por qué Notion + IA (y no Obsidian, OneNote, o papel)

| Herramienta | Lo probé | Por qué no |
|---|---|---|
| **Obsidian** | 2 semanas | Plugins de IA = configurar API keys, pagar, mantener. Quería algo que *funcione ya*. |
| **OneNote** | 1 mes | Búsqueda mala, sin bases de datos, IA (Copilot) solo en 365 empresarial. |
| **Papel + escáner** | Curso pasado | No buscas "excepción NullPointer en UserService" en papel. |
| **Notion + IA** | **Desde noviembre** | IA nativa (gratis 20 respuestas/día), bases de datos relacionales, plantillas, sincroniza en todos lados. |

**Lo que Notion IA me da gratis (plan Personal, sep 2026):**
- 20 respuestas IA / día (reset a medianoche)
- Resumir página, extraer acción items, traducir, mejorar redacción
- Generar contenido desde cero ("esquema de examen de BBDD")
- **No** incluye: búsqueda semántica en todo el workspace (eso es Notion AI add-on $10/mes)

Para mí, **20/día sobran** si los usas con cabeza (ver prompts abajo).

---

## Mi estructura: 3 bases de datos relacionales

No uses páginas sueltas. **Bases de datos** = filtros, vistas, relaciones, rollups.

### 1. `Módulos` (una fila por asignatura)

| Propiedad | Tipo | Ejemplo |
|---|---|---|
| Nombre | Title | "Desarrollo Web Entorno Servidor" |
| Curso | Select | 2º DAW |
| Profesor | Text | "Juan García" |
| Repo GitHub | URL | `github.com/ivanm/dwes-practicas` |
| Estado | Select | `En curso` / `Finalizado` / `Examen preparado` |
| **Relación → Temas** | Relation | (ver abajo) |
| **Rollup → Próximo examen** | Rollup | `Min(Fecha examen)` desde Temas |

### 2. `Temas` (una fila por tema de cada módulo)

| Propiedad | Tipo | Ejemplo |
|---|---|---|
| Nombre | Title | "Tema 3: Spring Boot + JPA" |
| Módulo | Relation → Módulos | "Desarrollo Web Entorno Servidor" |
| Tipo | Select | `Teoría` / `Práctica` / `Examen` / `Entrega` |
| Estado | Select | `Pendiente` / `En clase` / `Repasado` / `Dominado` |
| Fecha clase | Date | 2026-01-15 |
| Fecha examen | Date | 2026-02-20 |
| **Apuntes** | Relation → Páginas | (página de notas) |
| **IA: Resumen** | Formula | `""` (rellenado por botón IA) |
| **IA: Preguntas examen** | Formula | `""` (rellenado por botón IA) |

### 3. `Páginas` (las notas reales, una por tema)
Aquí es donde escribo. Cada fila de **Temas** tiene su página vinculada (Relación 1:1). La página usa una **plantilla** (ver abajo).

**Vista que más uso:** En `Temas`, agrupo por `Módulo` → `Estado` → veo de un vistazo qué temas de DWES tengo en `Repasado` y cuáles en `Pendiente` antes del examen.

---

## Plantilla de página de apuntes (la clave)

Cuando creo un tema nuevo → `New` en la base de datos `Temas` → se abre la página con esta plantilla ya puesta:

```markdown
# {{Nombre del tema}}

## Objetivo de la clase
<!-- Qué debemos saber al salir. Ej: "Entender ciclo de vida Bean Spring" -->

## Apuntes en bruto
<!-- Lo que escribo EN CLASE. Rápido, sucinto, sin ordenar. -->

## IA: Resumen estructurado
<!-- Botón: "Ask AI → Summarize → Structured notes" -->
*Se rellena solo tras la clase.*

## IA: Preguntas tipo examen
<!-- Botón: "Ask AI → Generate exam questions (5, DAW level)" -->
*Se rellena solo al repasar.*

## Recursos
- Repo: `@github.com/ivanm/...`
- Docs oficiales: ...
- Vídeo clase: ...

## ✅ Checklist de repaso
- [ ] Entiendo la teoría
- [ ] He hecho la práctica
- [ ] He resuelto las preguntas IA
- [ ] He explicado el tema en voz alta (técnica Feynman)
```

**Truco:** La plantilla se crea en la base de datos `Temas` → `...` → `Templates` → `New template`. Ahora cada tema nuevo trae esto listo.

---

## Prompts IA que uso (copia y pega)

### 1. Tras la clase: resumir y estructurar
> **En la página de notas, selecciónalo todo → Ask AI → Custom prompt:**
> ```
> Estructura estos apuntes en bruto de una clase de DAW en:
> 1. Conceptos clave (máx 5, con definición de una frase)
> 2. Código/patrón principal (con ejemplo mínimo)
> 3. Errores típicos / "trampas" que mencionó el profe
> 4. Qué tocará en examen (según lo dicho en clase)
> Formato: bullets, español neutro, técnico pero claro.
> ```

### 2. Al repasar: generar preguntas de examen
> **En la misma página → Ask AI → Custom prompt:**
> ```
> Genera 5 preguntas tipo examen DAW sobre este tema.
> Nivel: 2º DAW, módulo {{Módulo}}.
> Tipos: 2 opción múltiple, 2 desarrollo corto, 1 código.
> Incluye soluciones al final en bloque aparte.
> No uses jerga que no esté en los apuntes.
> ```

### 3. Antes del examen: simulacro
> **En la base de datos `Temas` filtrada por `Módulo = X` y `Estado = Repasado` → selecciona todas → Ask AI → Custom prompt:**
> ```
> Hazme un simulacro de examen con las notas de estos 8 temas.
> 10 preguntas: 4 test, 3 desarrollo, 3 código.
> Nivel real de examen DAW. Tiempo: 90 min.
> Devuelve: enunciado + soluciones separadas.
> ```

### 4. Para entender un concepto que no pillas
> **En cualquier página → selecciona el párrafo confuso → Ask AI → "Explain simpler":**
> ```
> Explícame este concepto como si fuera para un compañero de 1º DAW.
> Usa una analogía de la vida real (ej. parking, biblioteca, cocina).
> Dame un ejemplo de código MÍNIMO (10 líneas max).
> ```

---

## Sincronización con GitHub (el toque pro)

Cada práctica tiene su repo. En la base de datos `Módulos`, el campo `Repo GitHub` enlaza al repo. En la plantilla de `Páginas`, pongo `@github.com/usuario/repo` y Notion lo convierte en enlace bonito.

**Bonus:** Uso una **GitHub Action** que al hacer push a `main` en mis repos de prácticas, crea/actualiza una página en Notion con el resumen del commit (via Notion API). Es overkill, pero mola ver en Notion "Último push: feat: add JWT auth - 3 files changed".

```yaml
# .github/workflows/notion-sync.yml (simplificado)
name: Sync to Notion
on:
  push:
    branches: [main]
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Update Notion page
        uses: actions/http-request@v1
        with:
          url: https://api.notion.com/v1/pages/${{ secrets.NOTION_PAGE_ID }}
          method: PATCH
          headers: |
            Authorization: Bearer ${{ secrets.NOTION_TOKEN }}
            Notion-Version: 2022-06-28
            Content-Type: application/json
          data: '{"properties": {"Último push": {"rich_text": [{"text": {"content": "${{ github.event.head_commit.message }}"}}]}}}'
```
*(Requiere Notion Integration token y página compartida con la integración. Si no te apetece, saltatelo — no es esencial.)*

---

## Lo que NO funciona (errores que cometí)

1. **Poner TODO en Notion** (PDFs, capturas, docs enteros) → base de datos lenta, búsqueda basura. **Solo texto estructurado + enlaces a archivos en Drive/GitHub**.
2. **Usar IA para todo** ("resume este PDF de 50 páginas") → gasta las 20 respuestas/día en basura. **IA solo para tus apuntes en bruto**.
3. **No revisar los resúmenes IA** → a veces alucina (ej. "Spring usa Hibernate por defecto" cuando el profe dijo "usamos EclipseLink"). **Siempre lee el resumen antes de estudiar**.
4. **Demasiadas propiedades en bases de datos** → fricción al crear tema. **Mínimo viable: Nombre, Módulo, Tipo, Estado, Fecha examen, Relación a Página**.
5. **No usar la vista "Calendario"** → activa vista `Calendar` en `Temas` por `Fecha examen`. Ves la semana de exámenes de un vistazo.

---

## Mi rutina semanal real (15 min domingo)

1. **Filtro `Temas`**: `Estado = En clase` o `Repasado` → veo qué tocamos esta semana.
2. **Para cada tema sin `IA: Resumen`**: abro → `Ask AI → Resumir` (1 respuesta IA).
3. **Domingo noche**: `Temas` con examen en < 14 días → `Ask AI → Preguntas examen` (1 respuesta por tema).
4. **Simulacro** (si examen en < 3 días): filtro módulo → `Ask AI → Simulacro` (1 respuesta).
5. **Actualizo `Estado`** a `Dominado` cuando paso el simulacro > 80%.

**Total: ~4-6 respuestas IA/semana**. Me sobran de las 20/día.

---

## Lo que haría diferente si volviera a empezar

- **Empezaría desde día 1** con las 3 bases de datos. Migrar 3 meses de PDFs sueltos me costó 6 horas.
- **No compraría Notion AI add-on ($10/mes)**. El plan gratis + prompts bien hechos da para todo el curso.
- **Usaría la vista "Tablero Kanban" por Estado** (`Pendiente` → `En clase` → `Repasado` → `Dominado`) para arrastrar temas visualmente.
- **Compartiría la base de datos `Módulos` con 2-3 compañeros** (Notion permite compartir solo una BD). Así todos ven fechas de examen y recursos.

---

## Conclusión: el sistema te sirve, no tú a él

Notion + IA **no te aprueba el examen**. Tú estudias. Pero te quita la fricción de:
- "¿Dónde están mis apuntes de Spring Security?"
- "¿Qué temas entran en el examen de DWES?"
- "¿Cómo resumo 3 horas de clase en algo que se pueda repasar en 20 min?"

Mi sistema hoy: **abro Notion → filtro módulo → veo estado → leo resumen IA → hago preguntas IA → simulacro → examen**. Cero pánico, cero "¿qué estudié de esto?".

Si te montas algo parecido, **empieza simple**: una base de datos `Temas`, una plantilla de página, y el prompt de "Resumir estructurado". Lo demás lo añades cuando lo eches en falta.

---

Si ya vives en Notion y me mandas a ivan@codeandia.com una captura de tu base de apuntes, te digo qué me chirría y qué aprovecharía yo sin piedad.
