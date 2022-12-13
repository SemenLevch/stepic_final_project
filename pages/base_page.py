from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(5)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how_find, what_find):
        try:
            self.browser.find_element(how_find, what_find)
        except NoSuchElementException:
            return False
        return True
