# 🛒 Fakestore API Tests

Автоматизированные тесты на Python для REST API [Fake Store API](https://fakestoreapi.com), реализованные с использованием `pytest`, `requests` и `allure-pytest`. Проект создан как часть портфолио и демонстрирует навыки API-тестирования, генерации отчетов, структурирования кода и CI/CD.

---

## 🔍 Что покрыто

- ✅ Аутентификация (успешный и неуспешный логин)
- ✅ Получение списка и конкретных товаров
- ✅ Работа с корзиной: добавление, просмотр, валидация
- ✅ Структурированные отчёты с Allure
- ⚙️ Поддержка CI/CD через GitHub Actions

---

## ⚙️ Установка и запуск

1. Клонируй проект:
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

7. Открой HTML-отчёт:
   - Локально: `reports/report.html`
   - Онлайн: 👉 [Открыть Allure отчёт на GitHub Pages](https://igorgeraskin22.github.io/fakestore-api-tests/)

---

## 📂 Структура проекта с комментариями

```text
fakestore-api-tests/
├── .github/                          # Настройки GitHub Actions (CI/CD)
│   └── workflows/
│       └── tests.yml                # Конфигурация CI: запуск pytest при push
├── .pytest_cache/                   # Внутренний кэш pytest (авто)
├── reports/
│   ├── report.html                  # HTML-версия отчёта о тестировании
│   └── allure_screenshot_example.png  # Скриншот отчёта (для README)
├── tests/
│   ├── testdata/                    # Тестовые данные
│   ├── confest.py                   # Общие фикстуры pytest
│   ├── test_auth.py                 # Тесты авторизации
│   ├── test_cart.py                 # Тесты корзины
│   └── test_products.py             # Тесты товаров
├── utils/
│   ├── __init__.py                  # Делает папку `utils` пакетом
│   ├── api_client.py                # Универсальный HTTP-клиент
│   └── auth_api.py                  # Методы авторизации
├── start.py                         # Точка входа (по желанию)
├── api_client.log                   # Логи запросов (если логгирование включено)
├── requirements.txt                 # Зависимости проекта
├── pytest.ini                       # Конфигурация Pytest
├── .gitignore                       # Исключения для Git
├── .coverage                        # Отчёт покрытия (если используется)
└── README.md                        # Документация проекта (этот файл)
```

---

## 📊 Пример Allure-отчёта

Отчёт визуализирует:

- Количество и статус тестов
- Разделение по фичам и историям
- Полные шаги, данные запросов/ответов
- Графики прогонов и успешности

### 📷 Превью:

[![Allure report overview](https://raw.githubusercontent.com/IgorGeraskin22/fakestore-api-tests/main/reports/allure_screenshot_example.png)](https://igorgeraskin22.github.io/fakestore-api-tests/)

> 👆 Нажми на изображение, чтобы открыть **полный отчёт Allure**

---

## 🧰 Используемые технологии

- 🐍 Python 3.8+
- 🧪 Pytest
- 🌐 Requests
- 📋 Allure (через allure-pytest)
- ☁️ GitHub Actions (CI)

---

## ➕ Как добавить новый тест

1. Создай файл `test_<название>.py` в `tests/`
2. Импортируй клиент из `utils/`
3. Оформи тест с аннотациями Allure:

```python
import allure
from utils.api_client import send_request

@allure.feature("Orders")
@allure.story("Unauthorized access")
def test_create_order_unauthorized():
    response = send_request("POST", "/orders", json={})
    assert response.status_code == 401
```

---

## 🔄 CI/CD (GitHub Actions)

- Автоматический запуск тестов при push
- Проверка валидности кода
- Можно подключить:
  - Telegram-уведомления
  - публикацию отчёта в Pages

Конфигурация:
```
.github/workflows/tests.yml
```

---

## 🔗 Полезные ссылки

- 🔹 API Docs: [https://fakestoreapi.com](https://fakestoreapi.com)
- 🔹 GitHub Repo: [github.com/IgorGeraskin22/fakestore-api-tests](https://github.com/IgorGeraskin22/fakestore-api-tests)
- 🔹 Allure Report (GitHub Pages): [https://igorgeraskin22.github.io/fakestore-api-tests/](https://igorgeraskin22.github.io/fakestore-api-tests/)

---

## 👤 Автор

**Игорь Гераскин — QA Engineer**  
📧 igor.geraskin@example.com  
💼 [hh.ru/твой-профиль](https://hh.ru)

---
