class Product:
    def __init__(self, price):
        self.__price = price

    def set_price(self, price):
        if price > 0:
            self.__price = price
            print("Price updated")
        else:
            print("Invalid price")

    def get_price(self):
        print("Price =", self.__price)


p = Product(500)

p.set_price(800)
p.set_price(-100)

p.get_price()