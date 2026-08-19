#Find largest ansd smallest no.
# numbers = []

# n = int(input("How many numbers do you want to enter? "))

# for i in range(n):
#     value = int(input("Enter a number: "))
#     numbers.append(value)

# print("Your list is:", numbers)
# numbers = [23, 45, 67, 54, 32, 78]

# print("The smallest value is:", min(numbers))
# print("The largest value is:", max(numbers))
numbers = [23, 45, 67, 54, 32, 78]

numbers.sort()

print("The smallest value is:", numbers[0])
print("The largest value is:", numbers[-1])
