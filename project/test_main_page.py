#pytest -s test_main_page.py

from pages.main_page import MainPage
from pages.basket_page import BasketPage


#pytest -v --tb=line --language=en test_main_page.py

# link = "http://selenium1py.pythonanywhere.com/"

# def go_to_login_page(browser):
    # login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    # login_link.click()
    # ...

def test_guest_can_go_to_login_page(browser): 
#    browser.get(link) 
#    go_to_login_page(browser)
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"):
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.go_to_basket()
    basket_page.should_not_be_products_in_basket()
    basket_page.should_not_be_products_in_basket_text()