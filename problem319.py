patients = [
    ("Rahul", 3),
    ("Priya", 1),
    ("Aman", 2),
    ("Neha", 1)
]

# 1 = highest priority
patients.sort(key=lambda x: x[1])

print("Patient Treatment Order:")

for name, priority in patients:
    print(name, "Priority:", priority)