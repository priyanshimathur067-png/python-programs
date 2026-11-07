class Car:
    def __init__(self, speed):
        self.__speed = 0
        self.set_speed(speed)

    def set_speed(self, speed):
        if 0 <= speed <= 200:
            self.__speed = speed
        else:
            print("Invalid Speed")

    def get_speed(self):
        return self.__speed


c1 = Car(100)

print("Speed:", c1.get_speed())

c1.set_speed(150)

print("Updated Speed:", c1.get_speed())