# Запуск  pytest -s test_product_page.py

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
import random

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

@pytest.mark.xfail(reason="Success messages should appear after adding product to basket!")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_messages()

def test_guest_cant_see_success_message(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_messages()

@pytest.mark.xfail(reason="Success messages shouldn't disappear after adding product to basket!")
def test_message_disappeared_after_adding_product_to_basket(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_messages()

def test_guest_should_see_login_link_on_product_page(browser, link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"): 
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"):
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.go_to_basket()
    basket_page.should_not_be_products_in_basket()
    basket_page.should_not_be_products_in_basket_text()

@pytest.mark.registered_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"):
        register_page = LoginPage(browser, link)
        register_page.open()
        email = str(random.random()) + "@fakemail.com"  # генерация случайного email-адреса, чтобы избежать повторения в тестах
        password = "test_password"
        register_page.register_new_user(email, password)
        register_page.should_be_authorized_user()

    @pytest.mark.xfail(reason="Success messages should appear after adding product to basket!")
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_messages()
    
    def test_user_can_add_product_to_basket(self, browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.add_to_basket()
        page.allert_checking_product_name_added()
        page.allert_checking_product_price_added()
        page.should_be_add_to_alert_buttons()