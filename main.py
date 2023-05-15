import json
import re
import requests

login = 'macoveigrigoreinfo'
password = 'QsPJvwtE4s'

proxies = {
    'https': f'http://{login}:{password}@185.206.248.113:50100'
}

print('\n>> Cerere OPTIONS:')
response = requests.options("https://api.restful-api.dev/objects", proxies=proxies)
print(response.headers["allow"])

print('\n>> Cerere HEAD:')
response = requests.head("https://api.restful-api.dev/objects")
print(response.headers)
print(response.content)

print('\n>> Cerere GET:')
response = requests.get("https://api.restful-api.dev/objects")
regex = r'Apple'
nr = re.findall(regex, response.content.decode())
print(response.json())
print('Nr produse Apple:', len(nr))

print('\n>> Cerere POST:')
headers = {"content-type": "application/json"}
data = json.dumps(
    { "name": "Apple AirPods", 
        "data": {
          "year": 2019,
          "price": 1849.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB"
    }})
response = requests.post("https://api.restful-api.dev/objects", data=data, headers=headers)
print(response, "\n", response.json())
