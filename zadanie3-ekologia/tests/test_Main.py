# tests/test_Main.py
import sys
import os
import unittest
from io import StringIO
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'begin')))

from Main import print_menu, add_organism_menu


class TestMain(unittest.TestCase):
    def test_print_menu(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_menu()
            output = fake_out.getvalue().strip()
            self.assertIn("1. Przejdź do kolejnej tury", output)

    @patch('builtins.input', side_effect=['S', '1', '1'])
    def test_add_organism_menu_valid(self, mock_input):
        world_mock = unittest.mock.MagicMock()
        world_mock.worldX = 10
        world_mock.worldY = 10
        world_mock.add_custom_organism.return_value = True

        add_organism_menu(world_mock)
        world_mock.add_custom_organism.assert_called_once()


if __name__ == '__main__':
    unittest.main()