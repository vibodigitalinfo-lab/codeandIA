---
layout: article
title: "Warp terminal 2026: IA en la línea de comandos, ¿vale la pena cambiar de iTerm/WSL?"
description: "Review honesta de Warp terminal: bloques, IA integrada, precios, Windows/Linux/macOS, y si merece la pena para un estudiante de DAW."
category: "Review"
date: 2026-08-31
readtime: 7
affiliate_text: "Prueba Warp gratis y decide si te cambia el flujo en terminal"
affiliate_url: "https://www.warp.dev/pricing"
affiliate_label: "Ver planes Warp"
---

Confieso: durante años mi terminal fue "la que viene de serie" (Terminal.app en Mac, WSL en Windows, gnome-terminal en Linux). No le daba vueltas. Pero el año pasado empecé a ver a compañeros que usaban Warp y **hacían cosas en segundos que a mí me llevaban minutos**: buscar un comando que usé hace tres semanas, que la IA me escribiera un `find` complejo sin mirar la man page, compartir una sesión con un compañero para depurar juntos.

Me bajé Warp hace un par de meses. Esto es lo que he encontrado, lo bueno, lo malo, y si te compensa siendo estudiante.

---

## Qué es Warp y en qué se diferencia de tu terminal actual

Warp no es "una terminal con IA encima". Es **una terminal reescrita desde cero en Rust** (el frontend) con un modelo de **bloques** en lugar de flujo de texto lineal.

Cada comando que ejecutas genera un **bloque**: input + output + metadatos (tiempo, directorio, código de salida). Puedes:
- Navegar entre bloques con teclas (arriba/abajo) en lugar de `history | grep`
- Copiar solo el output de un comando sin arrastrar el ratón por toda la ventana
- Compartir un bloque (o sesión entera) con un link temporal — ideal para "mira este error, ¿qué hago?"
- La IA (Warp Agent) vive **dentro del bloque**, no en un panel aparte

Además trae **editor integrado con LSP** (autocompletado real, no solo historial), temas que funcionan out of the box, y **funciona igual en macOS, Linux y Windows** (sí, Windows nativo desde febrero 2025, no WSL).

---

## Experiencia real: lo que me cambió el día a día

### 1. Búsqueda de comandos que sí funciona
Antes: `history | grep docker` → scroll → copio → edito → ejecuto.
Ahora: `Ctrl+R` (o `Cmd+R` en Mac) → escribo "docker compose up" → me sale el bloque exacto con el output → `Enter` para reejecutar o `Tab` para editar antes.

### 2. Warp Agent: IA que entiende tu repo
Le das contexto (arrastras la carpeta del proyecto al chat o usas `@codebase`) y le pides:
- "Escribe un script bash que haga backup de la BD y suba a S3"
- "¿Por qué falla este `npm run build`?"
- "Genera un Dockerfile multi-stage para este Spring Boot"

Y **ejecuta los comandos por ti** (pregunta antes de cada uno peligroso). En un proyecto de prácticas con Docker, Kubernetes y CI/CD, me ahorró horas de buscar YAMLs en la doc oficial.

### 3. Bloques = contexto persistente
En terminal clásica, si cierras la pestaña, pierdes el contexto visual. En Warp, los bloques persisten entre sesiones. Abres mañana y ves exactamente qué hiciste ayer, con outputs completos. Para mí que salto entre clase, prácticas y proyectos personales, eso es **oro**.

### 4. Compartir sesión en 2 clicks
`Cmd+Shift+S` → link temporal → se lo mandas al compañero por Discord. Él ve tu terminal **en vivo** (read-only o read-write si das permiso). Depurar en remoto sin Zoom ni compartir pantalla completa.

---

## Lo que NO me gusta (y debes saber)

| Problema | Gravedad | Workaround |
|----------|----------|------------|
| **Login obligatorio** (incluso plan gratis) | Alta para privacidad | Cuenta burner, pero molesto |
| **Consumo memoria** (300-500MB base) | Media | Cierra pestañas que no uses |
| **Créditos opacos** (no ves cuántos gastas en tiempo real) | Media | Plan Build $18/mes anual = 1500 créditos, suficiente para uso diario |
| **No es 100% compatible conAlgunos TUIs** (htop, lazygit a veces fallan) | Baja | `warp run --passthrough` o terminal nativa puntual |
| **AGPL-3.0** (código abierto pero viral) | Solo si contribuyes | Usuario final: irrelevante |

