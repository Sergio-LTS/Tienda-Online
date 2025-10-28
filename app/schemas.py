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