# 🚀 Petstore API Automated Tests

Автоматизированные тесты для Swagger Petstore API  
https://petstore.swagger.io  
**Python + Pytest + Requests**

---

## 📦 Структура проекта

```
petstore_api_tests/
├── tests/
│   ├── test_pet.py         # Тесты для pet (питомцы)
│   ├── test_store.py       # Тесты для store (магазин, заказы)
│   └── test_user.py        # Тесты для user (пользователи)
├── utils/
│   └── config.py           # Конфигурация: базовый URL
├── requirements.txt        # Зависимости проекта
├── README.md               # Документация проекта
└── .gitignore              # Исключения для Git
```

---

## 🛠️ Используемые технологии

- **Python 3.8+**
- **Pytest** — фреймворк для модульного тестирования
- **Requests** — библиотека для HTTP-запросов
- **Фикстуры Pytest** — для изоляции данных и чистки после тестов

---

## 📝 Что реализовано

- ✅ CRUD-тесты для `pet`, `store`, `user`
- ✅ Поиск питомцев по статусу
- ✅ Авторизация пользователей (login/logout)
- ✅ Создание нескольких пользователей списком (array/list)
- ✅ Изоляция данных через фикстуры


## 🚀 Как запустить проект

1. **Клонируй репозиторий:**
   ```bash
   git clone https://github.com/IgorGeraskin22/petstore_api_tests.git
   cd ИМЯ_РЕПО
   ```

2. **Создай виртуальное окружение (опционально):**
   ```bash
   python -m venv venv
   venv\Scripts\activate         # Windows
   source venv/bin/activate      # macOS/Linux
   ```

3. **Установи зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Запусти все тесты:**
   ```bash
   pytest
   ```

   Или только один файл:

   ```bash
   pytest tests/test_pet.py
   ```

---

## 🧪 Заметки

- **Фикстуры** создают данные перед каждым тестом и очищают после (`yield` + `delete`)
- Тесты не зависят друг от друга: каждый сценарий полностью изолирован

---

