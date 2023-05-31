from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=30, timeout_test_negative=4):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.timeout_test_negative = timeout_test_negative

    def go_to_basket(self):
        basket_button = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located
                                                                        (BasePageLocators.BASKET_BUTTON))
        basket_button.click()

    def go_to_login_page(self):
        login_link = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located
                                                                     (BasePageLocators.LOGIN_LINK))
        login_link.click()

    def is_disappeared(self, selector):
        try:
            WebDriverWait(self.browser, self.timeout_test_negative).until_not(EC.presence_of_element_located(selector))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, selector):
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located(selector))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, selector):
        try:
            WebDriverWait(self.browser, self.timeout_test_negative).until(EC.presence_of_element_located(selector))
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                    " probably unauthorised user"

    def should_be_basket_button(self):
        assert self.is_element_present(BasePageLocators.BASKET_BUTTON), "The basket button is not presented"

    def should_be_login_link(self):
        assert self.is_element_present(BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
