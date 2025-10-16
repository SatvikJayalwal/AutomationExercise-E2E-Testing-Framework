# API 10: POST To Verify Login with invalid details
# API URL: https://automationexercise.com/api/verifyLogin
# Request Method: POST
# Expected Response Code: 404
# Expected Response Message: "User not found!"

import requests
import json

url = "https://automationexercise.com/api/verifyLogin"
payload = {
    "email": "invalid@example.com",
    "password": "wrongpassword"
}

response = requests.post(url, data=payload)

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
if actual_code != 404:
    print(f"[BUG] Expected 404, but got {actual_code}")

# Validate message
expected_msg = "User not found"
assert expected_msg in response_json.get("message", "") or expected_msg in response.text, "Unexpected response message!"
