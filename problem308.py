students = [
    ["Priya", 92],
    ["Aman", 76],
    ["Riya", 98],
    ["Rahul", 85],
    ["Neha", 89]
]

students.sort(key=lambda x: x[1], reverse=True)

print("Attendance Ranking")
print("------------------")

for i, student in enumerate(students):
    print(i + 1, student[0], "-", student[1], "%")