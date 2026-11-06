class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary")


e1 = Employee(30000)

print("Old Salary:", e1.get_salary())

e1.set_salary(40000)

print("New Salary:", e1.get_salary())