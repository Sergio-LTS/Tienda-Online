from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/productos", tags=["productos"])

@router.post("/", response_model=schemas.ProductoOut, status_code=201)
async def crear_producto(data: schemas.ProductoCreate, db: AsyncSession = Depends(get_db)):
    return await crud.crear_producto(db, data)

@router.get("/", response_model=list[schemas.ProductoOut])
async def listar_productos(precio: float | None = None, stock: int | None = None, db: AsyncSession = Depends(get_db)):
    return await crud.listar_productos(db, precio, stock)

@router.get("/{id}", response_model=schemas.ProductoOut)
async def obtener_producto(id: int, db: AsyncSession = Depends(get_db)):
    return await crud.obtener_producto(db, id)

@router.put("/{id}", response_model=schemas.ProductoOut)
async def actualizar_producto(id: int, data: schemas.ProductoUpdate, db: AsyncSession = Depends(get_db)):
    return await crud.actualizar_producto(db, id, data)

@router.delete("/{id}")
async def eliminar_producto(id: int, db: AsyncSession = Depends(get_db)):
    return await crud.eliminar_producto(db, id)