vehicles = [
    {"number": "UP25AB1234", "hours": 3},
    {"number": "UP25CD5678", "hours": 7},
    {"number": "UP25EF9012", "hours": 2},
    {"number": "UP25GH3456", "hours": 10}
]

for vehicle in vehicles:
    hours = vehicle["hours"]

    if hours <= 2:
        fee = 30
    else:
        fee = 30 + (hours - 2) * 20

    vehicle["fee"] = fee

vehicles.sort(key=lambda x: x["fee"], reverse=True)

for vehicle in vehicles:
    print(vehicle["number"], "→ ₹", vehicle["fee"])