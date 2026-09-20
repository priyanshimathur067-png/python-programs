def total_marks(marks, index=0):
    if index == len(marks):
        return 0

    return marks[index] + total_marks(marks, index + 1)


marks = [78, 85, 67, 92, 74]

print("Total marks:", total_marks(marks))