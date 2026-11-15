
class AgeValidator:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        return getattr(obj, self.name, None)

    def __set__(self, obj, value):
        if not 18 <= value <= 60:
            raise ValueError("Age must be between 18 and 60")

        setattr(obj, self.name, value)


class Employee:
    age = AgeValidator()

    def __init__(self, name, age):
        self.name = name
        self.age = age


e1 = Employee("Priya", 23)

print("Name:", e1.name)
print("Age:", e1.age)

e1.age = 25
print("Updated Age:", e1.age)
