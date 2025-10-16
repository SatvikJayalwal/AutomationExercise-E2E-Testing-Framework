"""
UI Test 3: Login User with incorrect email and password
Test Case: Login with invalid credentials
"""
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.login
class TestLoginUserWithInvalidCredentials:
    """Test class for login with invalid credentials."""
    
    def test_login_user_with_incorrect_email_and_password(self):
        """Test method with screenshot support."""
        try:
"""Test login with incorrect email and password."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Verify login form is visible
        assert login_page.is_login_form_visible(), "Login form not visible"
        
        # Get invalid user data
        invalid_user = test_data['invalid_users'][0]
        
        # Attempt login with incorrect credentials
        assert login_page.login(invalid_user['email'], invalid_user['password']), "Login attempt should be made"
        
        # Verify error message is displayed
        assert login_page.is_login_error_visible(), "Login error message not visible"
        assert "Your email or password is incorrect!" in login_page.get_login_error_message(), "Incorrect error message"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_login_user_with_incorrect_email_and_password: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_login_user_with_incorrect_email_and_password: {e}")
            raise e
        """Test login with incorrect email and password."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Verify login form is visible
        assert login_page.is_login_form_visible(), "Login form not visible"
        
        # Get invalid user data
        invalid_user = test_data['invalid_users'][0]
        
        # Attempt login with incorrect credentials
        assert login_page.login(invalid_user['email'], invalid_user['password']), "Login attempt should be made"
        
        # Verify error message is displayed
        assert login_page.is_login_error_visible(), "Login error message not visible"
        assert "Your email or password is incorrect!" in login_page.get_login_error_message(), "Incorrect error message"
    
    def test_login_user_with_nonexistent_email(self):
        """Test method with screenshot support."""
        try:
"""Test login with nonexistent email."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Get second invalid user data
        invalid_user = test_data['invalid_users'][1]
        
        # Attempt login with nonexistent email
        assert login_page.login(invalid_user['email'], invalid_user['password']), "Login attempt should be made"
        
        # Verify error message is displayed
        assert login_page.is_login_error_visible(), "Login error message not visible"
        assert "Your email or password is incorrect!" in login_page.get_login_error_message(), "Incorrect error message"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_login_user_with_nonexistent_email: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_login_user_with_nonexistent_email: {e}")
            raise e
        """Test login with nonexistent email."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Get second invalid user data
        invalid_user = test_data['invalid_users'][1]
        
        # Attempt login with nonexistent email
        assert login_page.login(invalid_user['email'], invalid_user['password']), "Login attempt should be made"
        
        # Verify error message is displayed
        assert login_page.is_login_error_visible(), "Login error message not visible"
        assert "Your email or password is incorrect!" in login_page.get_login_error_message(), "Incorrect error message"
    
    def test_login_user_with_wrong_password_format(self):
        """Test method with screenshot support."""
        try:
"""Test login with wrong password format."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Attempt login with wrong password format
        assert login_page.login("test@example.com", "123"), "Login attempt should be made with short password"
        
        # Verify error message is displayed
        assert login_page.is_login_error_visible(), "Login error message not visible"
        assert "Your email or password is incorrect!" in login_page.get_login_error_message(), "Incorrect error message"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_login_user_with_wrong_password_format: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_login_user_with_wrong_password_format: {e}")
            raise e
        """Test login with wrong password format."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Attempt login with wrong password format
        assert login_page.login("test@example.com", "123"), "Login attempt should be made with short password"
        
        # Verify error message is displayed
        assert login_page.is_login_error_visible(), "Login error message not visible"
        assert "Your email or password is incorrect!" in login_page.get_login_error_message(), "Incorrect error message"
    
    def test_login_user_with_sql_injection_attempt(self):
        """Test method with screenshot support."""
        try:
"""Test login with SQL injection attempt."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Attempt login with SQL injection
        sql_injection_email = "admin' OR '1'='1"
        sql_injection_password = "password' OR '1'='1"
        
        assert login_page.login(sql_injection_email, sql_injection_password), "Login attempt should be made"
        
        # Verify error message is displayed (should not allow SQL injection)
        assert login_page.is_login_error_visible(), "Login error message not visible"
        assert "Your email or password is incorrect!" in login_page.get_login_error_message(), "Incorrect error message"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_login_user_with_sql_injection_attempt: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_login_user_with_sql_injection_attempt: {e}")
            raise e
        """Test login with SQL injection attempt."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Attempt login with SQL injection
        sql_injection_email = "admin' OR '1'='1"
        sql_injection_password = "password' OR '1'='1"
        
        assert login_page.login(sql_injection_email, sql_injection_password), "Login attempt should be made"
        
        # Verify error message is displayed (should not allow SQL injection)
        assert login_page.is_login_error_visible(), "Login error message not visible"
        assert "Your email or password is incorrect!" in login_page.get_login_error_message(), "Incorrect error message"
    
    def test_login_user_with_xss_attempt(self):
        """Test method with screenshot support."""
        try:
"""Test login with XSS attempt."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Attempt login with XSS payload
        xss_email = "<script>alert('xss')</script>@example.com"
        xss_password = "<script>alert('xss')</script>"
        
        assert login_page.login(xss_email, xss_password), "Login attempt should be made"
        
        # Verify error message is displayed (should not execute XSS)
        assert login_page.is_login_error_visible(), "Login error message not visible"
        assert "Your email or password is incorrect!" in login_page.get_login_error_message(), "Incorrect error message"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_login_user_with_xss_attempt: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_login_user_with_xss_attempt: {e}")
            raise e
        """Test login with XSS attempt."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Attempt login with XSS payload
        xss_email = "<script>alert('xss')</script>@example.com"
        xss_password = "<script>alert('xss')</script>"
        
        assert login_page.login(xss_email, xss_password), "Login attempt should be made"
        
        # Verify error message is displayed (should not execute XSS)
        assert login_page.is_login_error_visible(), "Login error message not visible"
        assert "Your email or password is incorrect!" in login_page.get_login_error_message(), "Incorrect error message"
