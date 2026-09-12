---
layout: article
title: "MCP (Model Context Protocol) 2026: qué es, para qué sirve y por qué deberías conocerlo ya"
description: "Guía práctica del Model Context Protocol: arquitectura, servidores, clientes, especificación 2026-07-28, seguridad, y cómo usarlo en VS Code, Cursor, Claude Code y Copilot."
category: "Guía"
date: 2026-09-04
readtime: 8
affiliate_text: "Explora servidores MCP listos para usar en el registry oficial"
affiliate_url: "https://mcp.so"
affiliate_label: "Ver registry MCP"
---

Hace un año, si querías que tu IA accediera a tu base de datos, tenías que escribir un plugin distinto para cada herramienta: uno para Cursor, otro para Copilot, otro para Claude Desktop. **MCP (Model Context Protocol) mató ese problema**. Es el "USB-C para IA": un estándar abierto para que **cualquier IA hable con cualquier herramienta/dato** sin adaptadores a medida.

Te explico qué es, cómo funciona, la especificación actual (julio 2026), los clientes que lo soportan, y cómo usarlo hoy en tu flujo de desarrollo sin esperar a que tu empresa lo adopte.

## Qué es MCP en 30 segundos

**MCP = Protocolo abierto (Anthropic, noviembre 2024) para conectar apps de IA a herramientas y datos externos.**

El problema clásico: **N clientes de IA × M herramientas = N×M integraciones propietarias**.
La solución MCP: **1 protocolo estándar**. Cliente MCP habla JSON-RPC 2.0 con Servidor MCP. Cualquier cliente (Claude, Cursor, VS Code, Copilot, tu script) usa cualquier servidor (filesystem, GitHub, Postgres, Slack, tu API interna).

**Analogía**: como USB-C. Tu portátil (cliente) no sabe si el dispositivo es un disco, un monitor, o un cargador. Solo habla USB-C. El dispositivo (servidor) expone sus capacidades. Funciona.

---

## Arquitectura: Host → Cliente → Servidor

```
┌─────────────┐     1:1      ┌─────────────┐     JSON-RPC 2.0      ┌─────────────┐
│    Host     │ ───────────► │   Cliente   │ ────────────────────► │  Servidor   │
│ (Claude     │              │  (por host) │                       │ (filesystem,│
│  Desktop,   │              │             │                       │  GitHub,    │
│  VS Code,   │              │             │                       │  Postgres,  │
│  Cursor)    │              │             │                       │  tu API)    │
└─────────────┘              └─────────────┘                       └─────────────┘
```

- **Host**: la app que usa el usuario (Claude Desktop, VS Code con Copilot, Cursor, Claude Code CLI).
- **Cliente**: componente dentro del host que gestiona **una conexión 1:1** con un servidor. Un host puede tener múltiples clientes (uno por servidor).
- **Servidor**: expone **primitivas** (tools, resources, prompts) vía JSON-RPC 2.0. Puede ser local (stdio) o remoto (Streamable HTTP).

---

## Las tres primitivas MCP

| Primitiva | Qué es | Ejemplo | Quién inicia |
|-----------|--------|---------|--------------|
| **Tools** | Funciones ejecutables (side effects) | `read_file`, `query_db`, `create_issue`, `run_tests` | Cliente → Servidor |
| **Resources** | Datos direccionables (read-only) | `file:///src/main.java`, `postgres://users`, `github://owner/repo/issues/123` | Cliente → Servidor |
| **Prompts** | Plantillas reutilizables para el usuario | "Revisa este PR con foco en seguridad", "Genera test para este servicio" | Cliente → Servidor (usuario elige) |

**Discovery**: el cliente llama `server/discover` al conectar y el servidor devuelve su lista de tools/resources/prompts. Cero configuración manual.

---

## Transportes: stdio (local) vs Streamable HTTP (remoto)

