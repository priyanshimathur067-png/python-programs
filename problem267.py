arr = [-2, 5, -7, 8, 3, -1]

positive = []
negative = []

for num in arr:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print("Positive:", positive)
print("Negative:", negative)