from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from config.env import UserData

class BasePage(object):
    def __init__(self, driver, base_url=UserData.BaseURL):
        self.base_url = base_url
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)
    
    def goback(self):
        self.driver.back()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def locator_is_displayed(self, locator):
        if locator.is_displayed():
            return True
    
    def locator_is_hidden(self, locator):
        if locator.is_loaded():
            if locator.is_displayed() == False:
                return True

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def wait_element_alternate(self, *locator):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator))