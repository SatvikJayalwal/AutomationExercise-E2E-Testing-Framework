"""
Login page class for the AutomationExercise testing framework.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import logger


class LoginPage(BasePage):
    """Login page class containing locators and methods for the login page."""
    
    # Login page locators
    LOGIN_FORM = (By.XPATH, "//div[@class='login-form']")
    LOGIN_EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//p[normalize-space()='Your email or password is incorrect!']")
    
    # Signup form locators
    SIGNUP_FORM = (By.XPATH, "//div[@class='signup-form']")
    SIGNUP_NAME = (By.XPATH, "//input[@placeholder='Name']")
    SIGNUP_EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = "https://www.automationexercise.com/login"
    
    def navigate_to_login(self) -> bool:
        """Navigate to the login page."""
        return self.navigate_to_url(self.page_url)
    
    def is_login_form_visible(self) -> bool:
        """Check if login form is visible."""
        return self.helper.is_element_displayed(self.LOGIN_FORM)
    
    def is_signup_form_visible(self) -> bool:
        """Check if signup form is visible."""
        return self.helper.is_element_displayed(self.SIGNUP_FORM)
    
    def login(self, email: str, password: str) -> bool:
        """Login with email and password."""
        try:
            # Enter email
            if not self.helper.send_keys_to_element(self.LOGIN_EMAIL, email):
                return False
            
            # Enter password
            if not self.helper.send_keys_to_element(self.LOGIN_PASSWORD, password):
                return False
            
            # Click login button
            if not self.helper.click_element(self.LOGIN_BUTTON):
                return False
            
            logger.info(f"Attempted login with email: {email}")
            return True
        except Exception as e:
            logger.error(f"Failed to login: {e}")
            return False
    
    def is_login_error_visible(self) -> bool:
        """Check if login error message is visible."""
        return self.helper.is_element_displayed(self.LOGIN_ERROR_MESSAGE)
    
    def get_login_error_message(self) -> str:
        """Get the login error message."""
        return self.helper.get_element_text(self.LOGIN_ERROR_MESSAGE)
    
    def signup(self, name: str, email: str) -> bool:
        """Start signup process with name and email."""
        try:
            # Enter name
            if not self.helper.send_keys_to_element(self.SIGNUP_NAME, name):
                return False
            
            # Enter email
            if not self.helper.send_keys_to_element(self.SIGNUP_EMAIL, email):
                return False
            
            # Click signup button
            if not self.helper.click_element(self.SIGNUP_BUTTON):
                return False
            
            logger.info(f"Started signup process with name: {name}, email: {email}")
            return True
        except Exception as e:
            logger.error(f"Failed to start signup: {e}")
            return False
    
    def verify_login_page_elements(self) -> dict:
        """Verify all login page elements and return status."""
        return {
            'login_form_visible': self.is_login_form_visible(),
            'signup_form_visible': self.is_signup_form_visible()
        }
