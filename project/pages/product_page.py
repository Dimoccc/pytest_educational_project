from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
# from .login_page import LoginPage
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductPage(BasePage):

    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented") 
    
    def should_be_product_page(self):
        self.should_be_add_to_basket_button
        self.should_be_product_url()
        self.should_be_product_price()
        self.should_be_product_name()

    def should_be_product_url(self):
        # реализуйте проверку на корректный url адрес
        product_name = self.get_product_name()
        #print(product_name.lower().replace(" ","-"), self.browser.current_url)
        assert product_name.lower().replace(" ","-") in self.browser.current_url, "Login link is not presented" 

    def should_be_product_price(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "The product has no price"

    def should_be_product_name(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "The product has no name"
    
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "'Add to basket' button is not presented"

    # def shouuld_success_message(self):
    #     name_product = self.is_element_present(*ProductPageLocators.PRODUCT_NAME)

    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        # self.solve_quiz_and_get_code() # закоменитить в случае если нет на странице allert
        #time.sleep(600)

    def allert_checking_product_name_added(self):
       element_name_product =  WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
       name_product = element_name_product.text
       #print(name_product)
       name_product_alert = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
       #print(name_product_alert)
       assert name_product == name_product_alert
    
    def allert_checking_product_price_added(self):
        price_product =  self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        #print(price_product)
        price_product_alert = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        #print(price_product_alert)
        assert price_product == price_product_alert
    
    def should_be_add_to_alert_buttons(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_BTN_VIEW_BASKET), "'SUCCESS_BTN_VIEW_BASKET' button is not presented"
        assert self.is_element_present(*ProductPageLocators.SUCCESS_BTN_CHEKOUT_NOW), "'SUCCESS_BTN_CHEKOUT_NOW' button is not presented"

    def get_product_name(self):
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return self.product_name
    
    def should_not_be_success_messages(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME), \
        "Success message with product name is presented, but should not be"
        assert self.is_not_element_present(*ProductPageLocators.ALERT_PRODUCT_PRICE), \
        "Success message with product price is presented, but should not be"
    
    def should_disappear_success_messages(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_PRODUCT_NAME), \
        "Success message with product name hasn't disappeared, but should be"
        assert self.is_disappeared(*ProductPageLocators.ALERT_PRODUCT_PRICE), \
        "Success message with product price hasn't disappeared, but should be"