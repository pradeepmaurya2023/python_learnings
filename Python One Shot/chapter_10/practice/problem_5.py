# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

class Train:
    no_of_seats = 200
    train_fare = 150

    def book_ticket(self):
        print("Your Ticket has been booked")
        self.no_of_seats = self.no_of_seats-1

    def get_status(self):
        print(f"Available no of seats are {self.no_of_seats}")

    def fair_info(self):
        print(f"Price of ticket per person is {self.train_fare}Rs")

user1 = Train()

user1.get_status()

user1.book_ticket()

user1.get_status()