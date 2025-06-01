import unittest
from unittest.mock import Mock
from Invoice.Shop import Shop
from Invoice.InvoiceRepository import InvoiceRepository
from Invoice import InvoiceObject


class ShopTests(unittest.TestCase):
    def test_while_buy_the_repository_add_should_be_called(self):
        """Testuje, czy podczas zakupu faktura jest dodawana do repozytorium"""
        spy_repository = Mock(InvoiceRepository)
        shop = Shop(spy_repository)
        shop.buy(customer="Jan", items_list=["cukierki"])
        spy_repository.add.assert_called_once()

    def test_while_returning_goods_the_repository_returns_false_when_not_find(self):
        """Testuje, czy podczas zwrotu towarów, jeśli faktura nie istnieje, zwraca False"""
        stub_repository = Mock(InvoiceRepository)
        shop = Shop(stub_repository)
        stub_repository.find_by_number.return_value = None
        result = shop.returning_goods(Mock(InvoiceObject))
        self.assertEqual(result, False)

    def test_while_returning_goods_the_repository_delete_should_be_called_when_find(self):
        """Testuje, czy podczas zwrotu towarów, jeśli faktura istnieje, jest usuwana z repozytorium"""
        spy_repository = Mock(InvoiceRepository)
        shop = Shop(spy_repository)
        spy_repository.find_by_number.return_value = InvoiceObject()
        shop.returning_goods(Mock(InvoiceObject))
        spy_repository.delete.assert_called_once()
