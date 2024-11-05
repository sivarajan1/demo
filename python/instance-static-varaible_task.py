class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_gender(self):
        return self.gender
    
    def update_age(self,new_age):
        self.age=new_age

    def display_info(self):
        print(f"name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")


person1 = Person("siva",23,"male")
person2 = Person("balu",21,"male")
person3 = Person("jaswanth",24,"male")
person4 = Person("sai",20,"male")

person1.display_info()
print()
person2.display_info()
print()
person3.display_info()
print()
person3.update_age(23)
print()
person4.display_info()
print()
