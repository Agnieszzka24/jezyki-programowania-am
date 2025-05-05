import unittest
from generate_board import GenerateBoard


class TestGenerateBoard(unittest.TestCase):
    def setUp(self):
        self.board = GenerateBoard()

    def test_empty_board(self):
        """Czy plansza jest pusta po utworzeniu?"""
        for row in self.board.board:
            for cell in row:
                self.assertEqual(cell, ' ')

    def test_add_queen(self):
        """Czy hetman jest poprawnie dodawany?"""
        self.board.queens = []  # Wyczyść listę hetmanów
        self.board.board[0][0] = 'Q'  # Ręcznie dodaj hetmana
        self.board.queens.append((0, 0))

        self.assertEqual(self.board.board[0][0], 'Q')
        self.assertEqual(len(self.board.queens), 1)

    def test_add_pawn(self):
        """Czy pionek jest poprawnie dodawany?"""
        self.board.pawn_positions = None  # Wyczyść pozycję pionka
        self.board.board[1][1] = 'P'  # Ręcznie dodaj pionka
        self.board.pawn_positions = (1, 1)

        self.assertEqual(self.board.board[1][1], 'P')
        self.assertEqual(self.board.pawn_positions, (1, 1))

    def test_chess_notation(self):
        """Czy konwersja współrzędnych na notację szachową działa?"""
        self.assertEqual(self.board.chess_notation(0, 0), 'a8')
        self.assertEqual(self.board.chess_notation(7, 7), 'h1')
        self.assertEqual(self.board.chess_notation(3, 4), 'e5')