
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def calculate_rent(self, days):
        pass


class Car(Vehicle):
    def calculate_rent(self, days):
        return days * 2000


class Bike(Vehicle):
    def calculate_rent(self, days):
        return days * 500

car = Car()
bike = Bike()

print("Car Rent:", car.calculate_rent(3))
print("Bike Rent:", bike.calculate_rent(3))
