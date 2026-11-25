def frequency(s):
    count = {}

    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    return count

s = input("Enter string: ")
print(frequency(s))