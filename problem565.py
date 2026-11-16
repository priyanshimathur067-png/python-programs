
class Vehicle:
    def calculate_rent(self, days):
        return 0


class Car(Vehicle):
    def calculate_rent(self, days):
        return days * 1000


class Bike(Vehicle):
    def calculate_rent(self, days):
        return days * 400


class Truck(Vehicle):
    def calculate_rent(self, days):
        return days * 2000


car = Car()
bike = Bike()
truck = Truck()

days = 5

print("Car Rent:", car.calculate_rent(days))
print("Bike Rent:", bike.calculate_rent(days))
print("Truck Rent:", truck.calculate_rent(days))
