class Person:
    def display(self):
        print("I am a person")

class Student(Person):
    def display(self):
        super().display()
        print("I am a student")

class Teacher(Person):
    def display(self):
        super().display()
        print("I am a teacher")

s = Student()
t = Teacher()

s.display()
print()
t.display()