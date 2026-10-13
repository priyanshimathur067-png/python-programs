
def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            return False

    return True


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if are_anagrams(s1, s2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
