"""
API Test 7: POST To Verify Login
API URL: https://automationexercise.com/api/verifyLogin
Request Method: POST
Request Parameters: email, password
Response Code: 200
Response Message: User exists!
"""
import pytest
from utils.helpers import APIHelper
from config.config import API_BASE_URL
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.api
@pytest.mark.smoke
class TestVerifyLogin:
    """Test class for verify login API."""
    
    def test_verify_login_with_valid_credentials(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to verify login with valid credentials."""
        # API endpoint
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Get test user data
        user_data = test_data['test_users'][0]
        
        # Payload with valid credentials
        payload = {
            "email": user_data['email'],
            "password": user_data['password']
        }
        
        # Make POST request
        response = APIHelper.make_request('POST', url, data=payload)
        
        # Log response for debugging
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Assertions
        assert response['status_code'] == 200, f"Expected 200(OK) but got {response['status_code']}"
        
        # Check response content
        if response.get('json'):
            json_data = response['json']
            assert json_data.get('responseCode') == 200, f"Expected responseCode 200, but got {json_data.get('responseCode')}"
            assert "User exists" in json_data.get('message', ''), "Expected 'User exists' message"
        else:
            # If response is not JSON, check text content
            assert "User exists" in response['text'], "Expected 'User exists' message in response"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_login_with_valid_credentials: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_login_with_valid_credentials: {e}")
            raise e
        """Test POST request to verify login with valid credentials."""
        # API endpoint
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Get test user data
        user_data = test_data['test_users'][0]
        
        # Payload with valid credentials
        payload = {
            "email": user_data['email'],
            "password": user_data['password']
        }
        
        # Make POST request
        response = APIHelper.make_request('POST', url, data=payload)
        
        # Log response for debugging
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Assertions
        assert response['status_code'] == 200, f"Expected 200(OK) but got {response['status_code']}"
        
        # Check response content
        if response.get('json'):
            json_data = response['json']
            assert json_data.get('responseCode') == 200, f"Expected responseCode 200, but got {json_data.get('responseCode')}"
            assert "User exists" in json_data.get('message', ''), "Expected 'User exists' message"
        else:
            # If response is not JSON, check text content
            assert "User exists" in response['text'], "Expected 'User exists' message in response"
    
    def test_verify_login_with_invalid_credentials(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to verify login with invalid credentials."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Get invalid user data
        invalid_user = test_data['invalid_users'][0]
        
        # Payload with invalid credentials
        payload = {
            "email": invalid_user['email'],
            "password": invalid_user['password']
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Should return error for invalid credentials
        assert response['status_code'] in [200, 404], f"Unexpected status code: {response['status_code']}"
        
        # Check for error message
        if response.get('json'):
            json_data = response['json']
            assert json_data.get('responseCode') in [404, 200], f"Unexpected responseCode: {json_data.get('responseCode')}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_login_with_invalid_credentials: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_login_with_invalid_credentials: {e}")
            raise e
        """Test POST request to verify login with invalid credentials."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Get invalid user data
        invalid_user = test_data['invalid_users'][0]
        
        # Payload with invalid credentials
        payload = {
            "email": invalid_user['email'],
            "password": invalid_user['password']
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Should return error for invalid credentials
        assert response['status_code'] in [200, 404], f"Unexpected status code: {response['status_code']}"
        
        # Check for error message
        if response.get('json'):
            json_data = response['json']
            assert json_data.get('responseCode') in [404, 200], f"Unexpected responseCode: {json_data.get('responseCode')}"
    
    def test_verify_login_with_empty_credentials(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to verify login with empty credentials."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Payload with empty credentials
        payload = {
            "email": "",
            "password": ""
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Should handle empty credentials
        assert response['status_code'] in [200, 400], f"Unexpected status code: {response['status_code']}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_login_with_empty_credentials: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_login_with_empty_credentials: {e}")
            raise e
        """Test POST request to verify login with empty credentials."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Payload with empty credentials
        payload = {
            "email": "",
            "password": ""
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Should handle empty credentials
        assert response['status_code'] in [200, 400], f"Unexpected status code: {response['status_code']}"
    
    def test_verify_login_with_malformed_email(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to verify login with malformed email."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Payload with malformed email
        payload = {
            "email": "invalid-email-format",
            "password": "password123"
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Should handle malformed email
        assert response['status_code'] in [200, 400, 404], f"Unexpected status code: {response['status_code']}"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_login_with_malformed_email: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_login_with_malformed_email: {e}")
            raise e
        """Test POST request to verify login with malformed email."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Payload with malformed email
        payload = {
            "email": "invalid-email-format",
            "password": "password123"
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Should handle malformed email
        assert response['status_code'] in [200, 400, 404], f"Unexpected status code: {response['status_code']}"
