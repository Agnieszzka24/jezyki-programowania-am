from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Antelope import Antelope
from Organisms.Lynx import Lynx
import os
import random


def print_menu():
    print("\nMenu:")
    print("1. Przejdź do kolejnej tury")
    print("2. Aktywuj plagę")
    print("3. Dodaj nowy organizm")
    print("4. Wyjdź")


def add_organism_menu(world):
    print("\nDostępne organizmy:")
    print("G - Trawa")
    print("S - Owca")
    print("A - Antylopa")
    print("R - Ryś")

    org_type = input("Wybierz typ organizmu: ").upper()
    if org_type not in ['G', 'S', 'A', 'R']:
        print("Nieprawidłowy typ organizmu!")
        return

    try:
        x = int(input("Podaj pozycję pionowa (0-{}): ".format(world.worldX - 1)))
        y = int(input("Podaj pozycję pozioma (0-{}): ".format(world.worldY - 1)))
        if world.add_custom_organism(org_type, Position(xPosition=x, yPosition=y)):
            print("Organizm dodany pomyślnie!")
        else:
            print("Nie udało się dodać organizmu!")
    except ValueError:
        print("Nieprawidłowe współrzędne!")


if __name__ == '__main__':
    pyWorld = World(10, 10)

    # Poprawione tworzenie pozycji - używając nazwanych argumentów
    newOrg = Grass(position=Position(xPosition=9, yPosition=9), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Grass(position=Position(xPosition=1, yPosition=1), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Sheep(position=Position(xPosition=2, yPosition=2), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    for _ in range(3):
        newOrg = Lynx(
            position=Position(xPosition=random.randint(0, 9), yPosition=random.randint(0, 9)),
            world=pyWorld
        )
        pyWorld.addOrganism(newOrg)

    newOrg = Antelope(position=Position(xPosition=8, yPosition=4), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    while True:
        os.system('cls')
        print(pyWorld)
        print_menu()
        choice = input("Wybierz opcję: ")

        if choice == '1':
            pyWorld.makeTurn()
        elif choice == '2':
            pyWorld.activate_plague()
            input("Naciśnij Enter, aby kontynuować...")
        elif choice == '3':
            add_organism_menu(pyWorld)
            input("Naciśnij Enter, aby kontynuować...")
        elif choice == '4':
            break
        else:
            print("Nieprawidłowy wybór!")
            input("Naciśnij Enter, aby kontynuować...")