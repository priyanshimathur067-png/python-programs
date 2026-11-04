class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):
    def __init__(self, name, salary, language, bonus):
        super().__init__(name, salary)
        self.language = language
        self.bonus = bonus

    def display(self):
        print("Name:", self.name)
        print("Basic Salary:", self.salary)
        print("Language:", self.language)
        print("Bonus:", self.bonus)
        print("Total Salary:", self.salary + self.bonus)


d1 = Developer("Priya", 50000, "Python", 10000)
d1.display()