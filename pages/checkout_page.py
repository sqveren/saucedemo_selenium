from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class CheckoutPage(BasePage):

    INPUT_NAME_FIELD = (By.ID, "first-name")
    INPUT_LAST_NAME_FIELD = (By.ID, "last-name")
    INPUT_ZIP_FIELD = (By.ID, "postal-code")
