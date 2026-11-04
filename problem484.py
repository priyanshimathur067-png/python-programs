class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def account_type(self):
        print("Account Type: Savings")


class CurrentAccount(BankAccount):
    def account_type(self):
        print("Account Type: Current")


s1 = SavingsAccount("Priya", 50000)
s1.display_balance()
s1.account_type()

print()

c1 = CurrentAccount("Rahul", 80000)
c1.display_balance()
c1.account_type()