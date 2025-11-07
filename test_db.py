import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# --- Configuración ---
# Este script intentará usar la variable de entorno DATABASE_URL.
DATABASE_URL = os.getenv("DATABASE_URL")

# --- Test Functions ---
def test_connection():
    """Intenta conectar a la base de datos e imprime los detalles de la conexión."""
    if not DATABASE_URL:
        print("ERROR FATAL: La variable de entorno DATABASE_URL no está configurada.")
        print("Por favor, configúrala usando: $env:DATABASE_URL='...'")
        return

    # Imprimimos solo la parte del host para ocultar la contraseña en el log.
    host_info = DATABASE_URL.split('@')[-1]
    print(f"Intentando conectar usando el host: {host_info}")
    
    engine = None
    try:
        # Crea un motor de SQLAlchemy
        engine = create_engine(DATABASE_URL)

        # Intenta establecer una conexión
        # El timeout es para no esperar eternamente si la conexión está bloqueada
        with engine.connect() as connection: 
            print("\nÉXITO: La conexión a la base de datos fue exitosa!")
            # Ejecuta una consulta simple para confirmar
            result = connection.execute("SELECT version();").scalar()
            print(f"Versión de la base de datos: {result.split(',')[0]}")

    except OperationalError as e:
        print("\nCONEXIÓN FALLIDA: Ocurrió un Error Operacional.")
        
        error_message = str(e)
        if "could not translate host name" in error_message or "Non-existent domain" in error_message:
            print("\n*** ERROR CRÍTICO DE DNS DETECTADO ***")
            print("El nombre de host no pudo ser resuelto (problema de red/firewall/VPN).")
        elif "password authentication failed" in error_message:
             print("\n*** ERROR DE AUTENTICACIÓN DETECTADO ***")
             print("La contraseña en DATABASE_URL es incorrecta.")
        else:
            print("Detalles del error:")
            print(f"Detalles originales: {e.orig}")

    except Exception as e:
        print(f"\nOCURRIÓ UN ERROR INESPERADO: {e}")

# --- Ejecución ---
if __name__ == "__main__":
    test_connection()