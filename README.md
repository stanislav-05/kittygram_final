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

### Примеры запросов к API:
- POST-запрос на добавление котика: ```http://kittymeowww.servebeer.com/api/cats/```
- GET-запрос на получение списка достижений котиков: ```http://kittymeowww.servebeer.com/api/achievements/```


### Автор:
Марков Станислав Андреевич, ссылка на GitHub: https://github.com/stanislav-05
