"""
UI Test 5: Register User with existing email
Test Case: Registration with duplicate email
"""
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.signup
class TestRegisterUserWithExistingEmail:
    """Test class for registration with existing email."""
    
    def test_register_user_with_existing_email(self):
        """Test method with screenshot support."""
        try:
"""Test registration with existing email address."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Verify signup form is visible
        assert login_page.is_signup_form_visible(), "Signup form not visible"
        
        # Get test user data (use same email twice)
        user_data = test_data['test_users'][0]
        
        # First registration attempt
        assert login_page.signup(user_data['name'], user_data['email']), "Failed to start first signup process"
        
        # This should work for the first time
        # For the second attempt, we'll use the same email again
        
        # Navigate back to signup form
        assert home_page.click_signup_login(), "Failed to navigate back to signup form"
        
        # Second registration attempt with same email
        assert login_page.signup(user_data['name'], user_data['email']), "Failed to start second signup process"
        
        # This should show an error message about existing email
        # Note: The actual error message depends on the website's implementation
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_register_user_with_existing_email: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_register_user_with_existing_email: {e}")
            raise e
        """Test registration with existing email address."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Verify signup form is visible
        assert login_page.is_signup_form_visible(), "Signup form not visible"
        
        # Get test user data (use same email twice)
        user_data = test_data['test_users'][0]
        
        # First registration attempt
        assert login_page.signup(user_data['name'], user_data['email']), "Failed to start first signup process"
        
        # This should work for the first time
        # For the second attempt, we'll use the same email again
        
        # Navigate back to signup form
        assert home_page.click_signup_login(), "Failed to navigate back to signup form"
        
        # Second registration attempt with same email
        assert login_page.signup(user_data['name'], user_data['email']), "Failed to start second signup process"
        
        # This should show an error message about existing email
        # Note: The actual error message depends on the website's implementation
    
    def test_register_user_with_duplicate_email_different_name(self):
        """Test method with screenshot support."""
        try:
"""Test registration with duplicate email but different name."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Get test user data
        user_data = test_data['test_users'][0]
        
        # First registration
        assert login_page.signup(user_data['name'], user_data['email']), "Failed to start first signup"
        
        # Navigate back to signup form
        assert home_page.click_signup_login(), "Failed to navigate back to signup form"
        
        # Second registration with same email but different name
        different_name = "Different User Name"
        assert login_page.signup(different_name, user_data['email']), "Failed to start second signup with different name"
        
        # This should also show an error about existing email
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_register_user_with_duplicate_email_different_name: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_register_user_with_duplicate_email_different_name: {e}")
            raise e
        """Test registration with duplicate email but different name."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Get test user data
        user_data = test_data['test_users'][0]
        
        # First registration
        assert login_page.signup(user_data['name'], user_data['email']), "Failed to start first signup"
        
        # Navigate back to signup form
        assert home_page.click_signup_login(), "Failed to navigate back to signup form"
        
        # Second registration with same email but different name
        different_name = "Different User Name"
        assert login_page.signup(different_name, user_data['email']), "Failed to start second signup with different name"
        
        # This should also show an error about existing email
    
    def test_register_user_with_invalid_email_format(self):
        """Test method with screenshot support."""
        try:
"""Test registration with invalid email format."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Test with invalid email formats
        invalid_emails = [
            "invalid-email",
            "@example.com",
            "test@",
            "test..test@example.com",
            "test@.com",
            "test@com",
            ""
        ]
        
        for invalid_email in invalid_emails:
            # Attempt signup with invalid email
            result = login_page.signup("Test User", invalid_email)
            
            # The signup attempt should be made, but validation might occur
            print(f"Attempted signup with invalid email: {invalid_email}")
            
            # Navigate back to signup form for next attempt
            if result:
                # If signup form was submitted, navigate back
                assert home_page.click_signup_login(), "Failed to navigate back to signup form"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_register_user_with_invalid_email_format: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_register_user_with_invalid_email_format: {e}")
            raise e
        """Test registration with invalid email format."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Test with invalid email formats
        invalid_emails = [
            "invalid-email",
            "@example.com",
            "test@",
            "test..test@example.com",
            "test@.com",
            "test@com",
            ""
        ]
        
        for invalid_email in invalid_emails:
            # Attempt signup with invalid email
            result = login_page.signup("Test User", invalid_email)
            
            # The signup attempt should be made, but validation might occur
            print(f"Attempted signup with invalid email: {invalid_email}")
            
            # Navigate back to signup form for next attempt
            if result:
                # If signup form was submitted, navigate back
                assert home_page.click_signup_login(), "Failed to navigate back to signup form"
    
    def test_register_user_with_empty_fields(self):
        """Test method with screenshot support."""
        try:
"""Test registration with empty fields."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Test with empty name and email
        assert not login_page.signup("", ""), "Signup should fail with empty fields"
        
        # Test with empty name only
        assert not login_page.signup("", "test@example.com"), "Signup should fail with empty name"
        
        # Test with empty email only
        assert not login_page.signup("Test User", ""), "Signup should fail with empty email"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_register_user_with_empty_fields: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_register_user_with_empty_fields: {e}")
            raise e
        """Test registration with empty fields."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Test with empty name and email
        assert not login_page.signup("", ""), "Signup should fail with empty fields"
        
        # Test with empty name only
        assert not login_page.signup("", "test@example.com"), "Signup should fail with empty name"
        
        # Test with empty email only
        assert not login_page.signup("Test User", ""), "Signup should fail with empty email"
    
    def test_register_user_with_special_characters(self):
        """Test method with screenshot support."""
        try:
"""Test registration with special characters in name and email."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Test with special characters
        special_names = [
            "Test User!@#",
            "User@123",
            "Test$User",
            "User%Name",
            "Test^User"
        ]
        
        special_emails = [
            "test+special@example.com",
            "test.user@example.com",
            "test_user@example.com",
            "test-user@example.com"
        ]
        
        for name in special_names:
            for email in special_emails:
                # Attempt signup with special characters
                result = login_page.signup(name, email)
                print(f"Attempted signup with name: '{name}', email: '{email}'")
                
                # Navigate back to signup form for next attempt
                if result:
                    assert home_page.click_signup_login(), "Failed to navigate back to signup form"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_register_user_with_special_characters: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_register_user_with_special_characters: {e}")
            raise e
        """Test registration with special characters in name and email."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Signup/Login button
        assert home_page.click_signup_login(), "Failed to click Signup/Login button"
        
        # Test with special characters
        special_names = [
            "Test User!@#",
            "User@123",
            "Test$User",
            "User%Name",
            "Test^User"
        ]
        
        special_emails = [
            "test+special@example.com",
            "test.user@example.com",
            "test_user@example.com",
            "test-user@example.com"
        ]
        
        for name in special_names:
            for email in special_emails:
                # Attempt signup with special characters
                result = login_page.signup(name, email)
                print(f"Attempted signup with name: '{name}', email: '{email}'")
                
                # Navigate back to signup form for next attempt
                if result:
                    assert home_page.click_signup_login(), "Failed to navigate back to signup form"
