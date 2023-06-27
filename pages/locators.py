from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, ".navbar-right a")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')


class BasePageLocators:
    LOGIN_LINK = (By.ID, 'login_link')
    GO_BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    NOT_EMPTY_CONTAINER = (By.CSS_SELECTOR, '.basket-title.hidden-xs')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
