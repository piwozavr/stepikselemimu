import time
from selenium.webdriver.common.by import By


def test_user_can_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(link)

    time.sleep(30)

    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert button is not None, "Add to basket button is not present"