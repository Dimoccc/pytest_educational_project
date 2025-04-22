from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   marks=pytest.mark.xfail(reason="Product names on the page and on success message message don't match")),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])


def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.allert_checking_product_name_added()
    page.allert_checking_product_price_added()
    page.should_be_add_to_alert_buttons()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.should_not_be_success_messages()

# def test_guest_cant_see_success_message(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_messages()

# def test_message_disappeared_after_adding_product_to_basket(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.should_disappear_success_messages(ProductPageLocators.SUCCESS_DEFERRED_BENEFIT_OFFER)