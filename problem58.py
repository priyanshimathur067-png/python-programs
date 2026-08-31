def loan_check(func):
    def wrapper(name, salary):
        if salary >= 25000:
            return func(name, salary)
        else:
            print("Sorry! You are not eligible for the loan.")
    return wrapper


@loan_check
def apply_loan(name, salary):
    print(f"Congratulations {name}, your loan application is accepted!")


name = input("Enter your name: ")
salary = float(input("Enter your monthly salary: "))

apply_loan(name, salary)