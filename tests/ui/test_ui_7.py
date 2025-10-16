"""
UI Test 7: Verify Test Cases Page
Test Case: Navigate to test cases page
"""
import pytest
from pages.home_page import HomePage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
class TestTestCasesPage:
    """Test class for test cases page functionality."""
    
    def test_verify_test_cases_page(self):
        """Test method with screenshot support."""
        try:
"""Test navigation to test cases page."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Test Cases button
        assert home_page.click_test_cases(), "Failed to click Test Cases button"
        
        # Verify test cases page is loaded
        assert home_page.is_test_cases_page_loaded(), "Test cases page not loaded"
        assert "Test Cases" in home_page.get_test_cases_header_text(), "Test cases header not correct"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_test_cases_page: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_test_cases_page: {e}")
            raise e
        """Test navigation to test cases page."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Test Cases button
        assert home_page.click_test_cases(), "Failed to click Test Cases button"
        
        # Verify test cases page is loaded
        assert home_page.is_test_cases_page_loaded(), "Test cases page not loaded"
        assert "Test Cases" in home_page.get_test_cases_header_text(), "Test cases header not correct"
    
    def test_verify_test_cases_page_elements(self):
        """Test method with screenshot support."""
        try:
"""Test verification of test cases page elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Test Cases button
        assert home_page.click_test_cases(), "Failed to click Test Cases button"
        
        # Verify test cases page elements
        elements_status = home_page.verify_test_cases_page_elements()
        
        assert elements_status['test_cases_header_visible'], "Test cases header not visible"
        assert elements_status['test_cases_content_visible'], "Test cases content not visible"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_test_cases_page_elements: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_test_cases_page_elements: {e}")
            raise e
        """Test verification of test cases page elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Test Cases button
        assert home_page.click_test_cases(), "Failed to click Test Cases button"
        
        # Verify test cases page elements
        elements_status = home_page.verify_test_cases_page_elements()
        
        assert elements_status['test_cases_header_visible'], "Test cases header not visible"
        assert elements_status['test_cases_content_visible'], "Test cases content not visible"
    
    def test_verify_test_cases_page_navigation(self):
        """Test method with screenshot support."""
        try:
"""Test navigation to test cases page from different locations."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Test Cases button
        assert home_page.click_test_cases(), "Failed to click Test Cases button"
        
        # Verify test cases page is loaded
        assert home_page.is_test_cases_page_loaded(), "Test cases page not loaded"
        
        # Navigate back to home page
        assert home_page.navigate_to_home(), "Failed to navigate back to home page"
        
        # Click on Test Cases button again
        assert home_page.click_test_cases(), "Failed to click Test Cases button again"
        
        # Verify test cases page is loaded again
        assert home_page.is_test_cases_page_loaded(), "Test cases page not loaded on second visit"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_test_cases_page_navigation: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_test_cases_page_navigation: {e}")
            raise e
        """Test navigation to test cases page from different locations."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Test Cases button
        assert home_page.click_test_cases(), "Failed to click Test Cases button"
        
        # Verify test cases page is loaded
        assert home_page.is_test_cases_page_loaded(), "Test cases page not loaded"
        
        # Navigate back to home page
        assert home_page.navigate_to_home(), "Failed to navigate back to home page"
        
        # Click on Test Cases button again
        assert home_page.click_test_cases(), "Failed to click Test Cases button again"
        
        # Verify test cases page is loaded again
        assert home_page.is_test_cases_page_loaded(), "Test cases page not loaded on second visit"
