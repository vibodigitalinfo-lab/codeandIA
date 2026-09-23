---
layout: article
title: "Setup de desarrollo en macOS desde cero: la guía que me faltó"
description: "Guia completa para configurar macOS como entorno de desarrollo en 2026. Homebrew, terminal, IDE, Git, Docker y los mejores ajustes para programar."
category: "Guía"
date: 2026-08-22
readtime: 7
---

Cuando compré mi primer Mac para programar, me encontré con un sistema operativo que no tenía nada que ver con Windows. No sabía dónde estaba la terminal, no entendía Homebrew, y la primera vez que intenté instalar Node.js me saltaron 5 errores diferentes.

Si estás empezando con macOS como entorno de desarrollo, o simplemente quieres configurar tu Mac de la forma más eficiente posible, esta guía es para ti. Voy a ir paso a paso desde el primer arranque hasta tener un setup completo para desarrollar.

## Paso 0: Lo primero que hay que hacer

Antes de instalar nada, actualiza macOS a la última versión. Ve a **Preferencias del Sistema** → **Actualización de software** y asegúrate de estar en la última versión estable.

Después, ve a **App Store** y actualiza todas las apps que tengan actualizaciones pendientes. Es molesto pero necesario.

## Paso 1: Terminal y shell

macOS viene con Zsh como shell por defecto, lo cual está bien. Pero la terminal que trae es bastante básica. Instala **iTerm2**:

```bash
# Primero instala Homebrew (si no lo tienes)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Ahora instala iTerm2
brew install --cask iterm2
```

**Homebrew** es el gestor de paquetes de macOS. Es como apt o winget, pero mejor. Si no lo tienes instalado, esta es la primera cosa que debes hacer después de encender tu Mac.

### Oh My Zsh

Una vez con iTerm2, instala Oh My Zsh para una terminal mucho más usable:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Esto te da autocompletado, colores, git integration en el prompt, y cientos de plugins. Algunos plugins que recomiendo:

```bash
# Navegación rápida con z
brew install zsh-autosuggestions zsh-syntax-highlighting
```

Añade esto a tu `~/.zshrc`:

```bash
plugins=(git docker node npm zsh-autosuggestions zsh-syntax-highlighting)
```

## Paso 2: Herramientas基本icas

Instala todo lo básico de una vez:

```bash
# Git (viene con macOS pero mejor tener la última versión)
brew install git

# Node.js (usa nvm para gestionar versiones)
brew install nvm
nvm install --lts
nvm use --lts

# Python
brew install python

# Java (si haces desarrollo Android o backend Java)
brew install openjdk

# Docker
brew install --cask docker
```

### Configurar Git

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
git config --global init.defaultBranch main

