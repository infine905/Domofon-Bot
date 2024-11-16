from config import api_key, url
from requests import get, post
import json


data = {
    "phone": 79604664266
}

headers = {
    'x-api-key': api_key
}

req = post(url=url, data=data, headers=headers)
print(req.text)