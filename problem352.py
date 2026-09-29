trips = {
    "Trip 1": [10, 180],
    "Trip 2": [15, 300],
    "Trip 3": [8, 160],
    "Trip 4": [20, 450],
    "Trip 5": [12, 250]
}

total_distance = 0
total_earnings = 0

highest_fare = 0
highest_trip = ""

for trip, data in trips.items():

    distance = data[0]
    fare = data[1]

    total_distance += distance
    total_earnings += fare

    if fare > highest_fare:
        highest_fare = fare
        highest_trip = trip

average_per_km = total_earnings / total_distance

print("Total distance:", total_distance, "km")
print("Total earnings: ₹", total_earnings)
print("Average earning per km: ₹", round(average_per_km, 2))
print("Highest earning trip:", highest_trip)