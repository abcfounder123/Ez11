
"""

Encapsulation

1. Variable attributes
    - public
    - protected   _
    - private     __

2. Private variable attributes
    - control data by fun

3. Private variable attributes by Python style
    - @property
    - @name.getter
    - @name.setter
    - @name.deleter

-------------------------------------------------

"Normal"


class Account:
    def __init__(self):
        self.amount = 1000


user1 = Account()
print(user1.amount)

user1.amount -= 300
print(user1.amount)

-------------------------------------------------

2. Private variable attributes


class Account:
    def __init__(self, password):
        self.__amount = 1000
        self.__password = password

    def show_amount(self):
        print(self.__amount)

    def withdraw(self, amount):
        self.__amount -= amount
        
        
-------------------------------------------------
        
"Controlling data by fun"


class Account:
    def __init__(self, password):
        self.__amount = 1000
        self.__password = password

    def show_amount(self, password):
        if password == self.__password:
            print(self.__amount)

    def withdraw(self, amount, password):
        if password == self.__password:
            self.__amount -= amount
            
            
-------------------------------------------------


class Account:
    def __init__(self, name, password):
        self.__amount = 1000000
        self.user_name = name
        self.password = password

    def deposit(self, amount, password):
        if self.password == password:
            self.__amount += amount
        else:
            print("Wrong password")

    def withdraw(self, amount, password):
        if self.password == password and self.__amount >= amount and amount <= 50000:
            self.__amount -= amount
            print(f"successfully withdraw {amount}")
            print(f"Your new balance is {self.__amount}")
        else:
            print("Error")

    def show_balance(self, password):
        if self.password == password:
            return self.__amount
        else:
            return "Wrong password"


user1 = Account("Mg Mg", "123456")

user1.withdraw(30000, "123456")

-------------------------------------------------

"Test"


class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def show_price(self):
        return self.__price

    def update_price(self, price):
        if price < 0:
            print("Price should not less than 0.")
        else:
            self.__price = price
            print(f"New price of {self.name} is {self.__price}$.")

    def delete_price(self):
        ans = input("Are you sure to delete price?(y/n)\n>> ")
        if ans == "y":
            del self.__price


p1 = Product("apple", 2)
print(p1.show_price())
p1.update_price(1)
p1.delete_price()

-------------------------------------------------

3. Private variable attributes by Python style
    - @property
    - @name.getter
    - @name.setter
    - @name.deleter
    

class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            print("Price should not less than 0.")
        else:
            self.__price = price
            print(f"New price of {self.name} is {self.__price}$.")

    @price.deleter
    def price(self):
        ans = input("Are you sure to delete price?(y/n)\n>>")
        if ans == "y":
            del self.__price


p1 = Product("apple", 2)
print(p1.price)
p1.price += 1
del p1.price

-------------------------------------------------

"""


