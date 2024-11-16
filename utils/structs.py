class Tenant():
    def __init__(self, id:int) -> None:
        self.id = id
        
class Apartament():
    def __init__(self, id:int, name:str, address:str, tenants:list[Tenant]) -> None:
        self.id = id
        self.name = name
        self.adress = address
        self.tenants = tenants

class Domofon():
    def __init__(self, id, address:str, doors:list[tuple[str, int]]) -> None:
        self.id = id
        self.address = address
        self.doors = doors