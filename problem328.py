rides = [
    {"customer": "Riya", "distance": 5},
    {"customer": "Aman", "distance": 12},
    {"customer": "Neha", "distance": 8},
    {"customer": "Karan", "distance": 20}
]

for ride in rides:
    distance = ride["distance"]

    if distance <= 5:
        fare = 100
    else:
        fare = 100 + (distance - 5) * 15

    ride["fare"] = fare

rides.sort(key=lambda x: x["fare"], reverse=True)

for ride in rides:
    print(ride["customer"], "→ ₹", ride["fare"])