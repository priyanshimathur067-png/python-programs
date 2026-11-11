class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def display(self):
        print("Name =", self.__name)
        print("Salary =", self.__salary)


e = Employee("Rahul", 30000)
e.display()