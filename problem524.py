class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display(self):
        print("Balance =", self.__balance)


b = Bank(10000)

b.withdraw(3000)
b.withdraw(9000)
b.display()