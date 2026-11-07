class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def set_dimensions(self, length, breadth):
        if length > 0 and breadth > 0:
            self.__length = length
            self.__breadth = breadth
        else:
            print("Invalid Dimensions")

    def get_area(self):
        return self.__length * self.__breadth


r1 = Rectangle(10, 5)

print("Area:", r1.get_area())

r1.set_dimensions(20, 10)

print("Updated Area:", r1.get_area())