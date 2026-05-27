from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class CartPage(BasePage):

    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BUTTONS = (By.XPATH, "//button[text()='Remove']")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items_count(self):
        elements = self.driver.find_elements(*self.CART_ITEM)
        return len(elements)

    def remove_all_from_cart(self):
            buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
            for button in buttons:
                button.click()


    def go_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)


    def back_to_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def is_cart_empty(self):
        return len(self.driver.find_elements(*self.CART_ITEM)) == 0

    def get_cart_items_names(self):
        items = self.driver.find_elements(*self.CART_ITEM)
        return [item.text for item in items]

    def open_checkout(self):
        self.click(self.CHECKOUT_BUTTON)