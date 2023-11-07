from datetime import datetime

class Room:
    def __init__(self, number, max_occupancy, price_per_night):
        self.number = number
        self.max_occupancy = max_occupancy
        self.price_per_night = price_per_night
        self.occupants = []

    def __str__(self):
        occupant_info = "\n".join([f"{guest.name}   {guest.reservations[0][1]}   {guest.reservations[0][2]}" for guest in self.occupants])
        return f"Numer: {self.number}\nMaksymalna liczba osób: {self.max_occupancy}\nAktualna liczba osób: {len(self.occupants)}\nCena: {self.price_per_night}\nGoście:\n{occupant_info}\n"


class Guest:
    def __init__(self, name):
        self.name = name
        self.reservations = []

    def book(self, room, check_in_date, check_out_date):
        if len(room.occupants) < room.max_occupancy:
            room.occupants.append(self)
            self.reservations.append((room, check_in_date, check_out_date))
            print(f"Zarezerwowano pokój {room.number} dla {self.name} w terminie {check_in_date} - {check_out_date}")
        else:
            print("Brak wolnych miejsc w podanym terminie")

    def calculate_total_cost(self):
        total_cost = 0
        for reservation in self.reservations:
            room, check_in_date, check_out_date = reservation
            total_cost += (check_out_date - check_in_date).days * room.price_per_night
        return total_cost

    def __str__(self):
        return self.name

opis_formatu = "%d-%m-%Y"

list_of_rooms = [
    Room(1, 1, 100),
    Room(2, 3, 250),
    Room(3, 2, 200)
]

list_of_guests = [
    Guest("Jan Kowalski"),
    Guest("Anna Kowalska"),
    Guest("Joanna Bielecka")
]

while True:
    try:
        command = input("> ")
        if command == "rooms":
            for room in list_of_rooms:
                print(room)
        elif command == "guests":
            for guest in list_of_guests:
                print(guest,end=" ")
            print()
        elif command.startswith("guest"):
            _, guest_index = command.split()
            guest_index = int(guest_index)
            if guest_index < len(list_of_guests):
                guest = list_of_guests[guest_index]
                print(guest)
                for room, check_in_date, check_out_date in guest.reservations:
                    print(f"Pokój nr {room.number} {check_in_date} {check_out_date}")
                    total_cost = (check_out_date - check_in_date).days * room.price_per_night
                    print(f"Do zapłaty: {total_cost} złotych")
            else:
                print("Nieprawidłowy indeks gościa")

        elif command.startswith("book"):
            _, guest_index, room_index, check_in, check_out = command.split()
            guest_index = int(guest_index)
            room_index = int(room_index)
            check_in_date = datetime.strptime(check_in, opis_formatu).date()
            check_out_date = datetime.strptime(check_out, opis_formatu).date()
            if guest_index < len(list_of_guests) and room_index < len(list_of_rooms):
                list_of_guests[guest_index].book(list_of_rooms[room_index], check_in_date, check_out_date)
            else:
                print("Nieprawidłowy indeks gościa lub pokoju")
        else:
            print("Nieznana komenda")
    except EOFError:
        break
