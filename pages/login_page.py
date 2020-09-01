from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium import webdriver
driver = webdriver.Chrome()
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "There is no login in the url"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "There is not login form on the page"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "There is not register form on the page"


    def register_new_user(self, email, password):
        login_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        login_field.send_keys(email)

        pass_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD)
        pass_field.send_keys(password)
        pass_confirm_field = self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD_FIELD)
        pass_confirm_field.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
