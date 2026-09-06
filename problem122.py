def count_files(folder):
    count = 0

    for item in folder:
        if isinstance(item, list):
            count += count_files(item)
        else:
            count += 1

    return count


folder = [
    "resume.pdf",
    "photo.jpg",
    ["python.py", "java.java"],
    ["notes.txt", ["project.py", "data.csv"]]
]

print("Total files:", count_files(folder))