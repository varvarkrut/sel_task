from pages.product_page import ProductPage
import math
from selenium.common.exceptions import NoAlertPresentException
import pytest


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_the_basket()
    page.solve_quiz_and_get_code()
    page.check_basket_price()
    page.check_basket_title()
    
