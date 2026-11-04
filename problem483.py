class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type


class ElectricCar(Car):
    def __init__(self, brand, model, fuel_type, battery):
        super().__init__(brand, model, fuel_type)
        self.battery = battery

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)
        print("Battery:", self.battery, "kWh")


e1 = ElectricCar("Tata", "Nexon", "Electric", 40)
e1.display()