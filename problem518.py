class Product:
    def __init__(self, price):
        self.price = price

    def __mul__(self, other):
        return self.price * other.price

p1 = Product(100)
p2 = Product(5)

print(p1 * p2)