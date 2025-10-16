import requests
import json
import time

# API URL
url = "https://automationexercise.com/api/createAccount"

# Generate unique email
unique_email = f"satvik{int(time.time())}@example.com"

# Payload
payload = {
    "name": "Satvik Jayalwal",
    "email": unique_email,
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

# Send POST request
response = requests.post(url, data=payload)

# Capture status code
status = response.status_code
print(f"HTTP Status Code: {status}")

# Parse JSON response
response_json = response.json()
print("Response JSON:", response_json)

# Validate using API's responseCode
if response_json.get("responseCode") != 201:
    print(f"[BUG] Expected responseCode 201, but got {response_json.get('responseCode')}")

# Validate message
assert "User created" in response_json.get("message", ""), "Unexpected response message!" 
