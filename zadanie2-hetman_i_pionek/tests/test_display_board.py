import unittest
from display_board import DisplayBoard

class TestDisplayBoard(unittest.TestCase):

    def setUp(self):
        self.displayer = DisplayBoard()
        self.queens = [(0, 0), (3, 3)]
        self.pawn_pos = (2, 2)
        self.board = [[' ' for _ in range(8)] for _ in range(8)]

    def test_display_output(self):
        """Sprawdzenie, czy plansza jest wyświetlana poprawnie"""
        try:
            self.displayer.display_board(self.board, self.queens, self.pawn_pos)
        except Exception as e:
            self.fail(f"display_board() zgłosiło błąd: {e}")

    def test_get_attacked_positions(self):
        """Sprawdzenie, czy atakowane pozycje są poprawnie obliczane"""
        attacked = self.displayer.get_attacked_positions(self.queens, 8)
        self.assertIn((0, 7), attacked)
        self.assertIn((7, 0), attacked)
        self.assertIn((5, 5), attacked)  

    def test_display_without_attacks(self):
        """Test wyświetlania bez pokazywania atakowanych pól"""
        try:
            self.displayer.display_board(self.board, self.queens, self.pawn_pos, show_attacked=False)
        except Exception as e:
            self.fail(f"display_board() zgłosiło błąd: {e}")

if __name__ == '__main__':
    unittest.main()