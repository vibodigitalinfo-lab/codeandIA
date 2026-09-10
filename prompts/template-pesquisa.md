# Template de pesquisa — codeandIA

Este prompt se ejecuta **en paralelo con agentes** (WebSearch). Cada fase produce un bloque Markdown que luego se fusiona en un único dossier de pesquisa en `_entrada/<slug>/pesquisa.md`.

---

## Paso 0 — Configuración del escenario

Antes de investigar, define:
- **Tema/artículo:** ___
- **Categoría** (Review | Comparativa | Guía | Lista): ___
- **Palabra clave SEO principal:** ___
- **¿El producto monetiza por Skimlinks?** (Sí/No): ___

---

## Paso 1 — Pesquisa por fase (agente en paralelo por cada fase)

### 1A — Features y especificaciones
Prompt para agente:
```
Investiga la herramienta [NOMBRE] (URL oficial: [URL]).
Devuelve SOLO un bloque Markdown con:
- Qué es (1 párrafo, 50 palabras máx)
- Stack tecnológico / compatibilidad (macOS, Windows, Linux, web, extensión)
- Funciones principales (máx 5 bullets)
- Plan gratuito: qué incluye y límites reales (peticiones, tokens, tiempo)
- Plan de pago: precio real en € y $, qué cambia
- Últimas novedades relevantes (últimos 3 meses)
Fuentes con fecha.
```

### 1B — Opiniones reales de usuarios
Prompt para agente:
```
Busca opiniones REALES de [NOMBRE] en:
- Reddit (r/programming, r/learnprogramming, r/webdev)
- Foros de desarrollo
- YouTube (reviews, no patrocinados)
Devuelve un bloque Markdown con:
- 5-8 opiniones representativas (cita textual + fuente)
- Problemas recurrentes que mencionan
- Lo que más gusta
- Lo que más frustra
No incluir reviews de blogs de afiliado.
```

### 1C — Alternativas y contexto competitivo
Prompt para agente (solo para Comparativas y Reviews):
```
¿Cuáles son las 3 principales alternativas a [NOMBRE]?
Para cada una, devuelve: nombre, precio, diferencia clave con [NOMBRE], para quién es mejor.
En formato Markdown tabla.
```

### 1D — Enlaces de afiliado
Prompt para agente:
```
Verifica la URL oficial de [NOMBRE] con curl (curl -sL -o /dev/null -w "%{http_code}" URL).
Devuelve: URL canónica verificada (200), si tiene programa de afiliado propio, si Skimlinks lo cubre (hosting/nombre de dominio o SaaS conocido).
```

---

## Paso 2 — Fusión del dossier

Agrupa toda la pesquisa en un único archivo Markdown:

```markdown
# Pesquisa: [TÍTULO]
- Fecha: [YYYY-MM-DD]
- Categoría: [Review | Comparativa | Guía | Lista]
- Slug: [nombre-del-archivo]

## Datos clave
[Tabla con: precio, plan gratuito, URL, monitización]

## Features / Especificaciones
[Resultado 1A]

## Opiniones reales
[Resultado 1B]

## Alternativas (si aplica)
[Resultado 1C]

## Enlaces
[Resultado 1D — solo URL canónica]
```

**Guardar en:** `articulos/_entrada/<slug>/pesquisa.md`
