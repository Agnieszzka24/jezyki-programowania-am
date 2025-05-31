from abc import ABC


class Invoice(ABC):
    def __init__(self, number=None, customer=None, items=None):
        """Inicjalizuje fakturę z numerem, klientem i listą pozycji"""
        self.__number = number
        self.__customer = customer
        self.__items = items

    def __eq__(self, other):
        """Porównuje faktury na podstawie numeru - definiuje równość faktur"""
        if isinstance(other, Invoice):
            return self.number == other.number
        else:
            return False

    def __hash__(self):
        """Zwraca hash faktury na podstawie numeru - pozwala używać faktur w słownikach i zbiorach"""
        return hash(self.number)

    def __repr__(self):
        """Zwraca reprezentację faktury - reprezentacja tekstowa obiektu"""
        return f"Invoice({self.number}, {self.customer}, {self.items})"

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

