
class InsufficientBalanceError(Exception):
    pass


class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient account balance"
            )

        self.balance -= amount
        print("Withdrawal successful")
        print("Remaining Balance:", self.balance)


atm = ATM(10000)

try:
    atm.withdraw(12000)

except InsufficientBalanceError as e:
    print("Error:", e)
