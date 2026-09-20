---
layout: article
title: "Secrets y variables en GitHub Actions sin morir en el intento"
description: "Guia paso a paso para usar secrets, variables y environments en GitHub Actions. Con errores comunes, ejemplos reales y trucos que nadie te cuenta."
category: "Guía"
date: 2026-09-03
readtime: 7
---

Cuando empecé con GitHub Actions, me pasé una tarde entera intentando pasar una API key a mi workflow. No funcionaba, el error no decía nada útil, y estaba a punto de meter la key directamente en el archivo YAML (spoiler: eso es un error GRAVE).

Si te ha pasado algo similar, esta guía es para ti. Voy a explicar cómo funcionan los secrets y variables de entorno en GitHub Actions, los errores más comunes, y algunos trucos que me habría gustado saber antes.

## Por que no puedes meter API keys en el codigo

Antes de nada, por si alguien tiene dudas: **nunca** pongas contraseñas, tokens o API keys en tu archivo `workflow.yml` o en tu repositorio. Si lo haces:

- GitHub te alertará y puede suspender tu cuenta
- Cualquiera con acceso al repo ve tus credenciales
- Si el repo es público, bots rastrean GitHub buscando secrets expuestos

La solución correcta es usar **GitHub Secrets** y **GitHub Variables**.

## GitHub Secrets: para datos sensibles

Los secrets son pares de valor clave que GitHub encripta y nunca muestra en los logs. Una vez que guardas un secret, no puedes volver a verlo: solo puedes actualizarlo o eliminarlo.

### Como crear un secret

1. Ve a tu repositorio en GitHub
2. Pestaña **Settings** → **Secrets and variables** → **Actions**
3. Clica en **New repository secret**
4. Ponle un nombre (ej: `API_KEY`) y el valor
5. Guarda

### Como usarlo en tu workflow

```yaml
name: Mi Workflow
on: push

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Usar API key
        env:
          MI_API_KEY: ${{ secrets.API_KEY }}
        run: echo "La key existe: ${{ secrets.API_KEY != '' }}"
```

**Punto clave:** los secrets se acceden con `${{ secrets.NOMBRE_DEL_SECRET }}`. El nombre es case-sensitive, así que `api_key` y `API_KEY` son diferentes.

### Errores comunes con secrets

**Error 1: El secret no se encuentra**

Si ves `Error: Unable to resolve action`, puede ser que:
- El nombre del secret tenga un typo
- Estés en la rama incorrecta (los secrets son por rama por defecto)
- El secret esté en un environment y no lo estés especificando

**Error 2: El secret está vacío en el workflow**

Si `secrets.MI_KEY` devuelve vacío, verifica que:
- El secret existe en Settings → Secrets
- Lo estás llamando con el nombre exacto
- No lo estás usando en un step que no tiene acceso (por ejemplo, en un `if` condition)

**Error 3: El secret aparece en los logs**

Si ves algo como `***` en los logs, es correcto: GitHub enmascara los secrets automáticamente. Pero cuidado con `echo $VARIABLE` en bash: si la variable no está bien configurada, puede que se imprima sin enmascarar.

## GitHub Variables: para datos no sensibles

Las variables son similares a los secrets pero:
- **No son encriptadas** (se ven en texto plano)
- Puedes actualizarlas sin eliminar y recrear
- Son ideales para configuraciones que no son secrets pero varían por proyecto

### Crear una variable

1. **Settings** → **Secrets and variables** → **Actions**
2. Pestaña **Variables**
3. **New repository variable**
4. Nombre y valor

### Usarla en el workflow

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Configurar entorno
        env:
          NODE_ENV: ${{ vars.NODE_ENV }}
          APP_VERSION: ${{ vars.APP_VERSION }}
        run: |
          echo "Entorno: $NODE_ENV"
          echo "Versión: $APP_VERSION"
