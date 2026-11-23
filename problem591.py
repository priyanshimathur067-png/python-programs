def reverse_string(s):
    rev = ""

    for i in s:
        rev = i + rev

    return rev

s = input("Enter string: ")
print(reverse_string(s))