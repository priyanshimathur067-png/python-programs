class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


d1 = Dog()
d1.eat()
d1.bark()

c1 = Cat()
c1.eat()
c1.meow()