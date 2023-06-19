import time

import allure
from Pages.base_page import BasePage
from Pages.locators import ProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def add_product_to_basket(self):
        with allure.step('Add product to basket'):
            self.should_be_add_to_basket_button()
            add_to_basket_button = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located
                                                                                   (ProductPageLocators.
                                                                                    ADD_TO_BASKET_BUTTON))
            add_to_basket_button.click()

    def should_be_add_to_basket_button(self):
        with allure.step('Should be add to basket button'):
            assert self.is_element_present(ProductPageLocators.ADD_TO_BASKET_BUTTON), "The basket button is not found"

    # Positive test about success_messages

    def should_be_success_msgs(self):
        with allure.step('Should be success messages'):
            self.should_be_product_msg()
            self.should_be_product_name_in_msg()
            self.should_be_price_msg()
            self.should_be_product_price_in_msg()

    def should_be_product_msg(self):
        with allure.step('Should be product message'):
            assert self.is_element_present(ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "Success message " \
                                                                                                 "about added product" \
                                                                                                 " is not found"

    def should_be_product_name_in_msg(self):
        with allure.step('Should be product name in message'):
            product_name = WebDriverWait(self.browser, self.timeout).until(
                EC.visibility_of_element_located(ProductPageLocators.
                                                 PRODUCT_NAME))

            product_message = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located
                                                                              (ProductPageLocators.
                                                                               MESSAGE_PRODUCT_ADDED_TO_BASKET))
            product_name_value = product_name.text
            product_message_value = product_message.text

            assert f"{product_name_value} has been added to your basket." == product_message_value, "Incorrect success " \
                                                                                                    "message about " \
                                                                                                    "added product"

    def should_be_price_msg(self):
        with allure.step('Should be price message'):
            assert self.is_element_present(ProductPageLocators.MESSAGE_BASKET_PRICE), "The message with the cost of " \
                                                                                      "the basket is not found"

    def should_be_product_price_in_msg(self):
        with allure.step('Should be product price in message'):
            product_price = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located
                                                                            (ProductPageLocators.PRODUCT_PRICE))
            price_message = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located
                                                                            (ProductPageLocators.MESSAGE_BASKET_PRICE))

            product_price_value = product_price.text
            price_message_value = price_message.text

            assert f"Your basket total is now {product_price_value}" == price_message_value, "Incorrect message with " \
                                                                                             "the cost of the basket."

    # Negative tests about product success_messages

    def should_not_be_product_msg_after_added(self):
        with allure.step('Should not be product message after added product to basket'):
            self.should_be_product_msg()
            assert self.is_not_element_present(ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "Success message " \
                                                                                                     "about added " \
                                                                                                     "product is " \
                                                                                                     "presented" \
                                                                                                     " and should be"

    def should_not_be_product_msg_before_added(self):
        with allure.step('Should not be product message before added product to basket'):
            assert self.is_not_element_present(ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "Success message" \
                                                                                                     " about " \
                                                                                                     "added" \
                                                                                                     " product " \
                                                                                                     "is presented, " \
                                                                                                     "but should not be"

    def product_msg_is_disappeared(self):
        with allure.step('Product message is disappeared'):
            self.should_be_product_msg()
            assert self.is_disappeared(ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "Success message about " \
                                                                                             "added product is " \
                                                                                             "presented and should be"