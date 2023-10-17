import sys
import json


rozmiar_pokoju=[]
rozmiar_pokoju.append(0)
rozmiar_pokoju.append(1)
rozmiar_pokoju.append(3)
rozmiar_pokoju.append(2)


def zarezerwuj_pokoj(gosc, numer_pokoju, wykaz_pokoi):
    numer_pokoju = int(numer_pokoju)  # Konwersja na int
    if numer_pokoju not in wykaz_pokoi:
        print(f"Nie ma pokoju o numerze {numer_pokoju}.")
        return

    if len(wykaz_pokoi[numer_pokoju]) == rozmiar_pokoju[numer_pokoju]:
        print(f"Nie można zarezerwować pokoju {numer_pokoju}. Brak miejsc.")
        return

    wykaz_pokoi[numer_pokoju].append(gosc)

def wyswietl_stan_pokoi(wykaz_pokoi):
    print("---------------+--------+")
    print("| Numer pokoju | Goście |")
    print("---------------+--------+")
    for numer, goscie in wykaz_pokoi.items():
        print(f"{numer}\t\t", end='')
        for idx, gosc in enumerate(goscie):
            print(f"{idx + 1}. {gosc}", end='\t')
        print()

def zapisz_wykaz_do_pliku(wykaz_pokoi):
    with open("wykaz_pokoi.json", "w") as file:
        json.dump(wykaz_pokoi, file)

def wczytaj_wykaz_z_pliku():
    try:
        with open("wykaz_pokoi.json", "r") as file:
            return {int(k): v for k, v in json.load(file).items()}
    except FileNotFoundError:
        return {
            1: [],
            2: [],
            3: []
        }

wykaz_pokoi = wczytaj_wykaz_z_pliku()

for i in range(1, len(sys.argv)-1, 2):
    print(i)
    if sys.argv[i] == "--stan_pokoi":
        i += 1
    gosc = sys.argv[i]
    numer_pokoju = sys.argv[i + 1]
    zarezerwuj_pokoj(gosc, numer_pokoju, wykaz_pokoi)
zapisz_wykaz_do_pliku(wykaz_pokoi)

if "--stan_pokoi" in sys.argv:
    wyswietl_stan_pokoi(wykaz_pokoi)