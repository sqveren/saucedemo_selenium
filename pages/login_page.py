from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.settings import BASE_URL


class LoginPage(BasePage):

    USERNAME_INPUT = (By.CSS_SELECTOR, ".input_error.form_input")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-test='password']")
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".submit-button.btn_action")

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)

        self.type(self.PASSWORD_INPUT,password)

        self.click(self.BUTTON_LOGIN)


    def login_as_standard_user(self):
        self.login("standard_user", "secret_sauce")