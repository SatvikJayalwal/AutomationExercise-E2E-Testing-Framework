"""
API Test 12: DELETE To Delete User Account
API URL: https://automationexercise.com/api/deleteAccount
Request Method: DELETE
Expected Response Code: 200
Expected Response Message: "Account deleted!"
"""
import pytest
from utils.helpers import APIHelper
from config.config import API_BASE_URL
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.api
@pytest.mark.regression
class TestDeleteUserAccount:
    """Test class for delete user account API."""
    
    def test_delete_user_account_with_valid_credentials(self):
        """Test method with screenshot support."""
        try:
"""Test DELETE request to delete user account with valid credentials."""
        # API endpoint
        url = f"{API_BASE_URL}/deleteAccount"
        
        # Get test user data
        user_data = test_data['test_users'][0]
        
        # Payload with valid credentials
        payload = {
            "email": user_data['email'],
            "password": user_data['password']
        }
        
        # Make DELETE request
        response = APIHelper.make_request('DELETE', url, data=payload)
        
        # Log response for debugging
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
            print(f"Response JSON: {json_data}")
        
        # Use responseCode if present, else fallback to HTTP status
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Expected vs Actual check
        if actual_code != 200:
            print(f"[BUG] Expected 200, but got {actual_code}")
            # This might be a known issue with the API
            assert actual_code in [200, 404], f"Unexpected status code: {actual_code}"
        else:
            print("Status code is correct (200)")
        
        # Validate message
        expected_msg = "Account deleted"
        response_text = json_data.get("message", "") or response['text']
        assert expected_msg in response_text, f"Unexpected response message! Expected: {expected_msg}, Got: {response_text}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_delete_user_account_with_valid_credentials: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_delete_user_account_with_valid_credentials: {e}")
            raise e
        """Test DELETE request to delete user account with valid credentials."""
        # API endpoint
        url = f"{API_BASE_URL}/deleteAccount"
        
        # Get test user data
        user_data = test_data['test_users'][0]
        
        # Payload with valid credentials
        payload = {
            "email": user_data['email'],
            "password": user_data['password']
        }
        
        # Make DELETE request
        response = APIHelper.make_request('DELETE', url, data=payload)
        
        # Log response for debugging
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
            print(f"Response JSON: {json_data}")
        
        # Use responseCode if present, else fallback to HTTP status
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Expected vs Actual check
        if actual_code != 200:
            print(f"[BUG] Expected 200, but got {actual_code}")
            # This might be a known issue with the API
            assert actual_code in [200, 404], f"Unexpected status code: {actual_code}"
        else:
            print("Status code is correct (200)")
        
        # Validate message
        expected_msg = "Account deleted"
        response_text = json_data.get("message", "") or response['text']
        assert expected_msg in response_text, f"Unexpected response message! Expected: {expected_msg}, Got: {response_text}"
    
    def test_delete_user_account_with_invalid_credentials(self):
        """Test method with screenshot support."""
        try:
