employees = [
    ("Aman", 35000),
    ("Priya", 45000),
    ("Rahul", 30000),
    ("Neha", 50000)
]

employees.sort(key=lambda x: x[1], reverse=True)

for name, salary in employees:
    print(name, salary)

salaries = [salary for name, salary in employees]

print("Highest Salary:", max(salaries))
print("Lowest Salary:", min(salaries))
print("Average Salary:", sum(salaries) / len(salaries))