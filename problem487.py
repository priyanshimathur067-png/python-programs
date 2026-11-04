class Shape:
    def area(self):
        print("Calculating area")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Rectangle Area:", self.length * self.breadth)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area:", 3.14 * self.radius * self.radius)


r1 = Rectangle(10, 5)
r1.area()

c1 = Circle(7)
c1.area()