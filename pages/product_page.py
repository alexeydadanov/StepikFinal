from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button_add_to_basket.click()
    
    #def should_be_button_add(self):
        # реализуйте проверку, что есть форма логина
       # self.should_be_button_add(*ProductPageLocators.ADD_BUTTON), "Login form is not presented"
       # assert True
    
    def message_items_should_be_add_to_basket(self):
        #"""Проверка: название товара в сообщении совпадает с добавленным товаром"""
        title_of_item = self.browser.find_element(*ProductPageLocators.TITLE_OF_THE_ITEM).text
        message_after_add = self.browser.find_element(*ProductPageLocators.MESSAGE_AFTER_ADD_ITEM).text
        assert title_of_item == message_after_add, 'book title does not match message'
    
    def cost_should_be_eql_price(self):
        #"""Проверка: стоимость корзины равна цене товара"""
        price_item = self.browser.find_element(*ProductPageLocators.PRICE_ITEM).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert price_item == basket_total, 'price of items does not eql basket total'
        
        
