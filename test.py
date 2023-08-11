import requests


BASE_URL = 'https://randommer.io'
endpoint = '/api/Card/'

payload = {
    "type": "mastercard"
}

headers = {
    "X-Api-Key": "2d794c6f46094ceb96bd719c1c26c984"
}

url = BASE_URL + endpoint  # https://randommer.io/api/Card/

response = requests.get(url=url, params=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
else:
    data = {"error": "bad response"}

print(data)
