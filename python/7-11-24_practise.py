class company:
    def __init__(self,name,purpose):
        self.name = name
        self.purpose = purpose

    def disply(self):
        print(self.name)
        print(self.purpose)

class product(company):
    def __init__(self, name, purpose,groceryes,price):
        super().__init__(name, purpose)
        self.groceryes = groceryes
        self.price = price

    def disply(self):
        super().disply()
        print(self.groceryes)
        print(self.price)

c = product("blinkit","home_delivery","vegetables",350)
c.disply()

class party:
    def __init__(self,symbol,moto):
        self.symbol = symbol
        self.moto = moto

    def disply(self):
        print(self.symbol)
        print(self.moto)

class mla(party):
    def __init__(self, symbol, moto,name,constituency):
        super().__init__(symbol, moto)
        self.name = name
        self.constituency = constituency

    def disply(self):
        super().disply()
        print(self.name)
        print(self.constituency)

s = mla("gun","serve_to_people","siva","vijayawada")
s.disply()
print("----------------------------------------------------------")

class school:
    salary = 30000
    def __init__(self):
        self.fees = 100000

class claes(school):
    def m1(self):
        print(self.salary)
        print(self.fees)
        print(super().salary)
        #print(super().fees)

k = claes()
k.m1()
print("---------------------------------------------------------------------------")

class p:
    def __init__(self):
        print("parent class constructor")
    def m1(self):
        print("parent class instance method")
    @classmethod
    def m2(cls):
        print("parent class and class method")
    @staticmethod
    def m3():
        print("parent class and static method")

class c(p):
    def __init__(self):
        super().__init__
        super().m1()
        super().m2()
        super().m3()

    def m4(self):
        super().__init__
        super().m1()
        super().m2()
        super().m3()

s = c()
s.m4()

l = [1,2,3,4,4,5,5,6,7,7,8]
s = list(dict.fromkeys(l))
print(s)

l = [1,2,3,4,5,6,7,8]      
for s in (l):
     if s%2==0:
        print(s)

l = [1,2,3,4,5,6,7,8,89]
even = list(filter(lambda s:s%2==0,l))
print(even)

t = (1,2,3,4,5,6,7,8)
second = t[3]
print(second)

s = (1,2,3,4,5,6,7)
length = len(s)
print(length)














