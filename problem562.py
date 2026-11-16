
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def display(self):
        super().display()
        print("Specialization:", self.specialization)


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def display(self):
        super().display()
        print("Disease:", self.disease)


class Nurse(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


d1 = Doctor("Amit", 35, "Cardiologist")
p1 = Patient("Priyanshi", 23, "Fever")
n1 = Nurse("Neha", 28, "Emergency")

d1.display()
p1.display()
n1.display()
