employees = {
    "Rahul": [22, 25],
    "Priya": [24, 25],
    "Aman": [20, 25],
    "Neha": [23, 25]
}
for name , attendance in employees.items():
    present = attendance[0]
    total = attendance[1]
    print(f"{name} has attended {present} out of {total} days.")
    percentage = (present / total) * 100
    print(f"Attendance percentage: {percentage:.2f}%\n")