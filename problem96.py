students = [
    ("Priya", 85),
    ("Rahul", 72),
    ("Anu", 95),
    ("Riya", 80)
]

result = sorted(students, key=lambda x: x[1], reverse=True)

print(result)