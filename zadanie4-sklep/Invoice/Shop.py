from abc import ABC

from .exceptions import OutOfStore
from .Invoice import Invoice
from .InvoiceRepository import InvoiceRepository
from .Warehouse import Warehouse

class Shop(ABC):
    def __init__(self, repository=None, warehouse=None):
        self.__invoice_repository = repository
        self.__warehouse = warehouse  # Nowy parametr: magazyn

    def buy(self, customer: str, items_list: list[tuple[str, int]]):
        """Sprzedaż produktów. Aktualizuje magazyn i tworzy fakturę."""
        # Sprawdź dostępność produktów w magazynie
        for product_name, quantity in items_list:
            if not self.__warehouse.get_product_info(product_name) or \
               self.__warehouse.get_product_info(product_name)["quantity"] < quantity:
                raise OutOfStore(f"Brak produktu: {product_name}")

        # Wydaj produkty z magazynu
        for product_name, quantity in items_list:
            self.__warehouse.remove_product(product_name, quantity)

        # Stwórz fakturę (istniejąca logika)
        invoice = Invoice(number=self.invoice_repository.get_next_number(),
                         customer=customer,
                         items=items_list)
        self.invoice_repository.add(invoice)
        return invoice

    def returning_goods(self, invoice, items_to_return: list[tuple[str, int]] = None):
        """Zwrot całościowy lub częściowy towarów. Aktualizuje magazyn."""
        if not self.invoice_repository.find_by_number(invoice.number):
            return False

        # Jeśli nie podano listy, zwróć wszystko z faktury
        if items_to_return is None:
            items_to_return = invoice.items

        # Przyjmij produkty z powrotem do magazynu
        for product_name, quantity in items_to_return:
            self.__warehouse.add_product(product_name, quantity,
                                        self.__warehouse.get_product_info(product_name)["price"])

        # Jeśli zwrócono wszystko, usuń fakturę
        if set(items_to_return) == set(invoice.items):
            self.invoice_repository.delete(invoice)
        return True

    @property
    def warehouse(self):
        return self.__warehouse