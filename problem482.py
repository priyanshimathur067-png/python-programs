class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department, bonus):
        super().__init__(emp_id, name, salary)
        self.department = department
        self.bonus = bonus

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Total Salary:", self.salary + self.bonus)


m1 = Manager(101, "Rahul", 40000, "IT", 10000)
m1.display()