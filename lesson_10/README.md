# lessons_autotest# 🚀 Автотесты для калькулятора и интернет-магазина

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.0-green?logo=selenium)

## 📝 Описание
Проект содержит UI-автотесты с использованием:
- Selenium WebDriver
- Page Object Pattern
- Allure-отчёты

## 🔧 Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourname/project.git
   cd project
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Запуск тестов
```bash
# Все тесты с отчётом
pytest --alluredir=allure-results

# Просмотр отчёта
allure serve allure-results
```

## 📁 Структура
```
project/
├── pages/           # PageObject классы
├── tests/           # Тесты
└── allure-results/  # Результаты тестов
```

## 📧 Контакты
По вопросам пишите: email@example.com