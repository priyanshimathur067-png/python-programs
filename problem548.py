
class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers

    def __getitem__(self, index):
        return self.numbers[index]

    def __len__(self):
        return len(self.numbers)


obj = NumberCollection([10, 20, 30, 40, 50])

print("First Element:", obj[0])
print("Third Element:", obj[2])
print("Total Elements:", len(obj))

print("All Elements:")

for num in obj:
    print(num)
