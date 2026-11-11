class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        print("Marks =", self.__marks)


s = Student()

s.set_marks(85)
s.get_marks()