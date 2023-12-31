# Declare the class BankAccount
# Python convention is to capitalize first letter in each word of class name
class BankAccount:
    # __init__ method is like the constructor in Java
    # variales declared in the __init__ method are global and MUST
    # be refereced using self
    # self is like 'this' in Java
    # every class method in python must use self
    # constructor is a double under score
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # __str__ is like the toString() method in Java
    # it's used for debugging purposes
    def __str__(self):
        return self.account_number + ' has the balance ' + str(self.balance)


    # class methods below 
    # first parameter in class methods MUST be self
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

    def get_balance(self):
        return self.balance