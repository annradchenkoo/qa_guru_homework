import time
from selenium import webdriver

# 1. Запуск браузера Chrome
driver = webdriver.Chrome()
# 2. Открытие страницы
driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
driver.maximize_window()
time.sleep(5)  # Пауза, чтобы визуально заметить открытие

# Проверяем, что страница открылась и содержит нужный текст
assert "Text Box" in driver.title or "Text Box" in driver.page_source
print("Тест успешно пройден!")
# 3. Закрытие браузера в любом случае
driver.quit()
