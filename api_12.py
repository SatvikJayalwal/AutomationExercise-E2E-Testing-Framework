# API 12: DELETE To Delete User Account
# API URL: https://automationexercise.com/api/deleteAccount
# Request Method: DELETE
# Expected Response Code: 200
# Expected Response Message: "Account deleted!"

import requests
import json

url = "https://automationexercise.com/api/deleteAccount"

# Payload with email and password
payload = {
    "email": "satvikjayalwalips@gmail.com",  
    "password": "123456"
}

response = requests.delete(url, data=payload)

# Parse JSON response
try:
    response_json = response.json()
except json.JSONDecodeError:
    response_json = {}
print("Response JSON:", response_json)

# Use responseCode if present, else fallback to HTTP status
actual_code = response_json.get("responseCode", response.status_code)
print(f"Status / Response Code: {actual_code}")

# Expected vs Actual check
if actual_code != 200:
    print(f"[BUG] Expected 200, but got {actual_code}")

# Validate message
expected_msg = "Account deleted"
assert expected_msg in response_json.get("message", "") or expected_msg in response.text, "Unexpected response message!"