El **login obligatorio** es lo que más rechazo genera en la comunidad (Reddit, HN). Warp dice que es para sincronizar configuraciones, historial y equipo. Yo uso cuenta dedicada y listo, pero si eres purista de "mi terminal no llama a casa", esto te echa para atrás.

---

## Precios reales (septiembre 2026, anual = ~10% descuento)

| Plan | Mensual | Anual | Créditos/mes | Para quién |
|------|---------|-------|--------------|------------|
| **Free** | $0 | $0 | BYO inference + cloud agents limitados | Estudiante, uso ligero |
| **Build** (recomendado) | $20 | **$18/mes** | 1,500 | Dev diario, estudiante que quiere todo |
| **Max** | $200 | $180/mes | 18,000 | Power user, equipos pequeños |
| **Business** | $50/seat | $45/seat | 1,500/seat + SAML | Equipos 5-25 |
| **Enterprise | Custom | Custom | Ilimitado + BYOLLM + self-hosted | Empresas grandes |

**Créditos**: se gastan en Warp Agent (IA en la nube) y Warp Drive (sincronización). **Traes tu propio modelo (BYO)** en plan gratis = usas tu clave de OpenAI/Anthropic y no gastas créditos Warp. En planes de pago, los créditos cubren modelos de Warp (Sonnet 4, GPT-5, Grok Build, routers propios).

**Para estudiante**: el plan **Free + BYO** (tu API key de OpenAI/Anthropic) te da Warp Agent gratis. Si no quieres gestionar keys, **Build a $18/mes anual ($216/año)** es lo que yo pago y me sobra. No hay descuento estudiante oficial.

---

## Warp vs iTerm2 / Windows Terminal / Kitty

| | Warp | iTerm2 | Windows Terminal | Kitty |
|--|------|--------|------------------|-------|
| **Bloques/IA** | ✅ Nativo | ❌ (plugins) | ❌ | ❌ |
| **Editor LSP** | ✅ | ❌ | ❌ | ❌ |
| **Compartir sesión** | ✅ 1-click | ❌ | ❌ | ❌ |
| **Multiplataforma** | ✅ Mac/Linux/Win | Solo Mac | Solo Win | Linux/Mac |
| **Rendimiento** | Muy bueno (Rust) | Bueno | Bueno | Excelente (GPU) |
| **Configuración** | GUI + YAML | Lua/JSON | JSON | Conf file |
| **Precio base** | Free + login | Gratis | Gratis | Gratis |

Si ya tienes tu flujo perfeccionado en Kitty/iTerm con tmux + fzf + scripts propios, **Warp no te va a aportar tanto**. Si, como yo, usabas la terminal "de serie" y quieres IA integrada sin configurar nada, **Warp es un salto cualitativo grande**.

---

## Conclusión: ¿cambio o me quedo donde estoy?

**Cambia a Warp si:**
- Quieres IA en terminal **sin configurar plugins, keys, MCP, nada**
- Valoras la UX de bloques, búsqueda visual y compartir sesión
- Trabajas en Mac/Linux/Windows y quieres la misma experiencia en todos
- El plan Free + BYO o Build $18/mes te encaja

**Quédate en tu terminal si:**
- Eres power user de tmux + fzf + scripts bash personalizados y no quieres reaprender
- El login obligatorio te parece inaceptable (respeto total)
- Necesitas compatibilidad 100% con TUIs extraños (k9s, lazydocker, etc.)
- Prefieres herramienta 100% local, sin nube, sin cuentas

**Mi veredicto personal**: me quedo con Warp. El salto de "buscar en history" a "buscar por bloques con IA" me ahorra tiempo real cada día. El login me fastidia, pero gano más de lo que pierdo. Si eres estudiante y quieres probar IA en terminal **hoy**, bájalo, dale a Free + tu API key, y en 10 minutos tienes Warp Agent funcionando. Si no te convence, lo desinstalas y listo.

¿Lo has probado? Cuéntame en comentarios si los bloques te resultan naturales o te chirrían.