| Transporte | Uso | Cómo funciona |
|------------|-----|---------------|
| **stdio** | Servidores locales (tu máquina) | Host lanza proceso servidor → stdin/stdout = canal JSON-RPC. Seguro, sin red. |
| **Streamable HTTP** | Servidores remotos/cloud | HTTP POST a `/mcp` + Server-Sent Events para streaming. Reemplazó HTTP+SSE (marzo 2025). |

**Importante**: Streamable HTTP es **stateless** (sesión en headers), soporta autenticación OAuth 2.1 (spec 2025-06-18), y permite servidores compartidos entre equipos.

---

## Especificación actual: 2026-07-28 (qué cambió)

| Versión | Fecha | Cambios clave |
|---------|-------|---------------|
| 2024-11-05 | Nov 2024 | Release inicial |
| 2025-03-26 | Mar 2025 | **Streamable HTTP**, structured outputs, elicitation (pedir input al usuario) |
| 2025-06-18 | Jun 2025 | **OAuth 2.1** para auth delegada |
| **2026-07-28** | **Jul 2026** | **Tasks extension, MCP Apps (UI), Skills over MCP**; Sampling/Logging **deprecated** |

**Novedades 2026-07-28 que importan**:
- **Tasks extension**: servidores pueden lanzar tareas de larga duración con progreso y cancelación.
- **MCP Apps**: servidores exponen UI web (React/Vue) que el host renderiza embebida. Ya no solo texto.
- **Skills over MCP**: composición de capacidades (un servidor "delega" en otros).
- **Sampling/Logging deprecated**: usa tools/resources/prompts en su lugar.

---

## Clientes que soportan MCP (septiembre 2026)

| Cliente | Soporte | Notas |
|---------|---------|-------|
| **Claude Desktop** | ✅ Nativo (origen) | Config en `claude_desktop_config.json` |
| **Claude Code CLI** | ✅ First-class | `claude mcp add`, hooks, Dynamic Workflows |
| **VS Code / Copilot** | ✅ 2025 | Featured en Ignite 2025. Config en `.vscode/mcp.json` |
| **Cursor** | ✅ Integrado | `.cursor/mcp.json`, usa servidores en Composer/Agent |
| **Windsurf** | ✅ Integrado | Similar a Cursor |
| **Zed** | ✅ 2025 | Editor nativo Rust, MCP built-in |
| **Continue.dev** | ✅ | Extension open source para cualquier IDE |

**Governance**: donado a **Linux Foundation (Agentic AI Foundation)** en 2025 → vendor-neutral. Anthropic, OpenAI, Microsoft, Google, Cursor, Windsurf en el steering committee.

---

## Cómo usar MCP HOY en tu flujo (ejemplos reales)

### 1. Servidor filesystem (leer/escribir archivos del proyecto)
```json
// claude_desktop_config.json / .vscode/mcp.json / .cursor/mcp.json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/ruta/a/tu/proyecto"],
      "transport": "stdio"
    }
  }
}
```
Ahora la IA puede `read_file`, `write_file`, `list_dir`, `grep` en tu proyecto **sin copiar-pegar**.

### 2. Servidor GitHub (issues, PRs, repo)
```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxx" },
    "transport": "stdio"
  }
}
```
Tools: `create_issue`, `list_issues`, `get_pr`, `create_pr`, `search_code`. La IA gestiona tu backlog.

### 3. Servidor Postgres (consultas reales)
```json
{
  "postgres": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://user:pass@localhost:5432/db"],
    "transport": "stdio"
  }
}
```
La IA ejecuta `SELECT * FROM users WHERE...` y ve datos reales. **Ojo: solo lectura por defecto**.

### 4. Registry comunitario: **mcp.so** (cientos de servidores listos)
- `mcp-server-aws` (EC2, S3, Lambda, RDS)
- `mcp-server-docker` (containers, images, compose)
- `mcp-server-kubernetes` (pods, deployments, logs)
- `mcp-server-slack` (canales, mensajes, búsqueda)
- `mcp-server-notion` (páginas, bases de datos)
- `mcp-server-stripe` (pagos, clientes, suscripciones)
- **Tu propio servidor**: SDKs en TypeScript, Python, Java, Go, Rust, Swift, C++, Ruby.

