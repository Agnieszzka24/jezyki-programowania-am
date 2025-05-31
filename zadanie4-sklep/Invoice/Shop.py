from abc import ABC
from Invoice import Invoice


class Shop(ABC):
    def __init__(self, repository=None):
        """Inicjalizuje sklep z repozytorium faktur"""
        self.__invoice_repository = repository

    def buy(self, customer, items_list):
        """Tworzy fakturę na podstawie klienta i listy pozycji, dodaje ją do repozytorium"""
        invoice = Invoice(number=self.invoice_repository.get_next_number(), customer=customer, items=items_list)
        self.invoice_repository.add(invoice)
        return invoice

    def returning_goods(self, invoice):
        """Zwraca towary na podstawie faktury, usuwa fakturę z repozytorium jeśli istnieje"""
        if self.invoice_repository.find_by_number(invoice.number):
            self.invoice_repository.delete(invoice)
            return True
        else:
            return False

    @property
    def invoice_repository(self):
        """Zwraca repozytorium faktur - do odczytu"""
        return self.__invoice_repository
