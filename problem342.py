attendance = [
    "P", "P", "P", "A", "P",
    "P", "P", "P", "A", "P",
    "P", "P", "P", "P", "P",
    "A", "P", "P", "P", "P",
    "P", "P", "P", "P", "A",
    "P", "P", "P", "P", "P"
]

present = attendance.count("P")

percentage = (present / len(attendance)) * 100

print("Present days:", present)
print("Attendance:", percentage, "%")

if percentage >= 90:
    print("Eligible for attendance bonus")
else:
    print("Not eligible for attendance bonus")