---
layout: article
title: "Vercel vs Netlify vs GitHub Pages: dónde publicar tu portfolio"
description: "Comparativa real de las 3 plataformas gratis para deploy: límites, CI/CD, dominios y edge functions, y cuál elijo para portfolio y proyectos de DAW."
category: "Comparativa"
date: 2026-08-02
readtime: 8
---

El primer deploy de mi portfolio me costó dos tardes de lucha: DNS que no propagaba, build que fallaba en una y funcionaba en otra, límites de banda ancha que no entendía. Ahora, cada vez que termino un proyecto de prácticas o un side project, **tengo clara cuál uso y por qué**. Te ahorro las vueltas: comparo Vercel, Netlify y GitHub Pages con lo que de verdad importa a un estudiante.

---

## Lo que miro antes de decidir (mis criterios)

| Criterio | Por qué importa para DAW |
|---|---|
| **Generosidad del plan gratis** | Bandwidth, build minutes, sitios, funciones serverless |
| **DX (Developer Experience)** | `git push` → deploy automático, logs claros, rollback fácil |
| **Framework support nativo** | Next.js, Astro, Vite, Hugo, sin configurar `vercel.json` / `netlify.toml` |
| **Dominio personalizado** | Gratis, HTTPS automático, gestión DNS |
| **Edge / Serverless functions** | Para APIs, formularios, auth sin backend propio |
| **Límites reales que te muerden** | No lo que dice la web, lo que te encuentras en producción |

---

## 1. Vercel: el rey de Next.js (y mucho más)

**Plan gratis (Hobby, sep 2026):**
- **Sitios ilimitados**
- **100 GB bandwidth/mes** (generoso)
- **6.000 build minutes/mes** (~200 builds de Next.js medianos)
- **Serverless Functions**: 12s timeout, 1024 MB, 100k invocaciones/mes
- **Edge Functions**: 50ms CPU, 100k invocaciones/mes
- **Dominio personalizado**: gratis + HTTPS auto
- **Preview deployments**: cada push/PR = URL única (ideal para "mira esto, profe")

**Lo bueno:**
- **Next.js 15+ App Router**: zero config, ISR, Server Components, streaming — **funciona out of the box**.
- **Turborepo / monorepos**: detección automática, builds paralelos.
- **Analytics opcional** (10k eventos/mes gratis) — ves visitas reales sin GA.
- **Rollback instantáneo**: un click en el dashboard.

**Lo malo:**
- **No es agnóstico**: si no usas Next.js, pierdes ventajas (ISR, Image Optimization, Middleware).
- **Build minutes se comen rápido** si tienes monorepo o builds pesados (>5 min).
- **Serverless functions 12s** se quedan cortas para tareas largas (scraping, PDFs pesados).

**Mi experiencia:** Mi portfolio (Next.js 15 + Tailwind + MDX) deploya en **45 seg**. Cada PR de prácticas genera preview URL que le mando al profe por Discord. **Cero configuración**. Para proyectos React/Next.js, **es mi default**.

---

## 2. Netlify: el todo-terreno (Astro, Vite, Hugo, 11ty...)

**Plan gratis (Starter, sep 2026):**
- **Sitios ilimitados**
- **100 GB bandwidth/mes**
- **300 build minutes/mes** (más ajustado que Vercel)
- **Functions**: 125k invocaciones/mes, 10s timeout, 1024 MB
- **Edge Functions**: **NO en plan gratis** (solo Pro $19/mes+)
- **Dominio personalizado**: gratis + HTTPS auto
- **Deploy previews**: sí, cada PR
- **Forms gratis**: 100 envíos/mes (ideal para formulario de contacto sin backend)

**Lo bueno:**
- **Framework-agnostic**: Astro, Vite, SvelteKit, Hugo, 11ty, Remix — **detecta y configura solo**.
- **Netlify Functions (Node/Bun/Go/Python)**: más flexibles que Vercel para tareas no-Edge.
- **Split testing / A/B testing** nativo en gratis.
- **CLI potente**: `netlify dev` replica el entorno local (functions, redirects, headers).
- **Forms sin backend**: pones `data-netlify="true"` en tu `<form>` y llegan al dashboard.

**Lo malo:**
- **Build minutes (300)** se acaban rápido si haces muchos deploys o monorepo.
- **Sin Edge Functions en gratis** (límite duro vs Vercel).
- **Dashboard más lento** que Vercel a veces.
- **Image Optimization** no tan integrada como `next/image`.

**Mi experiencia:** Para mi blog de prácticas (Astro + MDX), Netlify deploya en **1 min 20 seg**. El formulario de contacto funciona sin escribir una línea de backend. **Si no usas Next.js, Netlify gana**.

---

## 3. GitHub Pages: el "gratis de verdad" (solo estático)

