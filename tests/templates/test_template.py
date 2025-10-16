"""
Test template with comprehensive screenshot handling.
Use this template for creating new test files.
"""
import pytest
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
class TestTemplate:
    """Template test class with comprehensive screenshot handling."""
    
    def test_with_screenshot_handling(self, driver, home_page, test_data):
        """Example test with comprehensive screenshot handling."""
        screenshot_manager = ScreenshotManager(driver)
        
        try:
            # Take screenshot before starting test
            screenshot_manager.take_screenshot_before_action("test_start", "test_with_screenshot_handling")
            
            # Navigate to home page
            assert home_page.navigate_to_home(), "Failed to navigate to home page"
            screenshot_manager.take_screenshot_after_action("navigate_to_home", "test_with_screenshot_handling")
            
            # Verify home page is loaded
            assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
            screenshot_manager.take_screenshot_after_action("verify_home_page_loaded", "test_with_screenshot_handling")
            
            # Perform test actions
            # ... your test logic here ...
            
            logger.info("Test completed successfully")
            
        except AssertionError as e:
            # Take screenshot on assertion failure
            screenshot_manager.take_screenshot_on_assertion_failure(str(e), "test_with_screenshot_handling")
            logger.error(f"Assertion failed: {e}")
            raise e
            
        except Exception as e:
            # Take screenshot on any other error
            screenshot_manager.take_screenshot_on_error(str(e), "test_with_screenshot_handling")
            logger.error(f"Test failed with error: {e}")
            raise e
    
    @screenshot_on_failure("test_with_decorator")
    def test_with_screenshot_decorator(self, driver, home_page):
        """Example test using screenshot decorator."""
        # This test will automatically take screenshots on failure
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Your test logic here...
        logger.info("Test with decorator completed successfully")
    
    def test_with_element_screenshot(self, driver, home_page):
        """Example test with element-specific screenshots."""
        screenshot_manager = ScreenshotManager(driver)
        
        try:
            # Navigate to home page
            assert home_page.navigate_to_home(), "Failed to navigate to home page"
            
            # Find an element and take its screenshot
            # element = home_page.find_element(By.ID, "some_element_id")
            # screenshot_manager.take_element_screenshot(element, "element_screenshot.png")
            
            # Take full page screenshot
            screenshot_manager.take_full_page_screenshot("full_page_test.png")
            
            logger.info("Element screenshot test completed successfully")
            
        except Exception as e:
            screenshot_manager.take_screenshot_on_error(str(e), "test_with_element_screenshot")
            raise e
