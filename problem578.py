class ElectricityBill:
    def __init__(self, customer_id, name, units):
        self.customer_id = customer_id
        self.name = name
        self.units = units
        self.paid = False

    def calculate_bill(self):
        units = self.units

        if units <= 100:
            bill = units * 3
        elif units <= 200:
            bill = (100 * 3) + (units - 100) * 5
        else:
            bill = (100 * 3) + (100 * 5) + (units - 200) * 8

        return bill

    def pay_bill(self):
        if self.paid:
            print("Bill already paid!")
        else:
            self.paid = True
            print("Payment successful!")

    def display_bill(self):
        bill = self.calculate_bill()

        if not self.paid:
            bill += 50

        print("\nCustomer ID:", self.customer_id)
        print("Customer Name:", self.name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", self.calculate_bill())
        print("Late Charge:", 0 if self.paid else 50)
        print("Total Amount:", bill)
        print("Payment Status:",
              "Paid" if self.paid else "Unpaid")


c1 = ElectricityBill(101, "Rahul", 250)
c2 = ElectricityBill(102, "Priya", 150)

c1.display_bill()
c1.pay_bill()
c1.display_bill(c2.display_bill())
