# API URL: https://automationexercise.com/api/verifyLogin
# Request Method: POST
# Request Parameters: email, password
# Response Code: 200
# Response Message: User exists!

import requests 
import json

# API URL
url = "https://automationexercise.com/api/verifyLogin"

# Email and Password
email = "satvikjayalwalips@gmail.com"
password = "123456"

# Payload
payload = {
    "email": email,
    "password": password
}

# POST request
response = requests.post(url,data= payload)

# Capture status code 
status = response.status_code

# Assert status code 
assert status == 200, f"Expected 200 (OK) and but got {status}"

# Print response text
print(response.text)