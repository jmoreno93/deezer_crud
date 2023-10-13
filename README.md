## About

Este proyecto pretende ser un clon de la api de Deezer, con el fin de rendir la evaluación para Silabuz usando Django Rest Framework.

## Remember

- Todas las rutas son protegidas, por lo que se debe usar un token de autenticación para cada petición.
- Debes crear un superusuario para poder acceder al panel de administración de Django y ver la documentation de la API.

## Installation

## Create virtualenv

```bash
virtualenv venv
```

## Activate virtualenv Windows

```bash
source venv/Scripts/activate
```

## Activate virtualenv Linux

```bash
source venv/bin/activate
```

## Install requirements

```bash
pip install django
pip install djangorestframework
pip install Pillow
```

## Database

```bash
python manage.py makemigrations
python manage.py migrate
```

## Create superuser

```bash
python manage.py createsuperuser
```

- username: admin
- password: admin
- email: admin@admin.com

## Usage

```bash
python manage.py runserver
```

## Endpoints

- http://localhost:8000/admin/
- http://localhost:8000/ -> Documentation
- http://localhost:8000/artist/ -> List of artists GET | POST | PUT | DELETE
- http://localhost:8000/album/ -> List of albums GET | POST | PUT | DELETE
- http://localhost:8000/track/ -> List of tracks GET | POST | PUT | DELETE

## Authentication Endpoints

- http://localhost:8000/auth/login/ -> Login (POST)
- http://localhost:8000/auth/logout/ -> Logout (POST)
- http://localhost:8000/auth/register/ -> Register (POST)

## In Postman

Todos los endpoint estan protegidos, en postman se estan manejando variables de entorno, por lo tanto sería bueno que al momento de importar el postman se asigne un entorno de variables vacia para que al logear el token se vaya actualice en los endpoint
