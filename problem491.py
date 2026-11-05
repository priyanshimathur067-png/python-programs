class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


class Cow(Animal):
    def sound(self):
        print("Cow moos")


d1 = Dog()
c1 = Cat()
c2 = Cow()

d1.sound()
c1.sound()
c2.sound()