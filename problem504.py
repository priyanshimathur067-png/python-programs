class Mobile:
    def __init__(self, brand, price):
        self.__brand = brand
        self.__price = price

    def display(self):
        print("Brand:", self.__brand)
        print("Price:", self.__price)


m1 = Mobile("Apple", 70000)
m1.display()