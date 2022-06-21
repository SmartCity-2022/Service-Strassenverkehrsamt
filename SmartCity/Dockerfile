FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN apk add --no-cache build-base && apk add --no-cache mariadb-connector-c-dev && pip install --no-cache-dir -r requirements.txt && apk del build-base

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
