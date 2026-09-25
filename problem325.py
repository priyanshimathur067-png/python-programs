properties = [
    {
        "location": "Delhi",
        "price": 4500000,
        "area": 1200,
        "bedrooms": 2
    },
    {
        "location": "Noida",
        "price": 5500000,
        "area": 1500,
        "bedrooms": 3
    },
    {
        "location": "Agra",
        "price": 3000000,
        "area": 1100,
        "bedrooms": 2
    },
    {
        "location": "Delhi",
        "price": 7000000,
        "area": 1800,
        "bedrooms": 3
    }
]

budget = int(input("Enter your maximum budget: "))
minimum_area = int(input("Enter minimum area required: "))

found = False

print("\nAvailable properties:")

for property in properties:

    if property["price"] <= budget and property["area"] >= minimum_area:

        print("\nLocation:", property["location"])
        print("Price:", property["price"])
        print("Area:", property["area"], "sq.ft")
        print("Bedrooms:", property["bedrooms"])

        found = True

if found == False:
    print("No property found according to your requirements.")