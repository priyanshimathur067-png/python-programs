def booking_charge(func):
    def wrapper(distance):
        fare = func(distance)

        charge = 50
        total = fare + charge

        print("Cab fare: ₹", fare)
        print("Booking charge: ₹", charge)
        print("Total fare: ₹", total)

    return wrapper


@booking_charge
def calculate_fare(distance):
    return distance * 15


distance = float(input("Enter distance in km: "))

calculate_fare(distance)