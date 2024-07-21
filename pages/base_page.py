from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def find(self, *args):
        return self.browser.find_element(*args)
    
    def keys(self, *args):
        return self.browser.send_keys(*args)
    
