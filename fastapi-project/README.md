# Mi API con FastAPI

Una API REST de ejemplo creada con FastAPI que maneja una colección de items.

## Características

- ✅ API REST completa con FastAPI
- ✅ Validación de datos con Pydantic
- ✅ Documentación automática con Swagger UI
- ✅ Endpoints CRUD para items
- ✅ Manejo de errores HTTP
- ✅ Estructura de proyecto organizada

## Requisitos

- Python 3.11+
- uv (gestor de paquetes y entornos virtuales)

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <tu-repositorio>
   cd fastapi-project
   ```

2. **Instalar dependencias:**
   ```bash
   uv sync
   ```

## Uso

### Ejecutar la aplicación

```bash
# Opción 1: Usando uv
uv run main.py

# Opción 2: Usando uvicorn directamente
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Acceder a la documentación

Una vez que la aplicación esté ejecutándose, puedes acceder a:

- **Swagger UI (documentación interactiva):** http://localhost:8000/docs
- **ReDoc (documentación alternativa):** http://localhost:8000/redoc
- **API raíz:** http://localhost:8000/

## Endpoints disponibles

### Información general
- `GET /` - Mensaje de bienvenida
- `GET /health` - Verificar estado de la API

### Gestión de items
- `GET /items` - Obtener todos los items
- `GET /items/{item_id}` - Obtener un item específico
- `POST /items` - Crear un nuevo item
- `PUT /items/{item_id}` - Actualizar un item existente
- `DELETE /items/{item_id}` - Eliminar un item

## Ejemplo de uso

### Crear un item
```bash
curl -X POST "http://localhost:8000/items" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Laptop",
       "description": "Laptop gaming de alta gama",
       "price": 1299.99,
       "is_available": true
     }'
```

### Obtener todos los items
```bash
curl -X GET "http://localhost:8000/items"
```

## Estructura del proyecto

```
fastapi-project/
├── main.py              # Archivo principal de la aplicación
├── pyproject.toml       # Configuración del proyecto
├── uv.lock             # Archivo de bloqueo de dependencias
├── README.md           # Este archivo
└── .venv/              # Entorno virtual (creado automáticamente)
```

## Desarrollo

### Agregar nuevas dependencias
```bash
uv add <nombre-del-paquete>
```

### Ejecutar en modo desarrollo
```bash
uv run uvicorn main:app --reload
```

### Verificar dependencias
```bash
uv tree
```

## Próximos pasos

- [ ] Agregar base de datos (SQLAlchemy + PostgreSQL)
- [ ] Implementar autenticación JWT
- [ ] Agregar tests unitarios
- [ ] Configurar Docker
- [ ] Implementar logging
- [ ] Agregar validaciones más complejas

## Licencia

MIT
