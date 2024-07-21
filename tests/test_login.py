from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_login(browser: webdriver.Chrome):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.set_user_name('standard_user')
    login_page.set_password('secret_sauce')
    login_page.click_login()
    time.sleep(2)
    
    assert browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
