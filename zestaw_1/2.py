# n % i == 0 <- pierwszy dzielnik, n/i <- drógi dzielnik
# np: n = 12 (2,(n**0.5) +1) -> (2,  pier z 12 = 3)
# i = 2 12%2 == 0 -> 12/2 = 6   (2, 6)
# i = 3 12%3 == 0 -> 12/3 = 4   (3, 4) [1,2,3,4,6]

def dzielniki_wlasciwe(n):
    if n == 1:
        return []
    dzielniki = set()
    dzielniki.add(1)  # 1 jest zawsze dzielnikiem

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dzielniki.add(i)
            if i != n // i:
                dzielniki.add(n // i)
    return sorted(dzielniki)

# print(dzielniki_wlasciwe(12))

def zaprzyjazniona(start, end):
    znalezione_pary = set()

    for a in range(start, end + 1):
        suma_a = sum(dzielniki_wlasciwe(a))
        if suma_a > a and suma_a <= end:
            suma_b = sum(dzielniki_wlasciwe(suma_a))
            if a == suma_b:
                znalezione_pary.add((a, suma_a))

    if znalezione_pary:
        for para in sorted(znalezione_pary):
            print(f"{para[0]} i {para[1]} są liczbami zaprzyjaźnionymi.")
    else:
        print(f"W zakresie od {start} do {end} nie ma liczb zaprzyjaźnionych.")



zaprzyjazniona(220, 284)  # 220 i 284
zaprzyjazniona(200, 300)  # 220 i 284
zaprzyjazniona(234, 222)  # blad