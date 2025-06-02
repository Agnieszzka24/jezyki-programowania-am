import unittest
from unittest.mock import patch, MagicMock
from Invoice.InvoiceObject import InvoiceObject
import Main


class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', 'banan', '10', '3.50', '0'])
    @patch.object(Main.warehouse, 'add_product')
    def test_add_product(self, mock_add, mock_input):
        """Test dodawania produktu do magazynu"""
        Main.main()
        mock_add.assert_called_with("banan", 10, 3.50)

    @patch('builtins.input', side_effect=['2', 'Jan', 'chleb', '2', 'koniec', '0'])
    @patch.object(Main.shop, 'buy')
    def test_buy_products(self, mock_buy, mock_input):
        """Test sprzedaży produktów"""
        mock_buy.return_value = InvoiceObject(number=1, customer="Jan", items=[("chleb", 2)])
        Main.main()
        mock_buy.assert_called_once_with("Jan", [("chleb", 2)])

    @patch('builtins.input', side_effect=['3', '1', 'T', '0'])
    @patch.object(Main.shop, 'returning_goods')
    def test_return_all_products(self, mock_return, mock_input):
        """Test zwrotu wszystkich produktów"""
        invoice = InvoiceObject(number=1, customer="Jan", items=[("chleb", 2)])
        Main.invoice_repo.add(invoice)

        Main.main()
        mock_return.assert_called_once_with(invoice)

    @patch('builtins.input', side_effect=['4', '0'])
    def test_show_warehouse_status(self, mock_input):
        """Test wyświetlania stanu magazynu"""
        Main.warehouse.add_product("test", 10, 5.0)
        with patch('builtins.print') as mock_print:
            Main.main()
            output = "".join(str(call) for call in mock_print.call_args_list)
            self.assertIn("test", output)

    @patch('builtins.input', side_effect=['5', '0'])
    def test_show_invoices(self, mock_input):
        """Test wyświetlania faktur"""
        invoice = InvoiceObject(number=1, customer="Jan", items=[("chleb", 2)])
        Main.invoice_repo.add(invoice)

        with patch('builtins.print') as mock_print:
            Main.main()
            output = "".join(str(call) for call in mock_print.call_args_list)
            self.assertIn("Nr 1", output)

    @patch('builtins.input', side_effect=['6', '0'])
    @patch.object(Main.invoice_repo, 'save_to_file')
    def test_save_invoices_to_file(self, mock_save, mock_input):
        """Test zapisu faktur do pliku"""
        mock_save.return_value = True
        Main.main()
        mock_save.assert_called_once()

    @patch('builtins.input', side_effect=['7', 'T', '0'])
    @patch.object(Main.invoice_repo, 'delete_all')
    def test_delete_all_invoices(self, mock_delete, mock_input):
        """Test usuwania wszystkich faktur"""
        invoice = InvoiceObject(number=1, customer="Jan", items=[("chleb", 2)])
        Main.invoice_repo.add(invoice)

        Main.main()
        mock_delete.assert_called_once()


if __name__ == '__main__':
    unittest.main()