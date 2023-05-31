import pytest
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.basket_page import BasketPage
import time


# Test data for checking parametrization

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer7", marks=pytest.mark.fail(reason="the link contains "
#                                                                                                "known bug")),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"


@pytest.mark.login_guest
class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.empty_basket_guest
class TestGuestSeeEmptyBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page_when_product_is_not_added(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_basket_button()
        product_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_product_in_basket()

    @pytest.mark.xfail(reason="The product should not be in the basket when a product isn't added")
    def test_guest_can_see_product_in_basket_opened_from_product_page_when_product_is_not_added(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_basket_button()
        product_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_product_in_basket()

    def test_guest_can_see_empty_message_in_basket_opened_from_product_page_when_product_is_not_added(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_basket_button()
        product_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_message_basket_is_empty()

    @pytest.mark.xfail(reason="The empty message should be in the basket when a product isn't added")
    def test_guest_cant_see_empty_message_in_basket_opened_from_product_page_when_product_is_not_added(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_basket_button()
        product_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_message_basket_is_empty()


@pytest.mark.add_product_guest
class TestGestAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_success_messages()

    @pytest.mark.xfail(reason="The success message about added product should be displayed")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_not_be_product_message_after_adding_product_to_basket()

    def test_guest_cant_see_success_message_before_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_product_message_before_adding_product_to_basket()

    @pytest.mark.xfail(reason="The success message about added product should not be disappeared")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.product_message_is_disappeared_after_adding_product_to_basket()


@pytest.mark.add_product_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "Fg6L0R2FY"
        new_user = LoginPage(browser, link)
        new_user.open()
        new_user.go_to_login_page()
        new_user.register_new_user(email, password)
        new_user.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_success_messages()

    @pytest.mark.xfail(reason="The success message about added product should be displayed")
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_not_be_product_message_after_adding_product_to_basket()

    def test_user_cant_see_success_message_before_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_product_message_before_adding_product_to_basket()

    @pytest.mark.xfail(reason="The success message about added product should not be disappeared")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.product_message_is_disappeared_after_adding_product_to_basket()
