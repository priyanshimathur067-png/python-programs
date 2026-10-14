
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if is_rotation(s1, s2):
    print("Strings are rotations")
else:
    print("Strings are not rotations")
