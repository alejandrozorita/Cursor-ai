from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Crear la instancia de FastAPI
app = FastAPI(
    title="Mi API con FastAPI",
    description="Una API de ejemplo creada con FastAPI",
    version="1.0.0"
)

# Modelos Pydantic para validación de datos
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

# Base de datos simulada
items_db = []
item_id_counter = 1

# Endpoints
@app.get("/")
async def root():
    """Endpoint raíz que devuelve un mensaje de bienvenida"""
    return {"message": "¡Bienvenido a mi API con FastAPI!", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    """Endpoint para verificar el estado de la API"""
    return {"status": "healthy", "message": "La API está funcionando correctamente"}

@app.get("/items", response_model=List[Item])
async def get_items():
    """Obtener todos los items"""
    return items_db

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Obtener un item específico por ID"""
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")

@app.post("/items", response_model=Item)
async def create_item(item: ItemCreate):
    """Crear un nuevo item"""
    global item_id_counter
    new_item = Item(
        id=item_id_counter,
        name=item.name,
        description=item.description,
        price=item.price,
        is_available=item.is_available
    )
    items_db.append(new_item)
    item_id_counter += 1
    return new_item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemCreate):
    """Actualizar un item existente"""
    for i, existing_item in enumerate(items_db):
        if existing_item.id == item_id:
            updated_item = Item(
                id=item_id,
                name=item.name,
                description=item.description,
                price=item.price,
                is_available=item.is_available
            )
            items_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item no encontrado")

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Eliminar un item"""
    for i, item in enumerate(items_db):
        if item.id == item_id:
            deleted_item = items_db.pop(i)
            return {"message": f"Item '{deleted_item.name}' eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Item no encontrado")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
