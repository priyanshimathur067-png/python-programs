class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


s1 = Student("Priya", 90)
s2 = Student("Rahul", 80)

print(s1 > s2)