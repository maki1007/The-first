from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.cant_see_success_message_after_adding_product_to_basket()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "kvbjkbnlkero5u9590hkj"
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link)
        page.open()
        page.cant_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        #page.solve_quiz_and_get_code()
        page.should_be_success_message()
        page.should_be_basket_total_message()
        page.should_be_correct_product_name()
        page.should_be_correct_product_price()

@pytest.mark.need_review
@pytest.mark.parametrize('num', [*range(0,7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_be_basket_total_message()
    page.should_be_correct_product_name()
    page.should_be_correct_product_price()
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.disappeared_after_adding_product_to_basket()
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.empty_basket()