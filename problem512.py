class Circle:
    def area(self):
        print("Area of circle = 78.5")

class Square:
    def area(self):
        print("Area of square = 25")

class Rectangle:
    def area(self):
        print("Area of rectangle = 50")

c = Circle()
s = Square()
r = Rectangle()

shapes = [c, s, r]

for i in shapes:
    i.area()