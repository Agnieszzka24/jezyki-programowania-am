import unittest
from generate_board import GenerateBoard

class TestGenerateBoard(unittest.TestCase):
    def setUp(self):
        self.board = GenerateBoard()
        self.board_with_figures = GenerateBoard()
        self.board_with_figures.add_random_queen(3)
        self.board_with_figures.add_random_pawn()

    def test_board_creation(self):
        """Sprawdzenie, czy plansza została poprawnie utworzona"""
        # lista wierszy
        self.assertEqual(len(self.board.board), 8)
        # lista kolumn
        self.assertEqual(len(self.board.board[0]), 8)

    def test_empty_board(self):
        """Sprawdzenie, czy wszystkie pola są puste"""
        for row in self.board.board:
            self.assertTrue(all(cell == ' ' for cell in row))

    def test_display_output(self):
        """Sprawdzenie, czy plansza jest wyświetlana poprawnie"""
        try:
            self.board.display_board()
        except Exception as e:
            self.fail(f"display_board() zgłosiło błąd: {e}")

    def test_add_queen(self):
        """Sprawdzenie, czy mamy 3 hetmany na planszy"""
        self.assertEqual(len(self.board_with_figures.queens), 3)
        for x, y in self.board_with_figures.queens:
            self.assertEqual(self.board_with_figures.board[x][y], 'Q')

    def test_add_pawn(self):
        """Sprawdzanie czy pionek jest na planszy"""
        self.assertIsNotNone(self.board_with_figures.pawn_positions)
        x, y = self.board_with_figures.pawn_positions
        self.assertEqual(self.board_with_figures.board[x][y], 'P')

    def test_if_not_collisions(self):
        """Czy figury nie nakładają się na siebie?"""
        queens = self.board_with_figures.queens
        pawn_pos = self.board_with_figures.pawn_positions

        self.assertNotIn(pawn_pos, queens)
        self.assertEqual(len(queens), len(set(queens)))

    def test_chess_notation(self):
        """Czy konwersja do notacji szachowej działa poprawnie?"""
        test_cases = [
            ((0, 0), 'a8'),
            ((7, 7), 'h1'),
            ((3, 4), 'e5'),
            ((1, 2), 'c7')
        ]

        for (x, y), expected in test_cases:
            result = self.board.chess_notation(x, y)
            self.assertEqual(result, expected , f"Dla ({x}, {y}) oczekiwano {expected}, a otrzymano {result}")

if __name__ == '__main__':
    unittest.main()









