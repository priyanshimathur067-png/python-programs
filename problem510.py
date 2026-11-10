class Car:
    def start(self):
        print("Car starts with a key")

class Bike:
    def start(self):
        print("Bike starts with a button")

def vehicle_start(obj):
    obj.start()

c = Car()
b = Bike()

vehicle_start(c)
vehicle_start(b)