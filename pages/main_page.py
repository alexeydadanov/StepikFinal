from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage
from .locators import ProductPageLocators
from .product_page import ProductPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

#class MainPage(BasePage):
    #def go_to_login_page(self):
      #  link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
     #   link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)
        
   # def should_be_login_link(self):
   #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        
    #def go_to_product_page(self):
       # link = self.browser.find_element(*MainPageLocators.ADD_BUTTON)
       # link.click()
            #return LoginPage(browser=self.browser, url=self.browser.current_url)
        
  #  def should_be_product_page(self):
    #    assert self.is_element_present(*MainPageLocators.ADD_BUTTON), "ADD BUTTON link is not presented"
        
