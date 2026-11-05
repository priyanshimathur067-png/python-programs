class Payment:
    def pay(self):
        print("Making payment")


class CreditCard(Payment):
    def pay(self):
        print("Payment through Credit Card")


class UPI(Payment):
    def pay(self):
        print("Payment through UPI")


class Cash(Payment):
    def pay(self):
        print("Payment through Cash")


p1 = CreditCard()
p2 = UPI()
p3 = Cash()

p1.pay()
p2.pay()
p3.pay()