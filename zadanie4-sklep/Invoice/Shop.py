from abc import ABC

from Invoice.InvoiceObject import InvoiceObject
from Invoice.Warehouse import Warehouse
from Invoice.exceptions import OutOfStore

class Shop(ABC):
    def __init__(self, repository=None, warehouse=None):
        self.__invoice_repository = repository
        self.__warehouse = warehouse

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

        # Stwórz fakturę
        invoice = InvoiceObject(number=self.__invoice_repository.get_next_number(),
                         customer=customer,
                         items=items_list)
        self.__invoice_repository.add(invoice)
        self.__invoice_repository.save_to_file()
        return invoice

    def returning_goods(self, invoice, items_to_return: list[tuple[str, int]] = None):
        """Zwrot całościowy lub częściowy towarów. Aktualizuje magazyn."""
        if not self.__invoice_repository.find_by_number(invoice.number):
            return False

        # Jeśli nie podano listy, zwróć wszystko z faktury - zwrot całościowy
        if items_to_return is None:
            items_to_return = invoice.items

        # Przyjmij produkty z powrotem do magazynu - zwrot częściowy
        for product_name, quantity in items_to_return:
            self.__warehouse.add_product(product_name, quantity,
            self.__warehouse.get_product_info(product_name)["price"])

        # Aktualizuj listę produktów na fakturze (tylko dla częściowego zwrotu)
        if items_to_return is not None and set(items_to_return) != set(invoice.items):
            new_items = []
            for product, qty in invoice.items:
                for returned_product, returned_qty in items_to_return:
                    if product == returned_product:
                        qty -= returned_qty
                if qty > 0:
                    new_items.append((product, qty))
            invoice.items = new_items
            self.__invoice_repository.update(invoice)

        # Jeśli zwrócono wszystko, usuń fakturę
        if set(items_to_return) == set(invoice.items):
            self.__invoice_repository.delete(invoice)
        else:
            self.__invoice_repository.update(invoice)
        self.__invoice_repository.save_to_file()
        return True

    @property
    def warehouse(self):
        return self.__warehouse