from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators(object):
    LOGIN_FORM_INVALID = (By.CSS_SELECTOR, "#login_form_red_test")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#registration_form")
    
    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASSWORD = (By.ID, "id_registration-password1")
    REG_REPEAT_PAS = (By.ID, "id_registration-password2")
    REG_BTN = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    
    #MESSAGE_AFTER_ADD_ITEM = (By.CSS_SELECTOR, '.alert-success:first-child .alertinner strong')
    TITLE_OF_THE_ITEM = (By.CSS_SELECTOR, "h1")
    PRICE_ITEM = (By.CSS_SELECTOR, ".product_main .price_color")
    #BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert:nth-child(1)')
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET = (By.XPATH, "//a[text()='View basket']")
    
    BASKET_BTN = (By.XPATH , "//span//a[contains(@href, '/basket') and @class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket is empty.')]")
