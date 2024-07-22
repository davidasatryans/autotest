from pages.base_page import BasePage
from selenium.webdriver.common.by import By

by_checkout = (By.ID, 'checkout')
by_remove = (By.ID, 'remove-sauce-labs-bike-light')
by_cart_list = (By.CLASS_NAME, 'cart_list')
by_cart_items = (By.CLASS_NAME, 'cart_item')

class CartPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_checkout(self):
        checkout_button = self.find(*by_checkout)
        checkout_button.click()

    def click_remove(self):
        remove_button = self.find(*by_remove)
        remove_button.click()

    def cart_items_count(self):   
        cart_list = self.find(*by_cart_list)
        cart_items = cart_list.find_elements(*by_cart_items)
        return len(cart_items)