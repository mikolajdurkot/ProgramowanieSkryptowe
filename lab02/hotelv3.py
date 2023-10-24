import sys
import json

rozmiar_pokoju = [0, 1, 3, 2]

def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {str(i): [] for i in range(1, len(rozmiar_pokoju))}

def save_data_to_file(filename, rooms_data):
    with open(filename, 'w') as file:
        json.dump(rooms_data, file)

def book_room(guest, term, room_number, rooms_data, rozmiar_pokoju):
    if room_number in rooms_data:
        if len(rooms_data[room_number]) == rozmiar_pokoju[int(room_number)]:
            print(f"Nie można zarezerwować pokoju {room_number}. Brak miejsc.")
        else:
            rooms_data[room_number].append((guest, term))
            print(f"Zarezerwowano pokój {room_number} dla {guest} w terminie {term}")
    else:
        print(f"Nie ma pokoju o numerze {room_number}.")

def show_reservations(guest, rooms_data):
    print(f"[{guest}]")
    print("---------------------+------------")
    print("Termin               | Numer pokoju")
    print("---------------------+------------")
    
    for room_number, reservations in rooms_data.items():
        for reservation in reservations:
            if reservation[0] == guest:
                term = reservation[1]
                print(f"{term:<20} | {room_number}")


def display_rooms(rooms_data):
    print("+" + "-"*16 + "+"
          + "-"*30 + "+")
    print("| Numer pokoju   | Goście i Termin              |")
    print("+" + "-"*16 + "+"
          + "-"*30 + "+")
    for room_number, reservations in rooms_data.items():
        print(f"| {room_number:<14} |", end='')
        guests_and_terms = [f"{reservation[0]} - {reservation[1]}\n|\t\t |" for reservation in reservations]
        print(f"{''.join(guests_and_terms):<29}")
    print("+" + "-"*15 + "+"
          + "-"*30 + "+")

if len(sys.argv) != 2:
    print("Podaj nazwę pliku JSON jako argument wywołania.")
    sys.exit(1)

filename = sys.argv[1]
rooms_data = load_data_from_file(filename)

while True:
    try:
        command = input("> ")
        if command.startswith("book"):
            _, guest, term, room_number = command.split()
            if str(room_number) in rooms_data:
                book_room(guest, term, room_number, rooms_data, rozmiar_pokoju)
                save_data_to_file(filename, rooms_data)
            else:
                print(f"Nie ma pokoju o numerze {room_number}.")
        elif command.startswith("show"):
            _, guest = command.split()
            show_reservations(guest, rooms_data)
        elif command == "rooms":
            display_rooms(rooms_data)
        else:
            print("Nieznana komenda")
    except EOFError:
        break

save_data_to_file(filename, rooms_data)
