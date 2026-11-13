
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

    def display(self):
        print(self.name, self.balance)


a1 = BankAccount("Rahul", 5000)
a2 = BankAccount("Priya", 7000)

total = a1 + a2

print("Combined Balance:", total)
