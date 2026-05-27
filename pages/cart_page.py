from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class CartPage(BasePage):

    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BUTTONS = (By.XPATH, "//button[text()='Remove']")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items_count(self):

    def remove_all_from_cart(self):

    def go_to_checkout(self):

    def back_to_checkout(self):

