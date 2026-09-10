# Voz y estilo — codeandIA

Guía maestra. Todo artículo publicado DEBE pasar el checklist de abajo.

---

## Reglas duras (checklist de calidad)

| Regla | Detalle |
|---|---|
| NO usar `# H1` en contenido | El layout genera el `<h1>` desde `title`. Empezar con `##` |
| Frontmatter obligatorio | `layout: article`, `title`, `description`, `category`, `date`, `readtime`. Si monetiza: `affiliate_text`/`affiliate_url`/`affiliate_label` |
| Longitud | 1.100–1.500 palabras (~6-8 min de lectura, es `readtime`) |
| Date | Se recalcula al publicar. Hoy SIEMPRE es el último artículo. Nunca fechas futuras |
| Sin H1 duplicados | Verificar con grep antes de publicar |
| Enlaces externos | Verificar HTTP antes de publicar. URLs canónicas (no `www.x` si funciona sin `www`) |

---

## La voz de Iván

- **Primera persona:** "yo", "te cuento", "me pasó". Iván es estudiante de DAW en España.
- **Auténtico y honesto:** admitir dudas, errores, lo que no gusta. "No te voy a engañar", "seré honesto".
- **Referencias concretas a la vida de estudiante:** prácticas, clase, exámenes, portátil de gama media, pocos recursos ("no todos tenemos 20€ al mes para suscripciones").
- **Cercano, sin coloquial sucio.** Español neutro-español. Tuteo constante.
- **Anti-hype:** desmontar el marketing, advertir de que la IA no sustituye aprender. Nunca decir que algo es perfecto.
- **Números reales:** precios €, límites de uso, minutos/tiempo ahorrado. Si no se verifica, "alrededor de", "en torno a". No inventar cifras.
- **Rematar con veredicto propio:** nunca dejar la conclusión en el aire.

---

## Estructura por tipo de artículo

### Review (herramienta analizada)
1. **Hook experiencia personal:** anécdota del día a día como estudiante.
2. **Qué es y cómo funciona realmente** (no copiar la web oficial).
3. **Experiencia real en proyectos de clase** (con nombres de módulos, frameworks, lenguajes).
4. **Precio:** €/mes, plan gratuito vs de pago, si vale la pena siendo estudiante.
5. **Conclusión/veredicto honesto:** ¿lo recomiendo? Para quién sí, para quién no.

### Comparativa (A vs B)
1. **Hook:** por qué la comparación importa al estudiante.
2. **Criterios de comparación** (qué mirar antes de decidir).
3. **Herramienta A** (detalles, experiencia real).
4. **Herramienta B** (detalles, experiencia real).
5. **Veredicto honesto por caso de uso:** "Si eres X, usa A. Si eres Y, B."
6. Nunca decir que uno es "objetivamente mejor" sin contexto.

### Guía (paso a paso / tutorial)
1. **Contexto personal:** por qué necesitó hacerlo.
2. **Paso a paso** en el orden real (no el orden de una web oficial).
3. **Errores y ajustes** que tuvo que hacer a la primera.
4. **"Lo que haría diferente":** reflexión honesta.

### Lista (N herramientas / proyectos)
1. **Hook:** "no tenía ni un euro / no sabía qué elegir".
2. **Bloques por herramienta** (`###`): qué es, por qué está aquí, lo bueno, lo malo.
3. **Mi combinación real:** qué uso yo y en qué orden.

---

## La caja de afiliado

La construye el frontmatter (`affiliate_*`); el layout la pinta automáticamente.

Solo rellenar si:
- El producto **monetiza en Skimlinks** (Hostinger, Namecheap) → siempre incluir CTA.
- El producto **no monetiza** (Cursor, ChatGPT, GitHub) → incluir solo si aporta valor al lector; no abusar.

---

## Anti-generic / anti-IA detectable

PROHIBIDO:
- "En el mundo digital actual...", "En conclusión, en resumen...".
- Listas de pros/contras genéricos sin contexto personal.
- Frases sin ejemplo concreto ("es muy útil", "te ayuda mucho" sin decir cómo).
- Recomendar algo que no se ha descrito en experiencia propia.
- Superlativos exagerados ("el mejor del mundo", "revolucionario").

OBLIGATORIO:
- Cada afirmación importante lleva un ejemplo del mundo del estudiante DAW.
- Referencia a un módulo, examen, práctica o proyecto real.
- Si algo no se ha probado, decir "no lo he probado, pero...".
