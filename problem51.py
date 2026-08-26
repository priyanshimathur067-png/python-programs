def calculate_premium(age, vehicle_type, **factors):
    premium = 5000

    # Age factor
    if age < 25:
        premium += 1500
    elif age > 50:
        premium += 1000

    # Vehicle type
    vehicle_rates = {
        "car": 3000,
        "bike": 1500,
        "suv": 5000
    }

    premium += vehicle_rates.get(vehicle_type.lower(), 0)

    # Previous claims
    claims = factors.get("previous_claims", 0)
    premium += claims * 1000

    # Coverage
    coverage = factors.get("coverage", "basic").lower()

    if coverage == "comprehensive":
        premium += 4000
    elif coverage == "premium":
        premium += 7000

    return premium


def display_policy(name, premium):
    print("\n----- INSURANCE POLICY -----")
    print("Customer:", name)
    print("Final Premium: ₹", premium)


def main():
    name = input("Enter customer name: ")
    age = int(input("Enter age: "))
    vehicle = input("Enter vehicle type (car/bike/suv): ")
    claims = int(input("Enter previous claims: "))
    coverage = input("Enter coverage (basic/comprehensive/premium): ")

    premium = calculate_premium(
        age,
        vehicle,
        previous_claims=claims,
        coverage=coverage
    )

    display_policy(name, premium)


main()