import random
import unittest
from unittest.mock import patch

from generate_board import GenerateBoard


class TestGenerateBoard(unittest.TestCase):
    def setUp(self):
        self.board = GenerateBoard()

    def test_empty_board(self):
        """Czy plansza jest pusta po utworzeniu? - init generate_empty_board"""
        for row in self.board.board:
            for cell in row:
                self.assertEqual(cell, ' ')

    def test_add_queen(self):
        """Czy hetman jest poprawnie dodawany?"""
        self.board.queens = []  # resetuje listę hetmanów
        self.board.board[0][0] = 'Q'  # Ręcznie dodaj hetmana
        self.board.queens.append((0, 0)) # Dodaj pozycję hetmana do listy

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

    def test_max_queens_limit(self):
        """Czy blokada dodania >5 hetmanów działa?"""
        with self.assertRaises(ValueError):
            self.board.add_random_queen(6)

    def test_pawn_collision_with_queen(self):
        """Czy pionek nie może stanąć na pozycji hetmana?"""
        self.board.queens = [(3, 3)]
        self.board.board[3][3] = 'Q'
        with patch.object(random, 'randint', side_effect=[3, 3, 4, 4]):  # Najpierw (3,3) potem (4,4)
            self.board.add_random_pawn()
        self.assertEqual(self.board.pawn_positions, (4, 4))

    def test_queen_collision_with_pawn(self):
        """Czy hetman nie może stanąć na pozycji pionka?"""
        self.board.pawn_positions = (2, 2)
        self.board.board[2][2] = 'P' #oznaczamy za zajete
        with patch.object(random, 'randint', side_effect=[2, 2, 1, 1]):  # Najpierw (2,2) potem (1,1)
            self.board.add_random_queen(1)
        self.assertEqual(self.board.queens[0], (1, 1))