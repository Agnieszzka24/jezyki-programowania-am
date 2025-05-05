import unittest
from unittest.mock import patch, MagicMock
from game_controller import GameController


class TestGameController(unittest.TestCase):
    def setUp(self):
        self.controller = GameController()
        self.controller.board = MagicMock()
        self.controller.display = MagicMock()
        self.controller.board.pawn_positions = (0, 0)  # Ustaw pozycję pionka
        self.controller.board.queens = [(0, 0), (1, 1)]

    def test_user_choice(self):
        """Czy wybór użytkownika jest poprawnie obsługiwany?"""
        with patch('builtins.input', return_value='1'):
            choice = self.controller._get_user_choice()
            self.assertEqual(choice, 1)

        with patch('builtins.input', side_effect=['5', '2']):
            choice = self.controller._get_user_choice()
            self.assertEqual(choice, 2)

    def test_move_pawn(self):
        """Czy pionek jest poprawnie przemieszczany?"""
        with patch.object(self.controller.board, 'add_random_pawn') as mock_add:
            self.controller._move_pawn()
            mock_add.assert_called_once()

    def test_remove_queen(self):
        """Czy hetman jest poprawnie usuwany?"""
        with patch('builtins.input', return_value='1'):
            self.controller._remove_queen()
            self.assertEqual(len(self.controller.board.queens), 1)