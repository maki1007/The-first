from pages.product_page import ProductPage
import pytest
@pytest.mark.parametrize('num', [*range(0,7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])

def test_guest_can_add_product_to_basket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_product_to_basket()          # выполняем метод страницы — переходим на страницу логина
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_be_basket_total_message()
    page.should_be_correct_product_name()
    page.should_be_correct_product_price()