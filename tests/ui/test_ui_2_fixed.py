"""
UI Test 2: Login User with correct email and password
Test Case: Login with valid credentials
"""
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_info_page import AccountInfoPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.login
class TestLoginUser:
    """Test class for user login flow."""
    
    def test_login_user_with_valid_credentials(self, driver, home_page, login_page, account_info_page, test_data):
        """Test login with valid credentials."""
        screenshot_manager = ScreenshotManager(driver)
        
        try:
            # Navigate to home page
            assert home_page.navigate_to_home(), "Failed to navigate to home page"
            assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
            
            # Click on Signup/Login button
            assert home_page.click_signup_login(), "Failed to click Signup/Login button"
            
            # Verify login form is visible
            assert login_page.is_login_form_visible(), "Login form not visible"
            
            # Get test user data
            user_data = test_data['test_users'][0]
            
            # Login with valid credentials
            assert login_page.login(user_data['email'], user_data['password']), "Failed to login with valid credentials"
            
            # Verify user is logged in
            assert home_page.is_logged_in(), "User not logged in after login"
            assert user_data['name'] in home_page.get_logged_in_username(), "Incorrect username displayed"
            
            # Click Delete Account button
            assert home_page.click_delete_account(), "Failed to click Delete Account button"
            
            # Verify account deleted message
            assert account_info_page.is_account_deleted_message_visible(), "Account deleted message not visible"
            assert "ACCOUNT DELETED!" in account_info_page.get_account_deleted_message(), "Incorrect account deleted message"
            
            # Click continue button
            assert account_info_page.click_continue(), "Failed to click continue button"
            
        except AssertionError as e:
            logger.error(f"Assertion failed in test_login_user_with_valid_credentials: {e}")
            screenshot_manager.take_screenshot_on_assertion_failure(str(e), "test_login_user_with_valid_credentials")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_login_user_with_valid_credentials: {e}")
            screenshot_manager.take_screenshot_on_error(str(e), "test_login_user_with_valid_credentials")
            raise e
    
    def test_login_user_with_invalid_credentials(self, driver, home_page, login_page, test_data):
        """Test login with invalid credentials."""
        screenshot_manager = ScreenshotManager(driver)
        
        try:
            # Navigate to home page
            assert home_page.navigate_to_home(), "Failed to navigate to home page"
            assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
            
            # Click on Signup/Login button
            assert home_page.click_signup_login(), "Failed to click Signup/Login button"
            
            # Verify login form is visible
            assert login_page.is_login_form_visible(), "Login form not visible"
            
            # Login with invalid credentials
            assert login_page.login("invalid@email.com", "wrongpassword"), "Login should fail with invalid credentials"
            
            # Verify error message is displayed
            assert login_page.is_login_error_message_visible(), "Login error message not visible"
            
        except AssertionError as e:
            logger.error(f"Assertion failed in test_login_user_with_invalid_credentials: {e}")
            screenshot_manager.take_screenshot_on_assertion_failure(str(e), "test_login_user_with_invalid_credentials")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_login_user_with_invalid_credentials: {e}")
            screenshot_manager.take_screenshot_on_error(str(e), "test_login_user_with_invalid_credentials")
            raise e
