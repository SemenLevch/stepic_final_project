from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

    login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    login_page = LoginPage(browser, login_link)
    login_page.should_be_login_page()
