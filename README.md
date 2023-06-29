# Crypto Deribit

### aiohttp-клиент для криптобиржи Deribit


## Технологии:
<details><summary>Подробнее</summary><br>
    
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)
[![asyncio](https://img.shields.io/badge/-asyncio-464646?logo=python)](https://docs.python.org/3/library/asyncio.html)
[![datetime](https://img.shields.io/badge/-datetime-464646?logo=python)](https://docs.python.org/3/library/datetime.html)
[![http](https://img.shields.io/badge/-http-464646?logo=Python)](https://docs.python.org/3/library/http.html)
[![logging](https://img.shields.io/badge/-logging-464646?logo=python)](https://docs.python.org/3/library/logging.html)
[![typing](https://img.shields.io/badge/-typing-464646?logo=Python)](https://docs.python.org/3/library/typing.html)
[![Pytest-asyncio](https://img.shields.io/badge/-Pytest--asyncio-464646?logo=Pytest)](https://pypi.org/project/pytest-asyncio/)
    
[![aiohttp](https://img.shields.io/badge/-aiohttp-464646?logo=aiohttp)](https://docs.aiohttp.org/en/stable/index.html)
[![APScheduler](https://img.shields.io/badge/-APScheduler-464646?logo=APScheduler)](https://apscheduler.readthedocs.io/en/stable/index.html)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?logo=Pydantic)](https://docs.pydantic.dev/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-v2.0-blue?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?logo=alembic)](https://alembic.sqlalchemy.org/en/latest/)
[![asyncpg](https://img.shields.io/badge/-asyncpg-464646?logo=PostgreSQL)](https://pypi.org/project/asyncpg/)    

[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?logo=NGINX)](https://nginx.org/ru/)
[![GitHub_Actions](https://img.shields.io/badge/-GitHub_Actions-464646?logo=GitHub)](https://docs.github.com/en/actions)

<br>

## Описание работы:
Приложение состоит из:
  1. `aiohttp`-клиента для криптобиржи **Deribit**
        - каждую минуту клиент забирает с биржи текущую цену `BTC` и `ETH` и сохраняет в базу данных тикер валюты, текущую цену и время в `UNIX`.
  3. API-сервиса для обработки сохраненных данных на `FastAPI` - реализует следующие GET-методы:
        - Получение всех сохраненных данных по указанной валюте
        - Получение последней цены валюты
        - Получение цены валюты с фильтром по дате

У каждого метода есть обязательный query-параметр __ticker__, обозначающий трехсимвольный код валюты, например `BTC` или `ETH`

<br>

## Установка и запуск:

<details><summary>Предварительные условия</summary>

Предполагается, что пользователь установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине или на удаленном сервере, где проект будет запускаться в контейнерах. Проверить наличие можно выполнив команды:
```bash
docker --version && docker-compose --version
```
<h1></h1>    
</details>

<details><summary>Локальный запуск: Docker Compose</summary>

1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):
```bash
git clone https://github.com/T1mBul/Derbit-aiohttp-fastapi.git && \
cd crypto-FastAPI && \
cp .env .env && \
nano .env
```
2. Из корневой директории проекта выполните команду:
```bash
docker compose -f infra/local/docker-compose.yml up -d --build
```
Проект будет развернут в трех docker-контейнерах `db, web, nginx` по адресу http://localhost. 

Администрирование приложения может быть осуществлено через Swagger доступный по адресу http://localhost/docs.

3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
docker compose -f infra/local/docker-compose.yml down
```
Если также необходимо удалить тома базы данных, статики и медиа:
```bash
docker compose -f infra/local/docker-compose.yml down -v
```

## Удаление:
Из корневой директории проекта выполните команду:
```bash
cd .. && rm -fr crypto-FastAPI
```
