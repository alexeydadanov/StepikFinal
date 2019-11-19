from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM_INVALID = (By.CSS_SELECTOR, "#login_form_red_test")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#registration_form")
