"""
API Test 11: POST To Create Account
API URL: https://automationexercise.com/api/createAccount
Request Method: POST
Request Parameters: name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number
Response Code: 201
Response Message: User created!
"""
import pytest
import time
from utils.helpers import APIHelper, DataGenerator
from config.config import API_BASE_URL
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.api
@pytest.mark.smoke
class TestCreateAccount:
    """Test class for create account API."""
    
    def test_create_account_with_valid_data(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to create account with valid data."""
        # API endpoint
        url = f"{API_BASE_URL}/createAccount"
        
        # Generate unique email to avoid conflicts
        unique_email = DataGenerator.generate_random_email()
        
        # Get test user data and update with unique email
        user_data = test_data['test_users'][0].copy()
        user_data['email'] = unique_email
        
        # Payload with all required fields
        payload = {
            "name": user_data['name'],
            "email": user_data['email'],
            "password": user_data['password'],
            "title": user_data['title'],
            "birth_date": user_data['day'],
            "birth_month": user_data['month'],
            "birth_year": user_data['year'],
            "firstname": user_data['first_name'],
            "lastname": user_data['last_name'],
            "company": user_data['company'],
            "address1": user_data['address1'],
            "address2": user_data.get('address2', ''),
            "country": user_data['country'],
            "zipcode": user_data['zipcode'],
            "state": user_data['state'],
            "city": user_data['city'],
            "mobile_number": user_data['mobile_number']
        }
        
        # Make POST request
        response = APIHelper.make_request('POST', url, data=payload)
        
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
        
        # Assertions
        assert actual_code == 201, f"Expected responseCode 201, but got {actual_code}"
        
        # Validate message
        expected_msg = "User created"
        response_text = json_data.get("message", "") or response['text']
        assert expected_msg in response_text, f"Unexpected response message! Expected: {expected_msg}, Got: {response_text}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_create_account_with_valid_data: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_create_account_with_valid_data: {e}")
            raise e
        """Test POST request to create account with valid data."""
        # API endpoint
        url = f"{API_BASE_URL}/createAccount"
        
        # Generate unique email to avoid conflicts
        unique_email = DataGenerator.generate_random_email()
        
        # Get test user data and update with unique email
        user_data = test_data['test_users'][0].copy()
        user_data['email'] = unique_email
        
        # Payload with all required fields
        payload = {
            "name": user_data['name'],
            "email": user_data['email'],
            "password": user_data['password'],
            "title": user_data['title'],
            "birth_date": user_data['day'],
            "birth_month": user_data['month'],
            "birth_year": user_data['year'],
            "firstname": user_data['first_name'],
            "lastname": user_data['last_name'],
            "company": user_data['company'],
            "address1": user_data['address1'],
            "address2": user_data.get('address2', ''),
            "country": user_data['country'],
            "zipcode": user_data['zipcode'],
            "state": user_data['state'],
            "city": user_data['city'],
            "mobile_number": user_data['mobile_number']
        }
        
        # Make POST request
        response = APIHelper.make_request('POST', url, data=payload)
        
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
        
        # Assertions
        assert actual_code == 201, f"Expected responseCode 201, but got {actual_code}"
        
        # Validate message
        expected_msg = "User created"
        response_text = json_data.get("message", "") or response['text']
        assert expected_msg in response_text, f"Unexpected response message! Expected: {expected_msg}, Got: {response_text}"
    
    def test_create_account_with_duplicate_email(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to create account with duplicate email."""
        url = f"{API_BASE_URL}/createAccount"
        
        # Use existing email from test data
        user_data = test_data['test_users'][0]
        
        # Payload with duplicate email
        payload = {
            "name": user_data['name'],
            "email": user_data['email'],
            "password": user_data['password'],
            "title": user_data['title'],
            "birth_date": user_data['day'],
            "birth_month": user_data['month'],
            "birth_year": user_data['year'],
            "firstname": user_data['first_name'],
            "lastname": user_data['last_name'],
            "company": user_data['company'],
            "address1": user_data['address1'],
            "address2": user_data.get('address2', ''),
            "country": user_data['country'],
            "zipcode": user_data['zipcode'],
            "state": user_data['state'],
            "city": user_data['city'],
            "mobile_number": user_data['mobile_number']
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle duplicate email
        assert actual_code in [200, 400, 409], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_create_account_with_duplicate_email: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_create_account_with_duplicate_email: {e}")
            raise e
        """Test POST request to create account with duplicate email."""
        url = f"{API_BASE_URL}/createAccount"
        
        # Use existing email from test data
        user_data = test_data['test_users'][0]
        
        # Payload with duplicate email
        payload = {
            "name": user_data['name'],
            "email": user_data['email'],
            "password": user_data['password'],
            "title": user_data['title'],
            "birth_date": user_data['day'],
            "birth_month": user_data['month'],
            "birth_year": user_data['year'],
            "firstname": user_data['first_name'],
            "lastname": user_data['last_name'],
            "company": user_data['company'],
            "address1": user_data['address1'],
            "address2": user_data.get('address2', ''),
            "country": user_data['country'],
            "zipcode": user_data['zipcode'],
            "state": user_data['state'],
            "city": user_data['city'],
            "mobile_number": user_data['mobile_number']
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle duplicate email
        assert actual_code in [200, 400, 409], f"Unexpected status code: {actual_code}"
    
    def test_create_account_with_missing_required_fields(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to create account with missing required fields."""
        url = f"{API_BASE_URL}/createAccount"
        
        # Payload with missing required fields
        payload = {
            "name": "Test User",
            "email": "test@example.com"
            # Missing other required fields
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle missing required fields
        assert actual_code in [200, 400], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_create_account_with_missing_required_fields: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_create_account_with_missing_required_fields: {e}")
            raise e
        """Test POST request to create account with missing required fields."""
        url = f"{API_BASE_URL}/createAccount"
        
        # Payload with missing required fields
        payload = {
            "name": "Test User",
            "email": "test@example.com"
            # Missing other required fields
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle missing required fields
        assert actual_code in [200, 400], f"Unexpected status code: {actual_code}"
    
    def test_create_account_with_invalid_email_format(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to create account with invalid email format."""
        url = f"{API_BASE_URL}/createAccount"
        
        # Payload with invalid email format
        payload = {
            "name": "Test User",
            "email": "invalid-email-format",
            "password": "password123",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "11",
            "birth_year": "2004",
            "firstname": "Test",
            "lastname": "User",
            "company": "Test Company",
            "address1": "Test Address",
            "country": "India",
            "zipcode": "12345",
            "state": "Test State",
            "city": "Test City",
            "mobile_number": "1234567890"
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle invalid email format
        assert actual_code in [200, 400], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_create_account_with_invalid_email_format: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_create_account_with_invalid_email_format: {e}")
            raise e
        """Test POST request to create account with invalid email format."""
        url = f"{API_BASE_URL}/createAccount"
        
        # Payload with invalid email format
        payload = {
            "name": "Test User",
            "email": "invalid-email-format",
            "password": "password123",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "11",
            "birth_year": "2004",
            "firstname": "Test",
            "lastname": "User",
            "company": "Test Company",
            "address1": "Test Address",
            "country": "India",
            "zipcode": "12345",
            "state": "Test State",
            "city": "Test City",
            "mobile_number": "1234567890"
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle invalid email format
        assert actual_code in [200, 400], f"Unexpected status code: {actual_code}"
    
    def test_create_account_with_special_characters(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to create account with special characters."""
        url = f"{API_BASE_URL}/createAccount"
        
        # Generate unique email
        unique_email = DataGenerator.generate_random_email()
        
        # Payload with special characters in name
        payload = {
            "name": "Test User!@#$%",
            "email": unique_email,
            "password": "password123",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "11",
            "birth_year": "2004",
            "firstname": "Test!@#",
            "lastname": "User$%^",
            "company": "Test & Company",
            "address1": "Test Address #123",
            "country": "India",
            "zipcode": "12345",
            "state": "Test State",
            "city": "Test City",
            "mobile_number": "1234567890"
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle special characters
        assert actual_code in [200, 201, 400], f"Unexpected status code: {actual_code}"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_create_account_with_special_characters: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_create_account_with_special_characters: {e}")
            raise e
        """Test POST request to create account with special characters."""
        url = f"{API_BASE_URL}/createAccount"
        
        # Generate unique email
        unique_email = DataGenerator.generate_random_email()
        
        # Payload with special characters in name
        payload = {
            "name": "Test User!@#$%",
            "email": unique_email,
            "password": "password123",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "11",
            "birth_year": "2004",
            "firstname": "Test!@#",
            "lastname": "User$%^",
            "company": "Test & Company",
            "address1": "Test Address #123",
            "country": "India",
            "zipcode": "12345",
            "state": "Test State",
            "city": "Test City",
            "mobile_number": "1234567890"
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle special characters
        assert actual_code in [200, 201, 400], f"Unexpected status code: {actual_code}"
