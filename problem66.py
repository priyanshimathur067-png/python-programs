employees = ["Priyanshi", "Khushi", "Rahul", "Aman"]


def check_employee(func):
    def wrapper(name):
        if name in employees:
            return func(name)
        else:
            print("Employee not registered!")

    return wrapper


@check_employee
def mark_attendance(name):
    print(f"Attendance marked for {name}")


name = input("Enter employee name: ")

mark_attendance(name)