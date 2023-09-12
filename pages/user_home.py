from selenium import webdriver
from config.locators import UserHomeLocators
from pages.base_page import BasePage
import time

class UserHome(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = UserHomeLocators
        
    def is_loaded(self):
        self.wait_element(*UserHomeLocators.DISPLAY_NAME)
        self.wait_element(*UserHomeLocators.DISPLAY_EMAIL)
        if self.get_url() == "https://www.hudl.com/home":
            return True
        else:
            return False

    def get_display_name(self):
        self.wait_element(*UserHomeLocators.DISPLAY_NAME)
        return self.find_element(*UserHomeLocators.DISPLAY_NAME).text

    def get_display_email(self):
        self.wait_element(*UserHomeLocators.DISPLAY_EMAIL)
        return self.find_element(*UserHomeLocators.DISPLAY_EMAIL).text
    
    def load_and_back(self):
        if self.is_loaded():
            self.driver.back()
            time.sleep(5)