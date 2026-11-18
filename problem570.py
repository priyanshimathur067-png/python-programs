class Vehicle:

    def __init__(self, name, rent):
        self.name = name
        self.rent = rent

    def calculate_rent(self, days):
        return self.rent * days


class Car(Vehicle):

    def calculate_rent(self, days):
        return (self.rent * days) + 500


class Bike(Vehicle):

    def calculate_rent(self, days):
        return self.rent * days


c1 = Car("Swift", 2000)
b1 = Bike("Honda", 500)

print("Car Rent:", c1.calculate_rent(3))
print("Bike Rent:", b1.calculate_rent(3))