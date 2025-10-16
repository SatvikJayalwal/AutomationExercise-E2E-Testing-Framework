"""
UI Test 11: Verify Subscription in Cart page
Test Case: Newsletter subscription from cart page
"""
import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.newsletter
class TestSubscriptionInCartPage:
    """Test class for newsletter subscription from cart page."""
    
    def test_verify_subscription_in_cart_page(self):
        """Test method with screenshot support."""
        try:
"""Test newsletter subscription from cart page."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page is loaded
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
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
            logger.error(f"Assertion failed in test_verify_subscription_in_cart_page: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_subscription_in_cart_page: {e}")
            raise e
        """Test newsletter subscription from cart page."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page is loaded
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
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
    
    def test_verify_subscription_with_different_emails_from_cart(self):
        """Test method with screenshot support."""
        try:
"""Test newsletter subscription with different emails from cart page."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
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
            logger.error(f"Assertion failed in test_verify_subscription_with_different_emails_from_cart: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_subscription_with_different_emails_from_cart: {e}")
            raise e
        """Test newsletter subscription with different emails from cart page."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
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
    
    def test_verify_cart_page_elements(self):
        """Test method with screenshot support."""
        try:
"""Test verification of cart page elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page elements
        elements_status = cart_page.verify_cart_page_elements()
        
        assert elements_status['cart_header_visible'], "Cart header not visible"
        assert elements_status['cart_items_visible'] or elements_status['cart_empty'], "Cart status not determined"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_cart_page_elements: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_cart_page_elements: {e}")
            raise e
        """Test verification of cart page elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page elements
        elements_status = cart_page.verify_cart_page_elements()
        
        assert elements_status['cart_header_visible'], "Cart header not visible"
        assert elements_status['cart_items_visible'] or elements_status['cart_empty'], "Cart status not determined"
    
    def test_verify_subscription_scrolling_from_cart(self):
        """Test method with screenshot support."""
        try:
"""Test scrolling to subscription section from cart page."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
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
            logger.error(f"Assertion failed in test_verify_subscription_scrolling_from_cart: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_subscription_scrolling_from_cart: {e}")
            raise e
        """Test scrolling to subscription section from cart page."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Scroll to subscription section
        assert home_page.scroll_to_subscription(), "Failed to scroll to subscription section"
        
        # Verify subscription section is visible after scrolling
        assert home_page.is_subscription_visible(), "Subscription section not visible after scrolling"
        
        # Scroll to top
        assert home_page.scroll_to_top(), "Failed to scroll to top"
        
        # Scroll back to subscription
        assert home_page.scroll_to_subscription(), "Failed to scroll to subscription section again"
        assert home_page.is_subscription_visible(), "Subscription section not visible after second scroll"
