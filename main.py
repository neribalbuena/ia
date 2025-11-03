# main.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware 

from servicios.base_de_datos import Base, motor 
from rutas import productos as productos_router 

# Carga el modelo antes de crear tablas
import modelos.producto 

app = FastAPI(title="API de Productos - POO", version="1.0")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creación de tablas
Base.metadata.create_all(bind=motor) 

# Montaje de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Rutas CRUD
app.include_router(productos_router.rutas_productos)

# Ruta raíz (HTML)
@app.get("/", response_class=HTMLResponse)
def inicio():
    try:
        with open("static/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    except FileNotFoundError:
        return HTMLResponse("<h1>Error: No se encontró el archivo index.html</h1>", status_code=404)
