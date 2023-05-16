import pytest
import time
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators
from .pages.login_page import LoginPage


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_basket_btn()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_product_add_to_basket()
    product_page.should_be_messsage_about_basket_price()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = ProductPageLocators.URL
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_be_not_success_message()


def test_guest_cant_see_success_message(browser):
    url = ProductPageLocators.URL
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.should_be_not_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    url = ProductPageLocators.URL
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_basket()
    product_page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, BasketPageLocators.BASKET_PAGE_LINK)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        reg_page_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        register_page = LoginPage(browser, reg_page_link)
        register_page.open()
        email= str(time.time()) + "@fakemail.org"
        password = "Jamal228000"
        register_page.register_new_user(email, password)
        register_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        url = ProductPageLocators.URL
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.should_be_basket_btn()
        product_page.add_to_basket()
        #product_page.solve_quiz_and_get_code()
        product_page.should_be_message_product_add_to_basket()
        product_page.should_be_messsage_about_basket_price()
        time.sleep(5)

    def test_guest_cant_see_success_message(self, browser):
        url = ProductPageLocators.URL
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.should_be_not_success_message()
        time.sleep(5)
