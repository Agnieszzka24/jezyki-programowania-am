from abc import ABC


class InvoiceRepository(ABC):
    def __init__(self, data_source=None):
        """Inicjalizuje repozytorium faktur z danymi źródłowymi"""
        self.__data_source = data_source if data_source is not None else []

    def find_by_number(self, number):
        """Zwraca fakturę na podstawie numeru, lub None jeśli nie znaleziono"""
        return next((inv for inv in self.data_source if inv.number == number), None)

    def add(self, invoice):
        """Dodaje fakturę do repozytorium, jeśli nie istnieje to dodaje do listy i zapisuje do pliku"""
        if not self.find_by_number(invoice.number):
            self.__data_source.append(invoice)
            self.save_to_file()

    def delete(self, invoice):
        """Usuwa fakturę z repozytorium, jeśli istnieje"""
        if invoice in self.__data_source:
            self.__data_source.remove(invoice)
            self.save_to_file()
            return True
        return False

    def update(self, invoice):
        """Aktualizuje fakturę w repozytorium, jeśli istnieje"""
        self.delete(invoice)
        self.add(invoice)

    def get_next_number(self):
        """Zwraca następny numer faktury, który powinien być użyty"""
        if not self.__data_source:  # Jeśli lista jest pusta
            return 1
        return max(inv.number for inv in self.__data_source) + 1  # Najwyższy numer + 1

    def save_to_file(self, filename="invoices.txt"):
        """Zapisuje faktury do pliku tekstowego"""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for invoice in self.__data_source:
                    f.write(f"Faktura nr {invoice.number}\n")
                    f.write(f"Klient: {invoice.customer}\n")
                    f.write("Produkty:\n")
                    for product, quantity in invoice.items:
                        f.write(f"- {product}: {quantity} szt.\n")
                    f.write("\n")
            return True
        except Exception as e:
            return False

    def delete_all(self):
        """Usuwa wszystkie faktury z repozytorium"""
        self.__data_source.clear()
        self.save_to_file()



    @property
    def data_source(self):
        """Zwraca źródło danych repozytorium - do odczytu"""
        return self.__data_source