class Cash:
    def payment(self):
        print("Payment using cash")

class UPI:
    def payment(self):
        print("Payment using UPI")

class Card:
    def payment(self):
        print("Payment using card")

def make_payment(obj):
    obj.payment()

c = Cash()
u = UPI()
d = Card()

make_payment(c)
make_payment(u)
make_payment(d)