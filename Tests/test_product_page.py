import allure
import pytest
import time
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage


@pytest.fixture(scope="function")
def user(browser):
    email = str(time.time()) + "@fakemail.org"
    password = "z7LtGBQCR"
    new_user = LoginPage(browser)
    new_user.open()
    new_user.go_to_login_page()
    new_user.register_new_user(email, password)
    new_user.should_be_authorized_user()


@pytest.fixture(scope="function")
def guest(browser):
    pass


@pytest.mark.parametrize('login', ['guest', 'user'])
class TestAddToBasket:
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    @allure.description('Test success msg')
    def test_success_msg(self, browser, login, request, logger):
        logger.add_start_step(method='test_success_msg')
        product_page = ProductPage(browser, self.link)
        request.getfixturevalue(login)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_success_msgs()
        logger.add_end_step(url=browser.current_url, method='test_success_msg')

    @pytest.mark.xfail(reason="The success message about added product should be displayed"
                              " when a product is added")
    @allure.description('Test no success msg when added')
    def test_no_success_msg_when_added(self, browser, login, request, logger):
        logger.add_start_step(method='test_no_success_msg_when_added')
        product_page = ProductPage(browser, self.link)
        request.getfixturevalue(login)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_not_be_product_msg_after_added()
        logger.add_end_step(url=browser.current_url, method='test_no_success_msg_when_added')

    @allure.description('Test no success msg before added')
    def test_no_success_msg_before_added(self, browser, login, request, logger):
        logger.add_start_step(method='test_no_success_msg_before_added')
        product_page = ProductPage(browser, self.link)
        request.getfixturevalue(login)
        product_page.open()
        product_page.should_not_be_product_msg_before_added()
        logger.add_end_step(url=browser.current_url, method='test_no_success_msg_before_added')

    @pytest.mark.xfail(reason="The success message about added product should not be disappeared")
    @allure.description('Test success msg disappeared')
    def test_success_msg_disappeared(self, browser, login, request, logger):
        logger.add_start_step(method='test_success_msg_disappeared')
        product_page = ProductPage(browser, self.link)
        request.getfixturevalue(login)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.product_msg_is_disappeared()
        logger.add_end_step(url=browser.current_url, method='test_success_msg_disappeared')
