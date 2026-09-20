def calculate_bill(units, index=0):
    rates = [5, 7, 10]

    if units <= 0:
        return 0

    if units <= 100:
        return units * rates[0]

    if units <= 200:
        return 100 * rates[0] + (units - 100) * rates[1]

    return 100 * rates[0] + 100 * rates[1] + (units - 200) * rates[2]


units = 250

print("Electricity bill:", calculate_bill(units))