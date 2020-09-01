from selenium.webdriver.common.by import By




class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators():
    ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_CONFIRM_PASSWORD_FIELD = " "
    REGISTER_BUTTON = " "


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    ITEM_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner > p >strong")
    BASKET_TITLE = (By.CSS_SELECTOR, ".alertinner > strong:nth-child(1)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

