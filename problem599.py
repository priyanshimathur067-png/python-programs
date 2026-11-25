def remove_duplicate(s):
    result = ""

    for ch in s:
        if ch not in result:
            result += ch

    return result

s = input("Enter string: ")
print(remove_duplicate(s))