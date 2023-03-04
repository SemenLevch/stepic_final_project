from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add to basket btn not present"

    def should_be_message_product_add_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_message, "Product message is not present"
        assert product_name == product_name_in_message, "Product name in product message wrong"

    def should_be_messsage_about_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price_message = self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET_MESSAGE).text
        assert basket_price_message, "Basket price message is not present"
        assert product_price in basket_price_message, "Product price in basket price message wrong"

    def should_be_not_success_message(self):
        assert self.is_element_not_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), \
            "Success message present, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), \
            "Success message present, but should be disappear"
