# Wrapping of data and methods into a single unit.
# making the data private to restrict access.
#getter and setter methods are used to access and modify the private variable.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner        # public
        self.__balance = balance  # private variable

    def show_balance(self):
        print(f"Balance for {self.owner}: ₹{self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

# Usage
acc = Account("Rahul", 1000)
acc.show_balance()
acc.deposit(500)
acc.show_balance()
acc.withdraw(2000)  # Tries to withdraw more than balance
acc.show_balance()

# Try accessing private variable directly
# print(acc.__balance)  # Will raise AttributeError

print(acc._Account__balance)  # Name mangling
# Accessing private variable using name mangling
