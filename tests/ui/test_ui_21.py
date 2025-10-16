"""
UI Test 21: Add Review on Product
Test Case: Add review on a product
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.review
class TestAddReviewOnProduct:
    """Test class for adding review on a product."""
    
    def test_add_review_on_product(self, driver, home_page, products_page, login_page, test_data):
        """Test adding review on a product."""
        screenshot_manager = ScreenshotManager(driver)
        
        try:
            # Navigate to home page
            assert home_page.navigate_to_home(), "Failed to navigate to home page"
            assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
            
            # Login to account
            assert home_page.click_signup_login(), "Failed to click Signup/Login button"
            assert login_page.is_login_form_visible(), "Login form not visible"
            
            user_data = test_data['test_users'][0]
            assert login_page.login(user_data['email'], user_data['password']), "Failed to login"
            
            # Verify user is logged in
            assert home_page.is_logged_in(), "User not logged in after login"
            
            # Go to products page
            assert home_page.click_products(), "Failed to click Products button"
            assert products_page.is_all_products_text_visible(), "Products page not visible"
            
            # Click on a product to view details
            assert products_page.click_view_product_button(1), "Failed to click view product button"
            assert products_page.is_product_detail_page_opened(), "Product detail page not opened"
            assert products_page.is_product_information_visible(), "Product information not visible"
            
            # Scroll to review section
            assert products_page.scroll_to_review_section(), "Failed to scroll to review section"
            assert products_page.is_write_your_review_visible(), "Write Your Review section not visible"
            
            # Fill review form
            review_data = {
                'name': user_data['name'],
                'email': user_data['email'],
                'review': 'This is a great product! Highly recommended.'
            }
            
            assert products_page.enter_review_details(
                review_data['name'], 
                review_data['email'], 
                review_data['review']
            ), "Failed to enter review details"
            
            # Submit review
            assert products_page.click_submit_review_button(), "Failed to click submit review button"
            assert products_page.is_review_success_message_visible(), "Review success message not visible"
            
        except AssertionError as e:
            logger.error(f"Assertion failed in test_add_review_on_product: {e}")
            screenshot_manager.take_screenshot_on_assertion_failure(str(e), "test_add_review_on_product")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_add_review_on_product: {e}")
            screenshot_manager.take_screenshot_on_error(str(e), "test_add_review_on_product")
            raise e