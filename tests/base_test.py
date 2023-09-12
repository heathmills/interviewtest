import pytest
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.env import UserData

class BaseTest:

    @pytest.fixture(autouse=True)
    def init_driver(self):
        print(UserData.Headless)
        # Set up Browser options and initialize driver
        if UserData.Browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            if UserData.Headless:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            try:
                self.driver = webdriver.Chrome(options=options)
            except Exception as e:
                print(f'Something went wrong: {e}')
        elif UserData.Browser == 'firefox':
            options = webdriver.FirefoxOptions()
            if UserData.Headless:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            try:
                self.driver = webdriver.Firefox(options=options)
            except Exception as e:
                print(f'Something went wrong: {e}')
        elif UserData.Browser == 'edge':
            options = webdriver.EdgeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            if UserData.Headless:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            try:
                self.driver = webdriver.Edge(options=options)
            except Exception as e:
                print(f'Something went wrong: {e}')
        elif UserData.Browser == 'safari':
            if platform.system() != 'darwin':
                raise Exception("Browser is only supported in Mac")
            options = webdriver.safari.options.Options()
            if UserData.Headless:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            try:
                self.driver = webdriver.Safari(options=options)
            except Exception as e:
                print(f'Something went wrong: {e}')
        else:
            raise Exception("Unsupported or Invalid Browser")

        self.driver.implicitly_wait(5)
        # Return driver
        yield
        # Teardown
        self.driver.close()
        self.driver.quit()

