class Shopping:
    class Product:
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def total_price(self):
            return self.price * self.quantity

s = Shopping()
p = s.Product("Laptop", 50000, 2)

print("Product:", p.name)
print("Total:", p.total_price())