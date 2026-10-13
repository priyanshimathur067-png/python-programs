
def second_most_frequent(arr):
    freq = []

    for i in arr:
        found = False

        for item in freq:
            if item[0] == i:
                item[1] += 1
                found = True
                break

        if not found:
            freq.append([i, 1])

    if len(freq) < 2:
        return None

    freq.sort(key=lambda item: item[1], reverse=True)

    first_frequency = freq[0][1]

    for item in freq:
        if item[1] < first_frequency:
            return item[0]

    return None


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

answer = second_most_frequent(arr)

if answer is None:
    print("No second frequency level exists")
else:
    print("Second most frequent element:", answer)
