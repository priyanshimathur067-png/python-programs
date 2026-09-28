patients = []

while True:

    print("\n1. Add Patient")
    print("2. Call Patient")
    print("3. Show Queue")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        name = input("Enter patient name: ")
        patients.append(name)

        print("Patient added.")

    elif choice == 2:

        if len(patients) > 0:
            patient = patients.pop(0)
            print("Now attending:", patient)
        else:
            print("No patients waiting.")

    elif choice == 3:

        print("Waiting Patients:", patients)

    elif choice == 4:
        break

    else:
        print("Invalid choice.")