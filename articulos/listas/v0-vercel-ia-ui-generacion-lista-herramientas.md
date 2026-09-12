---
layout: article
title: "v0 by Vercel y alternativas 2026: IA que genera interfaces, ¿cuál uso para mi portfolio?"
description: "Lista comparativa de v0, Bolt, Lovable, y herramientas de generación UI con IA. Precios, stack, limitaciones, y cuál elegir para portfolio, landing, o app real."
category: "Lista"
date: 2026-09-06
readtime: 7
affiliate_text: "Prueba v0 gratis y genera tu primera UI en minutos"
affiliate_url: "https://v0.app/pricing"
affiliate_label: "Ver planes v0"
---

El diseño visual nunca se me dio bien. CSS me parece luchar contra el navegador, Tailwind ayuda pero sigo mirando la pantalla en blanco 20 minutos antes de escribir una clase. **v0 de Vercel cambió eso**: le describes lo que quieres en lenguaje natural y te genera una interfaz React + Tailwind + shadcn/ui lista para copiar (o deployar a Vercel en 1 click).

Pero v0 no está solo. **Bolt.new** corre en el navegador (WebContainers), **Lovable** apunta a no-técnicos con Supabase, y hay más. Te comparo las principales para que elijas la que encaja en tu flujo (y tu bolsillo).

---

## v0 by Vercel: la referencia en calidad de código

**Qué es**: agente IA que genera **apps full-stack** (Next.js 16.2, React 19, Tailwind 4.2, shadcn/ui) desde prompt. 4M+ usuarios (feb 2026). Dominio: **v0.app** (migración desde v0.dev ago 2025).

**Stack por defecto**:
- Frontend: Next.js App Router, React Server Components, Tailwind 4, shadcn/ui
- Backend: **Neon (PostgreSQL serverless) + Drizzle ORM + Better Auth** (desde 2026)
- Extras: Python/SQL, React Three Fiber, **Nuxt 3** (marzo 2026)

**Precios (sep 2026)**:
| Plan | Mensual | Créditos/mes | Límites |
|------|---------|--------------|---------|
| **Free** | $0 | **$5/mes** | 7 msgs/día, modelos base |
| **Plus** | **$30** | $30 + $2/día | Todos los modelos, compra extra, team collab |
| **Business** | **$100** | Todo + | Training opt-out default, SSO |
| **Enterprise | Custom | Full | SSO, RBAC, SLAs, no training |

**Per-model pricing** (si compras extra): v0 Mini $0.20/$1.20, Pro $2/$10, Max $5/$25, Max Fast $10/$50 por MTok (in/out).

**Lo bueno**:
- **Calidad de código**: Next.js idiomático, shadcn/ui bien usado, TypeScript estricto. `AutoFix` (v0-1.5-md) = 93.87% error-free vs 78.43% Opus 4.
- **GitHub sync nativo**: crea rama, commitea, abre PR, CI checks, deploy a Vercel — **todo atómico** (sep 2026).
- **Visual Design Mode**: toolbar, capas, mediciones, click-to-edit. No solo chat.
- **Integraciones MCP**: Figma (import), Snowflake, Notion, Shopify, Stripe, Linear, custom (100/scope).
- **API v2 headless** (ago 2026): prompt → preview URL en Vercel Sandbox. Para CI/CD propio.

**Lo malo**:
- **Solo React/Next.js/Tailwind** (Nuxt añadido 2026, pero secundario). Si usas Vue/Svelte/Astro/Remix, no es tu herramienta.
- **Cloud-only**: no self-host, no offline.
- **Black box**: el código generado a veces tiene patrones que no entiendes. En prod, toca auditar.
- **Coste acumula**: $30-200/mes si lo usas en serio. Free ($5/mes) se queda corto rápido.
- **Middleware complejo**: auth, i18n, rate-limiting a veces necesita mano humana.

---

## Bolt.new: "corre en tu navegador, no en la nube"

