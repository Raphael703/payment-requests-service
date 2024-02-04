FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

COPY . .

# Установка зависимостей для компиляции расширений C, postgresql-dev - для psycopg2
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev libffi-dev python3-dev make

RUN pip install --upgrade pip
RUN pip install poetry &&  \
    poetry config virtualenvs.create false &&  \
    poetry install --no-root

RUN make collectstatic
