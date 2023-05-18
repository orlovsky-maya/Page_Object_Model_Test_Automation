from Pages.base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        current_url = self.browser.current_url
        assert login_url == current_url, "Incorrect url for login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is absent"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is absent"
