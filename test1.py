from requests import post, get
import json
from io import BytesIO

class Tenant():
    id = None
    def __init__(self, id:int) -> None:
        self.id = id
        
    def __repr__(self):
        return f"Tenant(id={self.id})"
    
class Apartment():
    id = None
    name = None
    address = None
    tenants = None
       
    def __init__(self, id:int, name:str, address:str, tenants:list[Tenant]) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.tenants = tenants
      
    def __repr__(self):
        return f"Apartment(id={self.id}, name='{self.name}', address='{self.address}', tenants={self.tenants})"
    
class Domofon():
    id = None
    name = None
    address = None
    def __init__(self, id:int, name:str, address:str) -> None:
        self.id = id
        self.name = name
        self.address = address
        
    def __repr__(self):
        return f"Domofon(id={self.id}, name='{self.name}', address='{self.address}')" 
    
def getTenantId(phone : int) -> int | None:
    url = "https://domo-dev.profintel.ru/tg-bot/check-tenant"
    data = {
        'phone': phone
    }
    headers = {
        'x-api-key': 'SecretToken'
    }

    request = post(url=url, headers=headers, data=json.dumps(data))

    if request.status_code == 200:
        content = json.loads(request.content.decode())
        return int(content["tenant_id"])
    
    return None

def getApartments(tenant_id:int) -> list[Apartment] | None:
    url = "https://domo-dev.profintel.ru/tg-bot/domo.apartment"
    params  = {
        "tenant_id": tenant_id
    }
    headers = {
        'x-api-key': 'SecretToken'
    }

    request = get(url=url, headers=headers, params=params )
    
    if request.status_code != 200:
        return None
    
    content = json.loads(request.content.decode())
    apartments = []
    for item in content:
        id = item['id']
        name = item['name']
        address = item['location']['readable_address']
        tenants_data = item.get('tenants', [])
        tenants = [Tenant(t['id']) for t in tenants_data]
        apartments.append(Apartment(id, name, address, tenants))
    return apartments    
    
def getDofons(apartment_id:int, tenant_id:int) -> list[Domofon] | None:
    url = f"https://domo-dev.profintel.ru/tg-bot/domo.apartment/{apartment_id}/domofon"
    params  = {
        "tenant_id" : tenant_id
    }
    headers = {
        'x-api-key': 'SecretToken'
    }

    request = get(url=url, headers=headers, params=params )
    print(request.status_code)
    print(request.content.decode())
    
    if request.status_code != 200:
        return None
    
    content = json.loads(request.content.decode())
    
    domofons = []
    for item in content:
        id = item['id']
        name = item['name']
        address = item['location']['readable_address']
        print(id, name, address)
        domofons.append(Domofon(id, name, address))
        
    return domofons  
     
def getDomofonImage(domofon_id:int, tenant_id:int, media_type:str="JPEG") -> BytesIO | None:
    url = f"https://domo-dev.profintel.ru/tg-bot/domo.domofon/urlsOnType"
    
    params  = {
        "tenant_id" : tenant_id
    }
    
    data = {
        "intercoms_id": [
            domofon_id
        ],
        "media_type": [
            "JPEG"
        ]
    }
    
    headers = {
        'x-api-key': 'SecretToken'
    }

    request = post(url=url, headers=headers, params=params, json=data)
    if request.status_code == 200:
        request_data = json.loads(request.content)
        image_url = request_data[0].get("jpeg")
        image_url_alt = request_data[0].get("alt_jpeg")
        req_image = get(image_url)
        if req_image.status_code == 200:
            image_bytes = BytesIO(req_image.content)
            image_bytes.name = "photo.jpg"
            return image_bytes
        else:
            req_image = get(image_url_alt)
            if req_image.status_code == 200:
                image_bytes = BytesIO(req_image.content)
                image_bytes.name = "photo.jpg"
                return image_bytes
    return None

def openDomofon(domofon_id:int, tenant_id:int, door_id:int = 0) -> bool:
    url = f"https://domo-dev.profintel.ru/tg-bot/domo.domofon/{domofon_id}/open"
    params  = {
        "tenant_id" : tenant_id
    }
    
    data = {
        "door_id" : door_id
    }
    
    headers = {
        'x-api-key': 'SecretToken'
    }

    request = post(url=url, headers=headers, params=params, json=data)
    
    if request.status_code == 200:
        return True
    
    return False


print(getDomofonImage(36, 22051))
