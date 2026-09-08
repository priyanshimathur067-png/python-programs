def calculate_bonus(salary, experience):

    if experience >= 10:
        bonus = salary * 20 / 100
    elif experience >= 5:
        bonus = salary * 15 / 100
    elif experience >= 2:
        bonus = salary * 10 / 100
    else:
        bonus = salary * 5 / 100

    return bonus


salary = 30000
experience = 6

print("Bonus:", calculate_bonus(salary, experience))