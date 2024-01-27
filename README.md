### Tests and linter status:

[![Actions Status](https://github.com/Raphael703/payment-requests-service/actions/workflows/linter.yml/badge.svg)](https://github.com/Raphael703/payment-requests-service/actions)
[![PyCI](https://github.com/Raphael703/payment-requests-service/actions/workflows/tests.yml/badge.svg)](https://github.com/Raphael703/python-project-83/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/d62f021ca57840d20258/maintainability)](https://codeclimate.com/github/Raphael703/payment-requests-service/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d62f021ca57840d20258/test_coverage)](https://codeclimate.com/github/Raphael703/payment-requests-service/test_coverage)

_____

# Менеджер заявок на оплату 🗂️

### Описание:

Менеджер заявок на оплату представляет сервис для управления и контроля потоком заявок на оплату в организации. Основной
задачей приложения является обеспечение прозрачности и эффективности процесса управления заявками на оплату, а также
контроль над финансовыми операциями.

**Основные функции:**

1. **Управление заявками**
2. **Контроль рассчетных счетов**
3. **Мониторинг пользователей**
4. **API для доступа к информации**

**Предназначено для:**
Организаций, предприятий и компаний, которые стремятся эффективно управлять процессом заявок на оплату, контролировать
финансовые потоки и обеспечивать прозрачность бухгалтерских операций.

## Содержание

- [Используемые пакеты](#используемые-пакеты)
- [Тестовый сервер](#тестовый-сервер)
- [Для разработчиков](#для-разработчиков)
- [API](#api)
- [Автор](#автор)

## Минимальные требования

- [Python 3.10+](https://www.python.org/downloads/release/python-3100/)
- [Poetry](https://python-poetry.org/)
- [Postgres](https://www.postgresql.org/)

## Используемые пакеты

- [Django](https://www.djangoproject.com/)
    - [django-bootstrap5](https://pypi.org/project/django-bootstrap5/)
    - [django-filter](https://django-filter.readthedocs.io/en/stable/)
    - [dj-database-url](https://pypi.org/project/django-phonenumbers/)
    - [django-phonenumbers](https://pypi.org/project/django-phonenumbers/)
    - [django-model-utils](https://pypi.org/project/django-model-utils/)

- [psycopg2-binary](https://www.psycopg.org/docs/install.html)
- [Django Rest Framework](https://www.django-rest-framework.org/)
    - [drf-yasg](https://pypi.org/project/django-model-utils/)
- [gunicorn](https://gunicorn.org/)
- [whitenoise](https://pypi.org/project/whitenoise/)

**Зависимости для разработки**:

- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [factory-boy](https://pypi.org/project/factory-boy/)
- [flake8](https://pypi.org/project/flake8/)
- [coverage](https://pypi.org/project/coverage/)

## Тестовый сервер

Перейдите по ссылке: [payment-requests-service.com](https://payment-requests-service.onrender.com)

Учётные данные администратора:

**login:** admin

**password:** qwer1234 _(для всех тестовых учётных записей)_

_P.S. У данного тестового сервера выделено не много ресурсов + переход в "режим сна (при бездействии)". Поэтому при первом запросе нужно подождать 2-3 минуты. То же самое с производительностью (мало ресурсов)_ 

______

## Для разработчиков

#### Склонируйте данный репозиторий:

```sh
git clone https://github.com/Raphael703/payment-requests-service.git
```

#### Перейдите в папку проекта

```sh
cd payment-requests-service
```

#### Установите зависимости

```sh
make install
```

#### Создайте .env файл и заполните его (пример)

```dotenv
SECRET_KEY=notsosecret
DEBUG=True
DATABASE_URL=postgresql://pguser:pgpass@localhost:5434/pgdb
```

#### Поднимите базу данных (В Docker(е) например):

```sh
docker run -d \
    --name dev-payment-requests-service \
    -e POSTGRES_USER=pguser \
    -e POSTGRES_PASSWORD=pgpass \
    -e POSTGRES_DB=pgdb \
    -p 5434:5432 \
    postgres:latest
```

#### Запустите сервер локально:

```shell
make dev
```

Перейдите по ссылке [localhost:7777](http://127.0.0.1:7777)



### Остальные полезные команды можете найти в `Makefile`(е)

## API

Документация доступна на следующих относительных путях от корня домена:

- **swagger/**
- **swagger<.json/.xml>/**
- **redoc/**

## Автор

- [Rafael Mukhametshin](https://github.com/Raphael703)
- Можете обращаться за интерисующими моментами `:)` 


