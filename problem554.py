
class Student:
    __slots__ = ("name", "marks")

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Priya", 90)

s1.display()

try:
    s1.age = 23
except AttributeError as e:
    print("Error:", e)
