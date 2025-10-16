"""
Contact page class for the AutomationExercise testing framework.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import logger


class ContactPage(BasePage):
    """Contact page class containing locators and methods for the contact page."""
    
    # Contact page locators
    CONTACT_HEADER = (By.XPATH, "//h2[@class='title text-center']")
    GET_IN_TOUCH_HEADER = (By.XPATH, "//h2[contains(text(), 'Get In Touch')]")
    CONTACT_NAME = (By.XPATH, "//input[@name='name']")
    CONTACT_EMAIL = (By.XPATH, "//input[@name='email']")
    CONTACT_SUBJECT = (By.XPATH, "//input[@name='subject']")
    CONTACT_MESSAGE = (By.XPATH, "//textarea[@name='message']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@data-qa='submit-button']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='status alert alert-success']")
    HOME_BUTTON = (By.XPATH, "//a[@class='btn btn-success']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = "https://www.automationexercise.com/contact_us"
    
    def navigate_to_contact(self) -> bool:
        """Navigate to the contact page."""
        return self.navigate_to_url(self.page_url)
    
    def is_contact_page_loaded(self) -> bool:
        """Check if contact page is loaded."""
        return self.helper.is_element_displayed(self.CONTACT_HEADER)
    
    def get_contact_header_text(self) -> str:
        """Get the contact page header text."""
        return self.helper.get_element_text(self.CONTACT_HEADER)
    
    def is_get_in_touch_visible(self) -> bool:
        """Check if 'Get In Touch' header is visible."""
        return self.helper.is_element_displayed(self.GET_IN_TOUCH_HEADER)
    
    def fill_contact_form(self, name: str, email: str, subject: str, message: str) -> bool:
        """Fill the contact form with provided data."""
        try:
            # Enter name
            if not self.helper.send_keys_to_element(self.CONTACT_NAME, name):
                return False
            
            # Enter email
            if not self.helper.send_keys_to_element(self.CONTACT_EMAIL, email):
                return False
            
            # Enter subject
            if not self.helper.send_keys_to_element(self.CONTACT_SUBJECT, subject):
                return False
            
            # Enter message
            if not self.helper.send_keys_to_element(self.CONTACT_MESSAGE, message):
                return False
            
            logger.info("Filled contact form")
            return True
        except Exception as e:
            logger.error(f"Failed to fill contact form: {e}")
            return False
    
    def submit_contact_form(self) -> bool:
        """Submit the contact form."""
        return self.helper.click_element(self.SUBMIT_BUTTON)
    
    def is_success_message_visible(self) -> bool:
        """Check if success message is visible."""
        return self.helper.is_element_displayed(self.SUCCESS_MESSAGE)
    
    def get_success_message(self) -> str:
        """Get the success message."""
        return self.helper.get_element_text(self.SUCCESS_MESSAGE)
    
    def click_home_button(self) -> bool:
        """Click home button."""
        return self.helper.click_element(self.HOME_BUTTON)
    
    def complete_contact_form(self, contact_data: dict) -> bool:
        """Complete the entire contact form process."""
        try:
            # Fill contact form
            if not self.fill_contact_form(
                contact_data.get('name', ''),
                contact_data.get('email', ''),
                contact_data.get('subject', ''),
                contact_data.get('message', '')
            ):
                return False
            
            # Submit form
            if not self.submit_contact_form():
                return False
            
            logger.info("Completed contact form submission")
            return True
        except Exception as e:
            logger.error(f"Failed to complete contact form: {e}")
            return False
    
    def verify_contact_page_elements(self) -> dict:
        """Verify all contact page elements and return status."""
        return {
            'contact_header_visible': self.is_contact_page_loaded(),
            'get_in_touch_visible': self.is_get_in_touch_visible()
        }
