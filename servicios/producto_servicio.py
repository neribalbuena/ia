# servicios/producto_servicio.py

from sqlalchemy.orm import Session
from modelos.producto import Producto
from esquemas.producto import ProductoCrear, ProductoActualizar
from typing import List, Optional

class ProductoServicio:
    """Clase que maneja la lógica de negocio (CRUD)."""
    
    def __init__(self, db: Session):
        self.db = db

    def crear(self, datos: ProductoCrear) -> Producto:
        producto = Producto(
            nombre=datos.nombre,
            descripcion=datos.descripcion,
            precio=datos.precio,
            categoria=datos.categoria
        )
        self.db.add(producto)
        self.db.commit()
        self.db.refresh(producto)
        return producto
    
    def obtener(self, producto_id: int) -> Optional[Producto]:
        return self.db.query(Producto).filter(Producto.id == producto_id).first()

    def listar(self, categoria: Optional[str] = None, q: Optional[str] = None) -> List[Producto]:
        consulta = self.db.query(Producto)
        if categoria:
            consulta = consulta.filter(Producto.categoria == categoria)
        if q:
            consulta = consulta.filter(
                Producto.nombre.like(f"%{q}%") | Producto.descripcion.like(f"%{q}%")
            )
        return consulta.all()

    def actualizar(self, producto_id: int, datos: ProductoActualizar) -> Optional[Producto]:
        producto = self.obtener(producto_id)
        if not producto:
            return None

        for campo, valor in datos.model_dump(exclude_unset=True).items():
            setattr(producto, campo, valor)

        self.db.commit()
        self.db.refresh(producto)
        return producto

    def eliminar(self, producto_id: int) -> bool:
        producto = self.obtener(producto_id)
        if not producto:
            return False

        self.db.delete(producto)
        self.db.commit()
        return True

    def precio_menor_que(self, max_precio: float) -> List[Producto]:
        return self.db.query(Producto).filter(Producto.precio <= max_precio).all()
