from selenium.webdriver.common.by import By
from config.custom import find_element_by_data_qa_id

class HomePageLocators:
    SITE_LOGO = find_element_by_data_qa_id('site-logo')
    LOGIN_SELECT = find_element_by_data_qa_id('login-select')
    LOGIN_ICON = find_element_by_data_qa_id('login-hudl')
    LOGIN = find_element_by_data_qa_id('login')

class LoginPageLocators:
    LOGIN_BOX = (By.ID, 'login-box')
    ERROR_BOX = (By.CLASS_NAME, 'error-container')
    RESET_BOX = (By.ID, 'reset-box')
    SIGNUP_BOX = (By.ID, 'signup-box')
    UNDEF_TEXT = find_element_by_data_qa_id('undefined-text')
    EMAIL_REQUIRED = (By.ID, 'uniName-947Help')
    HELP_MESSAGE = find_element_by_data_qa_id('undefined-help-text')
    USER_HELP = find_element_by_data_qa_id('useraccount-help-text')
    REQUIRED = find_element_by_data_qa_id('undefined-help-text')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    CONTINUE = (By.ID, 'logIn')
    FORGOT_PASSWORD = (By.ID, 'forgot-password')
    RESET_BACK_TO_LOGIN = (By.CLASS_NAME, 'btn-back-login')
    CREATE_ACCOUNT = (By.ID, 'btn-show-signup')
    SIGNUP_BACK_TO_LOGIN = (By.ID, 'btn-show-login')


class UserHomeLocators:
    DISPLAY_NAME = (By.CLASS_NAME, 'hui-globaluseritem__display-name')
    DISPLAY_EMAIL = (By.CLASS_NAME, 'hui-globaluseritem__email')