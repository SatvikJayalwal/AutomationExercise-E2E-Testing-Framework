# API 13: PUT To Update User Account
# API URL: https://automationexercise.com/api/updateAccount
# Request Method: PUT
# Expected Response Code: 200
# Expected Response Message: "User updated!"

import requests
import json

url = "https://automationexercise.com/api/updateAccount"

# Payload: all required fields (update the email you created)
payload = {
    "name": "Satvik Jayalwal Updated",
    "email": "satvikjayalwalips@gmail.com",
    "password": "123456",
    "title": "Mr",
    "birth_date": "15",
    "birth_month": "11",
    "birth_year": "2004",
    "firstname": "Satvik",
    "lastname": "Jayalwal",
    "company": "Satvik Solutions Pvt. Ltd.",
    "address1": "Sector-47, Gurugram, Haryana, India",
    "address2": "Sector-47, Gurugram, Haryana, India",
    "country": "India",
    "zipcode": "122001",
    "state": "Haryana",
    "city": "Gurugram",
    "mobile_number": "8810655751"
}

response = requests.put(url, data=payload)

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
expected_msg = "User updated"
assert expected_msg in response_json.get("message", "") or expected_msg in response.text, "Unexpected response message!"