class School:
    def __init__(self, school_name):
        self.school_name = school_name


class Teacher(School):
    def __init__(self, school_name, teacher_name, subject):
        super().__init__(school_name)
        self.teacher_name = teacher_name
        self.subject = subject


class Student(Teacher):
    def __init__(self, school_name, teacher_name, subject,
                 student_name, marks):
        super().__init__(school_name, teacher_name, subject)
        self.student_name = student_name
        self.marks = marks

    def display(self):
        print("School:", self.school_name)
        print("Teacher:", self.teacher_name)
        print("Subject:", self.subject)
        print("Student:", self.student_name)
        print("Marks:", self.marks)


s1 = Student("ABC School", "Amit", "Python", "Priya", 90)
s1.display()