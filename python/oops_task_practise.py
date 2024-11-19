"""from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class dog(animal):
    def make_sound(self):
        print("woof")

class cat(animal):
    def make_sound(self):
        print("meow")

class cow(animal):
    def make_sound(self):
        print("moo")

def play_sound(animal):
        animal.make_sound()

p = dog()
t = cat()
s = cow()
play_sound(p)
play_sound(s)
play_sound(t)"""

"""from abc import ABC,abstractmethod
class people(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class family(people):
    def make_sound(self):
        print("chinna")

class neighbours(people):
    def make_sound(self):
        print("abbai")

class friends(people):
    def make_sound(self):
        print("mama")

def play_sound(people):
    people.make_sound()

s = family()
p = neighbours()
r = friends()
play_sound(s)                                
play_sound(r)"""

#Create an abstract class BankAccount with methods deposit(), withdraw(), and get_balance(). Then, create two subclasses:

#SavingsAccount, where the withdraw() method ensures that the balance cannot go below $500.
#CurrentAccount, where the withdraw() method allows the balance to go negative (up to $1000 overdraft).
#Ensure that only deposit() and withdraw() are exposed to the user, and the balance is encapsulated (hidden).
"""from abc import ABC,abstractmethod
class bankaccount(ABC):
    @abstractmethod
    def __init__(self,intial_balance=0):
        self._balance = intial_balance

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def get_balance(self,amount):
        pass

class savingaccount(bankaccount):
    def __init__(self, intial_balance=0):
        super().__init__(intial_balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("deposit amount must be positive value.")

    def withdraw(self, amount):
        if amount>0:
           if self._balance -amount >= 500:
            self._balance -= amount
        else:
            raise ValueError("cannot withdraw : minimum balance is 500.")
    else:
    raise ValueError("with drawal amount must be positive.")


    def get_balance(self):
        return self._balance

class currentaccount(bankaccount):
    def __init__(self, intial_balance=0):
        super().__init__(intial_balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise TypeError("deposit amount must be positive value")

    def withdraw(self, amount):
        if amount >0:
           if self._balance - amount >= -1000:
            self._balance -= amount

        else:
            raise ValueError("with draw limit is up to -1000 only")

    def get_balance(self):
        return self._balance"""

"""class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: ${self.salary:.2f}"

    def get_salary(self):
        return self.salary

    def increase_salary(self, percent):
        if percent > 0:
            self.salary += self.salary * (percent / 100)
        else:
            raise ValueError("Increase percentage must be positive.")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"{super().get_details()}, Department: {self.department}"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_details(self):
        return f"{super().get_details()}, Programming Language: {self.programming_language}"""

class vehical:
    def get_info(self,brand,year):
        self.brand = brand
        self.year = year

class car(vehical):
    def get_info(self, brand, year,no_of_doors):
        self.no_of_doors = no_of_doors
        self.brand = brand
        self.year = year
        print(self.brand)
        print(self.year)
        print(self.no_of_doors)

class motorcycle(vehical):
    def get_info(self, brand, year,has_sidecar):
        self.has_sidecar = has_sidecar
        self.brand = brand
        self.year = year
        print(self.brand)
        print(self.year)
        print(has_sidecar)

s = car()
s.get_info("fortuner",2024,5)
r = motorcycle()
r.get_info("royalenfeild",2024,"none")        
                         






        
    
            

            