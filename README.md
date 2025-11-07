# API de Productos - FastAPI + POO + IA

Trabajo Práctico - Laboratorio de Programación III

## Objetivo
Desarrollar una API funcional aplicando Programación Orientada a Objetos, con estructura modular y endpoints CRUD.

## Estructura
- main.py  
- base_de_datos.py  
- modelos/producto.py  
- esquemas/producto.py  
- servicios/producto_servicio.py  
- rutas/productos.py  

## Instalación
```bash
pip install -r requirements.txt



-------------------------------------------------------
RESUMEN GENERAL

Este trabajo es una API REST desarrollada con FastAPI, bajo un modelo de programación orientada a objetos (POO).
La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una tabla de productos, conectada a 

🟩 1. main.py → Punto de entrada del sistema

Función:
Este archivo es el “cerebro” principal de la aplicación.
Se encarga de:

Inicializar FastAPI

Conectar la base de datos

Cargar las rutas (endpoints)

Montar los archivos estáticos (HTML y JS)

Configurar permisos CORS para el frontend


Lógica por bloques:

Bloque	Descripción

Importaciones	Se importan FastAPI, CORS, HTMLResponse y los módulos del proyecto (rutas, base de datos, modelos).
Configuración CORS	Permite que el navegador (index.html) pueda acceder a la API sin restricciones.
Creación de tablas	Usa SQLAlchemy (Base.metadata.create_all()) para crear la tabla productos automáticamente si no existe.
Montaje de archivos estáticos	Expone la carpeta /static para poder abrir el HTML directamente desde la API.
Incluir rutas de negocio	Conecta las funciones CRUD definidas en rutas/productos.py.
Ruta raíz /	Carga el index.html con un manejo de error si el archivo no se encuentra.


Dónde te ayudó la IA:

> La IA me ayudó a configurar correctamente el CORS y a mejorar el manejo de errores cuando el archivo index.html no existe, proponiendo envolverlo en un bloque try/except para evitar fallos del servidor.




🟦 2. servicios/base_de_datos.py → Configuración de la base de datos

Función:
Conecta la API con la base de datos.
Separa la lógica de conexión para poder usar diferentes motores (SQLite o Supabase).

Lógica:

Usa os.getenv() para leer la variable DATABASE_URL.

Si no existe, crea una base SQLite local (productos.db).

Configura el motor SQLAlchemy (create_engine) y la sesión de conexión (SessionLocal).

Define una función generadora obtener_sesion() que abre y cierra la conexión en cada petición (inyección de dependencia).


Dónde ayudó la IA:

> La IA me explicó cómo usar os.getenv para que la conexión sea flexible y no fija, así el mismo código sirve para Supabase, SQLite o cualquier otro motor.





🟧 3. modelos/producto.py → Definición del modelo ORM

Función:
Representa la tabla “productos” en la base de datos.
Cada atributo de la clase Producto es una columna real.

Lógica:

Usa SQLAlchemy para definir la estructura: id, nombre, descripcion, precio, categoria.

Incluye índices para acelerar búsquedas.

El método _repr_() devuelve una representación legible del objeto, útil para depurar.


Dónde me ayudó la IA:

> Me sugirió agregar el método _repr_() para facilitar el debugging al imprimir objetos en consola.




🟨 4. esquemas/producto.py → Validación y estructura de datos

Función:
Define cómo deben enviarse y recibirse los datos entre el frontend y la API usando Pydantic.

Lógica:

ProductoCrear: datos necesarios para crear un producto.

ProductoActualizar: datos opcionales para modificar un producto existente.

ProductoSalida: define qué se devuelve al usuario (incluye el id y activa orm_mode para convertir objetos SQLAlchemy a JSON).


Dónde  ayudó la IA:

> Me explicó la diferencia entre los modelos de base de datos y los esquemas Pydantic, y me ayudó a estructurar los tres modelos (Crear, Actualizar, Salida) de manera profesional.





🟥 5. servicios/producto_servicio.py → Lógica de negocio (POO)

Función:
Contiene la clase ProductoServicio, que implementa toda la lógica CRUD y aplica los principios de programación orientada a objetos.

Lógica de la clase:

Método	Descripción

_init_	Recibe la sesión de base de datos (inyección de dependencia).
crear()	Crea un nuevo producto y lo guarda.
obtener()	Devuelve un producto por ID.
listar()	Lista todos los productos o filtra por categoría/palabra clave.
actualizar()	Modifica un producto existente, usando setattr.
eliminar()	Borra un producto de la base de datos.
precio_menor_que()	Devuelve productos por debajo de un precio máximo.


Dónde nos ayudó la IA:

> La IA me ayudó a optimizar el método listar() para aceptar filtros opcionales (categoria, q) y a usar exclude_unset=True en actualizar(), evitando sobrescribir campos vacíos.




---

🟪 6. rutas/productos.py → Definición de endpoints (controladores)

Función:
Define todas las rutas HTTP de la API (/productos/, /productos/{id}, etc.).
Cada ruta llama a los métodos del servicio ProductoServicio.

Lógica:

Endpoint	Método	Función

/productos/	POST	Crea un nuevo producto.
/productos/	GET	Lista todos los productos.
/productos/{id}	GET	Obtiene un producto específico.
/productos/{id}	PUT	Actualiza un producto existente.
/productos/{id}	DELETE	Elimina un producto.


Usa inyección de dependencias con Depends(obtener_servicio) para crear una instancia del servicio automáticamente en cada petición.

Dónde ayudó la IA:

> Me ayudó a definir los decoradores de ruta correctamente (@rutas_productos.get, .post, .put, .delete) y a devolver los códigos HTTP adecuados como 201 o 204.




---

🟫 7. static/index.html → Interfaz de usuario (Frontend animado)

Función:
Es la parte visual del sistema.
Permite interactuar con la API desde el navegador, con animaciones y diseño moderno.

Lógica:

HTML: estructura general (formulario + tabla de productos).

CSS: efectos futuristas, fondo animado, botones con gradientes, y transiciones suaves.

JS (incrustado): realiza las llamadas fetch() a la API (GET, POST, DELETE).


Funciones principales en JavaScript:

Función	Acción

obtenerProductos()	Trae todos los productos de la API y los muestra en la tabla.
crearProducto()	Envía datos del formulario y crea un nuevo producto.
eliminarProducto(id)	Elimina un producto de la base de datos.
Filtro en tiempo real	Permite buscar productos en la tabla por nombre, descripción o categoría.


Dónde me ayudó la IA:

> La IA me ayudó a mejorar el diseño CSS agregando animaciones con keyframes, sombras suaves y un fondo animado con gradientes en movimiento.




---

  POO aplicada a FastAPI

Algo así:

> En lugar de escribir la lógica CRUD directamente dentro de las rutas, utilicé una clase ProductoServicio, que encapsula toda la lógica de negocio.
Esto hace que el código sea más modular, mantenible y reutilizable, siguiendo los principios de la programación orientada a objetos: encapsulamiento, modularidad y separación de responsabilidades.




---



> “Este archivo main.py actúa como el núcleo de la aplicación, inicializando el servidor FastAPI, montando las rutas y conectando la base de datos.”

La IA me ayudó a estructurar el proyecto en capas, separando los modelos, esquemas, servicios y rutas para mantener una arquitectura limpia.

En el servicio ProductoServicio, aplico POO creando una clase con métodos que representan cada operación CRUD.

El frontend se comunica con la API usando fetch en JavaScript, lo que permite manejar los datos de manera dinámica y actualizar la tabla sin recargar la página.

cd fastapi_poo
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
uvicorn main:app --reload