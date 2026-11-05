class InkjetPrinter:
    def print_document(self):
        print("Inkjet printer is printing")


class LaserPrinter:
    def print_document(self):
        print("Laser printer is printing")


class VirtualPrinter:
    def print_document(self):
        print("Virtual printer is printing")


def start_printing(obj):
    obj.print_document()


p1 = InkjetPrinter()
p2 = LaserPrinter()
p3 = VirtualPrinter()

start_printing(p1)
start_printing(p2)
start_printing(p3)