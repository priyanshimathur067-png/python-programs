
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        if price > 0:
            self.products.append((name, price))
            print(name, "added to cart")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed")
                return
        print("Product not found")

    def calculate_total(self):
        total = sum(price for name, price in self.products)

        discount = 0
        if total > 5000:
            discount = total * 0.10

        print("Total:", total)
        print("Discount:", discount)
        print("Final Amount:", total - discount)

    def display_products(self):
        for name, price in self.products:
            print(name, ":", price)


cart = ShoppingCart()

cart.add_product("Laptop", 40000)
cart.add_product("Mouse", 1000)

cart.display_products()
cart.calculate_total()
