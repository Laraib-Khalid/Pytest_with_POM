# utilities/driver.py
from selenium import webdriver


def create_driver(browser_name="chrome"):
    if browser_name.lower() == "chrome":
        options = webdriver.ChromeOptions()
        # ✅ Force Chrome UI and pages to use English
        options.add_argument("--lang=en")
        driver = webdriver.Chrome(options=options)
    elif browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        # ✅ Force Firefox UI and pages to use English
        options.set_preference("intl.accept_languages", "en-US, en")
        driver = webdriver.Firefox()
    elif browser_name.lower() == "edge":
        options = webdriver.EdgeOptions()
        # ✅ Force Edge UI and pages to use English
        options.add_argument("--lang=en")
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver
