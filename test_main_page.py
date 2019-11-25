from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, link)
        self.page.open()
        self.page.should_be_login_link()
    

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, link)
        self.page.open()
        self.page.go_to_basket_page()
        self.basket_page = BasketPage(browser, browser.current_url)
        self.basket_page.should_not_be_products()
        self.basket_page.should_be_message()
