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

## Activate virtualenv

```bash
source venv/Scripts/activate
```

## Install requirements

```bash
pip install -r requirements.txt
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

All endpoints are protected, so you need to add a token in the header of each request.
Example:

```bash
Authorization: token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
