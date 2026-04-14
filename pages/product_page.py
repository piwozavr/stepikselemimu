from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_correct_product_added(self, expected_name):
        success_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text

        assert expected_name == success_name, "Название товара не совпадает"


    def should_be_correct_price(self, expected_price):
        basket_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE_MESSAGE
        ).text

        assert expected_price == basket_price, "Цена корзины не совпадает"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text