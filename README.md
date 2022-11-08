Simple Api Project built with Djnago & Django REST Framework

What you need:
- Docker & Docker-Compose

How to install:
Git clone <ssh or http>
docker-compose build
docker-compose up db -d
docker-compose run --rm --service-ports web python manage.py makemigrations
dokcer-compose up web -d

You are done!
