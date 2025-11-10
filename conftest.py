# conftest.py
import pytest
from utilities.driver import create_driver
from utilities.config import APP_URL, BROWSER

@pytest.fixture(params=BROWSER,scope="function")
def setup(request):
    """Run each test on both Chrome and Firefox."""
    browser_name = request.param
    driver = create_driver(browser_name)
    driver.get(APP_URL)
    yield driver
    driver.quit()
