import pytest
import allure
from Pages.main_page import MainPage
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage


@pytest.fixture(scope="function")
def product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    return ProductPage(browser, link)


@pytest.fixture(scope="function")
def main_page(browser):
    return MainPage(browser)


@pytest.mark.parametrize('start_page_fix', ['product_page', 'main_page'])
class TestGuestLoginForm:

    def test_login_link(self, browser, start_page_fix, request, logger):
        logger.add_start_step(method='test_login_link')
        start_page = request.getfixturevalue(start_page_fix)
        start_page.open()
        start_page.should_be_login_link()
        logger.add_end_step(url=browser.current_url, method='test_login_link')

    def test_go_to_login_page(self, browser, start_page_fix, request, logger):
        logger.add_start_step(method='test_go_to_login_page')
        start_page = request.getfixturevalue(start_page_fix)
        start_page.open()
        start_page.should_be_login_link()
        start_page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.should_be_login_page()
        logger.add_end_step(url=browser.current_url, method='test_go_to_login_page')
