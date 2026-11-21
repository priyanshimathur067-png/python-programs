def salary_analyzer(employees):

    highest_salary = 0
    highest_employee = ""

    total = 0

    for name, salary in employees.items():

        total += salary

        if salary > highest_salary:
            highest_salary = salary
            highest_employee = name

    average = total / len(employees)

    print("Highest Salary:", highest_employee, "-", highest_salary)
    print("Average Salary:", average)

    print("Employees above average:")

    for name, salary in employees.items():

        if salary > average:
            print(name)


employees = {
    "Riya": 35000,
    "Aman": 45000,
    "Priya": 55000,
    "Rahul": 30000
}

salary_analyzer(employees)