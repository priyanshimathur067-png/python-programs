def find_employee(company, target):
    for employee in company:

        if employee["name"] == target:
            return True

        if employee["employees"]:
            if find_employee(employee["employees"], target):
                return True

    return False


company = [
    {
        "name": "Rahul",
        "employees": [
            {
                "name": "Aman",
                "employees": [
                    {
                        "name": "Priya",
                        "employees": []
                    }
                ]
            }
        ]
    }
]

print(find_employee(company, "Priya"))