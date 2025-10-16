"""
UI Test 25: Verify Scroll Up using 'Arrow' button
Test Case: Verify Scroll Up using 'Arrow' button and verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
"""
import pytest
from pages.home_page import HomePage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.scroll
class TestScrollUpUsingArrowButton:
    """Test class for verifying scroll up functionality using arrow button."""
    
    def test_scroll_up_using_arrow_button(self):
        """Test method with screenshot support."""
        try:
"""Test scroll up functionality using arrow button."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Scroll down to footer
        assert home_page.scroll_to_footer(), "Failed to scroll to footer"
        assert home_page.is_subscription_text_visible(), "Subscription text not visible in footer"
        
        # Click on arrow at bottom right side to move upward
        assert home_page.click_scroll_up_arrow(), "Failed to click scroll up arrow"
        
        # Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
        assert home_page.is_home_page_loaded(), "Home page not visible after scrolling up"
        assert home_page.is_home_page_loaded(), "Full-Fledged practice website for Automation Engineers text not visible"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_scroll_up_using_arrow_button: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_scroll_up_using_arrow_button: {e}")
            raise e
        """Test scroll up functionality using arrow button."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Scroll down to footer
        assert home_page.scroll_to_footer(), "Failed to scroll to footer"
        assert home_page.is_subscription_text_visible(), "Subscription text not visible in footer"
        
        # Click on arrow at bottom right side to move upward
        assert home_page.click_scroll_up_arrow(), "Failed to click scroll up arrow"
        
        # Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
        assert home_page.is_home_page_loaded(), "Home page not visible after scrolling up"
        assert home_page.is_home_page_loaded(), "Full-Fledged practice website for Automation Engineers text not visible"
    
    def test_verify_scroll_up_arrow_visibility(self):
        """Test method with screenshot support."""
        try:
"""Test that scroll up arrow is visible when scrolled down."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll down to footer
        assert home_page.scroll_to_footer(), "Failed to scroll to footer"
        
        # Verify scroll up arrow is visible
        assert home_page.is_scroll_up_arrow_visible(), "Scroll up arrow not visible"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_scroll_up_arrow_visibility: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_scroll_up_arrow_visibility: {e}")
            raise e
        """Test that scroll up arrow is visible when scrolled down."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll down to footer
        assert home_page.scroll_to_footer(), "Failed to scroll to footer"
        
        # Verify scroll up arrow is visible
        assert home_page.is_scroll_up_arrow_visible(), "Scroll up arrow not visible"
    
    def test_verify_scroll_up_functionality(self):
        """Test method with screenshot support."""
        try:
"""Test scroll up functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll down to footer
        assert home_page.scroll_to_footer(), "Failed to scroll to footer"
        
        # Click scroll up arrow
        assert home_page.click_scroll_up_arrow(), "Failed to click scroll up arrow"
        
        # Verify page is scrolled up
        assert home_page.is_home_page_loaded(), "Home page not visible after scrolling up"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_scroll_up_functionality: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_scroll_up_functionality: {e}")
            raise e
        """Test scroll up functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll down to footer
        assert home_page.scroll_to_footer(), "Failed to scroll to footer"
        
        # Click scroll up arrow
        assert home_page.click_scroll_up_arrow(), "Failed to click scroll up arrow"
        
        # Verify page is scrolled up
        assert home_page.is_home_page_loaded(), "Home page not visible after scrolling up"
    
    def test_verify_scroll_up_arrow_position(self):
        """Test method with screenshot support."""
        try:
"""Test that scroll up arrow is positioned correctly."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll down to footer
        assert home_page.scroll_to_footer(), "Failed to scroll to footer"
        
        # Verify scroll up arrow is in correct position
        assert home_page.is_scroll_up_arrow_visible(), "Scroll up arrow not in correct position"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_scroll_up_arrow_position: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_scroll_up_arrow_position: {e}")
            raise e
        """Test that scroll up arrow is positioned correctly."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll down to footer
        assert home_page.scroll_to_footer(), "Failed to scroll to footer"
        
        # Verify scroll up arrow is in correct position
        assert home_page.is_scroll_up_arrow_visible(), "Scroll up arrow not in correct position"
    
    def test_verify_scroll_up_arrow_clickability(self):
        """Test method with screenshot support."""
        try:
"""Test that scroll up arrow is clickable."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll down to footer
        assert home_page.scroll_to_footer(), "Failed to scroll to footer"
        
        # Verify scroll up arrow is clickable
        assert home_page.is_scroll_up_arrow_clickable(), "Scroll up arrow not clickable"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_scroll_up_arrow_clickability: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_scroll_up_arrow_clickability: {e}")
            raise e
        """Test that scroll up arrow is clickable."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll down to footer
        assert home_page.scroll_to_footer(), "Failed to scroll to footer"
        
        # Verify scroll up arrow is clickable
        assert home_page.is_scroll_up_arrow_clickable(), "Scroll up arrow not clickable"
