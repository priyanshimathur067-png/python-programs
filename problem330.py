orders = [
    {"id": 101, "type": "normal", "distance": 12},
    {"id": 102, "type": "urgent", "distance": 25},
    {"id": 103, "type": "normal", "distance": 5},
    {"id": 104, "type": "urgent", "distance": 8}
]

priority = {
    "urgent": 1,
    "normal": 2
}

orders.sort(key=lambda x: (priority[x["type"]], x["distance"]))

for order in orders:
    print(
        "Order:", order["id"],
        "| Type:", order["type"],
        "| Distance:", order["distance"], "km"
    )