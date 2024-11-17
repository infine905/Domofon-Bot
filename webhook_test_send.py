import requests
url = "http://127.0.0.1:5000"

tenant_id = 22051
domofon_id = 36
apartment_id = 14

data = {
    "tenant_id" : tenant_id,
    "domofon_id" : domofon_id,
    "apartment_id" : apartment_id
}

print("Test POST")
req = requests.post(url=url, json=data)
print(req.status_code)
print(req.content)

print("Test GET")
req = requests.get(url=url, params=data)
print(req.status_code)
print(req.content)

