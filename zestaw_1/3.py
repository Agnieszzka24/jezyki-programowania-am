# Krok 1: people = [1, 2, 3], index = 0
#   index = (0 + 1) % 3 = 1 -> usuwamy people[1] = 2
#   Nowa lista: [1, 3]
# Krok 2: people = [1, 3], index = 1
#   index = (1 + 1) % 2 = 0 -> usuwamy people[0] = 1
#   Nowa lista: [3]
# Koniec: people = [3] -> zwracamy 3

def josephus(n):
    people = list(range(1, n + 1))
    index = 0

    while len(people) > 1:
        index = (index + 1) % len(people)
        people.pop(index)

    return people[0]


n = int(input("Podaj liczbę żołnierzy: "))
print("Bezpieczna pozycja to:", josephus(n))