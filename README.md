Для клонирования репозитория
```
git clone https://github.com/Nauryeasy/UserAuthTest.git
```

Установка make
```
apt install make
```

После этого необходимо создать виртуальную среду Python.


Установка poetry
```
pip install poetry
```

Далее необходимо установить зависимости
```
poetry install
```

После этого нужно либо переименовать .env.example в .env, либо создать .env по подобию .env.example.

Для запуска приложения
```
make app
```

После запуска необходимо сделать миграции
```
make migrations
make migrate
```

Для создания супер пользователя (Необходимо для тестирования некоторых методов API)
```
make superuser
```

Для логов приложения
```
make app-logs
```

API для получения списка городов и их количества запросов
```
http://127.0.0.1:8000/api/v1/cities
```
