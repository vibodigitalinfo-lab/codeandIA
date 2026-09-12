---
layout: article
title: "Cursor Rules (.mdc) 2026: cómo configurar la IA para que programe como tú quieres"
description: "Guía completa del sistema de reglas de Cursor: formato .mdc, tipos de reglas (Always, File-scoped, Intelligent, Manual), mejores prácticas, y ejemplos reales para estudiantes."
category: "Guía"
date: 2026-09-03
readtime: 7
affiliate_text: "Prueba Cursor Pro y configura tus reglas para programar más rápido"
affiliate_url: "https://cursor.com/pricing"
affiliate_label: "Ver planes Cursor"
---

Llevo meses usando Cursor a diario y la diferencia entre "Cursor que alucina" y "Cursor que entiende mi proyecto" no es el modelo, **son las reglas**. El sistema `.cursor/rules/*.mdc` (olvida `.cursorrules`, eso es historia) es lo que convierte a Cursor de "autocompletado caro" a "compañero de equipo que sabe tus convenciones".

Te explico cómo funciona el sistema actual, los cuatro tipos de reglas, cómo escribirlas para que de verdad se apliquen, y ejemplos que uso en mis prácticas de DAW.

## El sistema actual: `.cursor/rules/*.mdc` (no `.cursorrules`)

Desde 2024-2025, Cursor migro de un único archivo `.cursorrules` (markdown plano) a **archivos `.mdc` individuales** en `.cursor/rules/`. Cada archivo es una regla independiente con metadatos YAML frontmatter.

**Estructura obligatoria**:
```markdown
---
alwaysApply: true|false          # Modo "Always"
description: "cuándo aplicar"    # Modo "Intelligent" (opcional)
globs: "src/**/*.tsx"            # Modo "File-scoped" (opcional)
---
# Cuerpo en markdown con referencias @archivo
```

**Tres formas de aplicar (precedencia: Team → Project → User)**:
| Configuración | Modo | Cuándo se aplica |
|---------------|------|------------------|
| `alwaysApply: true` | **Always** | En **cada** request, siempre |
| `globs` (sin description) | **File-scoped** | Solo si editas archivo que matchea el glob |
| `description` (sin globs) | **Intelligent** | El agente decide si es relevante |
| Ni alwaysApply, ni globs, ni description | **Manual** | Solo si invocas `@nombre-regla` en chat |

**Regla de oro**: una regla = una responsabilidad. Mejor 10 reglas de 50 líneas que 1 de 500.

---

## Los cuatro tipos en la práctica

### 1. Always — Reglas globales no negociables
```markdown
# .cursor/rules/project-standards.mdc
---
alwaysApply: true
description: "Estándares de proyecto que SIEMPRE aplican"
---
## Estándares obligatorios
- **Java 21 + Spring Boot 3.3**: nada de versiones viejas
- **Lombok @Data/@Builder** en DTOs, **records** en domain models
- **MapStruct** para mappers, nada de mapping manual
- **Testcontainers** para tests de integración (no H2 en memoria)
- **Convención de paquetes**: `com.empresa.proyecto.modulo.capa`
- **Commits**: Conventional Commits (`feat:`, `fix:`, `refactor:`)
```

Esta regla se inyecta **siempre**. Úsala con cuidado: contamina el contexto si es muy larga. Máximo 100-150 líneas.

### 2. File-scoped — Reglas por tipo de archivo
```markdown
# .cursor/rules/spring-controller.mdc
---
globs: "**/*Controller.java"
---
## Controladores Spring
- **@RestController** + **@RequestMapping** en clase (no en métodos sueltos)
- **DTOs de entrada**: `@Valid` + Bean Validation (`@NotNull`, `@Size`, `@Email`)
- **Respuestas**: `ResponseEntity<ApiResponse<T>>` wrapper consistente
- **Excepciones**: delega a `@ControllerAdvice` global (`GlobalExceptionHandler`)
- **Documentación**: `@Operation` + `@ApiResponses` en cada endpoint
```

