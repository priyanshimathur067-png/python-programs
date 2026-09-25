students = {
    "Rahul": [78, 82, 69, 90],
    "Priya": [88, 91, 84, 79],
    "Aman": [55, 61, 58, 64]
}

results = {}

for name, marks in students.items():

    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"

    results[name] = {
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

for name, data in results.items():
    print(name)
    print("Total:", data["total"])
    print("Percentage:", data["percentage"])
    print("Grade:", data["grade"])
    print()

top_student = max(
    results,
    key=lambda name: results[name]["percentage"]
)

print("Top student:", top_student)

print("Failed students:")

for name, data in results.items():
    if data["grade"] == "F":
        print(name)