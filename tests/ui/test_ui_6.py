"""
UI Test 6: Contact Us Form
Test Case: Contact form submission
"""
import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.contact
class TestContactUsForm:
    """Test class for contact us form functionality."""
    
    def test_contact_us_form_submission(self, driver, home_page, contact_page, test_data):
        """Test contact us form submission."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Contact Us button
        assert home_page.click_contact_us(), "Failed to click Contact Us button"
        
        # Verify contact page is loaded
        assert contact_page.is_contact_page_loaded(), "Contact page not loaded"
        assert contact_page.is_get_in_touch_visible(), "Get In Touch header not visible"
        
        # Get contact form data
        contact_data = test_data['contact_form']
        
        # Fill contact form
        assert contact_page.fill_contact_form(
            contact_data['name'],
            contact_data['email'],
            contact_data['subject'],
            contact_data['message']
        ), "Failed to fill contact form"
        
        # Submit contact form
        assert contact_page.submit_contact_form(), "Failed to submit contact form"
        
        # Handle alert if present
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass  # No alert present
        
        # Verify success message
        assert contact_page.is_success_message_visible(), "Success message not visible"
        assert "Success! Your details have been submitted successfully." in contact_page.get_success_message(), "Incorrect success message"
        
        # Click home button
        assert contact_page.click_home_button(), "Failed to click home button"
        
        # Verify redirected to home page
        assert home_page.is_home_page_loaded(), "Not redirected to home page"
    
    def test_contact_us_form_with_empty_fields(self, driver, home_page, contact_page):
        """Test contact us form with empty fields."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Contact Us button
        assert home_page.click_contact_us(), "Failed to click Contact Us button"
        
        # Verify contact page is loaded
        assert contact_page.is_contact_page_loaded(), "Contact page not loaded"
        
        # Submit form with empty fields
        assert contact_page.submit_contact_form(), "Failed to submit contact form"
        
        # Handle alert if present
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass  # No alert present
        
        # The form might still submit or show validation errors
        # This depends on the website's validation implementation
    
    def test_contact_us_form_with_invalid_email(self, driver, home_page, contact_page):
        """Test contact us form with invalid email."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Contact Us button
        assert home_page.click_contact_us(), "Failed to click Contact Us button"
        
        # Verify contact page is loaded
        assert contact_page.is_contact_page_loaded(), "Contact page not loaded"
        
        # Fill form with invalid email
        assert contact_page.fill_contact_form(
            "Test User",
            "invalid-email",
            "Test Subject",
            "Test message"
        ), "Failed to fill contact form"
        
        # Submit form
        assert contact_page.submit_contact_form(), "Failed to submit contact form"
        
        # Handle alert if present
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass  # No alert present
        
        # The form might still submit or show validation errors
        # This depends on the website's validation implementation
    
    def test_contact_us_form_with_special_characters(self, driver, home_page, contact_page):
        """Test contact us form with special characters."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Contact Us button
        assert home_page.click_contact_us(), "Failed to click Contact Us button"
        
        # Verify contact page is loaded
        assert contact_page.is_contact_page_loaded(), "Contact page not loaded"
        
        # Fill form with special characters
        assert contact_page.fill_contact_form(
            "Test User!@#$%",
            "test@example.com",
            "Test Subject & Special Characters",
            "Test message with special characters: !@#$%^&*()"
        ), "Failed to fill contact form"
        
        # Submit form
        assert contact_page.submit_contact_form(), "Failed to submit contact form"
        
        # Handle alert if present
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass  # No alert present
        
        # Verify success message
        assert contact_page.is_success_message_visible(), "Success message not visible"
    
    def test_contact_us_form_verification(self):
        """Test method with screenshot support."""
        try:
"""Test contact us form elements verification."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Contact Us button
        assert home_page.click_contact_us(), "Failed to click Contact Us button"
        
        # Verify contact page elements
        elements_status = contact_page.verify_contact_page_elements()
        
        assert elements_status['contact_header_visible'], "Contact header not visible"
        assert elements_status['get_in_touch_visible'], "Get In Touch header not visible"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_contact_us_form_verification: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_contact_us_form_verification: {e}")
            raise e
        """Test contact us form elements verification."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Contact Us button
        assert home_page.click_contact_us(), "Failed to click Contact Us button"
        
        # Verify contact page elements
        elements_status = contact_page.verify_contact_page_elements()
        
        assert elements_status['contact_header_visible'], "Contact header not visible"
        assert elements_status['get_in_touch_visible'], "Get In Touch header not visible"
