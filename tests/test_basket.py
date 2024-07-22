import time
from selenium import webdriver
from pages.cart_page import CartPage
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
    cart_page.click_remove()
    time.sleep(3)
    assert cart_page.cart_items_count() == 0
