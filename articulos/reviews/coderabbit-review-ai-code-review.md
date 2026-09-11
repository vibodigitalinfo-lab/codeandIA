---
layout: article
title: "CodeRabbit review 2026: ¿merece la pena pagar por IA que revisa tus PRs?"
description: "Analizo CodeRabbit, la herramienta que revisa pull requests con IA. Precios, comparativa con Copilot, el incidente de seguridad y si vale la pena para un estudiante."
category: "Review"
date: 2026-09-04
readtime: 7
affiliate_text: "Prueba CodeRabbit gratis en repos públicos y decide si te compensa"
affiliate_url: "https://coderabbit.ai/pricing"
affiliate_label: "Ver planes CodeRabbit"
---

Llevo semanas viendo cómo mis compañeros del ciclo se pasan horas revisando código a mano en GitHub, comentando línea por línea cosas que una IA podría pillar en segundos. El problema es que la mayoría piensa que "revisión con IA" es cosa de empresas grandes o que cuesta un riñón. CodeRabbit me llamó la atención porque tiene **plan gratis para repos públicos** y, siendo estudiante, eso ya es un filtro importante.

No voy a venderte la moto: la revisión de código con IA no es magia, y CodeRabbit tiene sus sombras (un incidente de seguridad gordo el año pasado que te cuento más abajo). Pero si estás en un equipo, haces PRs a diario y quieres pillar bugs antes de que lleguen a producción, merece la pena echarle un ojo con criterio.

---

## Qué es CodeRabbit y cómo funciona realmente

CodeRabbit es una herramienta que se enchufa a tu repositorio (GitHub, GitLab, Azure DevOps, Bitbucket) y **revisa automáticamente cada pull request** que abres. No es un linter ni un formateador: entiende el contexto del cambio, mira qué archivos tocas, y te sugiere mejoras, bugs potenciales, problemas de seguridad y hasta refactors.

Lo instalas desde el marketplace de GitHub, das permisos al repo, y a partir de ahí cada PR nuevo tiene un comentario de `coderabbitai` con:
- Resumen de los cambios en lenguaje natural
- Issues encontrados (bugs, seguridad, rendimiento, estilo)
- Sugerencias de código concreto que puedes aplicar con un click
- Preguntas al autor cuando algo no está claro

Lo probé en un proyecto de clase (API REST en Spring Boot con un par de controladores, servicios y repositorios) y lo primero que me sorprendió es que **no alucina librerías**. A diferencia de ChatGPT que a veces se inventa métodos, CodeRabbit analiza tu código real y sugiere sobre lo que ve.

---

## Experiencia real en proyectos de clase

Mi caso de uso principal: prácticas de DAW donde entregamos por PRs y el profe revisa (a veces con semanas de retraso). CodeRabbit me ha pillado un par de veces:

1. **Null pointer silencioso**: en un servicio que devolvía un `Optional` pero el controlador lo desempaquetaba sin check. CodeRabbit lo marcó como "potencial NPE en producción" y sugirió el `orElseThrow` con mensaje claro. Lo hubiera pasado por alto.
2. **Query N+1 en JPA**: tocaba una entidad con `@OneToMany` y el repositorio hacía lazy loading dentro de un bucle. CodeRabbit detectó el patrón y sugirió `JOIN FETCH` o `@EntityGraph`. En examen práctico eso te ahorra un suspenso.
3. **Validación faltante**: un DTO sin `@NotNull` en campos obligatorios. Lo marcó como "falta validación de entrada" con el código exacto para añadir.

Lo que **no me gustó**: a veces sugiere refactors de estilo que son opinables (extraer método de 3 líneas, renombrar variable que ya es clara). En el plan gratis no puedes configurar reglas propias para callar ese ruido, así que toca ignorar manualmente.

---

## Precios: ¿qué te cuesta siendo estudiante?

Aquí está la tabla real a septiembre 2026 (precios anuales, que son un 10-20% más baratos que mensuales):

