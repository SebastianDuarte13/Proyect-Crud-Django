# Sistema de Gestión de Suministros con Django 



### Descripción

Este sistema permite gestionar el control de suministros en nuestra empresa, cumpliendo con los requisitos estandarizados de nuestro cliente. El programa sigue la arquitectura **MTV (Model Template View)**, utilizando **HTML, CSS y Bootstrap** para el frontend.

Para el backend, emplearemos el **framework Django**, lo que garantizará mayor seguridad en el código, reducirá la cantidad de código necesario y facilitará la integración con una base de datos estructurada mediante **ORM (Object-Relational Mapping)**.

![IMAGEN DE INICIO](/images/index_proyect.png)

### Requerimientos

```tex
El sistema debe permitir la gestión de productos, proveedores y suministros, asegurando la actualización automática del stock y la validación de datos. Debe registrar, listar, editar y eliminar productos y proveedores, evitando la eliminación si hay dependencias. Además, debe permitir la creación y consulta de suministros con fecha de registro, filtrando por producto, proveedor o rango de fechas. Se requiere control de seguridad para evitar registros duplicados y reportes de suministros, productos con bajo stock e historial de movimientos.
```

![IMAGEN DE SUMINISTROS](/images/muestra_suministro.png)

## **Antes de ejecutar el proyecto**

Para que el proyecto funcione, es necesario instalar algunas dependencias con `pip`:

```bash
pip3 install django  # Permite ejecutar Django  
pip3 install pymysql  # Facilita la conexión y migraciones con MySQL  
pip3 install pillow  # Biblioteca para manejar imágenes en Django  
```

`Pillow` es una librería que permite procesar imágenes en Django, como redimensionarlas o convertir su formato.



## BASE DE DATOS

Esta es nuestra base de datos estandarizada, diseñada para cumplir con todos los requerimientos del sistema.

![base de datos](/images/Base%20de%20datos%20parcial.png)

### Base de datos en codigo sql

```sql
CREATE DATABASE IF NOT EXISTS crud_proyecto;

USE crud_proyecto;


CREATE TABLE proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    estado TINYINT(1) NOT NULL DEFAULT 1 -- Siempre inicia en 1 (activo)
);

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(200),
    stock INT NOT NULL DEFAULT 0, -- Siempre inicia en 0
    estado TINYINT(1) NOT NULL DEFAULT 1 -- Siempre inicia en 1 (activo)
);

CREATE TABLE suministros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT NOT NULL,
    id_proveedor INT NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0), -- No permite valores negativos o cero
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Fecha de creación automática
    FOREIGN KEY (id_producto) REFERENCES productos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id) ON UPDATE CASCADE ON DELETE RESTRICT
);
```

### Conexión con la base de datos en Django

Para que el proyecto funcione, debemos configurar la base de datos en el archivo `sistema/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'NOMBRE DE LA BASE DE DATOS', 
        'USER': 'USUARIO SI LO TIENES POR DEFECTO ESTE SERA ROOT',
        'PASSWORD': 'CONTRASEÑA PARA ACCEDER A LA BASE DE DATOS',
        'HOST': 'EL SERVIDOR POR DEFECTO ESTE SERA LOCALHOST',
        'PORT': 'PUERTO CONFIGURADO DE LA BDD'
    }
}
```

### Otro método para crear la base de datos

Django permite crear la base de datos sin escribir SQL, utilizando `PyMySQL` para gestionar las migraciones. Para instalarlo:

```bash
pip install PyMySQL
```

Luego, ejecutar los siguientes comandos para crear las tablas:

```bash
python3 manage.py makemigrations  # Crea y valida las migraciones
python3 manage.py migrate  # Aplica las migraciones a la base de datos
```

## CÓMO CREAR UN PROYECTO DJANGO 

Para crear un nuevo proyecto en Django, ejecuta el siguiente comando en la terminal:

```bash
python -m django startproject mi_proyecto .
```

`python -m django startproject mi_proyecto .` → Crea un nuevo proyecto llamado **mi_proyecto** en el directorio actual (`.` evita crear una carpeta adicional).



Para crear una aplicación dentro de tu proyecto Django, usa el siguiente comando:

```bash
python manage.py startapp nombre_app
```

`python manage.py startapp nombre_app` → Crea una nueva aplicación dentro de tu proyecto Django llamada **nombre_app**.



## Configuración del Superusuario y Sistema de Administración

Django incluye un panel de administración para gestionar el sistema.



### Crear un Superusuario

Ejecuta el siguiente comando y sigue las instrucciones:

```bash
python manage.py createsuperuser

Introduce un nombre de usuario.
Introduce un correo electrónico.
Introduce y confirma una contraseña.
```

### Habilitar la Administración en `settings.py`

Agrega la aplicación `admin` en la lista de aplicaciones instaladas:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion_suministros',
]
```

### Registrar Modelos en el Panel de Administración

Abre `admin.py` dentro de la aplicación y registra los modelos:

```python
from django.contrib import admin
from .models import Producto, Proveedor, Suministro

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Suministro)
```

### Iniciar el Servidor y Acceder al Panel de Administración

```bash
python manage.py runserver
```

Accede al panel en: http://127.0.0.1:8000/admin
