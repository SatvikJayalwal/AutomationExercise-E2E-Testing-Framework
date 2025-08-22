from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

class DriverFactory:
    # Singleton driver instance
    driver = None

    @staticmethod
    def get_driver(browser_name):
        # Initialize driver only if not already initialized
        if DriverFactory.driver is None:
            if browser_name.lower() == "chrome":
                # Chrome options: maximize window
                options = ChromeOptions()
                options.add_argument("--start-maximized")
                DriverFactory.driver = webdriver.Chrome(options=options)
            elif browser_name.lower() == "edge":
                # Edge options: maximize window
                options = EdgeOptions()
                options.add_argument("--start-maximized")
                DriverFactory.driver = webdriver.Edge(options=options)
            else:
                # Raise error if unsupported browser
                raise Exception(f"Browser '{browser_name}' not supported")
        return DriverFactory.driver

    @staticmethod
    def quit_driver():
        # Quit driver and reset instance
        if DriverFactory.driver:
            DriverFactory.driver.quit()
            DriverFactory.driver = None
