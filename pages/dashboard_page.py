# pages/dashboard_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    _welcome_text = (By.XPATH, "//h6[text()='Dashboard']")

    def get_welcome_message(self):
        return self.get_text(self._welcome_text)

