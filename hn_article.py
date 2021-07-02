import requests 
import json

# Make an API call, and store the response. 

r = requests.get(url)
print(f"Status code: {r.status_code}")

