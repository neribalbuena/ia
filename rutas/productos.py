# rutas/productos.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from esquemas.producto import ProductoCrear, ProductoActualizar, ProductoSalida
from servicios.producto_servicio import ProductoServicio
from servicios.base_de_datos import obtener_sesion

rutas_productos = APIRouter(prefix="/productos", tags=["productos"])

def obtener_servicio(db: Session = Depends(obtener_sesion)):
    return ProductoServicio(db)

@rutas_productos.post("/", response_model=ProductoSalida, status_code=201)
def crear_producto(payload: ProductoCrear, servicio: ProductoServicio = Depends(obtener_servicio)):
    return servicio.crear(payload)

@rutas_productos.get("/", response_model=List[ProductoSalida])
def obtener_productos(servicio: ProductoServicio = Depends(obtener_servicio)):
    return servicio.listar()

@rutas_productos.get("/{producto_id}", response_model=ProductoSalida)
def obtener_producto_por_id(producto_id: int, servicio: ProductoServicio = Depends(obtener_servicio)):
    producto = servicio.obtener(producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@rutas_productos.put("/{producto_id}", response_model=ProductoSalida)
def actualizar_producto(producto_id: int, payload: ProductoActualizar, servicio: ProductoServicio = Depends(obtener_servicio)):
    producto_actualizado = servicio.actualizar(producto_id, payload)
    if producto_actualizado is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto_actualizado

@rutas_productos.delete("/{producto_id}", status_code=204)
def eliminar_producto(producto_id: int, servicio: ProductoServicio = Depends(obtener_servicio)):
    if not servicio.eliminar(producto_id):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado exitosamente"}
