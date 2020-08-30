from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    ITEM_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner > p >strong")
    BASKET_TITLE = (By.CSS_SELECTOR, ".alertinner > strong:nth-child(1)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

