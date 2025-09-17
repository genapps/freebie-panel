criar um novo roda comando dentro da pasta freebie:

- docker-compose up -d
- docker-compose ps

- docker-compose exec web poetry run python src/manage.py createsuperuser

<http://localhost:8000/admin/>

Usuário: gen
Senha: root

- docker compose build
- docker compose up
