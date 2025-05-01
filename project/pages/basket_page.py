
from .locators import BasePageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BUTTON_PROCEED_TO_CHECKOUT), \
        "There are products in basket ('Proceed to checkout' button is presented), but should not be"

    def should_not_be_products_in_basket_text(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_TEXT), \
        "There are products in basket ('Proceed to checkout' button is presented), but should not be"
    