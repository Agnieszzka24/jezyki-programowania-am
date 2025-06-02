import unittest
from unittest.mock import Mock, MagicMock
from Invoice.Shop import Shop
from Invoice.InvoiceRepository import InvoiceRepository
from Invoice.InvoiceObject import InvoiceObject
from Invoice.exceptions import OutOfStore


class ShopTests(unittest.TestCase):

    def test_shop_initialization_with_dummy_objects(self):
        """Dummy -Test inicjalizacji Shop z dummy objects"""
        dummy_repository = object()  # Tworzymy dummy objects - puste atrapy, które nic nie robią
        dummy_warehouse = object()
        shop = Shop(repository=dummy_repository, warehouse=dummy_warehouse)
        self.assertIsInstance(shop, Shop)  # Testujemy tylko czy inicjalizacja się powiodła
        self.assertIs(shop.warehouse, dummy_warehouse) # Weryfikacja czy dummy objects zostały przypisane

    def test_while_buy_the_repository_add_should_be_called(self):
        """Spy-  Testuje, czy podczas zakupu faktura jest dodawana do repozytorium"""
        spy_repository = Mock(InvoiceRepository)
        spy_repository.get_next_number.return_value = 1
        spy_warehouse = Mock()
        spy_warehouse.get_product_info.return_value = {"quantity": 10, "price": 5.0}
        shop = Shop(spy_repository, spy_warehouse)
        shop.buy(customer="Jan", items_list=[("cukierki", 1)])
        spy_repository.add.assert_called_once()

    def test_while_returning_goods_the_repository_returns_false_when_not_find(self):
        """Stub-  Testuje, czy podczas zwrotu towarów, jeśli faktura nie istnieje, zwraca False"""
        stub_repository = Mock(InvoiceRepository) # Mock repozytorium
        stub_warehouse = Mock()
        shop = Shop(stub_repository, stub_warehouse) # Inicjalizacja sklepu z mockami
        stub_repository.find_by_number.return_value = None #konfiguracja stub dla repozytorium, aby zwracało None
        result = shop.returning_goods(InvoiceObject(number=1, customer="Test", items=[("prod", 1)])) # Wywołanie metody
        self.assertEqual(result, False)

    def test_while_returning_goods_the_repository_delete_should_be_called_when_find(self):
        """Testuje, czy podczas zwrotu towarów, jeśli faktura istnieje, jest usuwana z repozytorium"""
        spy_repository = Mock(InvoiceRepository)
        spy_warehouse = Mock()
        spy_warehouse.get_product_info.return_value = {"quantity": 10, "price": 5.0}
        shop = Shop(spy_repository, spy_warehouse)
        invoice = InvoiceObject(number=1, customer="Test", items=[("prod", 1)])
        spy_repository.find_by_number.return_value = invoice
        shop.returning_goods(invoice)
        spy_repository.delete.assert_called_once_with(invoice)
        spy_warehouse.add_product.assert_called_once_with("prod", 1, 5.0)

    def test_buy_with_mock_verifies_interactions(self):
        """mock- Test z użyciem mocków do weryfikacji interakcji z Warehouse"""
        mock_repo = Mock(InvoiceRepository)  # Mock repozytorium faktur
        mock_repo.get_next_number.return_value = 1
        mock_warehouse = Mock()  # Mock magazynu
        mock_warehouse.get_product_info.return_value = {"quantity": 10, "price": 5.0}

        shop = Shop(mock_repo, mock_warehouse)  #wywołanie metody buy z przykładowymi danymi
        result = shop.buy(customer="Jan", items_list=[("produkt1", 2)])

        self.assertIsInstance(result, InvoiceObject) # Sprawdzenie, czy wynik jest instancją InvoiceObject
        mock_warehouse.get_product_info.assert_called_with("produkt1")
        mock_warehouse.remove_product.assert_called_with("produkt1", 2)
        mock_repo.add.assert_called_once()

    def test_buy_with_stub_returns_correct_invoice(self):
        """Test z użyciem stubów do izolacji logiki Shop"""

        class StubRepository:
            def get_next_number(self):
                return 1

            def add(self, invoice):
                pass

            def save_to_file(self):
                pass

        class StubWarehouse:
            def get_product_info(self, product_name):
                return {"quantity": 10, "price": 5.0}

            def remove_product(self, product_name, quantity):
                pass

        shop = Shop(StubRepository(), StubWarehouse())
        result = shop.buy(customer="Anna", items_list=[("produktA", 1)])

        self.assertEqual(result.number, 1)
        self.assertEqual(result.customer, "Anna")
        self.assertEqual(result.items, [("produktA", 1)])

    def test_returning_goods_with_spy_tracks_calls(self):
        """Test z użyciem spy do śledzenia wywołań metod"""
        spy_repo = MagicMock(spec=InvoiceRepository)
        spy_warehouse = MagicMock()
        invoice = InvoiceObject(number=1, customer="Test", items=[("produkt1", 2)])
        spy_repo.find_by_number.return_value = invoice

        shop = Shop(spy_repo, spy_warehouse)
        shop.returning_goods(invoice, [("produkt1", 1)])

        spy_warehouse.add_product.assert_called_once()
        spy_repo.update.assert_called_once()

    def test_buy_with_fake_implementation(self):
        """Fake- Test z użyciem fake'ów - uproszczonych implementacji"""

        class FakeRepository: # Fake implementacja repozytorium faktur (InvoiceRepository)
            def __init__(self):
                # Inicjalizacja pustej listy faktur i numeru następnej faktury
                self.invoices = []
                self.next_number = 1

            def get_next_number(self):
                """Zwraca następny numer faktury"""
                return self.next_number

            def add(self, invoice):
                """Dodaje fakturę do repozytorium"""
                self.invoices.append(invoice)
                self.next_number += 1

            def save_to_file(self):
                pass

        class FakeWarehouse: # Fake implementacja magazynu
            def __init__(self):
                # Inicjalizacja przykładowych produktów w magazynie
                self.products = {"produkt1": {"quantity": 10, "price": 5.0}}

            def get_product_info(self, product_name):
                """Zwraca informacje o produkcie lub None jeśli nie istnieje"""
                return self.products.get(product_name)

            def remove_product(self, product_name, quantity):
                """Usuwa produkt z magazynu"""
                self.products[product_name]["quantity"] -= quantity

        fake_repo = FakeRepository()
        fake_warehouse = FakeWarehouse()
        shop = Shop(fake_repo, fake_warehouse) # Inicjalizacja sklepu z fake'ami
        result = shop.buy(customer="Fake", items_list=[("produkt1", 2)]) # Wywołanie metody buy

        self.assertEqual(len(fake_repo.invoices), 1)
        # Sprawdzenie, czy ilość produktu została zaktualizowana z 10 do 8
        self.assertEqual(fake_warehouse.products["produkt1"]["quantity"], 8)

    def test_buy_out_of_stock_raises_exception(self):
        """Test zachowania przy braku produktu w magazynie"""
        mock_repo = Mock(InvoiceRepository)
        mock_warehouse = Mock()
        mock_warehouse.get_product_info.return_value = None

        shop = Shop(mock_repo, mock_warehouse)
        with self.assertRaises(OutOfStore):
            shop.buy("test", [("brakujący", 1)])

    def test_return_all_goods_deletes_invoice(self):
        """Test zwrotu wszystkich towarów z faktury"""
        spy_repo = MagicMock(spec=InvoiceRepository)
        spy_warehouse = MagicMock()
        invoice = InvoiceObject(number=1, customer="Test", items=[("produkt1", 2)])
        spy_repo.find_by_number.return_value = invoice

        shop = Shop(spy_repo, spy_warehouse)
        shop.returning_goods(invoice)

        self.assertEqual(spy_warehouse.add_product.call_count, 1)
        spy_repo.delete.assert_called_once_with(invoice)


if __name__ == '__main__':
    unittest.main()