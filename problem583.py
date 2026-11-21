def second_highest(sales):

    first = float('-inf')
    second = float('-inf')

    for value in sales:

        if value > first:

            second = first
            first = value

        elif value > second and value != first:

            second = value

    if second == float('-inf'):
        return "Second highest value does not exist"

    return second


sales = [45000, 78000, 92000, 78000, 65000]

print("Second Highest Sales:", second_highest(sales))