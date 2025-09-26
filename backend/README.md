# Как запустить backend?

1. Активируйте poetry окружение и выполните команду

    ```bash
    poetry install
    ```

2. Запустите из-под poetry django

    ```bash
    poetry run python manage.py runserver
    ```

    При необходимости выполните миграции

    ```bash
    poetry run python manage.py migrate
    ```

3. Запуск системы управления очередями

    ```bash
    poetry run celery -A storage worker --loglevel=info
    ```
    
    ```bash
    poetry run celery -A storage beat --loglevel=info
    ```
4. Запустите только redis service в docker-compose