**Plan gratis (siempre):**
- **Sitios ilimitados** (uno por repo, o `username.github.io` + project pages)
- **Bandwidth: 100 GB/mes** (soft limit)
- **Build: GitHub Actions minutes** (2.000 min/mes gratis en cuenta personal)
- **NO serverless functions** (es hosting estático puro)
- **NO edge functions**
- **Dominio personalizado**: gratis + HTTPS (via Let's Encrypt, a veces tarda 24h)
- **Preview deployments**: NO nativo (haces workflow manual o usas `gh-pages` branch)

**Lo bueno:**
- **Cero coste real** (incluido en tu cuenta GitHub).
- **Actions = CI/CD completo**: puedes hacer lo que quieras en el build (tests, lint, deploy condicional).
- **Tu código y tu deploy en el mismo sitio**.
- **Jekyll nativo** (este blog corre en GH Pages + Jekyll).

**Lo malo:**
- **Solo estático**: nada de API routes, forms, ISR, middleware. Necesitas backend aparte.
- **DNS/HTTPS a veces caprichoso** (especialmente en `*.github.io` nuevo).
- **Sin preview deployments automáticos** por PR (montarlo con Actions = currar).
- **Cache headers limitados** (no controlas `Cache-Control` fino).

**Mi experiencia:** Este blog (Jekyll) está en GitHub Pages. **Para sitios 100% estáticos (docs, blog Jekyll/Hugo, landing HTML/CSS/JS puro) es imbatible por precio**. Para cualquier cosa que necesite server-side, **no sirve**.

---

## Comparativa cara a cara (tabla resumen)

| | Vercel | Netlify | GitHub Pages |
|---|---|---|---|
| **Mejor para** | Next.js, React SSR/ISR | Astro, Vite, Hugo, cualquier SSG | Jekyll, Hugo, docs, landing estáticas |
| **Build min/mes gratis** | 6.000 | 300 | 2.000 (Actions) |
| **Bandwidth/mes** | 100 GB | 100 GB | 100 GB |
| **Serverless Functions** | ✅ 100k/mes, 12s | ✅ 125k/mes, 10s | ❌ |
| **Edge Functions** | ✅ 100k/mes, 50ms | ❌ (solo Pro) | ❌ |
| **Forms gratis** | ❌ | ✅ 100/mes | ❌ |
| **Preview deployments** | ✅ Automático | ✅ Automático | ⚠️ Manual (Actions) |
| **Dominio gratis + HTTPS** | ✅ | ✅ | ✅ |
| **Monorepo / Turborepo** | ✅ Nativo | ⚠️ Config manual | ⚠️ Manual |
| **Analytics gratis** | ✅ 10k eventos | ❌ | ❌ |

---

## Mi veredicto honesto por caso de uso

| Proyecto | Uso | Por qué |
|---|---|---|
| **Portfolio personal (Next.js + Tailwind + MDX)** | **Vercel** | ISR, Image Opt, middleware, preview automático, zero config |
| **Blog de prácticas / docs (Astro / Hugo / 11ty)** | **Netlify** | Agnóstico, forms gratis, CLI `netlify dev`, edge no crítico |
| **Landing estática cliente (HTML/CSS/JS o Astro static)** | **Netlify** o **GitHub Pages** | Si quieres forms → Netlify. Si cero dependencias → GH Pages |
| **Proyecto final DAW con Spring Boot + React** | **Vercel (frontend) + Railway/Render (backend)** | Frontend en Vercel, API en contenedor barato |
| **Side project con API routes / auth / DB** | **Vercel** (Next.js API) o **Netlify Functions** | Edge/Serverless gratis en ambos |
| **Blog técnico personal (este)** | **GitHub Pages + Jekyll** | Cero coste, Actions para CI, control total, ya lo tengo |

---

## El truco que nadie te cuenta: combínalos

No te cases con uno. **Cada proyecto elige su plataforma**:

{% raw %}
```yaml
# .github/workflows/deploy.yml (ejemplo: Astro → Netlify)
name: Deploy to Netlify
on:
  push:
    branches: [main]
  pull_request:
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm ci && npm run build
      - uses: nwtgck/actions-netlify@v3
        with:
          publish-dir: ./dist
          production-branch: main
        env:
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
          NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
```
{% endraw %}

Tienes **Actions minutes gratis (2k/mes)** para buildar donde quieras. El deploy lo mandas a Vercel, Netlify, o GH Pages según el proyecto.

---

## Conclusión: no te compliques

- **Next.js / React con SSR/ISR** → **Vercel**. Punto.
- **Astro, Vite, SvelteKit, Hugo, 11ty, Remix (SSG/SPA)** → **Netlify**. Forms gratis, CLI, agnóstico.
- **100% estático, Jekyll/Hugo, docs, landing simple** → **GitHub Pages**. Gratis total, cero mantenimiento.
- **Necesitas backend real (Spring Boot, Node, Python)** → Despliega frontend en Vercel/Netlify, backend en **Railway ($5/mes), Render (gratis con sleep), Fly.io, o tu VPS**.

Yo tengo **los tres configurados**. Cada repo sabe a dónde va. No hay drama.

No lo pienses más: publica esta tarde algo tuyo en la que más te llame y deja el enlace en tu CV. El sitio perfecto que nunca se sube no cuenta. El feo que está en internet, sí.
