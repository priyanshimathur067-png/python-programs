
class Discount:
    def calculate_discount(self, amount):
        return 0


class RegularCustomer(Discount):
    def calculate_discount(self, amount):
        return amount * 0.05


class PremiumCustomer(Discount):
    def calculate_discount(self, amount):
        return amount * 0.20


regular = RegularCustomer()
premium = PremiumCustomer()

amount = 10000

print("Regular Discount:", regular.calculate_discount(amount))
print("Premium Discount:", premium.calculate_discount(amount))

print("Regular Final Bill:", amount - regular.calculate_discount(amount))
print("Premium Final Bill:", amount - premium.calculate_discount(amount))
