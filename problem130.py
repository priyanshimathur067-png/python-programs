def find_file(folder, target):
    for item in folder:

        if isinstance(item, str):
            if item == target:
                return True

        else:
            if find_file(item, target):
                return True

    return False


folder = [
    "resume.pdf",
    "photo.jpg",
    [
        "python.py",
        "java.java",
        [
            "project.py",
            "database.sql"
        ]
    ]
]

target = "database.sql"

if find_file(folder, target):
    print("File found")
else:
    print("File not found")