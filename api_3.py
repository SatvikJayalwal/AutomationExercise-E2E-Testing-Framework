# API 3: Get All Brands List
# API URL: https://automationexercise.com/api/brandsList
# Request Method: GET
# Response Code: 200
# Response JSON: All brands list

import requests
import json

# API URL
url = "https://automationexercise.com/api/brandsList"

# Send GET request
response = requests.get(url)

# Capture Status Code 
status = response.status_code
print("Status Code : ",status)

# Validate Status Code
assert status == 200, f"Expected 200(OK) but got {status}"

# Parse json data
data = response.json()              #json.dump → saves JSON into a file. 
print(json.dumps(data,indent=2))    #json.dumps → makes JSON into a string you can print.  

# Validate 'brands' key exists
assert 'brands' in data, "'brands key not found in response"

# Validate 'brands' list is not empty
assert len(data['brands']) > 0, "Brands list is empty"

# Print total count of brands
print("Total brands : ",len(data['brands']))