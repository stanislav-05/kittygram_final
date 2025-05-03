#  Kittygram

## О проекте

Kittygram это социальная сеть, позволяющая публиковать фото своих котиков, а также их достижения.

## Технологии
- Python 3.9
- Django 3.2.3
- PostgreSQL
- Docker
- Nginx
- GitHub Actions

## Установка

Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone git@github.com:stanislav-05/kittygram_final.git
```

Cоздайте и активируйте виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Установите зависимости из директории backend:

```
pip install -r requirements.txt
```
Собираем образы:
```
cd frontend
docker build -t username/taski_frontend .
cd ../backend
docker build -t username/taski_backend .
cd ../gateway
docker build -t username/taski_gateway .
```

Загружаем образы на Docker Hub:
```
docker push username/taski_frontend
docker push username/taski_backend
docker push username/taski_gateway
```

Запустите Docker Compose:
```
docker compose -f docker-compose.production.yml up
```

Выполните миграции и соберите статику:
```
docker compose -f docker-compose.production.yml exec backend python manage.py migrate
docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```

## Примеры запросов

- GET-запрос на получение достижений: ```https://kittymeowww.servebeer.com/api/achievements/```
- POST-запрос на добавление котика: ```https://kittymeowww.servebeer.com/api/cats/```
