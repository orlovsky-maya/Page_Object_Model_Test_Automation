from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.ID, "add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    MESSAGE_PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages>.alert.alert-safe.alert-noicon.alert-success:"
                                                        "nth-child(1)>div")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "#messages>.alert.alert-safe.alert-noicon.alert-info>div>p:nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
