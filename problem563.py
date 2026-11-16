
class Payment:
    def pay(self, amount):
        print("Processing payment")


class UPIPayment(Payment):
    def pay(self, amount):
        print("UPI Payment of", amount, "successful")


class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Credit Card Payment of", amount, "successful")


class NetBankingPayment(Payment):
    def pay(self, amount):
        print("Net Banking Payment of", amount, "successful")


p1 = UPIPayment()
p2 = CreditCardPayment()
p3 = NetBankingPayment()

payments = [p1, p2, p3]
amounts = [2000, 5000, 3000]

for payment, amount in zip(payments, amounts):
    payment.pay(amount)
