from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest


def test_guest_can_add_product_to_basket(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.allert_checking_product_name_added()
    page.allert_checking_product_price_added()
    page.should_be_add_to_alert_buttons()