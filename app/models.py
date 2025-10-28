from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(String(255))
    activa = Column(Boolean, default=True)

    productos = relationship("Producto", back_populates="categoria", cascade="all, delete")

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    descripcion = Column(String(255))
    activo = Column(Boolean, default=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id", ondelete="CASCADE"))
    categoria = relationship("Categoria", back_populates="productos")