class Employee:
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, salary, bonus):
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self):
        print("Full Time Salary:", self.salary + self.bonus)


class PartTimeEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        print("Part Time Salary:", self.hours * self.rate)


class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        print("Intern Stipend:", self.stipend)


e1 = FullTimeEmployee(40000, 5000)
e2 = PartTimeEmployee(100, 200)
e3 = Intern(10000)

e1.calculate_salary()
e2.calculate_salary()
e3.calculate_salary()