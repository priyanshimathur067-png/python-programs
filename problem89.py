# Find student who passed using filter
marks = [35, 78, 22, 91, 45, 29, 67]

passed = list(filter(lambda mark: mark >= 40, marks))

print(passed)