def electricity_bill(units):
    if units == 0:
        return 0

    if units <= 100:
        return 5 + electricity_bill(units - 1)

    elif units <= 200:
        return 7 + electricity_bill(units - 1)

    else:
        return 10 + electricity_bill(units - 1)


units = 150

print("Electricity bill:", electricity_bill(units))