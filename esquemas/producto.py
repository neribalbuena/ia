# esquemas/producto.py

from pydantic import BaseModel
from typing import Optional

class ProductoCrear(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    categoria: Optional[str] = None

class ProductoActualizar(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    categoria: Optional[str] = None

class ProductoSalida(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    categoria: Optional[str] = None

    class Config:
        orm_mode = True