Solo se activa cuando tocas un `*Controller.java`. Cursor la carga automáticamente, **no tienes que hacer nada**.

### 3. Intelligent — Reglas que el agente decide cuándo usar
```markdown
# .cursor/rules/testing-strategy.mdc
---
description: "Estrategia de testing: unitarios, integración, contratos, E2E"
---
## Cuándo aplicar esta regla
- El usuario pide "escribe tests para..."
- El usuario modifica archivos en `src/test/`
- El usuario menciona "cobertura", "mock", "testcontainers"

## Estrategia
### Unitarios (JUnit 5 + Mockito)
- Un test por método público del service
- Mocks estrictos (`Mockito.lenient()` solo si justificado)
- Nombrado: `should_[expected]_[when]`
- Cobertura objetivo: 80% en services, 100% en domain logic

### Integración (Spring Boot Test + Testcontainers)
- Un test por endpoint del controller
- BD real (PostgreSQL container), no H2
- Perfil `test` con `application-test.yml`
- Limpieza: `@DirtiesContext` o `@Transactional` rollback

### Contratos (Spring Cloud Contract)
- Solo si hay consumidores externos definidos
- Genera stubs en `build/stubs`
```

El agente **evalúa la description** y decide si inyecta la regla. Funciona bien para cosas transversales (testing, seguridad, logging) que no son "siempre" ni "solo este archivo".

### 4. Manual — Reglas invocadas a demanda
```markdown
# .cursor/rules/kotlin-migration.mdc
---
description: "Guía para migrar Java a Kotlin (solo si se pide explícitamente)"
---
# Migración Java → Kotlin
Solo se usa si el usuario escribe `@kotlin-migration` en el chat.
...
```

Útil para tareas puntuales que no quieres que contaminen el contexto habitual.

---

## Referencias `@archivo`: el superpoder de las reglas

En el cuerpo markdown, usa `@ruta/archivo` para **inyectar el contenido real del archivo** en el contexto de la regla. Ejemplo:

```markdown
# .cursor/rules/database-schema.mdc
---
globs: "**/resources/db/migration/*.sql"
---
## Esquema BD actual
Consulta `@src/main/resources/db/migration/V1__init.sql` para ver tablas, índices y constraints actuales.
Nuevas migraciones deben ser compatibles hacia atrás.
```

Cuando la regla se activa, **Cursor lee el archivo SQL real y lo mete en el contexto**. La IA ve tu esquema real, no alucina.

---

## Mejores prácticas (oficiales + experiencia real)

| Práctica | Por qué |
|----------|---------|
| **<500 líneas por regla** | Contexto limitado; reglas largas desplazan código real |
| **Divide en reglas composables** | `spring-service.mdc`, `spring-repository.mdc`, `spring-dto.mdc` mejor que `spring-all.mdc` |
| **Usa `@archivo` en lugar de copiar** | Siempre actualizado, no se desincroniza |
| **Escribe como docs internas** | Imperativo, específico, con ejemplos. "Haz X" no "Sería bueno X" |
| **Empieza simple, añade cuando falla** | Si Cursor repite un error → nueva regla o amplía existente |
| **Comité al repo (git)** | El equipo comparte reglas; `.cursor/rules/` en `.gitignore` = error |
| **AGENTS.md también funciona** | Markdown plano sin frontmatter, compatible con otras herramientas |

---

## Mis reglas reales para prácticas DAW (copia y adapta)

### `.cursor/rules/java-spring-boot.mdc` (Always)
```markdown
---
alwaysApply: true
description: "Configuración base Spring Boot 3.3 + Java 21"
---
- Java 21 (LTS), Spring Boot 3.3.x
- Gradle (Kotlin DSL `build.gradle.kts`), wrapper incluido
- Lombok: `@Data`, `@Builder`, `@RequiredArgsConstructor`, `@Slf4j`
- Records para domain models inmutables
- MapStruct para DTO ↔ Entity mapping
- Validation: Jakarta Bean Validation (`@NotNull`, `@Size`, `@Pattern`)
- Excepciones: `@ControllerAdvice` + `ProblemDetail` (RFC 9457)
- Log: SLF4J + Logback, MDC para traceId
```

