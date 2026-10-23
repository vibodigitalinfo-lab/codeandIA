# 🚀 Cómo desplegar el microservicio (gratis, 5 minutos)

Este microservicio es el "cerebro" del corrector de código. Lo vas a desplegar en **Vercel** (gratis) y le vas a dar una clave de **Groq** (gratis).

## Paso 1 — Conseguir la API key de Groq (gratis)

1. Ve a https://groq.com y crea una cuenta gratuita (puedes entrar con Google/GitHub).
2. Ve a "API Keys" en el panel de control.
3. Crea una nueva clave y **cópiala**. La necesitarás en el Paso 3.

## Paso 2 — Subir el código a GitHub

1. Copia la carpeta `_micro-saas/` de este repositorio a una carpeta nueva en tu ordenador.
2. **Renómbrala a `micro-saas`** (quita el guion bajo del principio).
3. Crea un repositorio nuevo en GitHub (puede ser privado, da igual).
4. Sube los archivos de esa carpeta al repositorio.

## Paso 3 — Conectar con Vercel (gratis)

1. Ve a https://vercel.com y crea una cuenta gratuita (con GitHub).
2. Clic en "Add New Project".
3. Importa el repositorio `micro-saas` que acabas de crear.
4. En "Environment Variables", añade:
   - Nombre: `GROQ_API_KEY`
   - Valor: la clave que copiaste en el Paso 1.
5. Clic en "Deploy".

## Paso 4 — Conectar el blog con el microservicio

1. Cuando Vercel termine, te dará una URL tipo `https://micro-saas-xyz.vercel.app`.
2. Abre el archivo `herramientas/corrector-java/index.html` de este blog.
3. Busca la línea que dice `const API_URL = 'TU_URL_DE_VERCEL_AQUI';` y pega la URL de Vercel.
4. Guarda y haz commit.

¡Listo! Tu corrector de código está en línea y es gratuito.

## ¿Cuánto cuesta?

- **Vercel:** plan gratuito (suficiente para este uso).
- **Groq:** plan gratuito con límites razonables (miles de peticiones al mes).
- Si algún día crece mucho, puedes poner un límite de usos gratuitos y cobrar después.

## ¿Qué hace exactamente?

El usuario pega código Java (o cualquier lenguaje) y opcionalmente un error de consola. El servidor:
1. Explica el error en pasos simples, en castellano.
2. Devuelve el código corregido completo.
3. Hace una mini pregunta tipo test (3 opciones) para comprobar que lo ha entendido.
4. Indica cuál es la respuesta correcta.

Todo automatizado, sin que tú tengas que revisar nada manualmente.