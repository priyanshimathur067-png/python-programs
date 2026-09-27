employees = {
    "Aman": "Present",
    "Riya": "Absent",
    "Karan": "Present",
    "Neha": "Present",
    "Vikas": "Absent",
    "Pooja": "Present"
}

present = []
absent = []

for name, status in employees.items():
    if status == "Present":
        present.append(name)
    else:
        absent.append(name)

print("Present:", present)
print("Absent:", absent)

attendance_percentage = (len(present) / len(employees)) * 100

print("Attendance:", attendance_percentage, "%")