**Qué es**: StackBlitz + WebContainers = **Node.js real en el browser**. Genera código y **lo ejecuta al instante** en una pestaña. No hay servidor de Vercel/Anthropic: tu browser compila y sirve.

**Stack**: Vite, React/Vue/Svelte/Solid/Astro, Tailwind, cualquier npm package. **Full-stack con backend en el browser** (hono, elysia, express).

**Precios (sep 2026)**:
| Plan | Mensual | Qué incluye |
|------|---------|-------------|
| **Free** | $0 | Proyectos ilimitados, 50 MB, público |
| **Pro** | $20 | Proyectos privados, 1 GB, custom domain, GitHub sync |
| **Team** | $40/user | Colaboración, SSO, billing centralizado |
| **Enterprise | Custom | Todo + SLAs, on-prem WebContainers |

**Lo bueno**:
- **Cero latencia**: editas y ves el resultado INSTANTÁNEO. No hay round-trip a servidor.
- **Stack libre**: no te casa con Next.js. Vue, Svelte, Astro, lo que quieras.
- **Funciona offline** (una vez cargado). Ideal para avión/tren.
- **Exporta a GitHub/Zip/Netlify/Vercel** en 1 click.

**Lo malo**:
- **RAM del browser**: proyectos grandes (>500 archivos) petan la pestaña. Chrome se come 2-4 GB.
- **No hay BD real**: backend corre en WebContainer (memoria). Para BD necesitas Supabase/Neon externo.
- **Menos pulido en UI**: shadcn/ui no viene por defecto, hay que configurar.
- **IA menos "senior"**: v0 genera código más limpio y con mejores patrones.

---

## Lovable: "para founders no-técnicos (y devs que quieren velocidad)"

**Qué es**: Enfoque **producto, no código**. "Describe tu idea → app funcional con auth, BD, pagos, email". Backend: **Supabase (PostgreSQL + Auth + Realtime + Storage + Edge Functions)**.

**Precios (sep 2026)**:
| Plan | Mensual | Qué incluye |
|------|---------|-------------|
| **Free** | $0 | 5 proyectos, 100 MB, público |
| **Launch** | $25 | Proyectos ilimitados, custom domain, GitHub sync |
| **Scale** | $100 | Team collab, SSO, priority support |
| **Enterprise | Custom | Dedicated infra, SLA, compliance |

**Lo bueno**:
- **Supabase nativo**: auth (email, OAuth, magic link), BD real, realtime, storage, edge functions. **Listo para prod**.
- **Prompts en lenguaje de negocio**: "marketplace de freelancers con chat, pagos Stripe, reviews" → te monta todo.
- **GitHub sync** bidireccional. Puedes tocar código y Lovable respeta tus cambios.
- **Precios claros**: incluye Supabase en el plan (hasta límites).

**Lo malo**:
- **Menos control granular**: v0/Bolt te dejan editar el Tailwind class a class. Lovable es más "caja negra".
- **Vendor lock-in Supabase**: migrar a otro backend = reescribir.
- **IA orientada a MVP, no a código mantenible**: a veces genera spaghetti que cuesta escalar.
- **Comunidad más pequeña** = menos templates, menos ejemplos.

---

## Comparativa rápida: ¿cuál elijo?

