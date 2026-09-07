def calculate_fine(days_late):

    if days_late <= 0:
        return 0
    elif days_late <= 5:
        return days_late * 2
    elif days_late <= 10:
        return days_late * 5
    else:
        return days_late * 10


days = int(input("Days late: "))

print("Fine:", calculate_fine(days))