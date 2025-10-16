"""
UI Test 1: Register User
Test Case: Complete user registration flow
"""
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_info_page import AccountInfoPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.signup
class TestRegisterUser:
    """Test class for user registration flow."""
    
    def test_register_user_complete_flow(self, driver, home_page, login_page, signup_page, account_info_page, test_data):
        """Test complete user registration flow."""
        screenshot_manager = ScreenshotManager(driver)
        
        try:
            # Navigate to home page
            assert home_page.navigate_to_home(), "Failed to navigate to home page"
            assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
            
            # Click on Signup/Login button
            assert home_page.click_signup_login(), "Failed to click Signup/Login button"
            
            # Verify signup form is visible
            assert login_page.is_signup_form_visible(), "Signup form not visible"
            
            # Get test user data
            user_data = test_data['test_users'][0]
            
            # Start signup process
            assert login_page.signup(user_data['name'], user_data['email']), "Failed to start signup process"
            
            # Verify account information form is visible
            assert signup_page.is_account_info_form_visible(), "Account information form not visible"
            
            # Complete signup process
            assert signup_page.complete_signup(user_data), "Failed to complete signup process"
            
            # Verify account created message
            assert signup_page.is_account_created(), "Account created message not visible"
            
            # Click continue button
            assert signup_page.click_continue(), "Failed to click continue button"
            
            # Verify user is logged in
            assert home_page.is_logged_in(), "User not logged in after registration"
            assert user_data['name'] in home_page.get_logged_in_username(), "Incorrect username displayed"
            
        except AssertionError as e:
            logger.error(f"Assertion failed in test_register_user_complete_flow: {e}")
            screenshot_manager.take_screenshot_on_assertion_failure(str(e), "test_register_user_complete_flow")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_register_user_complete_flow: {e}")
            screenshot_manager.take_screenshot_on_error(str(e), "test_register_user_complete_flow")
            raise e
        
        # Click Delete Account button
        assert home_page.click_delete_account(), "Failed to click Delete Account button"
        
        # Verify account deleted message
        assert account_info_page.is_account_deleted_message_visible(), "Account deleted message not visible"
        assert "ACCOUNT DELETED!" in account_info_page.get_account_deleted_message(), "Incorrect account deleted message"
        
        # Click continue button
        assert account_info_page.click_continue(), "Failed to click continue button"
    
    def test_register_user_with_different_data(self, driver, home_page, login_page, signup_page, account_info_page, test_data):
        """Test user registration with different user data."""
        screenshot_manager = ScreenshotManager(driver)
        
        try:
            # Navigate to home page
            assert home_page.navigate_to_home(), "Failed to navigate to home page"
            assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
            
            # Click on Signup/Login button
            assert home_page.click_signup_login(), "Failed to click Signup/Login button"
            
            # Get second test user data
            user_data = test_data['test_users'][1] if len(test_data['test_users']) > 1 else test_data['test_users'][0]
            
            # Start signup process
            assert login_page.signup(user_data['name'], user_data['email']), "Failed to start signup process"
            
            # Complete signup process
            assert signup_page.complete_signup(user_data), "Failed to complete signup process"
            
            # Verify account created message
            assert signup_page.is_account_created(), "Account created message not visible"
            
            # Click continue button
            assert signup_page.click_continue(), "Failed to click continue button"
            
            # Verify user is logged in
            assert home_page.is_logged_in(), "User not logged in after registration"
            
        except AssertionError as e:
            logger.error(f"Assertion failed in test_register_user_with_different_data: {e}")
            screenshot_manager.take_screenshot_on_assertion_failure(str(e), "test_register_user_with_different_data")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_register_user_with_different_data: {e}")
            screenshot_manager.take_screenshot_on_error(str(e), "test_register_user_with_different_data")
            raise e
        
        # Clean up - delete account
        assert home_page.click_delete_account(), "Failed to click Delete Account button"
        assert account_info_page.is_account_deleted_message_visible(), "Account deleted message not visible"
        assert account_info_page.click_continue(), "Failed to click continue button"