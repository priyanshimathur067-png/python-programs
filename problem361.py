def check_password (password):
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-+?_=,<>/"

    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    if len(password) < 8 and has_uppercase and has_lowercase and has_digit and has_special:
        return "Password is too short"
    if not (has_uppercase and has_lowercase and has_digit and has_special):
        return "Password does not meet complexity requirements"
    return "Password is valid"