| | v0 | Bolt.new | Lovable |
|--|----|----------|---------|
| **Stack** | Next.js + Tailwind + shadcn/ui (opinionado) | Libre (Vite + cualquier framework) | Next.js + Supabase (opinionado) |
| **Backend** | Neon + Drizzle + Better Auth | WebContainer (memoria) o externo | **Supabase nativo** (auth, DB, realtime, storage) |
| **Calidad código** | ⭐⭐⭐⭐⭐ (production-ready) | ⭐⭐⭐⭐ (bueno, menos convenciones) | ⭐⭐⭐ (MVP-ready, auditar para escalar) |
| **Velocidad iteración** | ⭐⭐⭐ (round-trip nube) | ⭐⭐⭐⭐⭐ (instantáneo, local) | ⭐⭐⭐⭐ (bueno, Supabase rápido) |
| **Offline** | ❌ | ✅ (tras carga) | ❌ |
| **Export/ownership** | ✅ Código tuyo, deploy donde quieras | ✅ Código tuyo, export ZIP/GitHub | ✅ Código tuyo, GitHub sync |
| **Curva aprendizaje** | Media (Next.js, shadcn) | Baja (tu stack) | Baja (enfoque producto) |
| **Coste entrada** | Free $5/mes | Free (generoso) | Free (5 proyectos) |
| **Mejor para** | **Devs React/Next.js, portfolio, SaaS serios** | **Devs multi-stack, prototipos rápidos, offline** | **Founders, MVPs con auth/BD/pagos YA** |

---

## Mi combo real para portfolio y prácticas DAW

| Necesidad | Herramienta | Por qué |
|-----------|-------------|---------|
| **Portfolio personal (Next.js + Tailwind)** | **v0 Free** | Calidad código, shadcn/ui nativo, deploy Vercel 1-click, GitHub sync |
| **Prototipo rápido para examen/entrega mañana** | **Bolt.new Free** | Instantáneo, cualquier framework, funciona offline, export ZIP |
| **MVP con auth + BD + pagos para proyecto fin de curso** | **Lovable Launch ($25)** | Supabase incluido, auth real, Stripe, listo prod en horas |
| **Landing page estática para cliente freelance** | **v0 o Bolt** | v0 si Next.js, Bolt si Astro/Hugo (más rápido build) |

**Flujo real que uso**:
1. **v0**: "landing page para mi portfolio: hero, projects grid, contact form, dark mode, animations" → copy/paste a mi repo Next.js → `npm run dev` → ajustes manuales → deploy Vercel.
2. **Bolt**: "component Vue 3 + Tailwind: tabla sortable, filterable, paginada para lista de usuarios" → export → integra en mi proyecto Vue de prácticas.
3. **Lovable**: solo si el proyecto **requiere auth/BD real desde día 1** y no quiero configurar Supabase a mano.

---

## Herramientas emergentes que vigilo (2026 H2)

| Herramienta | Qué promete | Estado |
|-------------|-------------|--------|
| **Tempo (tempo.new)** | React + Storybook + tests generados | Beta privada |
| **Magic Patterns** | Design system → código + Figma sync | Early access |
| **Create.xyz** | Full-stack con SQLite local + sync | Beta |
| **Replit Agent** | Replit + IA agente (código + deploy) | GA 2026 |
| **GitHub Spark** | Micro-apps en GitHub (experimental) | Preview |

---

## Conclusión: no te cases con una, úsalas por fase

**Fase 1: Exploración / Prototipo rápido** → **Bolt.new Free**. Cero fricción, stack libre, offline.
**Fase 2: Portfolio / SaaS serio / Código que mantendrás** → **v0 Plus ($30)**. Calidad Next.js, GitHub sync, deploy atómico, MCP para tu stack.
**Fase 3: MVP con auth/BD/pagos para validar idea** → **Lovable Launch ($25)**. Supabase incluido, listo prod, iteras en lenguaje de negocio.

**Para estudiante DAW**: **v0 Free + Bolt Free** cubren el 90% de casos (portfolio, prácticas web, componentes). **Lovable** solo si tu proyecto final de curso **necesita backend real** y no quieres perder tiempo en auth/BD.

Mi consejo: **prueba las tres versiones gratis esta tarde**. En 30 min cada una sabrás cuál "te habla". La IA no te va a escribir el portfolio por ti, pero te quita el síndrome de la pantalla en blanco y el CSS que no centra el div.

¿Cuál has probado? ¿Qué generaste? Deja en comentarios tu prompt y el resultado.