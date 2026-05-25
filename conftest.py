from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import pytest

@pytest.fixture()
def driver():

    service = Service(
        executable_path=ChromeDriverManager().install()
    )

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    yield driver

    driver.quit()