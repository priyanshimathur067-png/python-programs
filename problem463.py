class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def greet (self):
        print("Hello my name is " + self.name)   
p1 = Person("ravi", 33)
p1 .greet()
