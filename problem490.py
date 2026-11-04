class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no


class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id


class TeachingAssistant(Student, Employee):
    def __init__(self, name, age, roll_no, emp_id, department):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.emp_id = emp_id
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)


t1 = TeachingAssistant("Priya", 23, 101, 501, "Computer Science")
t1.display()