# Wrapping of data and methods into a single unit.
# Use private/protected/public access modifiers.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
# print(acc.__balance)  # Error: AttributeError
