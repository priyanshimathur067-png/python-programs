def calculate_salary(basic, allowance, deduction=0):
    net_salary = basic + allowance - deduction
    return net_salary


print(calculate_salary(25000, 5000))
print(calculate_salary(25000, 5000, 2000))