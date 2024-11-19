#public
"""name = "siva"
class test():
    def __init__(self):
        self.name = "public siva"
    def m1(self):
        print(self.name)
ob = test()
ob.m1()

#protected
_name = "siva"
class test():
    def __init__(self):
        self._name = "protected siva"
    def m1(self):
        print(self._name)
ob = test()
ob.m1()
print(ob._name)"""

"""class car:
    def __init__(self):
        self.__speed = 0
    def get_speed(self):
        return self.__speed
    def set_speed(self,speed):
        if speed >=0:
            self.__speed = speed
        else:
            print("invalid speed.speed cannot be nagetive.")

r = car()
r.set_speed(-80)
print("car speed:",r.get_speed())"""

class ATM:
    def __init__(self,card_number,pin):
        self.__card_number = card_number
        self.__pin = pin
        self.__balance = 1000
    def withdraw(self,amount):
        if self.__validate_pin():
            if amount<= self.__balance:
                self.__balance -= amount
                print(f"withdrew ${amount}.remaining balance:${self.__balance}")
            else:
                print("insufficient funds.")
        else:
            print("invalid pin.")

    def deposite(self,amount):
        if self.__validate_pin():
            self.__balance += amount
            print(f"deposited ${amount}.newbalance:${self.__balance}")
        else:
            print("invalid pin.")
    def __validate_pin(self):
        pin = input("enter your pin:")
        return pin == self.__pin

siva = ATM("123456","1234")
while True:
    print("\n1.withdraw\n2.deposite\n3. check balance\n4.exit")
    choice = input("choose an option:")
    if choice == "1":
        amount = int(input("enter withdrawl amount:1000"))
        ATM.withdraw(amount)
    elif choice == "2":
        amount = int(input("enter deposite amount:2000"))
        ATM.deposite(amount)
    elif choice == "3":
        ATM.check_balance()
    elif choice == "4":
        break
    else:
        print("invalid option.")                                         


