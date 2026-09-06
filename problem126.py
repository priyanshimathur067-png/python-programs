def reverse_name(name):
    if len(name) == 0:
        return ""

    return reverse_name(name[1:]) + name[0]


name = "Priyanshi"

print(reverse_name(name))