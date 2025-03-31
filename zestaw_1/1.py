def is_primary(n):
    """Sprawdza, czy liczba n jest pierwsza."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def print_primes(start, end):
    """Wypisuje liczby pierwsze z przedziału [start, end]."""
    print(f"Liczby pierwsze z przedziału od {start}, do {end}:")

    for num in range(start, end):
        if is_primary(num):
            print(num, end=" ")
    print()


start = int(input("Podaj początek przedziału: "))
end = int(input("Podaj koniec przedziału: "))

print_primes(start, end)