from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # BasePage contains common reusable Selenium actions
    def __init__(self, driver):
        self.driver = driver

    # Find element with explicit wait
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    # Click on element
    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    # Send keys to input field
    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    # Select option from dropdown by visible text
    def select_by_visible_text(self, locator, text):
        from selenium.webdriver.support.ui import Select
        Select(self.find_element(locator)).select_by_visible_text(text)
