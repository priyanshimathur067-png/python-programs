weights = [20, 22, 22, 25, 27, 30, 32]

maximum = max(weights)

improvement = weights[-1] - weights[0]

print("Maximum weight:", maximum, "kg")
print("Improvement:", improvement, "kg")

if improvement > 0:
    print("Strength increased")

elif improvement < 0:
    print("Strength decreased")

else:
    print("No change in strength")