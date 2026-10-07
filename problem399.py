def move_negative(arr):
    negative = []
    positive = []

    for i in arr:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)

    return negative + positive


arr = [3, -2, 5, -7, 8, -1]
print(move_negative(arr))