from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

#Categorias
async def crear_categoria(db: AsyncSession, data: schemas.CategoriaCreate):
    existe = await db.scalar(select(models.Categoria).where(models.Categoria.nombre == data.nombre))
    if existe:
        raise HTTPException(status_code=409, detail="La categoría ya existe")
    nueva = models.Categoria(**data.model_dump())
    db.add(nueva)
    await db.commit()
    await db.refresh(nueva)
    return nueva

async def listar_categorias_activas(db: AsyncSession):
    result = await db.scalars(select(models.Categoria).where(models.Categoria.activa == True))
    return result.all()

async def obtener_categoria(db: AsyncSession, id: int):
    categoria = await db.get(models.Categoria, id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

async def actualizar_categoria(db: AsyncSession, id: int, data: schemas.CategoriaUpdate):
    categoria = await db.get(models.Categoria, id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(categoria, k, v)
    await db.commit()
    await db.refresh(categoria)
    return categoria

async def eliminar_categoria(db: AsyncSession, id: int):
    categoria = await db.get(models.Categoria, id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    await db.delete(categoria)
    await db.commit()
    return {"mensaje": "Categoría eliminada"}


#Productooos
async def crear_producto(db: AsyncSession, data: schemas.ProductoCreate):
    cat = await db.get(models.Categoria, data.categoria_id)
    if not cat or not cat.activa:
        raise HTTPException(status_code=400, detail="Categoría inactiva o inexistente")
    nuevo = models.Producto(**data.model_dump())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo

async def listar_productos(db: AsyncSession, precio: float | None = None, stock: int | None = None):
    stmt = select(models.Producto).where(models.Producto.activo == True)
    if precio is not None:
        stmt = stmt.where(models.Producto.precio <= precio)
    if stock is not None:
        stmt = stmt.where(models.Producto.stock >= stock)
    result = await db.scalars(stmt)
    return result.all()

async def obtener_producto(db: AsyncSession, id: int):
    producto = await db.get(models.Producto, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

async def actualizar_producto(db: AsyncSession, id: int, data: schemas.ProductoUpdate):
    producto = await db.get(models.Producto, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(producto, k, v)
    await db.commit()
    await db.refresh(producto)
    return producto