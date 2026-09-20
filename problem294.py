def maximum_salary(salaries, index=0):
    if index == len(salaries) - 1:
        return salaries[index]

    current_max = maximum_salary(salaries, index + 1)

    if salaries[index] > current_max:
        return salaries[index]
    else:
        return current_max


salaries = [25000, 42000, 31000, 55000, 38000]

print("Highest salary:", maximum_salary(salaries))