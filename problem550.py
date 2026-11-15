
import copy

class Student:
    def __init__(self, marks):
        self.marks = marks


s1 = Student([[80, 90], [70, 85]])

s2 = copy.copy(s1)
s3 = copy.deepcopy(s1)

s1.marks[0][0] = 100

print("Original:", s1.marks)
print("Shallow Copy:", s2.marks)
print("Deep Copy:", s3.marks)
