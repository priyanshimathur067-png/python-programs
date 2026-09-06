def count_employees(company):
    count = 0

    for employee in company:
        count += 1

        if employee["employees"]:
            count += count_employees(employee["employees"])

    return count


company = [
    {
        "name": "Manager",
        "employees": [
            {
                "name": "Developer",
                "employees": []
            },
            {
                "name": "Tester",
                "employees": []
            }
        ]
    }
]

print("Total employees:", count_employees(company))