from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_LINK
        ), "Add to basket button don't present on the page."
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_button.click()

    def check_is_presented_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), 'Success message is presents on the page but should not be.'
