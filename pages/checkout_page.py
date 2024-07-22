from pages.base_page import BasePage
from selenium.webdriver.common.by import By

by_user_name = (By.ID, 'first-name')
by_password = (By.ID, 'last-name')
by_postal_code = (By.ID, 'postal-code')
by_continue_button = (By.ID, 'continue')

class CheckoutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def set_user_name(self, login):
        username_imput = self.find(*by_user_name)
        username_imput.send_keys(login)

    def set_password(self, password):
        password_imput = self.find(*by_password)
        password_imput.send_keys(password)
  
    def set_postal_code(self, code):
        postalcode_imput = self.find(*by_postal_code)
        postalcode_imput.send_keys(code)

    def click_continue(self):
        continue_button = self.find(*by_continue_button)
        continue_button.click()