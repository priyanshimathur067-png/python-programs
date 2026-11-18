class ATM:

    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def withdraw(self, entered_pin, amount):

        if entered_pin == self.__pin:

            if amount <= self.__balance:
                self.__balance -= amount
                print("Please collect your cash")
            else:
                print("Insufficient balance")

        else:
            print("Incorrect PIN")

    def check_balance(self, entered_pin):

        if entered_pin == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Incorrect PIN")


a1 = ATM(1234, 20000)

a1.withdraw(1234, 5000)
a1.check_balance(1234)