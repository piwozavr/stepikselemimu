from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # 1. Открыть страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # 2. Дождаться, когда цена дома уменьшится до $100
    # Ожидание 12 секунд для появления нужного текста в элементе с id="price"
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    # 3. Нажать на кнопку "Book"
    browser.find_element(By.ID, "book").click()

    # 4. Решить математическую задачу
    # Скроллим вниз, если нужно, и находим значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Ввод ответа в текстовое поле
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Нажать на кнопку "Submit"
    button = browser.find_element(By.ID, "solve")
    button.click()

    # Оставляем браузер открытым на пару секунд, чтобы увидеть число в alert
    time.sleep(5)

finally:
    browser.quit()
