## Установка и настройка
### 1. Установка Poetry
```sh
pip install poetry
```

### 2. Клонирование проекта и установка зависимостей
```sh
git clone https://github.com/Sergey37777/rostel_ex1.git
cd rostel_ex1
poetry install
```

### 3. Настройка переменных окружения (для SMTP)
Создай `.env` файл в корне проекта и добавь туда свои SMTP-данные:
```
SMTP_SERVER=smtp.yandex.ru
SMTP_PORT=465
SMTP_USER=your_email@example.com
SMTP_PASSWORD=your_password
RECIPIENT_EMAIL=recipient@example.com
```

---

## Использование
### Запуск парсинга и сохранения данных
```sh
poetry run python main.py
```