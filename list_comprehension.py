import json
import urllib
import requests

url = 'https://parseapi.back4app.com/classes/Cepcorreios_CEP?limit=10'
headers = {
    'X-Parse-Application-Id': 'KDscoJcVWclrKOKMoSmmkwzVnr2NVTJleUA17X0f', # This is your app's application id
    'X-Parse-REST-API-Key': 'qkxoXIfgK4oM3NAqdc0lFUw73wVpkHXymNdwHdoW' # This is your app's REST API key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
print(json.dumps(data, indent=2))