from abc import ABC

from .exceptions import OutOfStore


class Warehouse(ABC):
    def __init__(self):
        self.__products = {}  # Format: {product_name: {"quantity": int, "price": float}}

    def add_product(self, product_name: str, quantity: int, price: float):
        """Dodaje produkt do magazynu lub zwiększa jego ilość."""
        if product_name in self.__products:
            self.__products[product_name]["quantity"] += quantity
        else:
            self.__products[product_name] = {"quantity": quantity, "price": price}

    def remove_product(self, product_name: str, quantity: int):
        """Usuwa produkt z magazynu. Rzuca wyjątek OutOfStore, jeśli brakuje produktu."""
        if product_name not in self.__products or self.__products[product_name]["quantity"] < quantity:
            raise OutOfStore(f"Brak wystarczającej ilości produktu: {product_name}")
        self.__products[product_name]["quantity"] -= quantity

    def get_product_info(self, product_name: str) -> dict:
        """Zwraca informacje o produkcie (ilość, cenę)."""
        return self.__products.get(product_name, None)

    @property
    def products(self) -> dict:
        """Zwraca cały stan magazynu (tylko do odczytu)."""
        return self.__products.copy()