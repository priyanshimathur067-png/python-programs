class Student:
    def __init__(self, name):
        self.name = name

    class Address:
        def __init__(self, city, state):
            self.city = city
            self.state = state

s = Student("Priyanshi")
a = Student.Address("Bareilly", "UP")

print("Name:", s.name)
print("City:", a.city)
print("State:", a.state)