from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]/child::button')
    BOOK_TITLE = (By.XPATH, '//div[@id="messages"]/descendant::strong')
    BOOK_TITLE_IN_MESSAGE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/child::h1' )
    SUCCESS_MESSAGE = (By.XPATH, '//strong[text()="Coders at Work"]' )