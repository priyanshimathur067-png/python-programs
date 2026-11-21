def password_checker(password):

    upper = False
    lower = False
    digit = False
    special = False

    if len(password) < 8:
        return "Weak Password"

    for ch in password:

        if ch.isupper():
            upper = True

        elif ch.islower():
            lower = True

        elif ch.isdigit():
            digit = True

        else:
            special = True

    if upper and lower and digit and special:
        return "Strong Password"

    else:
        return "Weak Password"


password = input("Enter password: ")

print(password_checker(password))