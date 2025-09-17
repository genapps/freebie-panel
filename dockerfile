FROM python:3.13-slim

WORKDIR /code

# Dependências do sistema
RUN apt-get update && apt-get install -y libpq-dev build-essential gcc

# Copia arquivos do Poetry para cache
COPY pyproject.toml poetry.lock* ./

# Instala o Poetry e dependências
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root

# Copia a aplicação
COPY . .

# Expõe a porta
EXPOSE 8000

# Comando para desenvolvimento
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
