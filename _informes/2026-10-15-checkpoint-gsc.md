# Checkpoint GSC 2026-10-15

## Comparativa: baseline 21-27 sep vs 8-14 oct

| Ventana | Impresiones | Clics | CTR |
|---|---|---|---|
| 2026-09-21 → 2026-09-27 | 284 (49,44,42,45,43,33,28) | 6 (1+2+0+2+0+0+1) | ~2,1% |
| 2026-10-08 → 2026-10-14* | 6 (2+1+0+0+2+1+0) | 0 | 0% |

*10-14: 0 impresiones en 24h exportado hoy.

## Colapso y tendencia diaria (28d)

Del 2026-09-28 al 2026-10-02: máximo ~50–65 impresiones/día (pico 65 el 01-oct).
El 2026-10-03 cae a 2 → desde entonces **0–2 impresiones/día** (plano 12 días).
A día 15-oct (24h) → **0 impresiones**.

**Conclusión:** ha tocado fondo pero **no hay recuperación**. No hay incremento de impresiones, ni clics.

## Cobertura (Coverage)

- 2026-09-14: 56 indexadas / 23 sin indexar
- 2026-09-19: 89/13
- 2026-09-22: 123/52 (máximo)
- **2026-10-05: 123 → 89 indexadas**; sin indexar 52 → 88
- Desde 10-05: **89 indexadas / 88 sin indexar** estable

## Problemas críticos (GSC Coverage)

- Página con redirección (Error): **5** → stubs antiguos (sin categoría)
- Rastreada: actualmente sin indexar (Error): **55** (Crawled - currently not indexed)
- Descubierta: actualmente sin indexar (Iniciada): **26** (Discovered - currently not indexed)
- Excluida por etiqueta noindex: **1**
- Página alternativa con etiqueta canónica adecuada: **1**

Total "sin indexar" = 88. **Crawled/Discovered-not-indexed suman 81** → señal clásica de desindexado por calidad/confianza.

## Consultas (28d, 0 clics totales)

Top: "cascos cancelacion ruido para estudiar" (6 imp, pos 7.67), "keychron q1 max" (4, 21), "dominio .es barato" (4, 45), "cursor ai vs chatgpt" (4, 53), "ia para programar gratis" (3, 79). Mucho long-tail y ruido (ej. "si", "dan 6.0", "nerd lat", "trade ide"). Las queries relevantes de marca (github copilot estudiantes) aparecen con 1–2 impresiones.

## Páginas (28d)

Patrón: páginas sobre **marcas grandes** tienen muchas impresiones y 0 clics (p.e. `github-copilot-intellij-java-daw` 103/0%/6.76, `chatgpt-vs-cursor-para-programar` 78/0%/11.78, `github-copilot-gratis-estudiantes` 45/0%/9.4, `chatgpt-plus-para-programadores` 33/0%/6.48). Las que reciben clics son genéricas/hardware: `que-portatil-comprar-estudiar-daw-2026` 4/20%/4.9, `mejores-prompts...` 1/6%/8.19, `aprender-java-con-ia-daw` 1/12.5%/4.88.

## Hallazgos estructurales

- **Duplicados**: muchas URLs antiguas sin carpeta de categoría aparecen con impresiones junto a las nuevas (p.e. `/articulos/mejores-prompts...` vs `/articulos/guias/mejores-prompts...`). La conversión a 301 no es posible en GitHub Pages; los stubs están como 200 + noindex.
- **5 errores "página con redirección"** en Coverage — GSC los marca así.
- **Índice se ha estabilizado en 89** tras la caída (123→89), pero todas las URLs con tráfico útil están atascadas en 0 clics.

## Lectura para el plan de recuperación

- **Ha tocado fondo** (0–2 imp/día, estable) → no hay una recaída activa ahora mismo.
- **No hay señales de recuperación** → las pocas impresiones son básicamente ruido; no hemos vuelto a entrar en el funnel de consultas reales.
- El enfoque correcto sigue siendo **consolidación** (rutas + enlazado interno) + publicación **2–3/semana con fechas reales** (no retrofechar) + racionar producto, a la espera del siguiente **spam/update de calidad**. Los "fixes" de título son marginales: el bloqueo es site-level (confianza/indexación), no copy.