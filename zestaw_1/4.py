def sort_dates(dates):
    # zmiana na krotke
    def date_key(date):
        return (date['year'], date['month'], date['day'])

    n = len(dates)
    for i in range(n):
        for j in range(0, n - i - 1):
            if date_key(dates[j]) > date_key(dates[j + 1]):
                dates[j], dates[j + 1] = dates[j + 1], dates[j]


dates = [
    {'day': 15, 'month': 1, 'year': 2023},
    {'day': 5, 'month': 3, 'year': 2022},
    {'day': 20, 'month': 12, 'year': 2021},
    {'day': 10, 'month': 1, 'year': 2023},
    {'day': 1, 'month': 1, 'year': 2020}
]

print("Daty przed sortowaniem:")
for date in dates:
    print(f"{date['day']:02d}-{date['month']:02d}-{date['year']}")

sort_dates(dates)

print("\nDaty po sortowaniu:")
for date in dates:
    print(f"{date['day']:02d}-{date['month']:02d}-{date['year']}")