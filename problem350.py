speeds = {
    "8 AM": 25,
    "10 AM": 18,
    "12 PM": 32,
    "2 PM": 15,
    "4 PM": 28,
    "6 PM": 12,
    "9 PM": 35
}

highest = max(speeds.values())
lowest = min(speeds.values())

average = sum(speeds.values()) / len(speeds)

print("Highest speed:", highest, "Mbps")
print("Lowest speed:", lowest, "Mbps")
print("Average speed:", round(average, 2), "Mbps")

print("\nSpeed below 20 Mbps:")

for time, speed in speeds.items():

    if speed < 20:
        print(time, ":", speed, "Mbps")