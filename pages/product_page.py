from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    def click_add_to_cart_button(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        cart_button.click()
    
    def check_book_title(self): 
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        book_title_in_message = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_IN_MESSAGE)
        assert book_title.text == book_title_in_message.text, 'The fields have different names'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
