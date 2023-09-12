import pytest
from config.env import UserData
from pages.home_page import HomePage
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.user_home import UserHome

class TestLogin(BaseTest):

    @pytest.mark.regression()
    def test_hudl_to_login(self):
        # Verify user can get to login page from homepage
        test_page = HomePage(self.driver)
        test_page.open('')
        test_page.login_hudl_from_homepage()
        test_page = LoginPage(self.driver)
        assert test_page.is_loaded()

    @pytest.mark.regression()
    def test_login_valid_user(self):
        # Verify user can login with valid credentials
        test_page = LoginPage(self.driver)
        test_page.open('login')
        test_page.login(UserData.ValidEmail, UserData.ValidPassword)
        test_page = UserHome(self.driver)
        assert test_page.is_loaded()

    @pytest.mark.regression()
    def test_back_button_maintains_login(self):
        # Verify clicking back button after login doesn't log user out
        test_page = LoginPage(self.driver)
        test_page.open('login')
        test_page.login(UserData.ValidEmail, UserData.ValidPassword)
        test_page = UserHome(self.driver)
        test_page.load_and_back()
        assert test_page.is_loaded()

    @pytest.mark.regression()
    def test_login_invalid_user(self):
        # Verify login fails with invalid credentials & error message
        test_page = LoginPage(self.driver)
        test_page.open('login')
        test_page.login(UserData.InvalidEmail, UserData.ValidPassword)
        assert test_page.invalid_auth() == "We don't recognize that email and/or password"

    @pytest.mark.regression()
    def test_login_empty_user(self):
        # Verify login fails when username blank
        test_page = LoginPage(self.driver)
        test_page.open('login')
        test_page.login("", UserData.InvalidPassword)
        assert test_page.invalid_auth() == "Please fill in all of the required fields"

    @pytest.mark.regression()
    def test_login_empty_password(self):
        # Verify login fails when email is not registered
        test_page = LoginPage(self.driver)
        test_page.open('login')
        test_page.login(UserData.InvalidEmail, UserData.ValidPassword)
        assert test_page.invalid_auth() == "We don't recognize that email and/or password"

    @pytest.mark.regression()
    def test_nav_to_forgot_password(self):
        # Verify clicking Forgot Password hides LoginBox and displays ResetBox
        test_page = LoginPage(self.driver)
        test_page.open('login')
        test_page.forgot_password()
        # Login box is hidden
        assert LoginPage.loginbox_is_hidden
        # Reset box is visible
        assert LoginPage.resetbox_is_displayed

    @pytest.mark.regression()
    def test_reset_back_to_login(self):
        # Verify user can get back to login from Reset Password screen
        test_page = LoginPage(self.driver)
        test_page.open('login')
        test_page.forgot_password()
        test_page.reset_back_to_login()
        # Login box is displayed
        assert LoginPage.loginbox_is_displayed

    @pytest.mark.regression()
    def test_nav_to_create_account(self):
        # Verify clicking Forgot Password hides LoginBox and displays SignupBox
        test_page = LoginPage(self.driver)
        test_page.open('login')
        test_page.create_account()
        # Login box is hidden
        assert LoginPage.loginbox_is_hidden
        # Reset box is visible
        assert LoginPage.signupbox_is_displayed

    @pytest.mark.regression()
    def test_signup_back_to_login(self):
        # Verify user can return to login from Sign Up screen
        test_page = LoginPage(self.driver)
        test_page.open('login')
        test_page.create_account()
        test_page.signup_back_to_login()
        # Login box is displayed
        assert LoginPage.loginbox_is_displayed