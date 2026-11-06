class ATM:
    def __init__(self, pin):
        self.__pin = pin

    def verify_pin(self, entered_pin):
        if self.__pin == entered_pin:
            print("Access Granted")
        else:
            print("Incorrect PIN")


a1 = ATM(1234)

a1.verify_pin(1234)
a1.verify_pin(4567)