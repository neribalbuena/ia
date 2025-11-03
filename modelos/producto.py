# modelos/producto.py

from sqlalchemy import Column, Integer, String, Float, Text
from servicios.base_de_datos import Base 

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False, index=True)
    descripcion = Column(Text, nullable=True)
    precio = Column(Float, nullable=False)
    categoria = Column(String(100), nullable=True, index=True)

    def __repr__(self):
        return f"Producto(id={self.id}, nombre={self.nombre})"