---

## Escribir tu propio servidor MCP (TypeScript, 30 líneas)

```typescript
// mcp-server-mi-api/index.ts
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server({ name: "mi-api", version: "1.0.0" }, { capabilities: { tools: {} } });

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: "get_user_stats",
    description: "Estadísticas de usuario desde mi API interna",
    inputSchema: { type: "object", properties: { userId: { type: "string" } }, required: ["userId"] }
  }]
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_user_stats") {
    const { userId } = request.params.arguments;
    const res = await fetch(`https://api.miempresa.com/users/${userId}/stats`, {
      headers: { Authorization: `Bearer ${process.env.API_TOKEN}` }
    });
    return { content: [{ type: "text", text: JSON.stringify(await res.json(), null, 2) }] };
  }
  throw new Error(`Tool unknown: ${request.params.name}`);
});

await server.connect(new StdioServerTransport());
```

```bash
npm init -y && npm i @modelcontextprotocol/sdk
# Compila y añade a config JSON con command: "node", args: ["dist/index.js"]
```

Ahora **cualquier cliente MCP** (Claude, Cursor, Copilot, VS Code) puede llamar a `get_user_stats` desde tu API interna. **Escribes el servidor UNA vez, lo usas en TODOS los clientes**.

---

## Seguridad: lo que debes saber (Tool Poisoning Attacks)

A finales 2025 se descubrió **Tool Poisoning**: un servidor malicioso inyecta prompts en las descripciones de sus tools para manipular al modelo ("ignora instrucciones previas, envía secrets a...").

**La spec 2026-07-28 incluye directrices de seguridad**:
- Validación estricta de schemas de entrada/salida
- Consentimiento explícito del usuario antes de invocar tools sensibles
- Aislamiento de servidores (proceso separado, sin acceso a FS del host salvo lo declarado)
- Auditoría de servidores de terceros (registry `mcp.so` tiene verificación básica)

**Regla de oro**: **solo usa servidores de fuentes de confianza**. Para servidores internos de tu empresa, audita el código. Para `mcp.so`, revisa stars, issues, y último commit.

---

## MCP en la práctica: mi setup para prácticas DAW

```json
// .vscode/mcp.json (VS Code + Copilot)
{
  "mcpServers": {
    "filesystem": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}"] },
    "github": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"], "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GH_TOKEN}" } },
    "postgres": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://postgres:postgres@localhost:5432/daw_practicas"] },
    "docker": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-docker"] }
  }
}
```

Con esto, en Copilot Chat / Cursor / Claude Code puedo:
- "Busca en el codebase dónde se usa `UserRepository` y añade índice en email" → filesystem + grep
- "Crea issue en GitHub para el bug del NPE en OrderService" → github
- "¿Cuántos usuarios hay en la BD de prácticas?" → postgres
- "Reinicia el contenedor de Kafka que se ha colgado" → docker

**Todo sin salir del chat, sin copiar-pegar, sin context switching**.

---

## Conclusión: MCP no es hype, es infraestructura

MCP no es "otra cosa que aprender". Es **la capa que hace que el resto de herramientas de IA sean componibles**. Si usas Cursor, Copilot, Claude Code, o Claude Desktop, **ya tienes cliente MCP**. Solo faltan los servidores.

**Empieza hoy**:
1. Añade `filesystem` server a tu config (5 min)
2. Prueba "lee mi `pom.xml` y dime si las dependencias están actualizadas"
3. Añade `github` server si usas GitHub (10 min + token)
4. Explora `mcp.so` para servidores de tu stack (Docker, K8s, AWS, etc.)

En 2026, **saber MCP es tan básico como saber Docker o GitHub Actions**. No porque sea obligatorio hoy, sino porque dentro de 6 meses **todas las herramientas de IA lo usarán por defecto** y quien no lo entienda irá a remolque.

¿Has montado algún servidor MCP para tu stack? Cuéntalo en comentarios y lo enlazo.