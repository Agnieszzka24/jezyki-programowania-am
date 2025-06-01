import unittest
from Warehouse import Warehouse
from exceptions import OutOfStore

class TestWarehouse(unittest.TestCase):
    def setUp(self):
        self.warehouse = Warehouse()
        self.warehouse.add_product("cukierki", 100, 2.50)

    def test_add_product(self):
        self.warehouse.add_product("chleb", 10, 3.00)
        self.assertEqual(self.warehouse.products["chleb"]["quantity"], 10)

    def test_remove_product(self):
        self.warehouse.remove_product("cukierki", 10)
        self.assertEqual(self.warehouse.products["cukierki"]["quantity"], 90)

    def test_remove_product_out_of_stock(self):
        with self.assertRaises(OutOfStore):
            self.warehouse.remove_product("cukierki", 200)