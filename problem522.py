class Mobile:
    def __init__(self, price):
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        print("Mobile price =", self.__price)


m = Mobile(20000)

m.get_price()
m.set_price(25000)
m.get_price()