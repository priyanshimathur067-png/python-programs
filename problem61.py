def validate_patient(func):
    def wrapper(name, age):
        if age > 0:
            return func(name, age)
        else:
            print("Invalid age!")
    return wrapper


@validate_patient
def book_appointment(name, age):
    print(f"Appointment booked for {name}")
    print("Patient age:", age)


name = input("Enter patient name: ")
age = int(input("Enter age: "))

book_appointment(name, age)