### Проект QRKot

Проект асинхронного API для создания благотворительных проектов и сбора 
пожертвований на них с поддержкой авторизации и аутентификации.

#### Технологии:
- Python 3.9
- FastAPI 0.78.0
- FastAPI-Users 10.0.4
- SQLAlchemy 1.4.36 (с alembic 1.7.7)

#### Порядок установки
Клонировать репозиторий и перейти в него в командной строке:
```
https://github.com/cnlis/cat_charity_fund.git
cd cat_charity_fund
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
* Если у вас Linux/MacOS
    ```
    source venv/bin/activate
    ```
* Если у вас Windows
    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции
```
alembic upgrade head
```

#### Запуск тестового сервера с использованием Unicorn
```
uvicorn app.main:app --reload
```

**Полная спецификация к API приведена в файле openapi.json или по эндпоинту 
/docs на запущенном сервере**

*Автор: Кирилл Лисицынский (https://github.com/cnlis/)*