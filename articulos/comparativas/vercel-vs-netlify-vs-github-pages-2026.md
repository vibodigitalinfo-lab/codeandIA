---
layout: article
title: "Vercel vs Netlify vs GitHub Pages: dónde publicar tu portfolio"
description: "Comparativa real de las 3 plataformas gratis para deploy: límites, CI/CD, dominios y edge functions, y cuál elijo para portfolio y proyectos de DAW."
category: "Comparativa"
date: 2026-07-09
readtime: 11
updated: 2026-10-03
last_modified_at: 2026-10-03
---

El primer deploy de mi portfolio me costó dos tardes de lucha: DNS que no propagaba, build que fallaba en una y funcionaba en otra, límites de banda ancha que no entendía. Ahora, cada vez que termino un proyecto de prácticas o un side project, **tengo clara cuál uso y por qué**. Te ahorro las vueltas: comparo Vercel, Netlify y GitHub Pages con lo que de verdad importa a un estudiante.

---

## Lo que miro antes de decidir (mis criterios)

| Criterio | Por qué importa para DAW |
|---|---|
| **Generosidad del plan gratis** | Datos, cómputo, funciones, proyectos y qué pasa si te pasas |
| **DX (Developer Experience)** | `git push` → deploy automático, logs claros, rollback fácil |
| **Framework support nativo** | Next.js, Astro, Vite, Hugo, sin configurar `vercel.json` / `netlify.toml` |
| **Dominio personalizado** | Gratis, HTTPS automático, gestión DNS |
| **Edge / Serverless functions** | Para APIs, formularios, auth sin backend propio |
| **Límites reales que te muerden** | No lo que dice la web, lo que te encuentras en producción |

---

## 1. Vercel: el rey de Next.js (y mucho más)

**Plan gratis (Hobby, comprobado en su documentación el 3 de octubre de 2026):**
- **200 proyectos** (no ilimitados, aunque de sobra para toda una carrera)
- **100 GB de transferencia de datos/mes** (generoso) y 1 millón de peticiones CDN
- **Functions con fluid compute**: 1 millón de invocaciones, 4 horas de CPU activa y 360 GB-hora de memoria provisioned incluidas. Ya no se cobran "build minutes": lo que se mide es el cómputo que gastas
- **Duración máxima de una función: 300 s (5 minutos)** en Hobby, con 2 GB de memoria. Si tu proyecto se desplegó antes de abril de 2025 y no usa fluid compute, el máximo era 60 s
- **100 despliegues al día** y 45 minutos de build como máximo por despliegue
- **Dominio personalizado**: gratis + HTTPS automático
- **Preview deployments**: cada push/PR = URL única (ideal para "mira esto, profe")

**Lo bueno:**
- **Next.js 15+ App Router**: zero config, ISR, Server Components, streaming — **funciona out of the box**.
- **Turborepo / monorepos**: detección automática, builds paralelos.
- **Web Analytics opcional** (50.000 eventos/mes gratis) — ves visitas reales sin GA.
- **Rollback instantáneo**: un click en el dashboard.

**Lo malo:**
- **Hobby se pausa solo si te pasas.** Vercel no cobra de más en el plan gratuito: cuando agotas lo incluido, los despliegues se detienen hasta el siguiente ciclo de facturación. Si el proyecto es una práctica que enseñas el lunes, eso es un problema.
- **El presupuesto de cómputo es pequeño**: 4 horas de CPU activa al mes. Una función que llama a una API externa y se queda esperando gasta memoria mientras espera, aunque la CPU esté parada. Para un backend que hace scraping o genera PDFs, da para poco.

**Mi experiencia:** Mi portfolio (Next.js 15 + Tailwind + MDX) deploya en **45 seg**. Cada PR de prácticas genera preview URL que le mando al profe por Discord. **Cero configuración**. Para proyectos React/Next.js, **es mi default**.

---

## 2. Netlify: el todo-terreno (Astro, Vite, Hugo, 11ty...)

**Plan gratis (Free, con créditos; comprobado el 3 de octubre de 2026):**
- **300 créditos al mes**, con tope duro y sin recarga automática
- **Los build minutes ya no se cobran**: el build no consume créditos. Lo que se paga es el despliegue a producción (**15 créditos cada uno**); los despliegues de vista previa y de rama son **gratis**
- **Ancho de banda**: 20 créditos por GB (una bolsa de 300 créditos son unos 15 GB al mes si solo gastas ahí)
- **Peticiones web**: 2 créditos por cada 10.000 peticiones
- **Functions**: 10 créditos por GB-hora de cómputo. Ya no hay un contador de invocaciones, pero tampoco es gratis: una función que duerme mucho consume memoria
- **Edge Functions**: disponibles, se miden como peticiones web
- **Formularios**: **ilimitados y gratis** (desde abril de 2026)
- **Deploy previews**: ilimitados y gratis en cada PR
- **Dominio personalizado**: gratis + HTTPS automático

**Lo bueno:**
- **Framework-agnostic**: Astro, Vite, SvelteKit, Hugo, 11ty, Remix — **detecta y configura solo**.
- **Netlify Functions (Node/Bun/Go/Python)**: más flexibles que Vercel para tareas no-Edge.
- **CLI potente**: `netlify dev` replica el entorno local (functions, redirects, headers).
- **Forms sin backend**: pones `data-netlify="true"` en tu `<form>` y llegan al dashboard.

**Lo malo:**
- **El presupuesto se gasta en despliegues, no en builds**: 15 créditos por cada publicación a producción son 20 despliegues al mes. Si despliegas en cada commit a `main`, a mitad de mes ya has agotado la bolsa.
- **Si te pasas, el sitio se pausa**: al superar el tope, las páginas y los formularios dejan de responder hasta que renueva el ciclo. No cobra de más, pero un portfolio que se cae el día de la presentación es un susto.

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
| **Cómo se mide el uso gratis** | 4 h CPU + 360 GB-h memoria + 1M invocaciones | 300 créditos/mes | 2.000 min de Actions (cuenta personal) |
| **Ancho de banda/mes** | 100 GB | ~15 GB (20 créditos por GB) | 100 GB (límite blando) |
| **Serverless Functions** | ✅ 1M invocaciones, 300 s máx, 2 GB | ✅ 10 créditos por GB-hora de cómputo | ❌ |
| **Edge Functions** | ✅ (dentro del presupuesto de funciones) | ✅ (se cobran como peticiones web) | ❌ |
| **Forms gratis** | ❌ | ✅ Ilimitadas | ❌ |
| **Preview deployments** | ✅ Automático | ✅ Ilimitadas y gratis | ⚠️ Manual (Actions) |
| **Dominio gratis + HTTPS** | ✅ | ✅ | ✅ |
| **Monorepo / Turborepo** | ✅ Nativo | ⚠️ Config manual | ⚠️ Manual |
| **Analytics gratis** | ✅ 50.000 eventos/mes | ❌ | ❌ |
| **Si te pasas del límite** | ⏸️ Se pausa hasta el ciclo siguiente | ⏸️ Se pausa hasta el ciclo siguiente | ➖ Sin coste, pero sin funciones |

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

## Sigue por aquí

- [Hosting y dominios para tu primer proyecto de DAW](/hosting/)
- [Cómo publicar tu primera web en internet por menos de 5€ con IA](/articulos/guias/como-publicar-primera-web-internet-barato-ia/)
- [GitHub Actions para DAW: automatiza tests y despliegues](/articulos/guias/github-actions-estudiantes-daw/)
- [Cómo crear tu primer portfolio de desarrollador web con IA paso a paso](/articulos/guias/crear-portfolio-desarrollador-web-con-ia/)
