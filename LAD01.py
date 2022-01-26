class magazine:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class novel:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class comic:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class employee:
    def __init__(self, id, name, address, tel, age):
        self.id = id
        self.name = name
        self.address = address
        self.tel = tel
        self.age = age

magazine1 = magazine("001", "hobby toy", 199 )
print(magazine1.id)

novel1 = novel("001", "banana", 2500 )
print(novel1.name)

comic1 = comic("001", "marvel", 755 )
print(comic1.price)

employee1 = employee("001", "dew", "130 moo 99","0955555555", "22")
print(employee1.tel)


