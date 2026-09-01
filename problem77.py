def student_details(students):
    print("Student Names:")

    for name in students:
        print(name)

    highest = max(students, key=students.get)
    average = sum(students.values()) / len(students)

    print("Highest Scorer:", highest)
    print("Average Marks:", average)

    print("Students above 75:")

    for name, marks in students.items():
        if marks > 75:
            print(name)


students = {
    "Priya": 85,
    "Riya": 72,
    "Aman": 91,
    "Rahul": 65
}

student_details(students)