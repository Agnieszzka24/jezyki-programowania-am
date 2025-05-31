from abc import ABC


class InvoiceRepository(ABC):
    def __init__(self, data_source=[]):
        """Inicjalizuje repozytorium faktur z danymi źródłowymi"""
        self.__data_source = data_source

    def find_by_number(self, number):
        """Zwraca fakturę na podstawie numeru, lub None jeśli nie znaleziono"""
        return next((inv for inv in self.data_source if inv.number == number), None)

    def add(self, invoice):
        """Dodaje fakturę do repozytorium, jeśli nie istnieje już faktura o tym numerze"""
        if not self.find_by_number(invoice.number):
            self.__data_source.append(invoice)

    def delete(self, invoice):
        """Usuwa fakturę z repozytorium, jeśli istnieje"""
        self.__data_source.remove(invoice)

    def update(self, invoice):
        """Aktualizuje fakturę w repozytorium, jeśli istnieje"""
        self.delete(invoice)
        self.add(invoice)

    def get_next_number(self):
        """Zwraca następny numer faktury, który powinien być użyty"""
        return 1 if len(self.__data_source) else self.__data_source[len(self.__data_source) - 1].number + 1

    @property
    def data_source(self):
        """Zwraca źródło danych repozytorium - do odczytu"""
        return self.__data_source
