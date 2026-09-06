def max_salary(salaries, n):
    if n == 1:
        return salaries[0]

    previous_max = max_salary(salaries, n - 1)

    return max(previous_max, salaries[n - 1])


salaries = [25000, 32000, 28000, 45000, 37000]

print("Highest salary:", max_salary(salaries, len(salaries)))