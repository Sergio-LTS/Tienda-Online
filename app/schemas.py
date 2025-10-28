from pydantic import BaseModel, Field

#Categoriaaa
class CategoriaBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: str | None = None