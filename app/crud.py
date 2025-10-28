from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

#Categorias
async def crear_categoria(db: AsyncSession, data: schemas.CategoriaCreate):
    existe = await db.scalar(select(models.Categoria).where(models.Categoria.nombre == data.nombre))
    if existe:
        raise HTTPException(status_co