```

La diferencia con los secrets es que `${{ vars.NOMBRE }}` en lugar de `${{ secrets.NOMBRE }}`.

## Variables por defecto de GitHub

GitHub también tiene variables de sistema que no necesitas crear:

| Variable | Contenido |
|---|---|
| `github.repository` | Nombre del repo (owner/repo) |
| `github.ref` | Branch o tag que disparó el workflow |
| `github.sha` | Hash del commit |
| `github.actor` | Quién disparó la acción |
| `github.event_name` | Evento que disparó (push, pull_request, etc.) |
| `runner.os` | Sistema operativo del runner |
| `runner.temp` | Directorio temporal |

Estas son útiles para workflows dinámicos:

```yaml
- name: Info del commit
  run: |
    echo "Repo: ${{ github.repository }}"
    echo "Branch: ${{ github.ref }}"
    echo "Commit: ${{ github.sha }}"
    echo "Autor: ${{ github.actor }}"
```

## Environments: secrets por contexto

Si tu proyecto tiene un entorno de desarrollo y otro de producción (lo cual es muy recomendable), puedes crear **Environments** con secrets y variables diferentes.

### Crear un environment

1. **Settings** → **Environments**
2. **New environment** (ej: `production`, `staging`)
3. Añade secrets y variables específicas de ese environment
4. Opcionalmente, configura **required reviewers** para que alguien apruebe los despliegues

### Usarlo en el workflow

```yaml
jobs:
  deploy-production:
    runs-on: ubuntu-latest
    environment: production  # <-- aqui especificas el environment
    steps:
      - name: Deploy
        env:
          API_URL: ${{ secrets.API_URL }}
          DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
        run: ./deploy.sh
```

Esto es super potente porque el mismo workflow puede desplegar a staging con credenciales de testing y a producción con credenciales reales, simplemente cambiando el `environment`.

## Trucos avanzados

### Secrets en composite actions

Si estás creando una composite action (una acción reutilizable), los secrets se pasan así:

```yaml
# En la action
inputs:
  api-key:
    required: true

steps:
  - name: Usar key
    env:
      API_KEY: ${{ inputs.api-key }}
    run: ./script.sh
```

Y al llamarla:

```yaml
- uses: tu-usuario/mi-action@v1
  with:
    api-key: ${{ secrets.API_KEY }}
```

### USOS de secrets en多个jobs

Si necesitas el mismo secret en varios jobs, simplemente repites `${{ secrets.MI_KEY }}` en cada uno. Los secrets se cargan por job, no por workflow.

### Validar que un secret existe

```yaml
- name: Verificar secret
  run: |
    if [ -z "${{ secrets.MI_KEY }}" ]; then
      echo "Error: MI_KEY no está configurado"
      exit 1
    fi
```

## Flujo recomendado para proyectos de clase

Para un proyecto DAW, yo suelo hacer esto:

1. **Secrets**: API keys de servicios (base de datos, APIs externas, tokens de deploy)
2. **Variables**: configuración del proyecto (node version, nombre del proyecto, URLs de staging)
3. **Environment `production`**: secrets de deploy a producción
4. **Environment `staging`**: secrets de testing

Así mi workflow de CI/CD puede correr tests con credenciales de testing y desplegar a producción con credenciales reales, todo automaticamente.

## Errores que me costaron horas

Porque sé que el debugging de GitHub Actions es frustrante, aquí van algunos errores reales que me han pasado:

1. **Usar `${{ env.MI_KEY }}` en vez de `${{ secrets.MI_KEY }}`**: `env` solo funciona para variables que ya has seteado en el step actual
2. **Olvidar las comillas en el nombre del secret**: `${{ secrets.my secret }}` no funciona por el espacio
3. **Usar secrets en un step `if`**: las condiciones se evalúan antes de que los secrets estén disponibles
4. **Secrets de un fork no se copian**: cuando haces fork de un repo, los secrets no se transfieren (por seguridad)

## Conclusión

Configurar secrets y variables en GitHub Actions parece complicado al principio, pero una vez que entiendes la diferencia entre `secrets`, `vars` y `environments`, todo cobra sentido.

Lo más importante: **nunca** expongas credenciales en tu código, siempre usa secrets para datos sensibles, y aprovecha los environments para separar configuraciones por entorno.

Regla de oro: si un secreto se ha filtrado una vez, da por hecho que está comprometido y rótalo. Mejor pasar por aburrido que por hacker.
