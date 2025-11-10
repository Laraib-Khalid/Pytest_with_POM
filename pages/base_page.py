from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Parent class for all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # def find_element_text(self, locator):
    #     return self.driver.find_element(*locator)

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.is_visible(locator).click()

    def type_text(self, locator, text):
        self.is_visible(locator).send_keys(text)

    def get_text(self, locator):
        return self.is_visible(locator).text
