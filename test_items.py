import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_for_an_add_to_cart_button_on_the_product_page(browser):
    browser.get(link)
    time.sleep(30)
    basket_elements = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(basket_elements)>0, "button add to basket not found"