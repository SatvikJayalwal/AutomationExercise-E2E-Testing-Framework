# API 8: POST To Verify Login without email parameter
# API URL: https://automationexercise.com/api/verifyLogin
# Request Method: POST
# Expected Response Code: 400
# Expected Response Message: "Bad request, email or password parameter is missing in POST request"

import requests
import json

url = "https://automationexercise.com/api/verifyLogin"
payload = {"password": "mypassword123"}

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
if actual_code != 400:
    print(f"[BUG] Expected 400, but got {actual_code}")

# Validate message
expected_msg = "email or password parameter is missing"
assert expected_msg in response_json.get("message", "") or expected_msg in response.text, "Unexpected response message!"