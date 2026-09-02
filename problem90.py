# Get Even No. using filter
numbers = [12, 7, 8, 19, 24, 31, 40]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)