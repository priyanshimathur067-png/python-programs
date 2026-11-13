
class Product:
    total_products = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.total_products += 1

    def stock_value(self):
        return self.price * self.quantity

    @classmethod
    def show_total(cls):
        print("Total Products:", cls.total_products)


p1 = Product("Laptop", 50000, 5)
p2 = Product("Mouse", 500, 10)
p3 = Product("Keyboard", 1000, 4)

print("Laptop Stock Value:", p1.stock_value())
print("Mouse Stock Value:", p2.stock_value())
print("Keyboard Stock Value:", p3.stock_value())

Product.show_total()
