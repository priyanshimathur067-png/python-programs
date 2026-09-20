def count_passed(marks, index=0):
    if index == len(marks):
        return 0

    if marks[index] >= 40:
        return 1 + count_passed(marks, index + 1)
    else:
        return count_passed(marks, index + 1)


marks = [75, 32, 65, 28, 90, 41]

print("Students passed:", count_passed(marks))