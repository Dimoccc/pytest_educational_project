from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from .login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # перенесено в base_page.py т.к. проверки валидны к каждой странице 

    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    #     login_link.click()
    
    # def should_be_login_link(self):
    #     assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # alert = self.browser.switch_to.alert # обработка alert
        # alert.accept()
    
    # def test_guest_can_go_to_login_page(browser):
    #     link = "http://selenium1py.pythonanywhere.com"
    #     page = MainPage(browser, link)
    #     page.open()
    #     login_page = page.go_to_login_page()
    #     login_page = LoginPage(browser, browser.current_url)
    #     login_page.should_be_login_page()    
    