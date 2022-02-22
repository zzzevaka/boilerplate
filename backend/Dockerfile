FROM python:3

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update -y &&\
    apt-get install -y postgresql-13 &&\
    pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry install

RUN mkdir -p /root/.jupyter &&\
    echo '{"NotebookApp":{"base_url": "/shell/","password": "argon2:$argon2id$v=19$m=10240,t=10,p=8$ZWHeG/V+aYVqqj7MYESyeg$c5nOKY9qyHFdktoqAglIiEfBNdatcZqNUVAOJMkCEEg"}}' > /root/.jupyter/jupyter_notebook_config.json

COPY . /app

CMD gunicorn -w 2 application.wsgi -b 0.0.0.0:8000
