total_classes = int(input("Enter total classes held: "))
attended_classes = int(input("Enter classes attended: "))

attendance = (attended_classes / total_classes) * 100

print("Attendance:", round(attendance, 2), "%")

if attendance >= 75:
    print("Eligible for examination.")
else:
    shortage = 75 - attendance
    print("Not eligible.")
    print("Attendance shortage:", round(shortage, 2), "%")