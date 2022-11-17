import requests

URL = "https://dog.ceo/api/breeds/image/random"

result = requests.get(URL)

data = result.json()

print(data)