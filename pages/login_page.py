from config.locators import LoginPageLocators
from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)

    def is_loaded(self):
        self.wait_element(*LoginPageLocators.EMAIL)
        self.wait_element(*LoginPageLocators.PASSWORD)
        self.wait_element(*LoginPageLocators.CONTINUE)
        self.wait_element(*LoginPageLocators.FORGOT_PASSWORD)
        self.wait_element(*LoginPageLocators.CREATE_ACCOUNT)
        return True
        
    def resetbox_is_displayed(self):
        if LoginPageLocators.RESET_BOX.is_displayed():
            return True
    
    def signupbox_is_displayed(self):
        if LoginPageLocators.SIGNUP_BOX.is_displayed():
            return True
        
    def loginbox_is_displayed(self):
        if LoginPageLocators.LOGIN_BOX.is_displayed():
            return True
    
    def loginbox_is_hidden(self):
        if LoginPageLocators.LOGIN_BOX.is_loaded():
            if LoginPageLocators.LOGIN_BOX.is_displayed() == False:
                return True

    def invalid_auth(self):
        self.wait_element_alternate(*LoginPageLocators.ERROR_BOX)
        error_message = self.find_element(*LoginPageLocators.UNDEF_TEXT).text
        return error_message

    def enter_email(self, email):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.EMAIL).send_keys(email)

    def enter_password(self, password):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def click_login_button(self):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.CONTINUE).click()

    def login(self, user, password):
        self.enter_email(user)
        self.enter_password(password)
        self.click_login_button()

    def forgot_password(self):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.FORGOT_PASSWORD).click()

    def reset_back_to_login(self):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.RESET_BACK_TO_LOGIN).click()

    def create_account(self):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.CREATE_ACCOUNT).click()

    def signup_back_to_login(self):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.SIGNUP_BACK_TO_LOGIN).click()