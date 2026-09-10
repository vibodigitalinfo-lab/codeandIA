# 🔄 Pipeline de publicación automática — codeandIA

Sistema autónomo de publicación de artículos. Iván no tiene que hacer nada.

---

## Cómo funciona

```
1. Elegir tema (de _ideas.md, de abajo a arriba)
2. Pesquisa (WebSearch en paralelo con agentes)
3. Redacción (siguiendo _voz-y-estilo.md)
4. Auto-verificación de calidad
5. Publicar: mover a carpeta de categoría, recalcular fechas, commit+push
```

**Cadencia:** 1 artículo por día hábil (lunes a viernes, 9:00h). Los fines de semana NO se publica para simular comportamiento humano y no levantar sospechas de Google.

---

## Carpetas involucradas

```
prompts/                  ← Esta carpeta (templates internos, NO se publica)
├── _voz-y-estilo.md      ← Estándar de calidad
├── _ideas.md             ← Banco de temas pendientes
├── template-pesquisa.md  ← Cómo pesquisar
└── template-redaccion.md ← Cómo escribir

articulos/_entrada/       ← Borradores pendientes de publicar (Jekyll la ignora)
articulos/reviews/        ← Review publicados
articulos/comparativas/   ← Comparativas publicadas
articulos/guias/          ← Guías publicadas
articulos/listas/         ← Listas publicadas
```

---

## Flujo de publicación (cron diario lun-9h)

```
 [cron se activa lun-9h]
        │
        ▼
  Lee _ideas.md → elige el tema más reciente sin publicar
        │
        ▼
  Ejecuta template-pesquisa.md
  → lanza 4 agentes en paralelo (WebSearch)
  → guarda dossier en _entrada/<slug>/pesquisa.md
        │
        ▼
  Ejecuta template-redaccion.md
  → lee pesquisa + _voz-y-estilo.md
  → genera borrador en _entrada/<slug>/borrador.md
        │
        ▼
  Auto-verifica calidad (checklist)
  → si falla: NO publica, deja nota en _entrada/<slug>/error.log
        │
        ▼
  PUBLICA:
  → mueve borrador a articulos/<categoría>/<slug>.md
  → recalcula TODAS las fechas (hoy = último)
  → commit + push
  → actualiza _ideas.md (marca como publicado con fecha)
        │
        ▼
  listo, siguiente tema mañana
```

---

## Cuándo Iván sí debe intervenir

- Cuando el pipeline no puede verificar una URL (403).
- Cuando un tema requiere experiencia personal muy concreta (marcado en _ideas.md como "necesita input").
- Cuando quiera cambiar la cadencia o pausar el pipeline.
- Cuando quiera añadir un tema urgente al banco de ideas.

---

## Importante: calibrar el tono

Los primeros 2-3 artículos publicados por el pipeline deben ser **verificados por Iván** para calibrar que el tono es correcto. Después, el pipeline actúa de forma autónoma.

Si Iván detecta que un artículo no suena a él, puede editarlo en `articulos/<categoría>/` y hacer push manual.
