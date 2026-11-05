class Product:
    def __init__(self, price):
        self.price = price

    def __mul__(self, quantity):
        return self.price * quantity
p1 = Product(100)

print(p1 * 5)