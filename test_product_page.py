from pages.product_page import ProductPage
import math
from selenium.common.exceptions import NoAlertPresentException




def test_guest_can_add_product_to_basket(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_the_basket()
    page.solve_quiz_and_get_code()
    page.check_basket_price()
    page.check_basket_title()
    

