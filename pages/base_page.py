from socket import send_fds

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver


class BasePage:

    def __init__(self, driver):
        driver = self.driver
        self.wait = WebDriverWait(driver,10)

    def click(self,locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)

        )
        element.click()


    def type(self,locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.click()

    def get_text(self,locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)

        ).text

    def find(self,locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )