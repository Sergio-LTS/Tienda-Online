from pydantic import BaseModel, Field

#Categoriaaa
class CategoriaBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: str | None = None

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(BaseModel):
    nombre: str | None = None
    descripcion: str | None = None
    activa: bool | None = None


class CategoriaOut(CategoriaBase):
    id: int
    activa: bool

    class Config:
        from_attributes = True


#Productooo
class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=3)
    precio: float = Field(..., ge=0)
    stock: int = Field(..., ge=0)
    descripcion: str | None = None
    categoria_id: int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: str | None = None
    precio: float | None = Field(default=None, ge=0)
    stock: int | None = Field(default=None, ge=0)
    descripcion: str | None = None
    activo: bool | None = None
    categoria_id: int | None = None

class ProductoOut(ProductoBase):
    id: int
    activo: bool
    class Config:
        from_attributes = True