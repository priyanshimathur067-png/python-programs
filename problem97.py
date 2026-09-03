employees = [
    ("Amit", 30000),
    ("Priya", 45000),
    ("Riya", 25000),
    ("Rahul", 50000)
]

result = sorted(employees, key=lambda x: x[1])

print(result)