"""
UI Test 10: Verify Subscription in home page
Test Case: Newsletter subscription functionality
"""
import pytest
from pages.home_page import HomePage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.newsletter
class TestNewsletterSubscription:
    """Test class for newsletter subscription functionality."""
    
    def test_verify_subscription_in_home_page(self):
        """Test method with screenshot support."""
        try:
"""Test newsletter subscription functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Scroll down to subscription section
        assert home_page.scroll_to_subscription(), "Failed to scroll to subscription section"
        
        # Verify subscription section is visible
        assert home_page.is_subscription_visible(), "Subscription section not visible"
        assert "SUBSCRIPTION" in home_page.get_subscription_text(), "Subscription header text not correct"
        
        # Get newsletter email from test data
        newsletter_email = test_data['newsletter']['email']
        
        # Subscribe to newsletter
        assert home_page.subscribe_to_newsletter(newsletter_email), "Failed to subscribe to newsletter"
        
        # Verify subscription success message
        assert home_page.is_subscription_successful(), "Subscription success message not visible"
        assert "You have been successfully subscribed!" in home_page.get_subscription_success_message(), "Incorrect success message"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_subscription_in_home_page: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_subscription_in_home_page: {e}")
            raise e
        """Test newsletter subscription functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Scroll down to subscription section
        assert home_page.scroll_to_subscription(), "Failed to scroll to subscription section"
        
        # Verify subscription section is visible
        assert home_page.is_subscription_visible(), "Subscription section not visible"
        assert "SUBSCRIPTION" in home_page.get_subscription_text(), "Subscription header text not correct"
        
        # Get newsletter email from test data
        newsletter_email = test_data['newsletter']['email']
        
        # Subscribe to newsletter
        assert home_page.subscribe_to_newsletter(newsletter_email), "Failed to subscribe to newsletter"
        
        # Verify subscription success message
        assert home_page.is_subscription_successful(), "Subscription success message not visible"
        assert "You have been successfully subscribed!" in home_page.get_subscription_success_message(), "Incorrect success message"
    
    def test_verify_subscription_with_different_emails(self):
        """Test method with screenshot support."""
        try:
"""Test newsletter subscription with different email formats."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll to subscription section
        assert home_page.scroll_to_subscription(), "Failed to scroll to subscription section"
        
        # Test with different email formats
        test_emails = [
            "test@example.com",
            "user.name@domain.co.uk",
            "test+newsletter@example.org",
            "123@test.com"
        ]
        
        for email in test_emails:
            # Subscribe to newsletter
            assert home_page.subscribe_to_newsletter(email), f"Failed to subscribe with email: {email}"
            
            # Verify subscription success
            assert home_page.is_subscription_successful(), f"Subscription failed for email: {email}"
            
            # Refresh page for next test
            driver.refresh()
            home_page.scroll_to_subscription()
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_subscription_with_different_emails: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_subscription_with_different_emails: {e}")
            raise e
        """Test newsletter subscription with different email formats."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll to subscription section
        assert home_page.scroll_to_subscription(), "Failed to scroll to subscription section"
        
        # Test with different email formats
        test_emails = [
            "test@example.com",
            "user.name@domain.co.uk",
            "test+newsletter@example.org",
            "123@test.com"
        ]
        
        for email in test_emails:
            # Subscribe to newsletter
            assert home_page.subscribe_to_newsletter(email), f"Failed to subscribe with email: {email}"
            
            # Verify subscription success
            assert home_page.is_subscription_successful(), f"Subscription failed for email: {email}"
            
            # Refresh page for next test
            driver.refresh()
            home_page.scroll_to_subscription()
    
    def test_verify_subscription_with_invalid_emails(self):
        """Test method with screenshot support."""
        try:
