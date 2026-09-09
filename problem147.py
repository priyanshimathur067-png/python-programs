def convert_temperature(value, unit):

    if unit == "C":
        fahrenheit = (value * 9 / 5) + 32
        return fahrenheit

    elif unit == "F":
        celsius = (value - 32) * 5 / 9
        return celsius

    else:
        return "Invalid unit"


print("Fahrenheit:", convert_temperature(30, "C"))
print("Celsius:", convert_temperature(86, "F"))