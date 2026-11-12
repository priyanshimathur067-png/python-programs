class Car:
    def __init__(self, model):
        self.model = model

    class Engine:
        def __init__(self, engine_type):
            self.engine_type = engine_type

c = Car("BMW")
e = Car.Engine("Petrol")

print(c.model)
print(e.engine_type)