marks = {
    "Priya": 85,
    "Rahul": 72,
    "Anu": 95,
    "Riya": 80
}

result = sorted(marks.items(), key=lambda x: x[0])

print(result)