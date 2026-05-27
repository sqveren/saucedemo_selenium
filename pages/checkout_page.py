from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class CheckoutPage(BasePage):

    INPUT_NAME_FIELD = (By.ID, "first-name")
    INPUT_LAST_NAME_FIELD = (By.ID, "last-name")
    INPUT_ZIP_FIELD = (By.ID, "postal-code")
    FINISH_BUTTON = (By.ID, "finish")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")


    def enter_first_name(self,first_name):
        self.driver.find(*self.INPUT_NAME_FIELD).send_keys(first_name)

    def enter_last_name(self,last_name):
        self.driver.find(*self.INPUT_LAST_NAME_FIELD).send_keys(last_name)

    def enter_zip_code(self,zip_code):
        self.driver.find(*self.INPUT_ZIP_FIELD).send_keys(zip_code)

    def enter_all_information(self,first_name,last_name,zip_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)

    def cancel_checkout(self):
        self.click(self.CANCEL_BUTTON)

    def get_error_message(self):
        return self.find(self.ERROR_MESSAGE).text