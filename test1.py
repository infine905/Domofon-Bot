from requests import post, get
import json

class Tenant():
    _id = None
    def __init__(self, id:int) -> None:
        self._id = id
        
    def __repr__(self):
        return f"Tenant(id={self._id})"
    
    def getId(self) -> int:
        return self._id

    
class Apartment():
    _id = None
    _name = None
    _address = None
    _tenants = None
    def __init__(self, id:int, name:str, address:str, tenants:list[Tenant]) -> None:
        self._id = id
        self._name = name
        self._address = address
        self._tenants = tenants
        
    def __repr__(self):
        return f"Apartment(id={self._id}, name='{self._name}', address='{self._address}', tenants={self._tenants})"
    
class Domofon():
    _id = None
    _name = None
    _address = None
    def __init__(self, id:int, name:str, address:str) -> None:
        self._id = id
        self._name = name
        self._address = address
        
    def __repr__(self):
        return f"Domofon(id={self._id}, name='{self._name}', address='{self._address}')" 
    
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

def openDomofon(domofon_id:int, tenant_id:int, door_id:int = 0) -> bool:
    url = f"https://domo-dev.profintel.ru/tg-bot/domo.domofon/{domofon_id}/open"
    data  = {
        "tenant_id" : tenant_id
    }
    
    json_data = {
        "door_id" : door_id
    }
    
    headers = {
        'x-api-key': 'SecretToken'
    }

    request = post(url=url, headers=headers, params=data, json=json_data)
    
    if request.status_code == 200:
        return True
    
    return False    