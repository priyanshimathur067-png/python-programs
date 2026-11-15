
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    department: str
    monthly_salary: int

    def annual_salary(self):
        return self.monthly_salary * 12


e1 = Employee("Priya", "IT", 30000)

print(e1)
print("Annual Salary:", e1.annual_salary())
