from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    page.should_be_add_product_to_basket()
    time.sleep(1)
    product_page.solve_quiz_and_get_code()
    #product_page.check_add_item_to_basket()


