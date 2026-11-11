class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def display(self):
        print("Balance =", self.__balance)


b = BankAccount(5000)

b.deposit(2000)
b.display()