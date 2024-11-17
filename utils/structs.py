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