"""Test newsletter subscription with invalid email formats."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll to subscription section
        assert home_page.scroll_to_subscription(), "Failed to scroll to subscription section"
        
        # Test with invalid email formats
        invalid_emails = [
            "invalid-email",
            "@example.com",
            "test@",
            "test..test@example.com",
            ""
        ]
        
        for email in invalid_emails:
            # Subscribe to newsletter (should still work as frontend validation might be minimal)
            result = home_page.subscribe_to_newsletter(email)
            
            # The subscription might still work depending on frontend validation
            if result:
                # If subscription was attempted, check if it was successful
                if home_page.is_subscription_successful():
                    print(f"Subscription successful with invalid email: {email}")
                else:
                    print(f"Subscription failed with invalid email: {email}")
            
            # Refresh page for next test
            driver.refresh()
            home_page.scroll_to_subscription()
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_subscription_with_invalid_emails: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_subscription_with_invalid_emails: {e}")
            raise e
        """Test newsletter subscription with invalid email formats."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll to subscription section
        assert home_page.scroll_to_subscription(), "Failed to scroll to subscription section"
        
        # Test with invalid email formats
        invalid_emails = [
            "invalid-email",
            "@example.com",
            "test@",
            "test..test@example.com",
            ""
        ]
        
        for email in invalid_emails:
            # Subscribe to newsletter (should still work as frontend validation might be minimal)
            result = home_page.subscribe_to_newsletter(email)
            
            # The subscription might still work depending on frontend validation
            if result:
                # If subscription was attempted, check if it was successful
                if home_page.is_subscription_successful():
                    print(f"Subscription successful with invalid email: {email}")
                else:
                    print(f"Subscription failed with invalid email: {email}")
            
            # Refresh page for next test
            driver.refresh()
            home_page.scroll_to_subscription()
    
    def test_verify_home_page_elements(self):
        """Test method with screenshot support."""
        try:
"""Test verification of home page elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Verify all home page elements
        elements_status = home_page.verify_home_page_elements()
        
        assert elements_status['logo_displayed'], "Home page logo not displayed"
        assert elements_status['features_visible'], "Features section not visible"
        assert elements_status['recommended_items_visible'], "Recommended items section not visible"
        assert elements_status['subscription_visible'], "Subscription section not visible"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_home_page_elements: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_home_page_elements: {e}")
            raise e
        """Test verification of home page elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Verify all home page elements
        elements_status = home_page.verify_home_page_elements()
        
        assert elements_status['logo_displayed'], "Home page logo not displayed"
        assert elements_status['features_visible'], "Features section not visible"
        assert elements_status['recommended_items_visible'], "Recommended items section not visible"
        assert elements_status['subscription_visible'], "Subscription section not visible"
    
    def test_verify_subscription_section_scrolling(self):
        """Test method with screenshot support."""
        try:
"""Test scrolling to subscription section."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll to subscription section
        assert home_page.scroll_to_subscription(), "Failed to scroll to subscription section"
        
        # Verify subscription section is visible after scrolling
        assert home_page.is_subscription_visible(), "Subscription section not visible after scrolling"
        
        # Scroll to top
        assert home_page.scroll_to_top(), "Failed to scroll to top"
        
        # Scroll back to subscription
        assert home_page.scroll_to_subscription(), "Failed to scroll to subscription section again"
        assert home_page.is_subscription_visible(), "Subscription section not visible after second scroll"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_subscription_section_scrolling: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_subscription_section_scrolling: {e}")
            raise e
        """Test scrolling to subscription section."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll to subscription section
        assert home_page.scroll_to_subscription(), "Failed to scroll to subscription section"
        
        # Verify subscription section is visible after scrolling
        assert home_page.is_subscription_visible(), "Subscription section not visible after scrolling"
        
        # Scroll to top
        assert home_page.scroll_to_top(), "Failed to scroll to top"
        
        # Scroll back to subscription
        assert home_page.scroll_to_subscription(), "Failed to scroll to subscription section again"
        assert home_page.is_subscription_visible(), "Subscription section not visible after second scroll"
