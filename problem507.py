class Product:
    def __init__(self, name, stock):
        self.__name = name
        self.__stock = stock

    def add_stock(self, quantity):
        if quantity > 0:
            self.__stock += quantity
            print("Stock Added")

    def sell_product(self, quantity):
        if quantity <= self.__stock and quantity > 0:
            self.__stock -= quantity
            print("Product Sold")
        else:
            print("Insufficient Stock")

    def display(self):
        print("Product:", self.__name)
        print("Available Stock:", self.__stock)


p1 = Product("Laptop", 20)

p1.add_stock(10)
p1.sell_product(5)
p1.display()