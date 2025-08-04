# Comandos Útiles para el Desarrollo

## Comandos básicos de uv

### Gestión del proyecto
```bash
# Inicializar un nuevo proyecto
uv init nombre-del-proyecto --python 3.11

# Instalar dependencias
uv sync

# Agregar una nueva dependencia
uv add nombre-del-paquete

# Agregar dependencia de desarrollo
uv add --dev nombre-del-paquete

# Remover una dependencia
uv remove nombre-del-paquete

# Actualizar dependencias
uv lock --upgrade

# Ver el árbol de dependencias
uv tree
```

### Ejecutar la aplicación
```bash
# Ejecutar directamente con uv
uv run main.py

# Ejecutar con uvicorn
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Usar el script de inicio
uv run python start.py --reload

# Ejecutar en modo producción
uv run python start.py --workers 4 --log-level info
```

## Comandos de desarrollo

### Verificar la aplicación
```bash
# Verificar que la aplicación funciona
curl http://localhost:8000/

# Verificar el endpoint de salud
curl http://localhost:8000/health

# Obtener todos los items
curl http://localhost:8000/items

# Crear un nuevo item
curl -X POST "http://localhost:8000/items" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Laptop",
       "description": "Laptop gaming de alta gama",
       "price": 1299.99,
       "is_available": true
     }'
```

### Desarrollo con Python
```bash
# Activar el entorno virtual
source .venv/bin/activate

# Ejecutar Python interactivo
uv run python

# Ejecutar un script específico
uv run python script.py

# Verificar sintaxis
uv run python -m py_compile main.py
```

## Comandos de Git

```bash
# Inicializar repositorio
git init

# Agregar archivos
git add .

# Hacer commit
git commit -m "Mensaje del commit"

# Ver estado
git status

# Ver historial
git log --oneline
```

## Comandos de debugging

```bash
# Ejecutar con debug
uv run uvicorn main:app --reload --log-level debug

# Ver logs en tiempo real
tail -f logs/app.log

# Verificar puertos en uso
lsof -i :8000

# Matar proceso en puerto específico
kill -9 $(lsof -t -i:8000)
```

## Comandos de testing (futuro)

```bash
# Instalar pytest
uv add --dev pytest

# Ejecutar tests
uv run pytest

# Ejecutar tests con coverage
uv run pytest --cov=app

# Ejecutar tests específicos
uv run pytest tests/test_main.py
```

## Comandos de Docker (futuro)

```bash
# Construir imagen
docker build -t fastapi-app .

# Ejecutar contenedor
docker run -p 8000:8000 fastapi-app

# Ejecutar con docker-compose
docker-compose up -d
```

## Comandos de base de datos (futuro)

```bash
# Instalar SQLAlchemy
uv add sqlalchemy

# Instalar PostgreSQL driver
uv add psycopg2-binary

# Ejecutar migraciones
uv run alembic upgrade head

# Crear migración
uv run alembic revision --autogenerate -m "Descripción"
```

## Comandos de linting y formateo (futuro)

```bash
# Instalar herramientas
uv add --dev black flake8 mypy

# Formatear código
uv run black .

# Verificar estilo
uv run flake8 .

# Verificar tipos
uv run mypy .
```

## URLs útiles

- **API raíz:** http://localhost:8000/
- **Documentación Swagger:** http://localhost:8000/docs
- **Documentación ReDoc:** http://localhost:8000/redoc
- **OpenAPI JSON:** http://localhost:8000/openapi.json 