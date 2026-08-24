def student_marks(name, **subjects):
    print("Student:", name)

    total = sum(subjects.values())
    percentage = total / len(subjects)

    print("Total:", total)
    print("Percentage:", percentage)


student_marks(
    "Priyanshi",
    Python=85,
    Java=78,
    SQL=90,
    HTML=88
)