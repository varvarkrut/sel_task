from pages.base_page import BasePage
from pages.locators import MainPageLocators, BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), "Basket is not empty!"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY), \
            "Message of empty isn't presented"
        