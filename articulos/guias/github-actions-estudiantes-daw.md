---
layout: article
title: "GitHub Actions para estudiantes de DAW: automatiza tests, despliegues y builds sin configurar nada raro"
description: "Guía práctica de GitHub Actions para proyectos DAW: workflow de Java/Maven, deploy en Vercel/GitHub Pages, secrets, y cómo ahorrar dinero siendo estudiante. Todo con código real que funciona."
category: "Guía"
date: 2026-08-31
readtime: 9
---

Mi primer proyecto "profesional" en DAW tenía tests que pasaban en mi portátil y fallaban en el de mi compañero. Dos horas depurando para descubrir que él usaba Java 17 y yo Java 21. Si hubiéramos tenido GitHub Actions configurado, el CI nos lo habría dicho en el primer push. **GitHub Actions te da un pipeline de integración continua gratis** — tests, linting, builds, deploy automático — y lo mejor: funciona sin instalar Jenkins, sin configurar servidores, y sin pagar nada mientras seas estudiante (o tengas un repo público).

---

## Qué es GitHub Actions (la versión que importa)

GitHub Actions es el sistema de CI/CD integrado en GitHub. Cada vez que haces push, abres un PR, o creas un release, puede ejecutar scripts en un contenedor virtual Linux con lo que tú le digas. Piensa en ello como **un bot que ejecuta comandos en tu repo automáticamente**.

Lo que te importa saber:

- **Gratis para repos públicos**: minutos ilimitados. Si tu repo es público (y los de DAW deberían serlo), no pagas nada.
- **Gratis para repos privados**: 2,000 minutos/mes (con plan free). Sobra para un proyecto de DAW.
- **Ubuntu, Windows, macOS**: puedes elegir el SSOO donde corren tus workflows.
- **100+ actions pre-hechas**: para Java, Node, Python, Docker, deploy a Vercel/Netlify/AWS, etc.

---

## Estructura básica: un workflow

Todo vive en `.github/workflows/` dentro de tu repo. Cada archivo YAML es un "workflow". Ejemplo mínimo para un proyecto Java con Maven:

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout código
        uses: actions/checkout@v4

      - name: Configurar JDK 21
        uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'

      - name: Cache de Maven
        uses: actions/cache@v4
        with:
          path: ~/.m2/repository
          key: ${{ runner.os }}-maven-${{ hashFiles('**/pom.xml') }}

      - name: Compilar
        run: mvn -B compile

      - name: Tests
        run: mvn -B test

      - name: Build completo (skip tests)
        run: mvn -B package -DskipTests
```

**Qué hace**: cada push a `main` o PR contra `main` → levanta Ubuntu → instala JDK 21 → compila → ejecuta tests → empaqueta el JAR. Si falla, el commit aparece con ❌ en lugar de ✅. **Sin configurar Jenkins, sin pagar un servidor, sin acordarte de ejecutar tests manualmente.**

---

## Caso real: proyecto DAW con Spring Boot

Aquí va mi workflow real para un proyecto DWES con Spring Boot 3 + H2 + Testcontainers:

```yaml
# .github/workflows/ci.yml
name: CI - Spring Boot

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      # Redis para tests de caché
      redis:
        image: redis:7
        ports:
          - 6379:6379

    steps:
      - uses: actions/checkout@v4

      - name: Configurar JDK 21
        uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: 'maven'

      - name: Tests con cobertura
        run: mvn -B verify -Pcoverage

      - name: Subir cobertura a Codecov
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          fail_ci_if_error: false

      - name: Build Docker image
        run: docker build -t mi-app:${{ github.sha }} .

  deploy-preview:
    needs: test
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy preview a Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: '--pre'
```

**Qué hace este workflow**:
1. **En cada PR**: compila, ejecuta tests con cobertura, sube la cobertura a Codecov, genera una preview en Vercel.
2. **En push a main**: compila, tests, genera Docker image.
3. **Servicios**: levanta un Redis real para los tests de caché.
4. **Caché de Maven**: no descarga dependencias cada vez (ahorra 2-5 min por run).

---

## GitHub Actions para estudiantes: el plan gratis

| Recurso | Gratis (free tier) | Student pack |
|---|---|---|
| Repos públicos | Minutos ilimitados | — |
| Repos privados | 2,000 min/mes | — |
| Runner macOS | 500 min/mes (10x coste) | — |
| Runner Windows | 2x coste (equivalente 1,000 min) | — |
| LFS (archivos grandes) | 1 GB storage, 1 GB bandwidth | — |

**Para un estudiante DAW**: con repos públicos tienes CI **infinito y gratis**. No necesitas el Student Developer Pack para Actions. Con GitHub Actions puedes hacer deploy automático: cada push al repo → build Jekyll → deploy a GitHub Pages. Tu sitio se actualiza solo sin que tengas que hacer `bundle exec jekyll serve` en local.

---

## Secrets: no subas contraseñas al YAML

Si necesitas tokens (Codecov, Vercel, Docker Hub), **nunca los escribas en el YAML**. Usa GitHub Secrets:

1. Ve a tu repo → **Settings → Secrets and variables → Actions → New repository secret**
2. Añade el nombre (ej: `CODECOV_TOKEN`) y el valor
3. En el workflow: `${{ secrets.CODECOV_TOKEN }}`

GitHub enmascara el valor en los logs (sale `***`). Si alguien hace fork de tu repo, los secrets no se copian.

---

## Despliegue automático: tu web sin tocar nada

### GitHub Pages (la más fácil)
```yaml
# .github/workflows/deploy-pages.yml
name: Deploy a GitHub Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci && npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist/

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