### `.cursor/rules/spring-service.mdc` (File-scoped)
```markdown
---
globs: "**/service/**/*.java"
---
## Capa Service
- **@Service** + **@Transactional(readOnly = true)** por defecto
- Métodos de escritura: `@Transactional` (sin readOnly)
- Inyección: constructor (`@RequiredArgsConstructor`), no `@Autowired` en campo
- Excepciones de negocio: custom exceptions (`BusinessException`, `NotFoundException`)
- No lógica de presentación ni DTOs de respuesta aquí
```

### `.cursor/rules/testing-unit.mdc` (Intelligent)
```markdown
---
description: "Tests unitarios con JUnit 5 + Mockito + AssertJ"
---
## Unitarios
- `@ExtendWith(MockitoExtension.class)`
- `@Mock` para dependencias, `@InjectMocks` para SUT
- **Given/When/Then** con comentarios
- AssertJ: `assertThat(result).isEqualTo(expected)`
- Edge cases: null, empty, boundary, exception
- Nombrado: `shouldReturnUserWhenExists`, `shouldThrowWhenNotFound`
```

### `.cursor/rules/git-workflow.mdc` (Intelligent)
```markdown
---
description: "Workflow de git: ramas, commits, PRs, revisión"
---
## Git workflow
- Rama por issue: `feat/123-add-jwt-auth`, `fix/456-npe-order-service`
- Commits: Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`)
- PR: título = commit principal, descripción = qué + por qué + cómo testear
- Rebase sobre `main` antes de PR, no merge
- CI debe pasar: build, tests, checkstyle, dependency-check
```

---

## Precios Cursor (septiembre 2026) — qué incluye cada plan

| Plan | Mensual | Límites Agent | Modelos frontera | MCP | Teams |
|------|---------|---------------|------------------|-----|-------|
| **Hobby (Free)** | $0 | Limitado | ❌ | ❌ | ❌ |
| **Pro** | $20 | Extendido | ✅ | ✅ | ❌ |
| **Pro+** | $60 | Alto | ✅ | ✅ | ❌ |
| **Ultra** | $200 | Máximo | ✅ | ✅ | ❌ |
| **Teams Standard** | $40/user | Centralizado | ✅ | ✅ | ✅ SSO, marketplace |
| **Teams Premium** | $120/user | 5× Agent | ✅ | ✅ | ✅ Todo |

**Dos pools de uso**: Cursor Models (Grok, Composer) + Other Models (API pricing). Overages a precio API + $0.25M tokens "Cursor Tax" en third-party.

**Para estudiante**: **Hobby gratis** llega para uso diario moderado. **Pro ($20)** si necesitas modelos frontera y límites altos. No hay descuento estudiante oficial.

---

## Migración desde `.cursorrules` (si vienes de versión antigua)

1. Crea `.cursor/rules/` en la raíz del proyecto
2. Parte tu `.cursorrules` en archivos `.mdc` por responsabilidad
3. Añade frontmatter YAML según el modo que quieras
4. Borra `.cursorrules` (Cursor lo ignora si existe `.cursor/rules/`)
5. Commit y push

**Nota**: `AGENTS.md` (markdown plano en raíz) también lo lee Cursor como reglas "Manual" — útil para compatibilidad con otras herramientas (Claude Code, etc.).

---

## Conclusión: las reglas son tu "contrato" con la IA

Sin reglas, Cursor es un junior entusiasta que a veces acierta y a veces la lía. **Con reglas bien escritas, es un senior que conoce tu codebase, tus convenciones, y tu stack**.

Mi recomendación: empieza con **3-4 reglas Always/File-scoped** que cubran lo básico (stack, arquitectura, testing). Añade **Intelligent** para cosas transversales. Cuando Cursor falle en algo repetido, **escribe una regla para ese caso**. En dos semanas tienes un "manual de estilo ejecutable" que te ahorra revisar PRs propios.

¿Tienes reglas que te hayan salvado la vida? Compártelas en comentarios y las añado al artículo.