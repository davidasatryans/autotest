import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.cart_page import CartPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_cart(browser: webdriver.Chrome):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.set_user_name('standard_user')
    login_page.set_password('secret_sauce')
    login_page.click_login()
    time.sleep(3)
    produdcts_page = ProductsPage(browser)
    produdcts_page.click_add_to_cart()
    produdcts_page.click_shopping_cart()
    time.sleep(3)
    cart_page = CartPage(browser)
    cart_page.click_checkout()
    time.sleep(3)
    checkout_page = CheckoutPage(browser)
    checkout_page.set_user_name('Давид')
    checkout_page.set_password('Асатрян')
    checkout_page.set_postal_code(142541)
    checkout_page.click_continue()
    time.sleep(2)
    checkout_overview_page = CheckoutOverviewPage(browser)
    checkout_overview_page.click_finish()
    time.sleep(2)
    assert browser.find_element(By.CLASS_NAME, 'complete-header')
