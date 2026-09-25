salaries = {
    "Rahul": 35000,
    "Priya": 42000,
    "Aman": 28000,
    "Neha": 50000,
    "Ravi": 32000
}

total_salary = sum(salaries.values())
average_salary = total_salary / len(salaries)

highest_salary = max(salaries.values())
lowest_salary = min(salaries.values())

highest_employee = max(salaries, key=salaries.get)
lowest_employee = min(salaries, key=salaries.get)

print("Total salary expense:", total_salary)
print("Average salary:", average_salary)

print("Highest salary:", highest_salary)
print("Highest paid employee:", highest_employee)

print("Lowest salary:", lowest_salary)
print("Lowest paid employee:", lowest_employee)

print("\nEmployees earning above average:")

for name, salary in salaries.items():
    if salary > average_salary:
        print(name, ":", salary)