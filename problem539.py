
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks must be between 0 and 100")

    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")


s1 = Student("Priya", 85)

print("Marks:", s1.marks)
s1.result()

s1.marks = 95
print("Updated Marks:", s1.marks)
