def reverse_string(s):
    result = ""

    for i in range(len(s)-1, -1, -1):
        result += s[i]

    return result

s = input("Enter string: ")
print(reverse_string(s))