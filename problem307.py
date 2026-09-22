employees = [
    ["Priya", 45000],
    ["Aman", 60000],
    ["Riya", 75000],
    ["Rahul", 50000],
    ["Neha", 90000]
]

employees.sort(key=lambda x: x[1], reverse=True)

print("Top 3 Highest Paid Employees")

for i in range(3):
    print(i + 1, employees[i][0], "-", employees[i][1])