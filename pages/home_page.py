from pages.base_page import BasePage
from config.locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)  # Python2 version

    def expand_login_menu(self):
        self.wait_element(*HomePageLocators.LOGIN_SELECT)
        self.driver.find_element(*HomePageLocators.LOGIN_SELECT).click()

    def login_hudl(self):
        self.wait_element(*HomePageLocators.LOGIN_ICON)
        self.driver.find_element(*HomePageLocators.LOGIN_ICON).click()

    def login_hudl_from_homepage(self):
        self.expand_login_menu()
        self.login_hudl()
        return self.driver.current_url
