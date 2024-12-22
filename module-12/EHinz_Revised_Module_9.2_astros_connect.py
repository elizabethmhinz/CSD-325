import requests
import json

response = requests.get('http://api.open-notify.org/astros.json')
print(response.status_code)

print(response.json())

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())