class Person :
    def __init__(self, name , age =12):
        self.name = name
        self.age = age

p1 = Person("hari")
p2 = Person("shiv", 34)

print(p1.name, p1.age)
print(p2.name , p2.age)