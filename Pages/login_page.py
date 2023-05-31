from selenium.webdriver.support.wait import WebDriverWait
from Pages.base_page import BasePage
from Pages.locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


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
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM), "Login form is absent"

    def should_be_register_form(self):
        assert self.is_element_present(LoginPageLocators.REGISTER_FORM), "Register form is absent"

    def register_new_user(self, email, password):
        email_address_field = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located
                                                                            (LoginPageLocators.EMAIL_ADDRESS_REGISTER))

        password_field = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located
                                                                         (LoginPageLocators.PASSWORD_REGISTER))

        confirm_password_field = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located
                                                                        (LoginPageLocators.CONFIRM_PASSWORD_REGISTER))
        register_button = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located
                                                                          (LoginPageLocators.REGISTER_BUTTON))

        email_address_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)
        register_button.click()
