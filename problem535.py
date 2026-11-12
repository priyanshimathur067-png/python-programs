class Computer:
    def __init__(self, brand):
        self.brand = brand

    class Processor:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def discount(self):
            return self.price - (self.price * 10 / 100)

c = Computer("HP")
p = c.Processor("Intel i7", 30000)

print("Brand:", c.brand)
print("Processor:", p.name)
print("Price after discount:", p.discount())