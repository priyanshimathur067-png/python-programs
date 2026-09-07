def attendance_report(attendance):

    present = attendance.count("P")
    absent = attendance.count("A")
    leave = attendance.count("L")

    total_days = len(attendance)

    percentage = (present / total_days) * 100

    return present, absent, leave, percentage


attendance = ["P", "P", "A", "P", "L", "P", "A"]

result = attendance_report(attendance)

print("Present:", result[0])
print("Absent:", result[1])
print("Leave:", result[2])
print("Attendance Percentage:", round(result[3], 2))