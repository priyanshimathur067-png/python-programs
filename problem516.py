class Calculator:
    def add(self, *args):
        total = 0

        for i in args:
            total = total + i

        print("Sum =", total)

obj = Calculator()

obj.add(10, 20)
obj.add(10, 20, 30)
obj.add(5, 10, 15, 20)