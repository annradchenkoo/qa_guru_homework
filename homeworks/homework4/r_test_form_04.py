import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Первый шаг - выделение каждого теста в отдельную функцию и ее последующий вызов

def test01():
    print("Рефакторинг - итерация 1!")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие.

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("Марина Мариева")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("marina.marieva@test.ru")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Марина Мариева" in result_box.text
        assert "marina.marieva@test.ru" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test02():
    print("Рефакторинг - итерация 1!")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        # Находим поле Email по его ID и вводим текст без @
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("marieva.marinatest.ru")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        #assert "ivanexample.com" in result_box.text
        #print("Тест успешно пройден!")

        # Проверяем, что форма НЕ отправилась - блок пустой. блок кода выше ожидает то поведение, которое сайт дать не
        # может. Исправлено
        assert result_box.text == ""
        print("Тест успешно пройден: форма не отправилась с невалидными данными")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test_sql_injection():
    # Попытка SQL-инъекции
    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # пауза на загрузку страницы

        # Вводим SQL-инъекцию в имя и корректный email
        driver.find_element(By.ID, "userName").send_keys("' OR '1'='1")
        driver.find_element(By.ID, "userEmail").send_keys("marieva.marina@test.ru")

        # Кликаем Submit
        driver.find_element(By.ID, "submit").click()
        time.sleep(5)

        # Проверяем, что приложение не упало и вывело текст как есть
        result_box = driver.find_element(By.ID, "output")
        assert "' OR '1'='1" in result_box.text

        print("Тест SQL-инъекции пройден успешно")

    finally:
        driver.quit()


def test_email_with_invalid_chars():
    # email с пробелом
    driver = webdriver.Chrome()
    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(2)

        driver.find_element(By.ID, "userName").send_keys("Тест")
        driver.find_element(By.ID, "userEmail").send_keys("test test@example.com")  # пробел
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)

        result_box = driver.find_element(By.ID, "output")
        assert result_box.text == ""  # форма не отправилась
        print("Проверка на email с пробелом пройдена.")
    finally:
        driver.quit()


test01()
test02()
test_sql_injection()
test_email_with_invalid_chars()