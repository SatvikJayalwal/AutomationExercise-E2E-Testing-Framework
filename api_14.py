# API 14: GET user account detail by email
# API URL: https://automationexercise.com/api/getUserDetailByEmail
# Request Method: GET
# Expected Response Code: 200
# Expected Response: User Detail JSON

import requests
import json

url = "https://automationexercise.com/api/getUserDetailByEmail"

# Query parameters
params = {"email": "satvikjayalwalips@gmail.com"}

response = requests.get(url, params=params)

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

# Validate message / user detail existence
assert "email" in response_json or "user" in response_json, "Unexpected response content!"