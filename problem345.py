vehicles = {
    "UP25AB1234": 2,
    "UP25CD5678": 4,
    "UP25EF9012": 7
}

for vehicle, hours in vehicles.items():

    if hours <= 2:
        fee = 30

    elif hours <= 5:
        fee = 30 + (hours - 2) * 20

    else:
        fee = 30 + (3 * 20) + (hours - 5) * 15

    print(vehicle, "→ ₹", fee)