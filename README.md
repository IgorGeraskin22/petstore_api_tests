# 🛒 Fakestore API Tests

Автоматизированные тесты на Python для REST API [Fake Store API](https://fakestoreapi.com).  
Проект создан для портфолио и демонстрирует навыки тестирования API, генерации отчётов, работы с CI/CD и структурирования кода.

---

## ✅ Что покрыто

- 🔐 Аутентификация (успешный и неуспешный логин)
- 🛍️ Работа с товарами (получение всех и конкретного товара)
- 🧺 Работа с корзиной (создание, просмотр, проверка данных)
- 📊 Allure-отчёты с аннотациями (feature, story, severity)
- ⚙️ CI/CD через GitHub Actions

---

## 🚀 Установка и запуск

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/IgorGeraskin22/fakestore-api-tests.git
   cd fakestore-api-tests
   ```

2. Создай виртуальное окружение:
   ```bash
   python -m venv venv
   ```

3. Активируй окружение:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

4. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```

5. Запусти тесты:
   ```bash
   pytest -v
   ```

6. Сгенерируй Allure-отчёт:
   ```bash
   pytest --alluredir=allure-results
   allure serve allure-results
   ```

---

## 📊 Allure отчёт

🧪 [Открыть отчёт Allure на GitHub Pages](https://igorgeraskin22.github.io/fakestore-api-tests/)  

📌 В отчёте:
- Количество и статус тестов (Passed/Failed)
- Разделение по Feature / Story
- Графики, шаги, метки, тайминги

---

## 📁 Структура проекта с комментариями

```text
fakestore-api-tests/
├── .github/                          # Конфигурации CI/CD
│   └── workflows/
│       └── tests.yml                # Workflow GitHub Actions для запуска тестов
├── .pytest_cache/                   # Кэш pytest (автоматически создаётся)
├── reports/
│   ├── report.html                  # Сгенерированный HTML-отчёт Allure (локально)
├── tests/                           # Тесты
│   ├── testdata/                    # Тестовые данные (если будут)
│   ├── confest.py                   # Общие фикстуры и настройки pytest
│   ├── test_auth.py                 # Тесты авторизации
│   ├── test_cart.py                 # Тесты корзины
│   └── test_products.py             # Тесты товаров
├── utils/                           # Вспомогательные модули и клиенты API
│   ├── __init__.py                  # Делает `utils` Python-пакетом
│   ├── api_client.py                # Базовый клиент для HTTP-запросов
│   └── auth_api.py                  # Методы для работы с авторизацией
├── start.py                         # Точка входа (опционально)
├── api_client.log                   # Лог запросов (если включено логгирование)
├── requirements.txt                 # Список зависимостей проекта
├── pytest.ini                       # Конфигурация pytest
├── .gitignore                       # Исключаемые из Git файлы/папки
├── .coverage                        # Файл покрытия кода (если используется)
└── README.md                        # Документация проекта
```

---

## 🧪 Как добавить новый тест

1. Создай файл `test_<название>.py` в папке `tests/`
2. Используй готовые API-клиенты или универсальный `send_request()`
3. Добавь аннотации Allure (`@allure.feature`, `@allure.story`, `@allure.step`)

Пример:

```python
import allure
from utils.api_client import send_request

@allure.feature("Orders")
@allure.story("Unauthorized access")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_order_unauthorized():
    response = send_request("POST", "/orders", json={})
    assert response.status_code == 401
```

---

## 🔁 CI/CD (GitHub Actions)

- Автоматический запуск тестов при push в репозиторий
- Проверка корректности и статуса тестов
- Можно добавить:
  - Telegram-уведомления
  - Публикацию Allure-отчёта в Pages

Файл workflow:
```
.github/workflows/tests.yml
```

---

## 🔗 Полезные ссылки

- 🧩 API документация: [https://fakestoreapi.com](https://fakestoreapi.com)
- 🧑‍💻 GitHub проект: [https://github.com/IgorGeraskin22/fakestore-api-tests](https://github.com/IgorGeraskin22/fakestore-api-tests)
- 📊 Allure Report: [https://igorgeraskin22.github.io/fakestore-api-tests/](https://igorgeraskin22.github.io/fakestore-api-tests/)

---

## 👨‍💻 Автор

**Игорь Гераскин — QA Engineer**  
📧 igor.geraskin@example.com  
💼 [hh.ru/твой-профиль](https://hh.ru)

---
