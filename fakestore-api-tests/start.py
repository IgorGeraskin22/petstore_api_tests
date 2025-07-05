import os
import subprocess
import webbrowser
import sys


def run_pytest():
    print("[1/3] Запуск тестов...")
    result = subprocess.run(
        ["pytest", "-n", "auto", "--alluredir=allure-results"],
        shell=True
    )
    if result.returncode != 0:
        print("❌ Некоторые тесты не прошли.")
    else:
        print("✅ Все тесты прошли успешно.")


def generate_allure_report():
    print("[2/3] Генерация Allure-отчёта...")
    result = subprocess.run(
        ["allure", "generate", "allure-results", "-o", "allure-report", "--clean"],
        shell=True
    )
    if result.returncode != 0:
        print("❌ Не удалось сгенерировать Allure-отчёт.")
        sys.exit(1)


def open_report():
    print("[3/3] Открытие отчёта в браузере...")
    index_path = os.path.abspath("allure-report/index.html")
    if os.path.exists(index_path):
        webbrowser.open(f"file://{index_path}")
    else:
        print("❌ Файл отчёта не найден.")


if __name__ == "__main__":
    run_pytest()
    generate_allure_report()
    open_report()
