from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        
    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert ('login' in self.browser.current_url, True), "No 'Login' in url"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        self.should_be_login_form(*LoginPageLocators.LOGIN_FORM_INVALID), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        self.should_be_register_form(*LoginPageLocators.REGISTRATION_FORM), "registration form is not presented"
        assert True
    
    def register_new_user(self, email, password):
        email_area = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        password_area = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        pass_repeat_area = self.browser.find_element(*LoginPageLocators.REG_REPEAT_PAS)
        email_area.send_keys(email)
        password_area.send_keys(password)
        pass_repeat_area.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REG_BTN)
        reg_btn.click()
