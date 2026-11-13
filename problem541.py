
class Department:
    def __init__(self, dept):
        self.dept = dept


class Salary:
    def __init__(self, salary):
        self.salary = salary


class Employee(Department, Salary):
    def __init__(self, name, dept, salary):
        Department.__init__(self, dept)
        Salary.__init__(self, salary)
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("Department:", self.dept)
        print("Salary:", self.salary)


e1 = Employee("Priya", "IT", 45000)
e1.display()
