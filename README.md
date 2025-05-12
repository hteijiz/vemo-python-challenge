# Desafío Técnico - Python Developer Senior (API REST de Logs)

## Descripción

Este desafío evalúa tu capacidad para estructurar una aplicación en FastAPI, aplicando buenas prácticas de desarrollo backend. Deberás construir una pequeña API REST que interactúe con un archivo de logs y permita consultarlo de manera filtrada.

---

## Objetivo

Desarrollar un microservicio en Python usando FastAPI que exponga los siguientes endpoints:

### `GET /logs?filter=ERROR`
- Lee un archivo `logs/example.log`.
- Devuelve un JSON con todas las líneas que contengan el texto del filtro (opcional).
- Si no se pasa filtro, devuelve todas las líneas.

### Opcional (Bonus)

- `POST /logs` para agregar una línea nueva al archivo.
- Agregar logs enriquecidos en consola (colores, formato).
- Agregar Dockerfile funcional (solo construcción, no requiere deploy).
- Manejo elegante de errores y validaciones.

---

## Requisitos

- Usar **Python 3** y **FastAPI**.
- No se requiere ningún framework adicional salvo los necesarios para correr FastAPI.
- Estructurar el código de forma clara y modular.
- El archivo de log ya viene precargado (`example.log`), no modificarlo.

---

## Ejemplo de uso

```bash
GET /logs?filter=ERROR
```

**Respuesta esperada:**

```json
[
  "2024-05-10 12:00:06 ERROR Failed to connect to database",
  "2024-05-10 12:00:08 ERROR Timeout on database request",
  "2024-05-10 12:00:20 ERROR Permission denied for user1",
  "2024-05-10 12:00:29 ERROR Failed to write to disk",
  "2024-05-10 12:00:45 ERROR Cron task failed"
]
```

---

## Tiempo estimado

**30 a 40 minutos como máximo.**
