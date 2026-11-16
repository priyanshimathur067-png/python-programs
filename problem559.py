
class BankAccount:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.__balance)


b1 = BankAccount("Priyanshi", 101, 3000)

b1.deposit(5000)
b1.withdraw(2000)
b1.display_balance()
