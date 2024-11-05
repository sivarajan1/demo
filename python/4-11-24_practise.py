"""class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

    def m1(self,salary):
        self.salary = salary
        print(self.name)
        print(self.age)
        print(self.salary)

p = person ("siva",23)
p.m1(50000)"""

"""class subject:
    def _init_(self,math,physics):
        self.math = math
        self.physics = physics

        def m1(self,chemistry):
            self.chemistry = chemistry
            print(self.math)
            print(self.physics)
            print(self.chemistry)

s = subject ()
s.m1(78,65,998)"""

#class method
"""class person:
    salary = 50000
    @classmethod
    def m1(cls,name,age):
        cls.company = "wipro"
        print(name)
        print(age)
        print(person.salary)
        print(cls.company)
p=person()
p.m1("sai",24)"""

"""class marks:
    @classmethod
    def m1(cls,math,physics):
        marks.chemistry = 46
        cls.telugu = 87
        print(math)
        print(physics)
        print(marks.chemistry)
        print(cls.telugu)

s = marks()
s.m1(56,86) """

"""class collage:
    @classmethod
    def m1(cls,name,rollno):
        cls.branch = "mechannical"
        print(name)
        print(rollno)
        print(cls.branch)

c = collage()
c.m1("siva",191)  """

#static method

class test:
    @staticmethod
    def m2():
        a = 400
        b = 500
        print(a+b)

t = test()
t.m2()

class details:
    @staticmethod
    def m1():
        name = "siva"
        age = 23
        height = 5.11
        print(name)
        print(age)
        print(height)

d = details()
d.m1()        

