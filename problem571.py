class Restaurant:

    def __init__(self):
        self.menu = {
            "Pizza": 200,
            "Burger": 100,
            "Pasta": 150
        }

    def place_order(self, item, quantity):
        if item in self.menu:
            total = self.menu[item] * quantity
            print("Order:", item)
            print("Quantity:", quantity)
            print("Total:", total)
        else:
            print("Item not available")


r1 = Restaurant()

r1.place_order("Pizza", 2)
r1.place_order("Burger", 3)