# Genera un SSH key para GitHub
ssh-keygen -t ed25519 -C "tu@email.com"
```

Copia la clave pública (`cat ~/.ssh/id_ed25519.pub`) y añádela en GitHub → Settings → SSH Keys.

## Paso 3: El IDE

Para desarrollo web, las opciones principales son VS Code y Cursor. Si todavía no tienes preferencia:

**VS Code** es la opción segura:
```bash
brew install --cask visual-studio-code
```

**Cursor** si quieres IA integrada:
```bash
brew install --cask cursor
```

Yo uso Cursor como IDE principal y VS Code como backup. En ambos casos, después de instalar:

1. Instala las extensiones esenciales:
   - ESLint
   - Prettier
   - GitLens
   - Thunder Client (para APIs)
   - Material Icon Theme

2. Configura el auto-save en Settings
3. Activa el formateo al guardar
4. Configura el terminal integrado con tu shell

## Paso 4: Docker

Docker en Mac funciona un poco diferente que en Linux. Apple tiene **OrbStack** que es más ligero que Docker Desktop:

```bash
brew install --cask orbstack
```

OrbStack es más rápido, consume menos RAM, y es gratis para uso personal. Una vez instalado, tienes `docker` y `docker-compose` disponibles en la terminal.

Para comprobar que funciona:

```bash
docker --version
docker-compose --version
docker run hello-world
```

## Paso 5: Ajustes del sistema para programar

Hay varios ajustes de macOS que deberías cambiar para una mejor experiencia de programación:

### Mostrar la ruta completa en Finder

```bash
defaults write com.apple.finder FXShowPosixPathInTitle -bool true
```

### Mostrar archivos ocultos

```bash
defaults write com.apple.finder AppleShowAllFiles -bool true
```

### Accelerar el key repeat

Ve a **Preferencias del Sistema** → **Teclado** y ajusta:
- Repetición de tecla: **Rápido**
- Retardo antes de repetir: **Corto**

Esto es fundamental para programar. Con los valores por defecto, mantener pulsada una tecla es lentísimo.

### Disable autocorrect

En **Preferencias del Sistema** → **Teclado** → **Texto**, desactiva:
- Corrección ortográfica automática
- Capitalización automática

El autocorrect en código es un infierno. Te cambia variables, nombres de funciones y todo tipo de cosas.

## Paso 6: Herramientas de productividad

Algunas apps que no son esenciales pero mejoran mucho la experiencia:

**Rectangle** (gratis): para gestionar ventanas con atajos de teclado. Imprescindible si trabajas con pantalla dividida.

```bash
brew install --cask rectangle
```

**Stats** (gratis): monitor del sistema en la barra de menús. CPU, RAM, temperatura, disco.

```bash
brew install --cask stats
```

**MQTT Explorer** o **Postman** (gratis): para testing de APIs.

```bash
brew install --cask postman
```

## Paso 7: Configurar el entorno de un proyecto real

Una vez tienes todo lo básico, para empezar un proyecto de DAW (o cualquier proyecto web):

```bash
# Crear un nuevo proyecto con Vite
npm create vite@latest mi-proyecto -- --template react-ts

# Entrar en el proyecto
cd mi-proyecto

# Instalar dependencias
npm install

# Arrancar en desarrollo
npm run dev
```

Si usas Docker para el proyecto:

```bash
# Clonar el proyecto
git clone git@github.com:usuario/proyecto.git
cd proyecto

# Arrancar con Docker
docker-compose up -d

# Ver logs
docker-compose logs -f
```

## Errores comunes en macOS

Algunos problemas que vas a encontrar (y cómo solucionarlos):

**"Permission denied" al instalar cosas con npm:**
```bash
# Solución: usa nvm en vez de npm global con sudo
nvm install --lts
nvm use --lts
npm install -g paquete
```

**Homebrew no funciona después de actualizar macOS:**
```bash
# Reinstala Xcode Command Line Tools
xcode-select --install
```

**Puerto 3000 ocupado:**
```bash
# Encuentra qué lo usa
lsof -i :3000
# Mata el proceso
kill -9 [PID]
```

**Docker consume mucha RAM:**
En OrbStack/Docker Desktop, ajusta los límites de memoria a 4GB como máximo. macOS asigna mucha memoria a Docker por defecto.

## Mi setup personal

Para que tengáis una referencia, este es mi setup actual:

- **Sistema**: macOS Sequoia
- **Shell**: Zsh + Oh My Zsh + iTerm2
- **IDE**: Cursor (con GitHub Copilot)
- **Navegador**: Chrome + Arc para testing
- **Terminal tools**: tmux, fzf, bat, exa
- **Docker**: OrbStack
- **Gestor de versiones**: nvm (Node), pyenv (Python)
- **Database**: TablePlus + Docker para PostgreSQL

## Conclusión

Montar un setup de desarrollo en macOS parece una odisea al principio, pero una vez que tienes Homebrew, una terminal decente y tu IDE configurado, todo fluye.

Lo que más me gusta de macOS para programar es la estabilidad y la integración con herramientas Unix. Si vienes de Windows, la curva de aprendizaje es real, pero una vez que te acostumbras, es difícil volver.

Mi consejo: no copies un setup entero de internet. Instala lo que te quite fricción hoy y añade cuando duela. Un setup se construye por dolor, no por descarga.
