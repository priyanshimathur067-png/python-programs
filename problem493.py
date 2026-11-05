class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def calculate_area(obj):
    print("Area:", obj.area())


r1 = Rectangle(10, 5)
c1 = Circle(7)
s1 = Square(4)

calculate_area(r1)
calculate_area(c1)
calculate_area(s1)