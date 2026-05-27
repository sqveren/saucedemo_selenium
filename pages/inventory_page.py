from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class InventoryPage(BasePage):

    ADD_TO_CART_BACKPACK_BUTTON = (By.CSS_SELECTOR, "input[data-test='add-to-cart-sauce-labs-backpack']")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    DROPDOWN_BUTTON_LOCATOR = (By.CLASS_NAME, "product_sort_container")

    def add_to_cart_by_locator(self, locator):
        self.click(locator)

    def add_to_cart_by_name(self, item_name):
        locator = (By.CSS_SELECTOR, f"[data-test='add-to-cart-{item_name}']")
        self.click(locator)

    def open_cart(self):
        self.click(self.CART_BUTTON)


    def get_num_of_items_in_cart(self):
        locator = (By.CLASS_NAME, "shopping_cart_badge")
        elements = self.driver.find_elements(*locator)

        if len(elements) == 0:
            return 0

        return int(elements[0].text)

    def get_items_count(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "inventory_item_name"))

    def  get_list_of_item_names(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [e.text for e in elements]

    def cart_is_not_empty(self):
        return self.get_num_of_items_in_cart() > 0

    def add_item_open_cart(self, item_name):
        self.add_to_cart_by_name(item_name)
        self.open_cart()

    def get_item_prices(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(price.text.replace("$","")) for price in elements]

    def get_dropdown(self):
        element = self.find(self.DROPDOWN_BUTTON_LOCATOR)
        return Select(element)

#Видалення речей з кошика
    def remove_from_cart(self, item_name):
        locator = (By.CSS_SELECTOR, f"[data-test='remove-{item_name}']")
        self.click(locator)

    def remove_all_items_inventory_page(self):
        while self.driver.find_elements(
                By.CSS_SELECTOR,
                "[data-test^='remove']"
        ):
            buttons = self.driver.find_elements(
                By.CSS_SELECTOR,
                "[data-test^='remove']"
            )

            buttons[0].click()

#Сортування

    def sort_by(self, sorting_method):
        dropdown = self.get_dropdown()
        dropdown.select_by_visible_text(sorting_method)


