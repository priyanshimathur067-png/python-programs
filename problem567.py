class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Manager(Employee):

    def calculate_salary(self):
        bonus = 10000
        return self.salary + bonus


class Developer(Employee):

    def calculate_salary(self):
        bonus = 5000
        return self.salary + bonus


m1 = Manager("Rahul", 40000)
d1 = Developer("Aman", 30000)

print("Manager Salary:", m1.calculate_salary())
print("Developer Salary:", d1.calculate_salary())