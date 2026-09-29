salaries = [35000, 52000, 48000, 75000, 62000, 42000]

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above_50000 = 0

for salary in salaries:
    if salary > 50000:
        above_50000 += 1

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees earning above ₹50,000:", above_50000)