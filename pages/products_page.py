from pages.base_page import BasePage
from selenium.webdriver.common.by import By

by_add_to_cart = (By.ID, 'add-to-cart-sauce-labs-bike-light')
by_shopping_cart = (By.CLASS_NAME, 'shopping_cart_link')

class ProductsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_add_to_cart(self):
        add_button = self.find(*by_add_to_cart)
        add_button.click()

    def click_shopping_cart(self):
        shopping_button = self.find(*by_shopping_cart)
        shopping_button.click()