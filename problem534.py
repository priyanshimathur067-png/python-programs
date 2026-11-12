class Hospital:
    def __init__(self, name):
        self.name = name

    class Patient:
        def __init__(self, name, days, charge):
            self.name = name
            self.days = days
            self.charge = charge

        def bill(self):
            return self.days * self.charge

h = Hospital("City Hospital")
p = h.Patient("Amit", 5, 2000)

print("Hospital:", h.name)
print("Patient:", p.name)
print("Total Bill:", p.bill())