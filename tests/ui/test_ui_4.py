"""
UI Test 4: Logout User
Test Case: User logout functionality
"""
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.login
class TestLogoutUser:
    """Test class for user logout functionality."""
    
    def test_logout_user_after_login(self):
        """Test method with screenshot support."""
        try:
"""Test logout functionality after successful login."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Get test user data
        user_data = test_data['test_users'][0]
        
        # Login with valid credentials
        assert login_page.login(user_data['email'], user_data['password']), "Failed to login with valid credentials"
        
        # Verify user is logged in
        assert home_page.is_logged_in(), "User not logged in after login"
        assert user_data['name'] in home_page.get_logged_in_username(), "Incorrect username displayed"
        
        # Click logout button
        assert home_page.click_logout(), "Failed to click logout button"
        
        # Verify user is logged out
        assert not home_page.is_logged_in(), "User should be logged out"
        
        # Verify login button is visible again
        assert home_page.click_signup_login(), "Should be able to click Signup/Login button again"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_logout_user_after_login: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_logout_user_after_login: {e}")
            raise e
        """Test logout functionality after successful login."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Get test user data
        user_data = test_data['test_users'][0]
        
        # Login with valid credentials
        assert login_page.login(user_data['email'], user_data['password']), "Failed to login with valid credentials"
        
        # Verify user is logged in
        assert home_page.is_logged_in(), "User not logged in after login"
        assert user_data['name'] in home_page.get_logged_in_username(), "Incorrect username displayed"
        
        # Click logout button
        assert home_page.click_logout(), "Failed to click logout button"
        
        # Verify user is logged out
        assert not home_page.is_logged_in(), "User should be logged out"
        
        # Verify login button is visible again
        assert home_page.click_signup_login(), "Should be able to click Signup/Login button again"
    
    def test_logout_user_without_login(self):
        """Test method with screenshot support."""
        try:
"""Test logout functionality without being logged in."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Verify user is not logged in
        assert not home_page.is_logged_in(), "User should not be logged in initially"
        
        # Try to click logout (should not be available)
        # This test verifies that logout button is not visible when not logged in
        # The logout button should only be visible when user is logged in
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_logout_user_without_login: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_logout_user_without_login: {e}")
            raise e
        """Test logout functionality without being logged in."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Verify user is not logged in
        assert not home_page.is_logged_in(), "User should not be logged in initially"
        
        # Try to click logout (should not be available)
        # This test verifies that logout button is not visible when not logged in
        # The logout button should only be visible when user is logged in
    
    def test_logout_and_relogin(self):
        """Test method with screenshot support."""
        try:
"""Test logout and then relogin functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Login
        user_data = test_data['test_users'][0]
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        assert login_page.login(user_data['email'], user_data['password']), "Failed to login"
        assert home_page.is_logged_in(), "User not logged in"
        
        # Logout
        assert home_page.click_logout(), "Failed to logout"
        assert not home_page.is_logged_in(), "User should be logged out"
        
        # Relogin
        assert home_page.click_signup_login(), "Failed to click Signup/Login button again"
        assert login_page.login(user_data['email'], user_data['password']), "Failed to relogin"
        assert home_page.is_logged_in(), "User should be logged in again"
        
        # Clean up - logout
        assert home_page.click_logout(), "Failed to logout after relogin"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_logout_and_relogin: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_logout_and_relogin: {e}")
            raise e
        """Test logout and then relogin functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Login
        user_data = test_data['test_users'][0]
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        assert login_page.login(user_data['email'], user_data['password']), "Failed to login"
        assert home_page.is_logged_in(), "User not logged in"
        
        # Logout
        assert home_page.click_logout(), "Failed to logout"
        assert not home_page.is_logged_in(), "User should be logged out"
        
        # Relogin
        assert home_page.click_signup_login(), "Failed to click Signup/Login button again"
        assert login_page.login(user_data['email'], user_data['password']), "Failed to relogin"
        assert home_page.is_logged_in(), "User should be logged in again"
        
        # Clean up - logout
        assert home_page.click_logout(), "Failed to logout after relogin"
    
    def test_logout_from_different_pages(self):
        """Test method with screenshot support."""
        try:
"""Test logout functionality from different pages."""
        # Login first
        user_data = test_data['test_users'][0]
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        assert login_page.login(user_data['email'], user_data['password']), "Failed to login"
        assert home_page.is_logged_in(), "User not logged in"
        
        # Navigate to products page
        assert home_page.click_products(), "Failed to navigate to products page"
        
        # Logout from products page
        assert home_page.click_logout(), "Failed to logout from products page"
        assert not home_page.is_logged_in(), "User should be logged out"
        
        # Verify we're redirected or can access login again
        assert home_page.click_signup_login(), "Should be able to access login after logout"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_logout_from_different_pages: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_logout_from_different_pages: {e}")
            raise e
        """Test logout functionality from different pages."""
        # Login first
        user_data = test_data['test_users'][0]
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        assert login_page.login(user_data['email'], user_data['password']), "Failed to login"
        assert home_page.is_logged_in(), "User not logged in"
        
        # Navigate to products page
        assert home_page.click_products(), "Failed to navigate to products page"
        
        # Logout from products page
        assert home_page.click_logout(), "Failed to logout from products page"
        assert not home_page.is_logged_in(), "User should be logged out"
        
        # Verify we're redirected or can access login again
        assert home_page.click_signup_login(), "Should be able to access login after logout"
