import unittest
from display_board import DisplayBoard


class TestDisplayBoard(unittest.TestCase):
    def setUp(self):
        self.display = DisplayBoard()
        self.queens = [(0, 0), (3, 3)]
        self.pawn_pos = (4, 4)
        self.board = [[' ' for _ in range(8)] for _ in range(8)]

    def test_attacked_positions(self):
        """Czy atakowane pozycje są poprawnie obliczane?"""
        attacked = self.display.get_attacked_positions(self.queens, 8)

        # Sprawdź kilka kluczowych pozycji
        self.assertIn((0, 7), attacked)  # Koniec wiersza
        self.assertIn((7, 0), attacked)  # Koniec kolumny
        self.assertIn((5, 5), attacked)  # Przekątna

    def test_display_output(self):
        """Czy wyświetlanie planszy działa bez błędów?"""
        try:
            self.display.display_board(self.board, self.queens, self.pawn_pos) # Wywołanie metody wyświetlającej planszę
        except Exception as e:
            self.fail(f"Wyświetlanie planszy zgłosiło błąd: {e}")