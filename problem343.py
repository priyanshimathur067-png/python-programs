usage = [3.2, 4.5, 6.1, 5.4, 3.8, 4.2, 6.5]

limit = 30

total_usage = sum(usage)
remaining = limit - total_usage
average = total_usage / len(usage)

print("Total usage:", total_usage, "GB")
print("Remaining data:", remaining, "GB")
print("Daily average:", average, "GB")

if average > 5:
    print("Warning: High data usage")
else:
    print("Data usage is normal")