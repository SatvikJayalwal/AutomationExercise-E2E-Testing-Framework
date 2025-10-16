"""
Base page class for the AutomationExercise testing framework.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import WebDriverHelper, ScreenshotHelper
from datetime import datetime
from utils.logger import logger
from config.config import EXPLICIT_WAIT


class BasePage:
    """Base page class containing common functionality for all pages."""
    
    def __init__(self, driver):
        self.driver = driver
        self.helper = WebDriverHelper(driver)
        self.screenshot_helper = ScreenshotHelper(driver)
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
    
    # Common locators
    LOGO = (By.XPATH, "//img[@alt='Website for automation practice']")
    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//a[@href='/login']")
    LOGGED_IN_AS = (By.XPATH, "//li[contains(.,'Logged in as')]")
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/delete_account']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")
    CART_BUTTON = (By.XPATH, "//a[@href='/view_cart']")
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")
    CONTACT_US_BUTTON = (By.XPATH, "//a[@href='/contact_us']")
    
    def navigate_to_url(self, url: str) -> bool:
        """Navigate to the specified URL."""
        try:
            self.driver.get(url)
            logger.info(f"Navigated to: {url}")
            return True
        except Exception as e:
            logger.error(f"Failed to navigate to {url}: {e}")
            return False
    
    def get_page_title(self) -> str:
        """Get the current page title."""
        return self.driver.title
    
    def get_current_url(self) -> str:
        """Get the current URL."""
        return self.driver.current_url
    
    def is_logo_displayed(self) -> bool:
        """Check if the home page logo is displayed."""
        return self.helper.is_element_displayed(self.LOGO)
    
    def click_signup_login(self) -> bool:
        """Click on Signup/Login button."""
        return self.helper.click_element(self.SIGNUP_LOGIN_BUTTON)
    
    def is_logged_in(self) -> bool:
        """Check if user is logged in."""
        return self.helper.is_element_displayed(self.LOGGED_IN_AS)
    
    def get_logged_in_username(self) -> str:
        """Get the logged in username."""
        if self.is_logged_in():
            return self.helper.get_element_text(self.LOGGED_IN_AS)
        return ""
    
    def click_delete_account(self) -> bool:
        """Click on Delete Account button."""
        return self.helper.click_element(self.DELETE_ACCOUNT_BUTTON)
    
    def click_logout(self) -> bool:
        """Click on Logout button."""
        return self.helper.click_element(self.LOGOUT_BUTTON)
    
    def click_cart(self) -> bool:
        """Click on Cart button."""
        return self.helper.click_element(self.CART_BUTTON)
    
    def click_products(self) -> bool:
        """Click on Products button."""
        return self.helper.click_element(self.PRODUCTS_BUTTON)
    
    def click_contact_us(self) -> bool:
        """Click on Contact Us button."""
        return self.helper.click_element(self.CONTACT_US_BUTTON)
    
    def scroll_to_bottom(self) -> bool:
        """Scroll to the bottom of the page."""
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            logger.info("Scrolled to bottom of page")
            return True
        except Exception as e:
            logger.error(f"Failed to scroll to bottom: {e}")
            return False
    
    def scroll_to_top(self) -> bool:
        """Scroll to the top of the page."""
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            logger.info("Scrolled to top of page")
            return True
        except Exception as e:
            logger.error(f"Failed to scroll to top: {e}")
            return False
    
    def take_screenshot(self, filename: str = None) -> str:
        """Take a screenshot."""
        return self.screenshot_helper.take_screenshot(filename)
    
    def take_screenshot_on_failure(self, test_name: str = None) -> str:
        """Take a screenshot when a test fails."""
        if not test_name:
            test_name = "test_failure"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        filename = f"{test_name}_failure_{timestamp}.png"
        return self.take_screenshot(filename)
    
    def take_screenshot_on_error(self, error_message: str = None) -> str:
        """Take a screenshot when an error occurs."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        error_suffix = error_message[:20].replace(" ", "_") if error_message else "error"
        filename = f"error_{error_suffix}_{timestamp}.png"
        return self.take_screenshot(filename)
    
    def wait_for_page_load(self, timeout: int = None) -> bool:
        """Wait for page to load completely."""
        try:
            wait_time = timeout or EXPLICIT_WAIT
            WebDriverWait(self.driver, wait_time).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            return True
        except Exception as e:
            logger.error(f"Page did not load within timeout: {e}")
            return False
