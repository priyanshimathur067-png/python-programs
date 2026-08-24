def calculate_salary(basic, *allowances):
    total = basic + sum(allowances)

    print("Basic Salary:", basic)
    print("Total Allowances:", sum(allowances))
    print("Final Salary:", total)


calculate_salary(25000, 3000, 2000, 1500)