import requests

url = requests.get('https://randomuser.me/api/?nat=us')
data = url.json()

print(data)
