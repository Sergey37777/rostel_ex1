## 🛠 Установка и настройка
### 🔹 1. Установка Poetry
```sh
pip install poetry
```

### 🔹 2. Клонирование проекта и установка зависимостей
```sh
git clone https://github.com/Sergey37777/rostel_ex1.git
cd rostel_ex1
poetry install
```

### 🔹 3. Настройка переменных окружения (для SMTP)
Создай `.env` файл в корне проекта и добавь туда свои SMTP-данные:
```
SMTP_SERVER=smtp.yandex.ru
SMTP_PORT=465
SMTP_USER=your_email@example.com
SMTP_PASSWORD=your_password
RECIPIENT_EMAIL=recipient@example.com
```

---

## 🚀 Использование
### 🔹 1. Запуск парсинга и сохранения данных
```sh
poetry run python main.py
```
Этот скрипт:
1. Загружает список ID из файла.
2. Асинхронно делает запросы к сайту.
3. Парсит данные через **XPath**.
4. Сохраняет их в **Excel** по пути: `C:/Users/{username}/Documents/Данные контрагентов/{ГГГГ.ММ.ДД ЧЧ-ММ-СС} Данные контрагентов.xlsx`.
5. Автоматически отправляет Excel-файл на email.

---

## 📂 Структура проекта
```
📦 your_project
├── 📂 data_processing  # Обработка и сохранение данных
│   ├── data_processor.py
│   ├── email_sender.py
├── 📂 parser  # Асинхронный парсер данных
│   ├── async_parser.py
│   ├── selenium_parser.py
├── 📂 configs  # Конфигурационные файлы (селекторы, SMTP)
│   ├── selectors.py
│   ├── settings.py
├── .env  # Переменные окружения
├── main.py  # Основной скрипт
├── README.md  # Документация
└── pyproject.toml  # Конфигурация Poetry
```

---

## 📌 Основные модули
### 🔹 `async_parser.py`
- Асинхронный парсинг через `aiohttp`.
- Использует **XPath** для извлечения данных.
- Обрабатывает ошибки при получении данных.

### 🔹 `selenium_parser.py`
- Используется для обработки **динамического контента**.
- Имитация работы браузера с `Selenium`.

### 🔹 `data_processor.py`
- Преобразует полученные данные в **Pandas DataFrame**.
- Сохраняет результаты в **Excel** в нужном формате.

### 🔹 `email_sender.py`
- Отправляет сохранённый **Excel-файл** по **SMTP**.
- Автоматически находит **последний файл** для отправки.

---

## 📌 Требования
- Python 3.9+
- Poetry
- `aiohttp`, `aiofiles`, `lxml`, `selenium`, `pandas`
- SMTP-сервер для отправки email

---

## 📧 Поддержка
Если у тебя возникли вопросы или предложения, **создай issue** в репозитории! 🚀

