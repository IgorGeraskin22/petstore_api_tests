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

7. Альтернатива: открыть HTML-отчёт в `reports/report.html`.

---

## 📂 Структура проекта с комментариями

```text
fakestore-api-tests/
├── .github/                          # Настройки GitHub Actions (CI/CD)
│   └── workflows/
│       └── tests.yml                # Конфигурация CI: запуск pytest при push
├── .pytest_cache/                   # Внутренний кэш pytest (автоматически создаётся)
├── reports/
│   └── report.html                  # HTML-версия отчёта о тестировании
│   └── allure_screenshot_example.png  # Скриншот отчёта (для README)
├── tests/                           # Папка с тестами
│   ├── testdata/                    # Файлы с тестовыми данными (если используются)
│   ├── confest.py                   # Фикстуры и хуки для pytest
│   ├── test_auth.py                 # Тесты авторизации
│   ├── test_cart.py                 # Тесты корзины
│   └── test_products.py            # Тесты для работы с товарами
├── utils/                           # Утилиты и API-клиенты
│   ├── __init__.py                  # Делает папку `utils` модулем
│   ├── api_client.py                # Базовый HTTP-клиент для всех запросов
│   └── auth_api.py                  # Клиент конкретно для методов авторизации
├── start.py                         # (Необязательно) точка запуска/отладки
├── api_client.log                   # Лог-файл с запросами и ответами (если включено)
├── requirements.txt                 # Список зависимостей проекта
├── pytest.ini                       # Конфигурация Pytest (например, кодировка, опции)
├── .gitignore                       # Игнорируемые файлы и папки для Git
├── .coverage                        # Отчёт покрытия кода (после запуска coverage)
└── README.md                        # Документация проекта (этот файл)
```

---

## 📊 Пример Allure-отчёта

Сгенерированный отчёт визуализирует:

- количество пройденных тестов,
- распределение по "фичам" (features) и "сюжетам" (stories),
- статус каждого теста,
- графики и тренды успешности прогонов.

### 📷 Скриншот:
![Allure report overview](https://igorgeraskin22.github.io/fakestore-api-tests/#)



## 🧰 Используемые технологии

- 🐍 Python 3.8+
- 🧪 Pytest — тестовый фреймворк
- 🌐 Requests — HTTP-клиент
- 📋 Allure — генерация красивых отчётов
- ☁️ GitHub Actions — CI/CD pipeline

---

## ➕ Как добавить новый тест

1. Создай файл `test_<название>.py` в папке `tests/`
2. Импортируй клиент из `utils/api_client.py` или `auth_api.py`
3. Напиши тест с Allure-аннотациями:

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

- Автоматический запуск тестов при `push` и `pull request`
- Настроен через `.github/workflows/tests.yml`
- Можно расширить до:
  - Отправки отчётов в Telegram
  - Публикации отчётов через GitHub Pages

---

## 🔗 Полезные ссылки

- 🔹 API документация: [https://fakestoreapi.com](https://fakestoreapi.com)
- 🔹 Репозиторий GitHub: [https://github.com/IgorGeraskin22/fakestore-api-tests](https://github.com/IgorGeraskin22/fakestore-api-tests)

---

## 👤 Автор

**Игорь Гераскин — QA Engineer**  
📧 igor.geraskin@example.com  
💼 [hh.ru/твоя-ссылка](https://hh.ru)

---