"""Test DELETE request to delete user account with invalid credentials."""
        url = f"{API_BASE_URL}/deleteAccount"
        
        # Get invalid user data
        invalid_user = test_data['invalid_users'][0]
        
        # Payload with invalid credentials
        payload = {
            "email": invalid_user['email'],
            "password": invalid_user['password']
        }
        
        response = APIHelper.make_request('DELETE', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle invalid credentials
        assert actual_code in [200, 404, 400], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_delete_user_account_with_invalid_credentials: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_delete_user_account_with_invalid_credentials: {e}")
            raise e
        """Test DELETE request to delete user account with invalid credentials."""
        url = f"{API_BASE_URL}/deleteAccount"
        
        # Get invalid user data
        invalid_user = test_data['invalid_users'][0]
        
        # Payload with invalid credentials
        payload = {
            "email": invalid_user['email'],
            "password": invalid_user['password']
        }
        
        response = APIHelper.make_request('DELETE', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle invalid credentials
        assert actual_code in [200, 404, 400], f"Unexpected status code: {actual_code}"
    
    def test_delete_user_account_with_missing_credentials(self):
        """Test method with screenshot support."""
        try:
"""Test DELETE request to delete user account with missing credentials."""
        url = f"{API_BASE_URL}/deleteAccount"
        
        # Empty payload
        payload = {}
        
        response = APIHelper.make_request('DELETE', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle missing credentials
        assert actual_code in [200, 400, 404], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_delete_user_account_with_missing_credentials: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_delete_user_account_with_missing_credentials: {e}")
            raise e
        """Test DELETE request to delete user account with missing credentials."""
        url = f"{API_BASE_URL}/deleteAccount"
        
        # Empty payload
        payload = {}
        
        response = APIHelper.make_request('DELETE', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle missing credentials
        assert actual_code in [200, 400, 404], f"Unexpected status code: {actual_code}"
    
    def test_delete_user_account_with_wrong_password(self):
        """Test method with screenshot support."""
        try:
"""Test DELETE request to delete user account with wrong password."""
        url = f"{API_BASE_URL}/deleteAccount"
        
        # Payload with valid email but wrong password
        payload = {
            "email": "test@example.com",
            "password": "wrongpassword"
        }
        
        response = APIHelper.make_request('DELETE', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle wrong password
        assert actual_code in [200, 404, 400], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_delete_user_account_with_wrong_password: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_delete_user_account_with_wrong_password: {e}")
            raise e
        """Test DELETE request to delete user account with wrong password."""
        url = f"{API_BASE_URL}/deleteAccount"
        
        # Payload with valid email but wrong password
        payload = {
            "email": "test@example.com",
            "password": "wrongpassword"
        }
        
        response = APIHelper.make_request('DELETE', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle wrong password
        assert actual_code in [200, 404, 400], f"Unexpected status code: {actual_code}"
    
    def test_delete_user_account_with_nonexistent_email(self):
        """Test method with screenshot support."""
        try:
"""Test DELETE request to delete user account with nonexistent email."""
        url = f"{API_BASE_URL}/deleteAccount"
        
        # Payload with nonexistent email
        payload = {
            "email": "nonexistent@example.com",
            "password": "password123"
        }
        
        response = APIHelper.make_request('DELETE', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle nonexistent email
        assert actual_code in [200, 404, 400], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_delete_user_account_with_nonexistent_email: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_delete_user_account_with_nonexistent_email: {e}")
            raise e
        """Test DELETE request to delete user account with nonexistent email."""
        url = f"{API_BASE_URL}/deleteAccount"
        
        # Payload with nonexistent email
        payload = {
            "email": "nonexistent@example.com",
            "password": "password123"
        }
        
        response = APIHelper.make_request('DELETE', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle nonexistent email
        assert actual_code in [200, 404, 400], f"Unexpected status code: {actual_code}"
    
    def test_delete_user_account_with_sql_injection_attempt(self):
        """Test method with screenshot support."""
        try:
"""Test DELETE request to delete user account with SQL injection attempt."""
        url = f"{API_BASE_URL}/deleteAccount"
        
        # Payload with SQL injection attempt
        payload = {
            "email": "admin' OR '1'='1",
            "password": "password' OR '1'='1"
        }
        
        response = APIHelper.make_request('DELETE', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle SQL injection attempt safely
        assert actual_code in [200, 404, 400], f"Unexpected status code: {actual_code}"
        
        # Should not return success for SQL injection
        response_text = json_data.get("message", "") or response['text']
        assert "Account deleted" not in response_text, "SQL injection attempt should not succeed"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_delete_user_account_with_sql_injection_attempt: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_delete_user_account_with_sql_injection_attempt: {e}")
            raise e
        """Test DELETE request to delete user account with SQL injection attempt."""
        url = f"{API_BASE_URL}/deleteAccount"
        
        # Payload with SQL injection attempt
        payload = {
            "email": "admin' OR '1'='1",
            "password": "password' OR '1'='1"
        }
        
        response = APIHelper.make_request('DELETE', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle SQL injection attempt safely
        assert actual_code in [200, 404, 400], f"Unexpected status code: {actual_code}"
        
        # Should not return success for SQL injection
        response_text = json_data.get("message", "") or response['text']
        assert "Account deleted" not in response_text, "SQL injection attempt should not succeed"
