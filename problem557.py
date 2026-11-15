
class Product:
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.product_id == other.product_id


p1 = Product(101, "Laptop")
p2 = Product(101, "Gaming Laptop")
p3 = Product(102, "Mouse")

print(p1 == p2)
print(p1 == p3)
