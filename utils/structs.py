class Tenant():
    _id = None
    def __init__(self, id:int) -> None:
        self._id = id
        
    def getId(self) -> int:
        return self._id
        
class Apartament():
    _id = None
    _name = None
    _adress = None
    _tenants = None
    def __init__(self, id:int, name:str, address:str, tenants:list[Tenant]) -> None:
        self._id = id
        self._name = name
        self._adress = address
        self._tenants = tenants

class Domofon():
    _id = None
    _doors = None
    _address = None
    def __init__(self, id, address:str, doors:list[tuple[str, int]]) -> None:
        self.id = id
        self.doors = doors
        self.address = address