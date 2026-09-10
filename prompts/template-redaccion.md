# Template de redacción — codeandIA

Se ejecuta **después de la pesquisa**. Recibe `articulos/_entrada/<slug>/pesquisa.md` y produce el borrador final en `articulos/_entrada/<slug>/borrador.md`.

**IMPORTANTE:** Leer `prompts/_voz-y-estilo.md` ANTES de redactar. Aplicar todas las reglas.

---

## Paso 1 — Estructurar el artículo

Según la categoría, seguir la estructura de `_voz-y-estilo.md`:

| Categoría | Estructura |
|---|---|
| Review | Hook → Qué es/cómo funciona → Experiencia en proyectos de clase → Precio → Veredicto |
| Comparativa | Hook → Criterios → A → B → Veredicto por caso de uso |
| Guía | Contexto → Paso a paso real → Errores → "Lo que haría diferente" |
| Lista | Hook → Bloques ### por herramienta → Mi combinación real |

---

## Paso 2 — Redactar (reglas de estilo)

- **NO** `# H1` → empezar directamente con texto (el layout genera el título).
- Longitud: 1.100–1.500 palabras.
- **Un solo tema por párrafo.** Frases cortas.
- Primera persona ("yo", "me pasó", "te cuento").
- Ejemplo concreto del mundo DAW en cada afirmación importante.
- Sin jerga de marketing: nada de "revolucionario", "game-changer", "en el mundo digital actual".
- Si algo no se ha probado, decirlo ("no lo he probado").
- Rematar SIEMPRE con veredicto propio.

---

## Paso 3 — Frontmatter

```yaml
---
layout: article
title: "[título SEO-friendly, máx. 70 caracteres]"
description: "[meta description, 120-160 caracteres, incluir keyword]"
category: "Review | Comparativa | Guía | Lista"
date: 2026-MM-DD  # Se actualizará al publicar
readtime: [X]     # Nº de minutos según word count / 160
affiliate_text: "[CTA personalizado, solo si monetiza]"
affiliate_url: "[URL canónica verificada]"
affiliate_label: "[Texto del botón]"
---
```

**Regla de afiliado:** solo incluir si el producto monetiza (Hostinger, Namecheap) o si el enlace aporta valor real al lector. No meter CTA donde no tiene sentido.

---

## Paso 4 — Auto-verificación (checklist de calidad)

Antes de marcar como "borrador listo", verificar:

- [ ] NO hay ningún `# H1` en el contenido (solo `##` y `###`).
- [ ] Frontmatter tiene todos los campos obligatorios.
- [ ] Longitud entre 1.100 y 1.500 palabras.
- [ ] Al menos 2 referencias a la vida de estudiante DAW (clase, prácticas, módulos, exámenes, portátil).
- [ ] Al menos 1 cifra concreta (€/mes, minutos ahorrados, peticiones, límites).
- [ ] El veredicto/conclusión tiene postura propia ("recomiendo / no recomiendo").
- [ ] No hay frases genéricas de IA (pasar el ojo).
- [ ] `affiliate_url` responde 200 (curl verificado).
- [ ] Enlaces internos (si los hay) usan `/articulos/[slug]/`.
- [ ] Sin `readtime` alto de más (si 1.500 palabras → ~8 min).

**Si alguna falla → corregir ANTES de marcar como listo.**

---

## Paso 5 — Guardar

El borrador se guarda en:
```
articulos/_entrada/<slug>/borrador.md
```

**NO mover a la carpeta de categoría ni hacer commit.** Eso lo hace el paso de publicación tras la cadencia programada.
