
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


class Developer(Employee):
    def __init__(self, name, salary, incentive):
        super().__init__(name, salary)
        self.incentive = incentive

    def calculate_salary(self):
        return self.salary + self.incentive


m1 = Manager("Priyanshi", 30000, 10000)
d1 = Developer("Rahul", 25000, 5000)

print("Manager Salary:", m1.calculate_salary())
print("Developer Salary:", d1.calculate_salary())
