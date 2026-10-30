class Person :
    def __init__(self,name,age):
       self.name = name
       self.age = age
    def __add__(self, other):
       return self.age + other.age
p1 = Person("Emy", 22)
p2 = Person("Tuba",23)

print(p1 + p2)




