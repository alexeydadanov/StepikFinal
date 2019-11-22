from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
import time
import pytest


#def test_guest_can_add_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#    page = ProductPage(browser, link)
#   page.open()
#    product_page = ProductPage(browser, browser.current_url)
#    page.should_be_add_product_to_basket()
#    time.sleep(1)
#    product_page.solve_quiz_and_get_code()
    #product_page.check_add_item_to_basket()

#def test_user_cant_see_success_message(browser):
#    """Тест нет success_message"""
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#    page = ProductPage(browser, link)
#    page.open()
#    product_page = ProductPage(browser, browser.current_url)
#    product_page.should_not_be_success_message()



#Negative test cases:
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()
    page.should_not_be_success_message()
    

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()
    time.sleep(1)
    page.should_disappear_success_message()

#гость может перейти на страницу логина со страницы Х
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(2)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()
    
    
