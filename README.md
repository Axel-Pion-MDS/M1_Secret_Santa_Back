# SecretSantaBack
![Python3.10.7](https://img.shields.io/badge/Python-v.3.10.7-%23316A9A)
![Django3.2.16](https://img.shields.io/badge/Django-v.3.2.16-%230C4B33)

## Packages
![Psycopg2>=2.8](https://img.shields.io/badge/Psycogp2-%3E%3D2.8-%23009977)

## Getting started

This repository is used to interact with our front application for managing data and sending email notifications to users.

## Before starting

Check if you have installed the following application :

- Docker

## How use application

### Create .env file

```bash
$ cp .env.sample .env
```

### Update variables inside .env file

```bash
$ touch .env
```

Modify the file with the value you want
```pycon
# Configure database name, user and password.
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password

# Database manager PGADMIN
PGADMIN_DEFAULT_EMAIL=your_email
PGADMIN_DEFAULT_PASSWORD=your_password
```

### Build application

```bash
$ docker-compose build
```

### Start application

```bash
$ docker-compose up -d
```

### Migrate the database

```bash
$ docker-compose run --rm api python manage.py makemigrations
$ docker-compose run --rm api python manage.py migrate
```

Use -d if you want to detach the container

## Postman

[Postman Collection](https://www.getpostman.com/collections/3d765a6f9fc25adb41d5)

## Routes

### Users

| API             | Url          | Route                   | Method |
|-----------------|--------------|-------------------------|--------|
| get every users | 0.0.0.0:8000 | /users/                 | GET    |
| get user        | 0.0.0.0:8000 | /users/<id_user>        | GET    |
| add user        | 0.0.0.0:8000 | /users/add              | POST   |
| update user     | 0.0.0.0:8000 | /users/update           | PATCH  |
| delete user     | 0.0.0.0:8000 | /users/delete/<id_user> | DELETE |

### Roles
| API             | Url          | Route                   | Method |
|-----------------|--------------|-------------------------|--------|
| get every roles | 0.0.0.0:8000 | /roles/                 | GET    |
| get role        | 0.0.0.0:8000 | /roles/<id_role>        | GET    |
| add role        | 0.0.0.0:8000 | /roles/add              | POST   |
| update role     | 0.0.0.0:8000 | /roles/update           | PATCH  |
| delete role     | 0.0.0.0:8000 | /roles/delete/<id_role> | DELETE |

### Promotions
| API                  | Url          | Route                             | Method |
|----------------------|--------------|-----------------------------------|--------|
| get every promotions | 0.0.0.0:8000 | /roles/                           | GET    |
| get promotion        | 0.0.0.0:8000 | /promotions/<id_promotion>        | GET    |
| add promotion        | 0.0.0.0:8000 | /promotions/add                   | POST   |
| update promotion     | 0.0.0.0:8000 | /promotions/update                | PATCH  |
| delete promotion     | 0.0.0.0:8000 | /promotions/delete/<id_promotion> | DELETE |

### Santa
| API                 | Url          | Route                                 | Method |
|---------------------|--------------|---------------------------------------|--------|
| get every santas    | 0.0.0.0:8000 | /santas/                              | GET    |
| get santa           | 0.0.0.0:8000 | /santas/<id_santa>                    | GET    |
| get active santa    | 0.0.0.0:8000 | /santas/active                        | GET    |
| add santa           | 0.0.0.0:8000 | /santas/add                           | POST   |
| update santa        | 0.0.0.0:8000 | /santas/update/<id_santa>             | PATCH  |
| delete santa        | 0.0.0.0:8000 | /santas/delete/<id_santa>             | DELETE |
| get santa members   | 0.0.0.0:8000 | /santas/<id_santa>/members            | GET    |
| get santa member    | 0.0.0.0:8000 | /santas/<id_santa>/member/<id_member> | GET    |
| add santa member    | 0.0.0.0:8000 | /santas/<id_santa>/add                | POST   |
| update santa member | 0.0.0.0:8000 | /santas/<id_santa>/update/<id_member> | PATCH  |
| delete santa member | 0.0.0.0:8000 | /santas/<id_santa>/delete/<id_member> | DELETE |

## Authors

- [Sylvain Dendele](https://gitlab.com/sylvaindnd)
- [Axel Pion](https://gitlab.com/Maengdok)
- [Rémi Rubis](https://gitlab.com/remirubis)