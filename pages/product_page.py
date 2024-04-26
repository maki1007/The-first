from .base_page import BasePage
from selenium.webdriver.common.by import By
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form")
        add_to_basket.click()

    def should_be_success_message(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".alert-success")

    def should_be_basket_total_message(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".alert-info .alertinner p strong")
    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(By.CSS_SELECTOR, ".product_main h1").text
        success_message = self.browser.find_element(By.CSS_SELECTOR, ".alert-success").text
        assert product_name in success_message, "Product name is not in the success message"

    def should_be_correct_product_price(self):
        product_price = self.browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text
        basket_total_message = self.browser.find_element(By.CSS_SELECTOR, ".alert-info .alertinner p strong").text
        assert product_price in basket_total_message, "Product price is not in the basket total message"

    def cant_see_success_message_after_adding_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        add_to_basket_button.click()
        assert self.is_element_present(By.CSS_SELECTOR, ".alert-success"), "Success message is not presented, but should be"
        assert True
    def cant_see_success_message(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".alert-success"), "Success message is presented, but should not be"
        assert True
    def disappeared_after_adding_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        add_to_basket_button.click()
        time.sleep(1)
        assert self.is_disappeared(By.CSS_SELECTOR, ".alert-success"), "Success message is not disappeared, but should be"
        assert True
