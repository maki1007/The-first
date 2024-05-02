from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), \
        "Basket is not empty, but it should be"
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
        "Empty basket message is not presented, but it should be"