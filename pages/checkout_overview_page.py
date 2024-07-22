from pages.base_page import BasePage
from selenium.webdriver.common.by import By

by_finish = (By.ID, 'finish')

class CheckoutOverviewPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_finish(self):
        finish_button = self.find(*by_finish)
        finish_button.click()
