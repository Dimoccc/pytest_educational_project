from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_GO_TO_BUSKET = (By.XPATH, "//span/a[contains(@class, 'btn')][contains(@href, 'basket')]")
    BUTTON_PROCEED_TO_CHECKOUT = (By.XPATH, "//div/a[contains(@class, 'btn')][contains(@href, 'checkout')]")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    #Перенесено в BasePageLocators
    # LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    # REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    


class ProductPageLocators:
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ALERT_PRODUCT_NAME= (By.XPATH, "//div[@id='messages']/div[1]/div[@class='alertinner ']/strong")
    ALERT_PRODUCT_PRICE = (By.XPATH,"//div[@id='messages']/div[3]/div[@class='alertinner ']//strong")
    SUCCESS_DEFERRED_BENEFIT_OFFER = (By.XPATH, "//div[@id='messages']/div[2]//div[@class='alertinner ']/strong")
    SUCCESS_BTN_VIEW_BASKET = (By.XPATH, "//div[@class='alertinner ']/p/a[contains(@href, '/basket/')]")
    SUCCESS_BTN_CHEKOUT_NOW = (By.XPATH, "//div[@class='alertinner ']/p/a[contains(@href, '/checkout')]")
    
    
