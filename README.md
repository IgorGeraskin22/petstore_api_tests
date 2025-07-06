# 🛒 Fakestore API Tests
# 🔹 Заголовок проекта. Используем emoji, чтобы выделить.

Автоматизированные тесты на Python для REST API [Fake Store API](https://fakestoreapi.com), реализованные с использованием `pytest`, `requests` и `allure-pytest`. Проект создан как часть портфолио и демонстрирует навыки API-тестирования, генерации отчетов, структурирования кода и CI/CD.
# 🔹 Вводный абзац с описанием проекта — кратко кто, что, зачем и как.

---

## 🔍 Что покрыто
# 🔹 Раздел с перечислением покрытого функционала

- ✅ Аутентификация (успешный и неуспешный логин)
- ✅ Получение товаров, проверка структуры и данных
- ✅ Работа с корзиной (создание, просмотр, валидация)
- ✅ Структурированные отчёты с Allure
- ⚙️ Готов к CI/CD (GitHub Actions)
# 🔹 Чеклист функциональности, покрытой тестами

---

## ⚙️ Установка и запуск
# 🔹 Инструкция по установке и запуску проекта

1. Клонируй проект:
   ```bash
   git clone https://github.com/IgorGeraskin22/fakestore-api-tests.git
   cd fakestore-api-tests
   ```
   # 🔹 Клонируем репозиторий и переходим в директорию

2. Создай виртуальное окружение:
   ```bash
   python -m venv venv
   ```
   # 🔹 Создаем виртуальное окружение для изоляции зависимостей

3. Активируй окружение:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   # 🔹 Активируем venv в зависимости от ОС

4. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```
   # 🔹 Устанавливаем библиотеки проекта

5. Запусти тесты:
   ```bash
   pytest -v
   ```
   # 🔹 Простой запуск тестов

6. Генерация Allure отчёта:
   ```bash
   pytest --alluredir=allure-results
   allure serve allure-results
   ```
   # 🔹 Генерация и запуск Allure-отчета

7. Локальный HTML-отчёт:
   Открой `reports/report.html` в браузере.
   # 🔹 Если используешь HTML-файл вместо Allure UI — укажи путь

---

## 📂 Структура проекта
# 🔹 Визуальная структура проекта (аски-графика)

```text
fakestore-api-tests/
├── .github/                 # GitHub Actions workflows
│   └── workflows/
│       └── tests.yml
├── reports/                # Allure/HTML отчёты
│   └── report.html
├── tests/                  # Тесты
│   ├── testdata/           # Тестовые данные (JSON, payloads)
│   ├── confest.py          # Фикстуры pytest
│   ├── test_auth.py        # Тесты авторизации
│   ├── test_cart.py        # Тесты корзины
│   └── test_products.py    # Тесты товаров
├── utils/                  # Вспомогательные классы и API-клиенты
│   ├── __init__.py
│   ├── api_client.py
│   └── auth_api.py
├── start.py                # Возможный стартовый файл
├── requirements.txt        # Список зависимостей
├── pytest.ini              # Настройки pytest
├── README.md               # Этот файл
```
---

## 📊 Allure отчёт
# 🔹 Раздел о результатах тестирования

В отчёте отображаются:

- Общая статистика по тестам
- Разделение по функционалу (авторизация, корзина, товары)
- Сюжеты (Stories) и признаки (Features)
- Графики и тренды успешности
# 🔹 Что отображается в Allure

![Allure report overview](https://raw.githubusercontent.com/IgorGeraskin22/fakestore-api-tests/main/reports/allure_screenshot_example.png)


## 🧰 Используемые технологии
# 🔹 Технологии проекта

- 🐍 Python 3.8+
- ✅ Pytest
- 🌐 Requests
- 📋 Allure (allure-pytest)
- ☁️ GitHub Actions

---

## ➕ Как добавить новый тест
# 🔹 Объясняем, как расширить тесты

1. Создай файл `test_<название>.py` в `tests/`
2. Импортируй API-клиент или универсальную функцию
3. Оформи тест с `@allure.feature` и `@allure.story`

Пример:
```python
import allure
from utils.api_client import send_request

@allure.feature("Orders")
@allure.story("Unauthorized order creation")
def test_create_order_unauthorized():
    response = send_request("POST", "/orders", json={})
    assert response.status_code == 401
```
# 🔹 Конкретный пример теста с Allure-аннотациями

---

## 🔄 CI/CD (GitHub Actions)
# 🔹 CI-интеграция: автозапуск тестов

- Автозапуск тестов при push
- Генерация отчёта
- Возможна интеграция с Telegram или GitHub Pages

Файл конфигурации:
```
.github/workflows/tests.yml
```

---

## 🔗 Ссылки
# 🔹 Внешние полезные ссылки

- 🌐 API Docs: [https://fakestoreapi.com](https://fakestoreapi.com)
- 💻 GitHub: [https://github.com/IgorGeraskin22/fakestore-api-tests](https://github.com/IgorGeraskin22/fakestore-api-tests)

---

## 👤 Автор
**Игорь Гераскин — QA Engineer**  
📧 ign.mln20@gmail.com
💼 https://t.me/IgStrive
