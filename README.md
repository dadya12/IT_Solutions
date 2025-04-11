1. Клонирование репозитория
git clone https://github.com/dadya12/IT_Solutions.git
cd your-project

2. Создание и активация виртуального окружения
python -m venv venv
venv\Scripts\activate

3. Установка зависимостей
pip install -r requirements.txt

4. Настройка базы данных
python manage.py migrate

5. Создание суперпользователя (по желанию)
python manage.py createsuperuser

6. Запуск сервера
python manage.py runserver
http://127.0.0.1:8000/