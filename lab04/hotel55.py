from datetime import datetime

class Guest:
    def __init__(self, pesel, last_name, first_name):
        self.pesel = pesel
        self.last_name = last_name
        self.first_name = first_name
        self.reservations = []

    def book(self, room, check_in_date, check_out_date):
        reservation = Reservation(self, room, check_in_date, check_out_date)
        self.reservations.append(reservation)
        room.occupants.append(self)
        print(f"Zarezerwowano pokój {room.number} dla {self.first_name} {self.last_name} w terminie {check_in_date} - {check_out_date}")

    def __str__(self):
        return f"{self.first_name} {self.last_name} (PESEL: {self.pesel})"


class Room:
    def __init__(self, number, max_occupancy, price_per_night):
        self.number = number
        self.max_occupancy = max_occupancy
        self.price_per_night = price_per_night
        self.occupants = []

    def __str__(self):
        occupant_info = "\n".join([f"{guest.first_name} {guest.last_name}   {guest.reservations[0].check_inDate}   {guest.reservations[0].check_outDate}" for guest in self.occupants])
        return f"Numer: {self.number}\nMaksymalna liczba osób: {self.max_occupancy}\nAktualna liczba osób: {len(self.occupants)}\nCena: {self.price_per_night}\nGoście:\n{occupant_info}\n"


class Reservation:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.guest = guest
        self.room = room
        self.check_inDate = check_in_date
        self.check_outDate = check_out_date


class Hotel:
    rooms = [
        Room(1, 1, 100),
        Room(2, 3, 250),
        Room(3, 2, 200)
    ]
    reservations = []

    @classmethod
    def book_room(cls, pesel, room_index, check_in, check_out):
        guest = next((guest for guest in list_of_guests if guest.pesel == pesel), None)
        if not guest:
            last_name, first_name = input("Podaj nazwisko i imię: ").split()
            guest = Guest(pesel, last_name, first_name)

        room = cls.rooms[room_index]
        if len(room.occupants) < room.max_occupancy:
            guest.book(room, check_in, check_out)
            reservation = Reservation(guest, room, check_in, check_out)
            cls.reservations.append(reservation)
        else:
            print("Brak wolnych miejsc w podanym terminie")

    @classmethod
    def display_guest_reservations(cls, pesel):
        guest = next((guest for guest in list_of_guests if guest.pesel == pesel), None)
        if guest:
            print(guest)
            for reservation in guest.reservations:
                print(f"Pokój nr {reservation.room.number} {reservation.check_inDate} {reservation.check_outDate}")
                total_cost = (reservation.check_outDate - reservation.check_inDate).days * reservation.room.price_per_night
                print(f"Do zapłaty: {total_cost} złotych")
        else:
            print("Nieprawidłowy numer PESEL")

    @classmethod
    def display_reservations_in_date_range(cls, start_date, end_date):
        for reservation in cls.reservations:
            if start_date <= reservation.check_inDate <= end_date or start_date <= reservation.check_outDate <= end_date:
                print(f"{reservation.guest.first_name} {reservation.guest.last_name} (PESEL: {reservation.guest.pesel})")
                print(f"Pokój nr {reservation.room.number} {reservation.check_inDate} {reservation.check_outDate}")
                total_cost = (reservation.check_outDate - reservation.check_inDate).days * reservation.room.price_per_night
                print(f"Do zapłaty: {total_cost} złotych")
                print()


opis_formatu = "%d-%m-%Y"

# Dodaj przykładowych gości
list_of_guests = [
    Guest("123", "Kowalski", "Jan"),
    Guest("456", "Kowalska", "Anna"),
    Guest("789", "Bielecka", "Joanna")
]

while True:
    try:
        command = input("> ")
        if command == "rooms":
            for room in Hotel.rooms:
                print(room)
        elif command == "guests":
            for guest in list_of_guests:
                print(guest, end=" ")
            print()
        elif command.startswith("guest"):
            _, pesel = command.split()
            Hotel.display_guest_reservations(pesel)
        elif command.startswith("book"):
            _, pesel, room_index, check_in, check_out = command.split()
            room_index = int(room_index)
            check_in_date = datetime.strptime(check_in, opis_formatu).date()
            check_out_date = datetime.strptime(check_out, opis_formatu).date()
            Hotel.book_room(pesel, room_index, check_in_date, check_out_date)
        elif command.startswith("reservations"):
            _, start_date, end_date = command.split()
            start_date = datetime.strptime(start_date, opis_formatu).date()
            end_date = datetime.strptime(end_date, opis_formatu).date()
            Hotel.display_reservations_in_date_range(start_date, end_date)
        else:
            print("Nieznana komenda")
    except EOFError:
        break
