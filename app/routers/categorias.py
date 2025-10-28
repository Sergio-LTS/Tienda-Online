from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .. import crud, schemas
from ..database import get_db, Base, engine

router = APIRouter(prefix="/categorias", tags=["categorias"])

@router.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@router.post("/", response_model=schemas.CategoriaOut, status_code=201)
async def crear_categoria(data: schemas.CategoriaCreate, db: AsyncSession = Depends(get_db)):
    return await crud.crear_categoria(db, data)

@router.get("/", response_model=list[schemas.CategoriaOut])
async def listar_categorias(db: AsyncSession = Depends(get_db)):
    return await crud.listar_categorias_activas(db)

@router.get("/{id}", response_model=schemas.CategoriaOut)
async def obtener_categoria(id: int, db: AsyncSession = Depends(get_db)):
    return await crud.obtener_categoria(db, id)

@router.put("/{id}", response_model=schemas.CategoriaOut)
async def actualizar_categoria(id: int, data: schemas.CategoriaUpdate, db: AsyncSession = Depends(get_db)):
    return await crud.actualizar_categoria(db, id, data)

@router.delete("/{id}")
async def eliminar_categoria(id: int, db: AsyncSession = Depends(get_db)):
    return await crud.eliminar_categoria(db, id)