### Vercel (para proyectos Next.js/React)
```yaml
# Reutiliza la action de Vercel
- uses: amondnet/vercel-action@v25
  with:
    vercel-token: ${{ secrets.VERCEL_TOKEN }}
    vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
    vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
```

---

## Errores que vi en DAW (y cómo Actions los evita)

| Error | Sin CI | Con GitHub Actions |
|---|---|---|
| "Funciona en mi portátil" | Lo descubres el día de la entrega | El primer push lo dice en 3 min |
| Olvidar compilar antes de push | QA manual, lento | `mvn compile` en cada push |
| Merge conflict que rompe main | Lo descubres cuando despliegas | PR check lo bloquea |
| Tests que fallan silenciosamente | Nadie los ejecuta | `mvn test` automático |
| Secrets en el código | Posible leak | GitHub Secrets enmascara |
| Deploy manual (copiar archivos) | olvidas archivos, versiones | Automático tras merge |

---

## Tips que me habría gustado saber antes

1. **Empieza con el workflow de compilation/test**. No necesitas deploy, Docker, ni Codecov al principio. Solo `mvn test` o `npm test`.
2. **Usa `cache: 'maven'` en setup-java**. Ahorra 2-5 minutos por run. En un examen con tiempo limitado, cada minuto cuenta.
3. **Los runners macOS cuestan 10x**. Si no necesitas macOS explícitamente (para iOS), usa `ubuntu-latest`. Ahorras minutos del tier gratis si tienes repos privados.
4. **Activa los warnings de seguridad**. GitHub te avisa si tienes dependencias con CVEs: `actions/dependency-review-action@v4`.
5. **Puedes ejecutar workflows manualmente**: añade `workflow_dispatch` al trigger y podrás lanzarlos desde la pestaña Actions.
6. **`if: success()` y `if: failure()`** te permiten hacer pasos condicionales (ej: subir logs solo si falla).
7. **Reusable workflows**: si tienes 3 proyectos DAW con el mismo setup, crea una plantilla YAML y reutilízala.

---

## Mi workflow real (el que uso en prácticas)

```yaml
name: DAW CI/CD

on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: 'maven'
      - run: mvn -B verify
      - uses: codecov/codecov-action@v4
        if: always()
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          fail_ci_if_error: false

  notify:
    needs: test
    if: failure()
    runs-on: ubuntu-latest
    steps:
      - name: Aviso en Discord (webhook)
        run: |
          curl -X POST "${{ secrets.DISCORD_WEBHOOK }}" \
            -H "Content-Type: application/json" \
            -d '{"content": "❌ Build falló en ${{ github.repository }}: ${{ github.sha }}"}'
```

**Lo que hace**: compila + test + si falla, manda un aviso a Discord. Cuatro líneas que me ahorran mirar GitHub cada vez que hago push.

---

GitHub Actions no es solo para empresas. **Es la herramienta que separa "funciona en mi máquina" de "funciona"**. Si estás en DAW y todavía no tienes un workflow básico, créalo hoy — te va a ahorrar un dolor de cabeza en el examen.

¿Ya usas GitHub Actions en tus proyectos? ¿Tienes algún workflow que te haya salvado la vida? Cuéntame por email (ivan@codeandia.com).
