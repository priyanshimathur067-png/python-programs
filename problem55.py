def calculate_hotel_bill(room_price, nights, **services):
    room_cost = room_price * nights

    service_cost = sum(services.values())

    subtotal = room_cost + service_cost

    gst = subtotal * 0.12

    final_bill = subtotal + gst

    return final_bill


def hotel_bill(name, room_price, nights, **services):
    total = calculate_hotel_bill(
        room_price,
        nights,
        **services
    )

    print("\n--- HOTEL BILL ---")
    print("Guest:", name)
    print("Nights:", nights)
    print("Services:", services)
    print("Final Bill: ₹", total)


hotel_bill(
    "Priyanshi",
    2500,
    3,
    food=1200,
    laundry=500,
    room_service=300
)