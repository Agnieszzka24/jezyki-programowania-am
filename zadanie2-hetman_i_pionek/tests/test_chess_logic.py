import unittest
from chess_logic import ChessLogic

class TestChessLogic(unittest.TestCase):

    def test_is_queen_threatening_pawn(self):
        """Testuje czy jeden hetman grozi pionkowi"""
        self.assertTrue(ChessLogic.is_queen_threatening_pawn((0, 0), (0, 1)))  # Ta sama kolumna
        self.assertTrue(ChessLogic.is_queen_threatening_pawn((0, 0), (1, 0)))  # Ten sam wiersz
        self.assertTrue(ChessLogic.is_queen_threatening_pawn((0, 0), (1, 1)))  # Ta sama przekątna
        self.assertFalse(ChessLogic.is_queen_threatening_pawn((0, 0), (1, 2))) # Inna pozycja
        self.assertTrue(ChessLogic.is_queen_threatening_pawn((3, 3), (5, 1)))
        self.assertFalse(ChessLogic.is_queen_threatening_pawn((3, 3), (3, 3))) # Ta sama pozycja

    def test_find_threatening_queens(self):
        queens = [(0, 0), (3, 4), (7, 7)]
        pawn_pos = (5, 4)

        # Tylko hetman (3,4) może zbić pionka (ten sam wiersz)
        threatening = ChessLogic.find_threatening_queens(queens, pawn_pos)
        self.assertEqual(len(threatening), 1)
        self.assertIn((3, 4), threatening)

        # Test z pionkiem na przekątnej
        pawn_pos = (5, 5)
        threatening = ChessLogic.find_threatening_queens(queens, pawn_pos)
        self.assertEqual(len(threatening), 2)  # (0,0) i (7,7) mogą zbić
        self.assertIn((0, 0), threatening)
        self.assertIn((7, 7), threatening)


    def test_multiple_threats(self):
        """Testuje czy funkcja znajduje wszystkie hetmany grożące pionkowi"""
        queens = [(2, 5), (5, 2), (2, 2)]
        pawn_pos = (2, 7)
        self.assertEqual(sorted(ChessLogic.find_threatening_queens(queens, pawn_pos)),
                         sorted([(2, 5), (2, 2)]))

    def test_no_threats(self):
        """Testuje czy funkcja nie znajduje hetmanów grożących pionkowi"""
        queens = [(1, 3), (4, 6), (7, 1)]
        pawn_pos = (2, 5)
        self.assertEqual(ChessLogic.find_threatening_queens(queens, pawn_pos), [])

    def test_empty_queens_list(self):
        """Testuje przypadek gdy nie ma hetmanów"""
        self.assertEqual(ChessLogic.find_threatening_queens([], (2, 2)), [])

if __name__ == '__main__':
    unittest.main()