"""class animal:
    def __init__(self,name):
        self.name = name
    def speak(self,sound):
        self.sound = sound

class dog(animal):
    def speak(self):
        print(self.name)
        print("bark")

p = dog("titu")
p.speak()  """

"""class teacher:
    def m1(self,subject):
        self.subject = subject
class reseacher:
    def m2(self,feild):
        self.feild = feild
class teachingreseacher(teacher,reseacher):
    def m3(self):
        print(self.subject)
        print(self.feild)

r = teachingreseacher()
r.m1("math")
r.m2("aerospace")
r.m3()
"""
"""class bird:
    def m1(self,species):
        self.species = species
class flyable:
    def fly(self,flying):
        self.flying = flying
class eagle(bird,flyable):
    def disply(self):
        print(self.species)
        print(self.flying)
s = eagle()
s.m1("cornivous")
s.fly("high")
s.disply()"""

"""class person:
    def m1(self,name,age):
        self.name = name
        self.age = age

class employee(person):
    def m2(self,salary):
        self.salary = salary
        print(self.name)
        print(self.age)


class manager(employee):
    def m3(self,department):
        self.department = department
        print(self.salary)
        print(self.department)

s = manager()
s.m1("siva",23)
s.m2(50000)
s.m3("it") """

"""class employee:
    def m1(self):
        self.name = "siva"
        self.age = 23
        print(self.name)
        print(self.age)
        
class developer(employee):
    def m2(self,name,age,programming_language):
        self.programming_language = programming_language
        print(self.name)
        print(self.age)
        print(self.programming_language)
class manager(employee):
    def m3(self,name,age,team_size):
        self.team_size = team_size
        print(self.name)
        print(self.age)
        print(self.team_size)
class intern(developer):
    def m4(self,internship_duration):
        self.internship_duration = internship_duration
        print(self.internship_duration)
r1 = developer()
r1.m2("siva",23,"python")
r2 = manager()
r2.m3("siva",23,30)
r3 = intern()
r3.m4("8months")    """

"""class vehicle:
    def __init__(self):
        self.brand = "tata"
        self.model = 2015
class car(vehicle):
    def m1(self):
        print(self.brand)
        print(self.model)
        self.num_doors = 4
        print(self.num_doors)
class bike(vehicle):
    def m2(self):
        print(self.brand)
        print(self.model)
        self.type = "heavy_vehicle"
        print(self.type)

r1 = car()
r1.m1()
r2 = bike()
r2.m2()""" 

"""class device:
    def m1(self,name):
        self.name = name
        print(self.name)
class phone(device):
    def m2(self,phone_number):
        self.phone_number = phone_number
        print(self.phone_number)
class tablet(device):
    def m3(self,screen_size):
        self.scree_size = screen_size
        print(self.scree_size)
class smart_phone(phone,tablet):
    def m4(self,os):
        self.os = os
        print(self.os)

k = phone()
k.m1("oppo")
k.m2(7337558583)

r = tablet()
r.m1("vivo")
r.m3(6)

i = smart_phone()
i.m2(999999999999)
i.m3(8)
i.m4("linux_os")"""




