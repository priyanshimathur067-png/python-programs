class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display_student(self):
        self.display_person()
        print("Roll No:", self.roll_no)
        print("Course:", self.course)


s1 = Student("Priyanshi", 23, 101, "MCA")
s1.display_student()