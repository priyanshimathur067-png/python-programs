def attendance_tracker(attendance):

    print("Employee Attendance Report")

    for name, days in attendance.items():

        present = days.count("P")

        total_days = len(days)

        percentage = (present / total_days) * 100

        print(name, ":", percentage, "%")

        if percentage < 75:
            print("Low Attendance:", name)

attendance = {
    "Riya": ["P", "P", "A", "P", "P"],
    "Aman": ["P", "A", "A", "P", "A"],
    "Priya": ["P", "P", "P", "P", "A"]
}

attendance_tracker(attendance)