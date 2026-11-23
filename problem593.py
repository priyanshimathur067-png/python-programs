def count(s):
    vowels = 0
    consonants = 0

    for i in s.lower():
        if i.isalpha():
            if i in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)

s = input("Enter string: ")
count(s)