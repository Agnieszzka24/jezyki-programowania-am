import unittest
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
        queens = [(0, 0), (3, 3), (7, 0)]  # Hetmany
        pawn_pos = (3, 0)  # Pionek

        # (0,0) - ta sama kolumna (0)
        # (3,3) - przekątna (różnica x i y = 3)
        # (7,0) - ta sama kolumna (0)
        threats = ChessLogic.find_threatening_queens(queens, pawn_pos)

        # Powinny być 3 grożące hetmany!
        self.assertEqual(len(threats), 3)
        self.assertIn((0, 0), threats)
        self.assertIn((3, 3), threats)
        self.assertIn((7, 0), threats)

    def test_no_threats(self):
        """Czy brak zagrożeń jest poprawnie wykrywany?"""
        queens = [(1, 3), (2, 5)]  # Hetmany
        pawn_pos = (4, 4)  # Pionek

        # Żaden hetman nie grozi pionkowi
        threats = ChessLogic.find_threatening_queens(queens, pawn_pos)
        self.assertEqual(threats, [])