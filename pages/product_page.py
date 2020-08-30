from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def click_on_the_basket(self):
        basket = self.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()

    def check_basket_price(self):
        assert self.find_element(
            *ProductPageLocators.ITEM_PRICE).text == self.find_element(
            *ProductPageLocators.BASKET_PRICE).text, "Price does not correspond!"


    def check_basket_title(self):
        assert self.find_element(
            *ProductPageLocators.ITEM_TITLE).text == self.find_element(
            *ProductPageLocators.BASKET_TITLE).text, "Title does not correspond!"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
    
    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
