def positive_numbers(numbers):
    for num in numbers:
        if num > 0:
            yield num


numbers = [-2, 5, -7, 8, 0, 10, -3]

for num in positive_numbers(numbers):
    print(num)