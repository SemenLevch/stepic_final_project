from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_busket(self):
        assert self.is_element_not_present(*BasketPageLocators.BASKET_ITEMS), "Items present in busket"

    def should_be_empty_busket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty busket message is not present"
