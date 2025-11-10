# tests/test_login.py
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.config import USERNAME, PASSWORD

def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.login(USERNAME, PASSWORD)

    assert "Dashboard" in dashboard_page.get_welcome_message()

def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    login_page.login("invalid_user", "wrong_pass")

    assert "Invalid credentials" in login_page.get_error_message()
