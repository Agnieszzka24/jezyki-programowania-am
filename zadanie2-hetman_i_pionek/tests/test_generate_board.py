import unittest
from generate_board import GenerateBoard

class TestGenerateBoard(unittest.TestCase):
    def setUp(self):
        self.board = GenerateBoard()

    def test_board_creation(self):
        # lista wierszy
        self.assertEqual(len(self.board.board), 8)
        # lista kolumn
        self.assertEqual(len(self.board.board[0]), 8)

    def test_empty_board(self):
        # Sprawdzenie, czy wszystkie pola są puste
        for row in self.board.board:
            self.assertTrue(all(cell == ' ' for cell in row))

    def test_display_output(self):
        try:
            self.board.display_board()
        except Exception as e:
            self.fail(f"display_board() zgłosiło błąd: {e}")