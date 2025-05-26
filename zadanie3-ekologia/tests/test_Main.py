# tests/test_Main.py
import sys
import os
import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'begin')))

from Main import print_menu, add_organism_menu
from Position import Position


class TestMain(unittest.TestCase):
    """Testy jednostkowe dla funkcji w Main.py"""
    def test_print_menu(self):
        """Test wyświetlania menu"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_menu()
            output = fake_out.getvalue()
            self.assertIn("1. Przejdź do kolejnej tury", output)

    @patch('builtins.input', side_effect=['S', '1', '1'])  # owca, pozycja 1,1
    def test_add_organism_menu_valid(self, mock_input):
        """Test dodawania organizmu do świata"""
        world_mock = MagicMock()
        world_mock.worldX = 10
        world_mock.worldY = 10
        world_mock.add_custom_organism.return_value = True
        add_organism_menu(world_mock)
        world_mock.add_custom_organism.assert_called_once_with('S', Position(xPosition=1, yPosition=1))

    @patch('builtins.input', side_effect=['X', '1', '1'])  # Nieprawidłowy typ organizmu X
    def test_add_organism_menu_invalid_type(self, mock_input):
        """Test dodawania organizmu z nieprawidłowym typem"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            world_mock = MagicMock()
            add_organism_menu(world_mock)
            self.assertIn("Nieprawidłowy typ organizmu!", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()