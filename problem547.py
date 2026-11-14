
class Calculator:
    def __init__(self, operation):
        self.operation = operation

    def __call__(self, a, b):
        if self.operation == "add":
            return a + b

        elif self.operation == "multiply":
            return a * b

        else:
            return "Invalid operation"


add = Calculator("add")
multiply = Calculator("multiply")

print("Addition:", add(10, 20))
print("Multiplication:", multiply(10, 20))
