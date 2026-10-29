import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_positive_form():
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

        full_name_field.send_keys("Мария Маринина")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("maria.marinina@test.ru")

        # Находим и добавляем поля адресов (пункт 6 задания)
        driver.find_element(By.ID, "currentAddress").send_keys("г. Москва, ул. Московская, 10")
        driver.find_element(By.ID, "permanentAddress").send_keys("г. Санкт-Петербург, ул. Ленинградская, 5")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Мария Маринина" in result_box.text
        assert "maria.marinina@test.ru" in result_box.text
        assert "г. Москва" in result_box.text
        assert "г. Санкт-Петербург" in result_box.text
        print("Тест с новыми данными и адресами успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

test_positive_form()