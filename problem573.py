class ParkingLot:

    def __init__(self, capacity):
        self.capacity = capacity
        self.vehicles = []

    def park_vehicle(self, vehicle):

        if len(self.vehicles) < self.capacity:
            self.vehicles.append(vehicle)
            print(vehicle, "parked successfully")
        else:
            print("Parking Full")

    def remove_vehicle(self, vehicle):

        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            print(vehicle, "removed")
        else:
            print("Vehicle not found")

    def available_slots(self):
        print("Available Slots:",
              self.capacity - len(self.vehicles))


p = ParkingLot(3)

p.park_vehicle("UP25AB1234")
p.park_vehicle("UP25CD5678")

p.available_slots()

p.remove_vehicle("UP25AB1234")

p.available_slots()