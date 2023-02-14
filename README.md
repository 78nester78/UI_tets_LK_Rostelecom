Тестирование регистрации и авторизации в Личном Кабинете Ростелеком.
https://b2c.passport.rt.ru
При тестировании применялись техники тест-дизайна: 
пограничные значения, 
эквивалентное разделение, 
предугадывание ошибок, 
исследовательское тестирование,
парамертизация тестов.
Проект выполнен на Python 3.9
Использовались библиотеки Pytest и Selenium
Браузер Google Chrome версия 109.0.5414.120 и chromedriver для этой версии.
Проект содержит файлы и папки:
conftest.py содержит весь необходимый код для отлова неудачных тестовых случаев и создания скриншота страницы в случае, если какой-либо тестовый пример не сработает.
pages/base.py содержит реализацию шаблона PageObject для Python.
pages/auth_locators.py локаторы страницы авторизации для работы с автотестами.
pages/elements.py содержит вспомогательный класс для определения веб-элементов на веб-страницах.
test_rostelecom.py содержит тесты для ЛК Ростелеком
settings.py содержит тестовые данные для тестов

Запуск тестов:
Установите все требования: pip install -r requirements.txt
Загрузите Selenium WebDriver с https://chromedriver.chromium.org/downloads (выберите версию, совместимую с вашим браузером)
Запустите тесты все тесты разом командой из терминала: 
python -m pytest -v --driver Chrome --driver-path C:/Drivers_for_Selenium/chromedriver.exe
где C:/Drivers_for_Selenium/chromedriver.exe путь до chromedriver.exe

Запустить каждый тест по отдельности:
pytest test_rostelecom.py::test_wrong --driver Chrome --driver-path C:/Drivers_for_Selenium/chromedriver.exe
где test_wrong название теста, который хотим запустить.