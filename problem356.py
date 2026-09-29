projects = {
    "Website": [25000, "Completed"],
    "Mobile App": [40000, "Pending"],
    "Portfolio": [15000, "Completed"],
    "E-commerce": [50000, "Pending"],
    "Dashboard": [30000, "Completed"]
}

completed_income = 0
pending_payment = 0
completed_count = 0

highest_payment = 0
highest_project = ""

for project, data in projects.items():

    payment = data[0]
    status = data[1]

    if status == "Completed":

        completed_income += payment
        completed_count += 1

        if payment > highest_payment:
            highest_payment = payment
            highest_project = project

    elif status == "Pending":

        pending_payment += payment

print("Completed project income: ₹", completed_income)
print("Pending payment: ₹", pending_payment)
print("Completed projects:", completed_count)
print("Highest-paying completed project:", highest_project)