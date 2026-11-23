def count_char(s):
    digit = 0
    alphabet = 0
    special = 0

    for i in s:
        if i.isdigit():
            digit += 1
        elif i.isalpha():
            alphabet += 1
        else:
            special += 1

    print("Digits:", digit)
    print("Alphabets:", alphabet)
    print("Special characters:", special)

s = input("Enter string: ")
count_char(s)