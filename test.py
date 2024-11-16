from requests import get, post
import json

#401 Bad Token
#404 User not found

url = "https://domo-dev.profintel.ru/tg-bot/check-tenant"

data = {
    'phone': 79604664266
}

headers = {
    'x-api-key': "SecretToken"
}

request = post(url=url, headers=headers, data=json.dumps(data))
content = json.loads(request.content.decode())
print(content)

if request.status_code == 200:
    tenant_id = content["tenant_id"]
