students = [
    ("Priya", 85),
    ("Rahul", 92),
    ("Aman", 78),
    ("Neha", 95),
    ("Riya", 88)
]

students.sort(key=lambda x: x[1], reverse=True)

print("Student Ranking:")

for name, marks in students:
    print(name, marks)

print("\nTop 3 Students:")

for student in students[:3]:
    print(student)