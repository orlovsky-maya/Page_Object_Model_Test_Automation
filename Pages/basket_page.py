from Pages.base_page import BasePage
from Pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "The message 'Your basket is" \
                                                                                    " empty. Continue shopping' " \
                                                                                    "is not presented, but should be"

    def should_not_be_message_basket_is_empty(self):
        assert self.is_not_element_present(BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "The message 'Your basket is" \
                                                                                        " empty. Continue shopping' " \
                                                                                        "is presented, and should be"

    def should_be_product_in_basket(self):
        assert self.is_element_present(BasketPageLocators.PRODUCT_IS_IN_BASKET), "The product is not in basket, and " \
                                                                                 "should not be"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(BasketPageLocators.PRODUCT_IS_IN_BASKET), "The product is in basket, but " \
                                                                                     "should not be"
