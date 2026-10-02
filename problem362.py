def medicine_reminder(medicine, time):
    return f"Reminder: Take {medicine} at {time}."


medicine = input("Enter medicine name: ")
time = input("Enter medicine time: ")

print(medicine_reminder(medicine, time))