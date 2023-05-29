import pytest

from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.basket_page import BasketPage



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

# Links for testing site with promo

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"

# Links for testing site without promo

# link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

"""Adding a product to basket flow"""


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_messages()

# Fail -  the message should be


@pytest.mark.xfail(reason="The success message about added product should be displayed")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_product_message_after_adding_product_to_basket()

# Pass - the message shouldn't be


def test_guest_cant_see_success_message_before_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_product_message_before_adding_product_to_basket()

# Fail -  the message should be


@pytest.mark.xfail(reason="The success message about added product should not be disappeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_message_is_disappeared_after_adding_product_to_basket()


"""Checking Login link"""


def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


"""Checking empty basket"""

# Pass - The product shouldn't be


def test_guest_cant_see_product_in_basket_opened_from_product_page_when_product_is_not_added(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_basket_button()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()

# Fail - The product shouldn't be


@pytest.mark.xfail(reason="The product should not be in the basket when a product isn't added")
def test_guest_can_see_product_in_basket_opened_from_product_page_when_product_is_not_added(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_basket_button()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_product_in_basket()

# Pass - The empty message should be


def test_guest_can_see_empty_message_in_basket_opened_from_product_page_when_product_is_not_added(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_basket_button()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_message_basket_is_empty()


# # Fail - The empty message should be

@pytest.mark.xfail(reason="The empty message should be in the basket when a product isn't added")
def test_guest_cant_see_empty_message_in_basket_opened_from_product_page_when_product_is_not_added(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_basket_button()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_message_basket_is_empty()
