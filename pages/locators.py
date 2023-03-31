from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_REPEAT_PASSWORD = (By.ID, "id_registration-password2")


class ProductPageLocators:
    URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div[id='messages'] strong")
    PRICE_OF_BASKET_MESSAGE = (By.CSS_SELECTOR, "div[id='messages'] div[class='alertinner '] p")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class~='product_main'] h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class~='product_main'] p[class='price_color']")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div[class='alertinner '] strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '[href = "/en-gb/basket/"]')
    BASKET_PAGE_LINK = "selenium1py.pythonanywhere.com/basket/"
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p/a")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
