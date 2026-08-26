def calculate_fare(distance, *charges):
    base_fare = 50
    distance_charge = distance * 15

    extra_charges = sum(charges)

    total = base_fare + distance_charge + extra_charges

    return total


def print_fare(distance, waiting_charge, night_charge):
    total = calculate_fare(
        distance,
        waiting_charge,
        night_charge
    )

    print("\n--- CAB BILL ---")
    print("Distance:", distance, "km")
    print("Waiting Charge: ₹", waiting_charge)
    print("Night Charge: ₹", night_charge)
    print("Total Fare: ₹", total)


distance = float(input("Enter distance: "))
waiting = float(input("Enter waiting charge: "))
night = float(input("Enter night charge: "))

print_fare(distance, waiting, night)