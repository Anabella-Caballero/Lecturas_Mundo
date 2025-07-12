
# 📚 Lecturas Mundo

Aplicación web desarrollada con Django y PostgreSQL que permite registrar, listar, puntuar y analizar libros. Pensado tanto para usuarios lectores como para desarrolladores que quieran explorar un backend API RESTful y estadísticas automatizadas con visualización.



## 🛠️ Tecnologías utilizadas

- Python 3.11
- Django 4.2
- PostgreSQL 13+
- Pandas: 2.2+
- Matplotlib/Searborn: para visualización
- Scikit-learn: 1.4+
- Djangorestframework: 3.15


## ⚙️ Instalación del proyecto

### 1. Crear y activar entorno virtual


python -m venv env
env\Scripts\activate       # En Windows

### 2. # Instalar Django y crear proyecto Django


pip install django psycopg2 pandas scikit-learn matplotlib seaborndjango-admin startproject lecturas_mundo
cd lecturas_mundo
python manage.py startapp libros_app


### 3. Instalar dependencias


pip install -r requirements.txt


### 4. Configurar la base de datos (PostgreSQL)

Crear una base de datos en PostgreSQL y actualizar en settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'buscador_lecturas',
        'USER': 'postgres',
        'PASSWORD': '1602',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```


### 5. Migraciones


python manage.py makemigrations
python manage.py migrate


### 6. Correr el servidor

python manage.py runserver


### 🧠 7. ¿Cómo funciona el programa?


El sistema permite:

- Registrar libros con campos como título, autor, género y valoración.
- Visualizar los libros registrados.
- Analizar y graficar valoraciones por género.
- Obtener recomendaciones por género con mayor puntuación.



###  8. API REST 
El proyecto cuenta con una API RESTful desarrollada con Django REST Framework, que permite gestionar libros, usuarios y valoraciones. A continuación se describen los principales endpoints y cómo usarlos.


#### 📘 Libros

- `GET /api/libros/`  
  Retorna el listado completo de libros registrados.

- `POST /api/libros/`  
  Permite registrar un nuevo libro. Requiere autenticación.

  Ejemplo de body JSON:
  ```json
  {
    "titulo": "Hábitos atómicos",
    "fecha_lanzamiento": "2019-06-11",
    "genero": 11,
    "autor": 34,
    "book_url": "https://drive.google.com/uc?export=download&id=1ofelGVWrkwjresU-LMSIZmsv1n-fOU5O"
  }
  ```

- `GET /api/libros/{id}/`  
  Muestra los detalles de un libro específico.

#### 👤 Usuarios

- `POST /api/usuarios/registro/`  
  Registra un nuevo usuario.  

  JSON:
  ```json
  {
    "username": "usuario1",
    "email": "correo@example.com",
    "password": "contraseña123"
  }
  ```

- `POST /api/usuarios/login/`  
  Retorna el token JWT para autenticación.  

  JSON:
  ```json
  {
    "username": "usuario1",
    "password": "contraseña123"
  }
  ```

#### ⭐ Puntuaciones

- `POST /api/puntuar/`  
  Permite calificar un libro ya existente. Requiere autenticación.  
  
  JSON:
  ```json
  {
    "libro": 5,
    "puntuacion": 4
  }
  ```

- `GET /api/puntuaciones/`  
  Listado de todas las puntuaciones registradas (admin o autenticado).



### 9. 📊 Estadísticas y visualizaciones

Generación automática de gráficos accesibles desde el navegador:

- `/estadisticas/libros-por-genero/` → Barras de cantidad por género
![Gráfico](http://127.0.0.1:8000/estadisticas/libros-por-genero/)

- `/estadisticas/promedio-puntuaciones-libro/` → Promedios de puntuaciones
![Gráfico](http://127.0.0.1:8000/estadisticas/promedio-puntuaciones-libro/)




### 10. 🧪 Pruebas con Postman

Podés utilizar Postman o cualquier herramienta REST para:

- Crear usuarios
- Registrar libros
- Enviar puntuaciones
- Ver visualizaciones



### 11. 📄 Licencias

Este proyecto utiliza herramientas y librerías con licencias open source:

- Django: BSD License
- Python: PSF License
- PostgreSQL: PostgreSQL License
- Pandas y Scikit-learn: BSD 
- Matplotlib: PSF-based
- Seaborn: BSD


