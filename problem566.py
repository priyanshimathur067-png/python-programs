class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.__balance)


b1 = BankAccount("Priya", 10000)

b1.deposit(2000)
b1.withdraw(3000)
b1.check_balance()