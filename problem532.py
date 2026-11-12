class Mobile:
    def __init__(self, brand):
        self.brand = brand

    class Battery:
        def __init__(self, capacity, percentage):
            self.capacity = capacity
            self.percentage = percentage

        def display(self):
            print("Capacity:", self.capacity)
            print("Battery:", self.percentage, "%")

m = Mobile("Apple")
b = m.Battery("4000 mAh", 85)

print(m.brand)
b.display()