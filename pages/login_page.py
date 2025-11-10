# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # Locators
    _username = (By.NAME, "username")
    _password = (By.NAME, "password")
    _login_btn = (By.XPATH, "//button[@type='submit']")
    _error_msg = (By.XPATH, "//p[text()='Invalid credentials']")

    # PageFactory-style properties
    # @property
    # def username_field(self):
    #     return self.find_element_text(self._username)
    #
    #
    # @property
    # def password_field(self):
    #     return self.find_element_text(self._password)
    #
    # @property
    # def login_button(self):
    #     # return self.driver.find_element(*self._login_btn)
    #     return self.find_element_text(self._login_btn)

    # Actions
    def login(self, username, password):
        self.type_text(self._username, username)
        self.type_text(self._password, password)
        self.click(self._login_btn)

    def get_error_message(self):
        return self.get_text(self._error_msg)
