from Pages.base_page import BasePage
from Pages.locators import ProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        add_to_basket_button = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located
                                                                               (ProductPageLocators.
                                                                                ADD_TO_BASKET_BUTTON))
        add_to_basket_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(ProductPageLocators.ADD_TO_BASKET_BUTTON), "The basket button is not found"

    # Positive test about success_messages

    def should_be_success_messages(self):
        self.should_be_product_message()
        self.should_be_product_name_in_message()
        self.should_be_price_message()
        self.should_be_product_price_in_message()

    def should_be_product_message(self):
        assert self.is_element_present(ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "Success message about " \
                                                                                             "added product is not " \
                                                                                             "found"

    def should_be_product_name_in_message(self):
        product_name = WebDriverWait(self.browser, self.timeout).until(
            EC.visibility_of_element_located(ProductPageLocators.
                                             PRODUCT_NAME))

        product_message = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located
                                                                          (ProductPageLocators.
                                                                           MESSAGE_PRODUCT_ADDED_TO_BASKET))
        product_name_value = product_name.text
        product_message_value = product_message.text

        assert f"{product_name_value} has been added to your basket." == product_message_value, "Incorrect success " \
                                                                                                "message about added " \
                                                                                                "product"

    def should_be_price_message(self):
        assert self.is_element_present(ProductPageLocators.MESSAGE_BASKET_PRICE), "The message with the cost of " \
                                                                                  "the basket is not found"

    def should_be_product_price_in_message(self):
        product_price = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located
                                                                        (ProductPageLocators.PRODUCT_PRICE))
        price_message = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located
                                                                        (ProductPageLocators.MESSAGE_BASKET_PRICE))

        product_price_value = product_price.text
        price_message_value = price_message.text

        assert f"Your basket total is now {product_price_value}" == price_message_value, "Incorrect message with " \
                                                                                         "the cost of the basket."

    # Negative tests about product success_messages

    def should_not_be_product_message_after_adding_product_to_basket(self):
        self.should_be_product_message()
        assert self.is_not_element_present(ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "Success message " \
                                                                                                 "about " \
                                                                                                 "added product is " \
                                                                                                 "presented and " \
                                                                                                 "should be"

    def should_not_be_product_message_before_adding_product_to_basket(self):
        assert self.is_not_element_present(ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "Success message " \
                                                                                                 "about " \
                                                                                                 "added product is" \
                                                                                                 "presented, but " \
                                                                                                 "should not be"

    def product_message_is_disappeared_after_adding_product_to_basket(self):
        self.should_be_product_message()
        assert self.is_disappeared(ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "Success message about " \
                                                                                         "added product is presented" \
                                                                                         " and should be"

