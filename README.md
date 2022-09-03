<h1 align="left">Инструкция по запуску проекта</h1>

1. Скачать образ:
```
docker pull alexcodesxg/api_yamdb:v1.09.2022
```

2. Собрать контейнеры:
```
docker-compose up -d --build
```

3. Провести миграции:
```
docker-compose exec web python manage.py migrate
```

4. Собрать статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```

5. Запуск проекта по ссылке:

    http://localhost/