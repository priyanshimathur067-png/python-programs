employees = [
    {"name": "Aman", "hours": 42},
    {"name": "Riya", "hours": 48},
    {"name": "Karan", "hours": 40},
    {"name": "Neha", "hours": 55}
]

for employee in employees:
    overtime = max(0, employee["hours"] - 40)
    employee["overtime"] = overtime

employees.sort(key=lambda x: x["overtime"], reverse=True)

for employee in employees:
    print(employee["name"], "→", employee["overtime"], "overtime hours")