| Plan | Precio/año por dev | Qué incluye | Límite reviews/hora |
|------|-------------------|-------------|---------------------|
| **Gratis (OSS)** | $0 | Solo repos públicos | 5 |
| **Essentials** | $24/mes ($288/año) | 5 MCP, 1 multi-repo | 5 |
| **Team** | $48/mes ($576/año) | 10 MCP, 5 multi-repo, Triage | 8 |
| **Advanced** | $72/mes ($864/año) | 15 MCP, 10 multi-repo, Security scans | - |

**Clave importante**: **solo cuentan como "asiento" los creadores de PR**. Si tu equipo son 5 pero solo 3 abren PRs habitualmente, pagas 3 asientos. Los revisores pasan gratis.

Para un estudiante solo: el plan **gratis en repos públicos** cubre portfolio, prácticas públicas y proyectos open source. Si haces prácticas en repo privado de la empresa/uni, toca Essentials ($24/mes). No hay descuento estudiante oficial (lo pregunté en soporte), pero el plan gratis es generoso comparado con competidores.

---

## CodeRabbit vs GitHub Copilot Code Review

Esta es la comparativa que me pidieron en clase y que nadie te explica claro:

| | CodeRabbit | Copilot Code Review |
|--|------------|---------------------|
| **Dónde vive** | Multi-plataforma (GH, GL, Azure, BB) | Solo GitHub |
| **Facturación** | Por asiento fijo/mes | Por créditos IA ($0.01/crédito) |
| **Plan gratis** | Sí, repos públicos ilimitados | No (solo en Pro/Business/Enterprise) |
| **Seguridad** | Pilar específico (blast radius, attack surface) | Básico, parte del plan |
| **Triage/Prioridad** | Sí (plan Team+) | No nativo |

**Mi veredicto**: si tu repo está en GitHub y ya pagas Copilot Pro/Business, **prueba primero Copilot Code Review** (está incluido). Si usas GitLab, necesitas multi-plataforma, o quieres pricing predecible sin sorpresas de créditos, **CodeRabbit gana**. Para mí, que muevo proyectos entre GitHub y GitLab según la práctica, la multi-plataforma pesa.

---

## El elefante en la sala: incidente de seguridad agosto 2025

No te lo voy a esconder. En agosto 2025, Kudelski Security publicó una cadena de explotación (RCE) que permitía, desde un PR malicioso, tomar control del runner de CodeRabbit y acceder a **1 millón de repositorios**. Llegó a portada de Hacker News (687 puntos).

CodeRabbit lo parcheó en horas, publicó post-mortem transparente y lanzó su **pilar de seguridad** (julio 2026) con mapas de superficie de ataque y monitorización continua. ¿Significa que no lo uses? Para mí, **no**. Cualquier herramienta que tenga acceso a tu código es vector de ataque (Copilot, Cursor, todo). Lo que importa es la respuesta y la transparencia. La tuvieron.

Dicho esto: **no des permisos a repos con secretos reales en producción** sin revisar bien qué alcance das. Y rota tokens habitualmente, que eso es higiene básica independientemente de la herramienta.

---

## Conclusión honesta: ¿lo recomiendo?

**Sí, con matices.**

- **Para portfolio y prácticas públicas**: plan gratis, instálalo ya. Te pilla errores tontos antes que el profe y aprendes de las sugerencias.
- **Para prácticas en empresa/repo privado**: Essentials a $24/mes si el equipo lo paga. Si sale de tu bolsillo, valora si los PRs que abres al mes justifican el coste.
- **Para equipo de 3-5 devs**: Team ($48/dev/mes) trae Triage, que prioriza PRs automáticamente. Útil si tenéis mucha cola.

Lo que **no** hace: sustituir la revisión humana. CodeRabbit pilla bugs mecánicos, patrones conocidos y seguridad básica. No entiende la lógica de negocio de tu aplicación, no sabe si el algoritmo es el óptimo para tu caso, y a veces sugiere "limpieza" que solo añade complejidad. Úsalo como **red de seguridad**, no como árbitro final.

Si lo pruebas, dime en los comentarios qué tal te fue. Y si tienes repo público, el plan gratis no te cuesta nada perder 5 minutos en ver si te pilla algo.