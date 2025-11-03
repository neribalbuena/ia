# servicios/base_de_datos.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./productos.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

motor = create_engine(DATABASE_URL, connect_args=connect_args, echo=False)

SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=motor)

Base = declarative_base()

def obtener_sesion():
    """Devuelve una sesión de base de datos para inyectar en FastAPI."""
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()
