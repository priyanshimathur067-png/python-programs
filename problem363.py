def calculate_fare(distance, waiting_time):
    base_fare = 50
    distance_charge = distance * 15
    waiting_charge = waiting_time * 2

    total_fare = base_fare + distance_charge + waiting_charge

    return total_fare


distance = float(input("Enter distance in km: "))
waiting_time = int(input("Enter waiting time in minutes: "))

if distance >= 0 and waiting_time >= 0:
    print("Total Cab Fare: ₹", calculate_fare(distance, waiting_time))
else:
    print("Invalid input.")