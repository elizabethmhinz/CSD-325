# Module 9.2 Test Code with different URL than first
import requests

response = requests.get('https://catfact.ninja/fact')
print(response.status_code)

