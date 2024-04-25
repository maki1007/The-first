from .base_page import BasePage
from selenium.webdriver.common.by import By

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