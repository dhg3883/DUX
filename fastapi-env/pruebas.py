import requests

url = 'http://127.0.0.1:8000/clientes'
payload ={'user': 'foo'}
resp = requests.post(url=url, json=payload)
print(resp.json())