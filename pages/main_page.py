from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage
from .locators import ProductPageLocators
from .product_page import ProductPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)  
