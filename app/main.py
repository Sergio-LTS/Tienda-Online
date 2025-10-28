from fastapi import FastAPI
from .routers import categorias, productos

app = FastAPI(title="Tienda Online Async")

app.include_router(categorias.router)
app.include_router(productos.router)
