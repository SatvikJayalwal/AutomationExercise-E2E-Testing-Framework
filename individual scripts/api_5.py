# API URL: https://automationexercise.com/api/searchProduct
# Request Method: POST
# Request Parameter: search_product (For example: top, tshirt, jean)
# Response Code: 200
# Response JSON: Searched products list

import requests
import json

# API URL 
url = "https://automationexercise.com/api/searchProduct"


# Payload (Data we want to send Eg. searching for 'top')
payload = {"search_product" : "top"}

# POST request
response = requests.post(url,data=payload)

# Capture status code 
status = response.status_code
print(f"Status Code : {status}")

# Assert status code 
assert status == 200, f"Expected 200(OK) but got {status}"

# Read json
data = response.json()

# Print data
print(json.dumps(data,indent=2))

# Assert that 'products' exist 
assert 'products' in data, "'products' key not found"

# Assert 'products' key is not empty 
assert len(data['products']) >0, "'products' key is empty"