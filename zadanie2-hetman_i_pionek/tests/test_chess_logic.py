import unittest
from unittest.mock import MagicMock

from chess_logic import ChessLogic


class TestChessLogic(unittest.TestCase):
    def test_queen_threat(self):
        """Czy hetman grozi pionkowi w różnych sytuacjach?"""
        # Ta sama kolumna
        self.assertTrue(ChessLogic.is_queen_threatening_pawn((0, 0), (7, 0)))
        # Ten sam wiersz
        self.assertTrue(ChessLogic.is_queen_threatening_pawn((3, 3), (3, 7)))
        # Ta sama przekątna
        self.assertTrue(ChessLogic.is_queen_threatening_pawn((0, 0), (7, 7)))
        # Brak zagrożenia
        self.assertFalse(ChessLogic.is_queen_threatening_pawn((0, 0), (1, 2)))
        # To samo pole
        self.assertFalse(ChessLogic.is_queen_threatening_pawn((3, 3), (3, 3)))

    def test_find_threatening_queens(self):
        """Czy znajdujemy hetmany grożące pionkowi?"""
        queens = [(0, 0), (3, 3), (7, 0)]
        pawn_pos = (3, 0)

        threats = ChessLogic.find_threatening_queens(queens, pawn_pos)

        self.assertEqual(len(threats), 3)
        # (0,0) - ta sama kolumna (0)
        self.assertIn((0, 0), threats)
        # (3,3) - przekątna (różnica x i y = 3)
        self.assertIn((3, 3), threats)
        # (7,0) - ta sama kolumna (0)
        self.assertIn((7, 0), threats)

    def test_no_threats(self):
        """Czy brak zagrożeń jest poprawnie wykrywany?"""
        queens = [(1, 3), (2, 5)]
        pawn_pos = (4, 4)

        # Żaden hetman nie grozi pionkowi
        threats = ChessLogic.find_threatening_queens(queens, pawn_pos)
        self.assertEqual(threats, [])

    def test_empty_queens_list(self):
        """Czy brak hetmanów jest poprawnie obsługiwany?"""
        threats = ChessLogic.find_threatening_queens([], (4, 4))
        self.assertEqual(threats, [])

    def test_edge_positions(self):
        """Czy hetman w narożniku poprawnie atakuje?"""
        # Hetman w (0,0), pionek w (7,7) - ta sama przekątna
        self.assertTrue(ChessLogic.is_queen_threatening_pawn((0, 0), (7, 7)))

        # Hetman w (7,0), pionek w (0,7) - przeciwna przekątna
        self.assertTrue(ChessLogic.is_queen_threatening_pawn((7, 0), (0, 7)))

    def test_multiple_threats(self):
        """Czy wykrywa wszystkie hetmany grożące pionkowi?"""
        queens = [(1, 1), (1, 5), (5, 1), (5, 5)]  # 4 hetmany w rogach
        pawn_pos = (3, 3)  # Pionek w centrum

        threats = ChessLogic.find_threatening_queens(queens, pawn_pos)
        self.assertEqual(len(threats), 4)  # Wszystkie powinny grozić
