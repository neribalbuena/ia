# SQLAlchemy es una librería de Python que permite conectarte y trabajar con bases de datos SQL 
# (como PostgreSQL, MySQL, SQLite, etc.) sin tener que escribir directamente consultas SQL complicadas.
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
# create_engine()
# Crea una “puerta de entrada” a la base de datos.
# SQLAlchemy usa ese engine para abrir conexiones y ejecutar consultas.


from dotenv import load_dotenv
import os

# Carga las variables del archivo .env
load_dotenv()

# Lee la URL del entorno
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("No se encontró la variable 'DATABASE_URL' en el archivo .env")

#Estoy cambiando el psycopg para que ande, no le gusta el 2
DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://")

# Conexión a Supabase
engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)