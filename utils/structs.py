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