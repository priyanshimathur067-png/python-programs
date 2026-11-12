class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name

    class Account:
        def __init__(self, holder, balance):
            self.holder = holder
            self.balance = balance

b = Bank("SBI")
a = b.Account("Priyanshi", 25000)

print(b.bank_name)
print(a.holder)
print(a.balance)