from pages.base_page import BasePage
from selenium.webdriver.common.by import By

by_user_name = (By.ID, 'user-name')
by_password = (By.ID, 'password')
by_login_button = (By.ID, 'login-button')

class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://www.saucedemo.com/")

    def set_user_name(self, login):
        username_imput = self.find(*by_user_name)
        username_imput.send_keys(login)

    def set_password(self, password):
        password_imput = self.find(*by_password)
        password_imput.send_keys(password)
  
    def click_login(self):
        login_button = self.find(*by_login_button)
        login_button.click()

    