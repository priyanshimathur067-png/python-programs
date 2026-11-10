class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cow(Animal):
    def sound(self):
        print("Cow moos")

a = Animal()
d = Dog()
c = Cow()

a.sound()
d.sound()
c.sound()