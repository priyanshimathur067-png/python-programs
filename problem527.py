class Company:
    def __init__(self, name):
        self.name = name

    class Employee:
        def __init__(self, emp_name, salary):
            self.emp_name = emp_name
            self.salary = salary

c = Company("Google")
e = c.Employee("Rahul", 50000)

print(c.name)
print(e.emp_name)
print(e.salary)