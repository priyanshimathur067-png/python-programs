class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_product(self, name, price):
        self.items.append((name, price))
        print(name, "added to cart")

    def remove_product(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                print(name, "removed")
                return

        print("Product not found")

    def total_bill(self):
        total = 0

        for item in self.items:
            total += item[1]

        print("Total Bill:", total)


cart = ShoppingCart()

cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 500)
cart.add_product("Keyboard", 1000)

cart.remove_product("Mouse")
cart.total_bill()