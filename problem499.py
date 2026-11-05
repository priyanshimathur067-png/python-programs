class Vehicle:
    def speed(self):
        print("Vehicle has different speeds")


class Car(Vehicle):
    def speed(self):
        print("Car speed: 120 km/h")


class Bike(Vehicle):
    def speed(self):
        print("Bike speed: 80 km/h")


class Train(Vehicle):
    def speed(self):
        print("Train speed: 200 km/h")


c1 = Car()
b1 = Bike()
t1 = Train()

c1.speed()
b1.speed()
t1.speed()