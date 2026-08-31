def booking_fee(func):
    def wrapper(movie, tickets):
        ticket_amount = func(movie, tickets)

        fee = 30
        total = ticket_amount + fee

        print("Movie:", movie)
        print("Ticket amount: ₹", ticket_amount)
        print("Booking fee: ₹", fee)
        print("Total amount: ₹", total)

    return wrapper


@booking_fee
def book_ticket(movie, tickets):
    price = 200
    return tickets * price


movie = input("Enter movie name: ")
tickets = int(input("Enter number of tickets: "))

book_ticket(movie, tickets)