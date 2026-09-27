customers = [
    {"name": "Aman", "speed": 25},
    {"name": "Riya", "speed": 8},
    {"name": "Karan", "speed": 15},
    {"name": "Neha", "speed": 5},
    {"name": "Vikas", "speed": 30}
]

complaints = []

for customer in customers:
    if customer["speed"] < 10:
        complaints.append(customer)

print("Customers needing attention:")

for customer in complaints:
    print(customer["name"], "→", customer["speed"], "Mbps")