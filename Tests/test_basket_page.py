import pytest
import time
from Pages.basket_page import BasketPage
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


@pytest.fixture(scope="function")
def user(browser):
    email = str(time.time()) + "@fakemail.org"
    password = "Fg6L0R2FY"
    new_user = LoginPage(browser)
    new_user.open()
    new_user.go_to_login_page()
    new_user.register_new_user(email, password)
    new_user.should_be_authorized_user()


@pytest.fixture(scope="function")
def guest(browser):
    pass


@pytest.mark.parametrize('start_page_fix', ['product_page', 'main_page'])
@pytest.mark.parametrize('login', ['guest', 'user'])
class TestEmptyBasket:

    def test_no_product(self, browser, start_page_fix, login, request, logger):
        logger.add_start_step(method='test_no_product')
        start_page = request.getfixturevalue(start_page_fix)
        request.getfixturevalue(login)
        start_page.open()
        start_page.should_be_basket_button()
        start_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_product()
        logger.add_end_step(url=browser.current_url, method='test_no_product')

    @pytest.mark.xfail(reason="The product should not be in the basket when a product isn't added")
    def test_has_product(self, browser, start_page_fix, login, request, logger):
        logger.add_start_step(method='test_has_product')
        start_page = request.getfixturevalue(start_page_fix)
        request.getfixturevalue(login)
        start_page.open()
        start_page.should_be_basket_button()
        start_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_product()
        logger.add_end_step(url=browser.current_url, method='test_has_product')

    def test_empty_message(self, browser, start_page_fix, login, request, logger):
        logger.add_start_step(method='test_empty_message')
        start_page = request.getfixturevalue(start_page_fix)
        request.getfixturevalue(login)
        start_page.open()
        start_page.should_be_basket_button()
        start_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_msg()
        logger.add_end_step(url=browser.current_url, method='test_empty_message')

    @pytest.mark.xfail(reason="The empty message should be in the basket when a product isn't added")
    def test_no_empty_message(self, browser, start_page_fix, login, request, logger):
        logger.add_start_step(method='test_no_empty_message')
        start_page = request.getfixturevalue(start_page_fix)
        request.getfixturevalue(login)
        start_page.open()
        start_page.should_be_basket_button()
        start_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_empty_msg()
        logger.add_end_step(url=browser.current_url, method='test_no_empty_message')
