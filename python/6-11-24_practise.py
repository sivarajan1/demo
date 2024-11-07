#inheritance,single:
 
"""class p:
    a = "sivajanga"
    def m1(self):
        print("instance method in parent class")
 
class c(p):
   b = " manager"
   def m2(self):
       print("instance method in child class")

s = c()
s.m1()
s.m2() 
print(c.a+c.b)"""

"""class bikes:
    def __init__(self,hero,honda,royalenfeild):
        self.hero = hero
        self.honda = honda
        self.royalenfeild = royalenfeild

class features(bikes):
    def m1(self,milage,model):
        self.milage = milage
        self.model = model
        print(self.hero)
        print(self.honda)
        print(self.royalenfeild)
        print(self.milage)
        print(self.model)

s = features("glamar","unicorn","bullet")
s.m1("70kmpl",2024)"""

#multilevel
class consitable:
    def m1(self):
        self.commition = 10000

class asi(consitable):
    def m2(self):
        print(self.commition)
        self.commition = 20000

class si(asi):
    def m3(self):
        print(self.commition)
        self.commition = 30000
        print(self.commition)

r = si()
r.m1()
r.m2()
r.m3()

class f:
    def m1(self):
        self.nature = "hardworking"

class m:
    def m2(self):
        self.nature1 = "caring"

class c(f,m):
    def m3(self):
        print(self.nature)
        print(self.nature1)

r = c()
r.m1()
r.m2()
r.m3()

class company:
    def _init_(self):
        self.salary = 40000

class emp1(company):
    def m1(self):
        print(self.salary -20000)

class emp2(company):
    def m2(self):
        print(self.salary - 20000)

r1 = emp1()
r1.m1()
r2 = emp2()
r2.emp2()        

