import unittest
from unittest.mock import patch, MagicMock
from game_controller import GameController
from generate_board import GenerateBoard


class TestGameController(unittest.TestCase):
    def setUp(self):
        """Mockowanie obiektów"""
        self.game = GameController()

        self.game.board = MagicMock(spec=GenerateBoard)
        self.game.display = MagicMock()

        # ustawienie potrzebnych atrybutów
        self.game.board.queens = [(0, 0), (1, 1), (2, 2)]
        self.game.board.pawn_positions = (3, 3)
        self.game.board.chess_notation = lambda x, y: f"{chr(97 + y)}{8 - x}"
        self.game.board.board = [[' ' for _ in range(8)] for _ in range(8)]  # dodanie planszy

    def test_initialize_game(self):
        """Testowanie inicjalizacji gry"""
        self.game.initialize_game()
        self.game.board.add_random_queen.assert_called_once()
        self.game.board.add_random_pawn.assert_called_once()

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice(self, mock_input):
        """Testowanie pobierania wyboru użytkownika"""
        choice = self.game.get_user_choice()
        self.assertEqual(choice, 1)

    @patch('builtins.input', side_effect=['5', '2'])
    def test_get_user_choice_invalid(self, mock_input):
        """Testowanie niepoprawnego wyboru"""
        choice = self.game.get_user_choice()
        self.assertEqual(choice, 2)

    def test_move_pawn(self):
        """Test zmiany pozycji pionka"""
        self.game.move_pawn()
        self.game.board.add_random_pawn.assert_called_once()

    @patch('builtins.input', side_effect=['1'])
    def test_remove_queen_valid(self, mock_input):
        """Test usunięcia hetmana"""
        initial_count = len(self.game.board.queens)
        result = self.game.remove_queen()
        self.assertTrue(result)
        self.assertEqual(len(self.game.board.queens), initial_count - 1)

    @patch('builtins.input', side_effect=['0'])
    def test_remove_queen_cancelled(self, mock_input):
        """Test anulowania usunięcia hetmana"""
        initial_count = len(self.game.board.queens)
        result = self.game.remove_queen()
        self.assertFalse(result)
        self.assertEqual(len(self.game.board.queens), initial_count)

    @patch('chess_logic.ChessLogic.find_threatening_queens')
    def test_check_pawn_threat(self, mock_find):
        """Test sprawdzania zagrożenia pionka"""
        # Przypadek z zagrożeniem
        mock_find.return_value = [(0, 0), (1, 1)]
        with patch('builtins.print') as mock_print:
            self.game.check_pawn_threat()
            mock_find.assert_called_once_with(self.game.board.queens, self.game.board.pawn_positions)
            mock_print.assert_any_call("\n Pionek może być zbity przez:")
            mock_print.assert_any_call(" - a8")

        # Przypadek bezpieczny
        mock_find.reset_mock()
        mock_find.return_value = []
        with patch('builtins.print') as mock_print:
            self.game.check_pawn_threat()
            mock_print.assert_called_with("\n Pionek jest bezpieczny")

    def test_display_current_state(self):
        """Test wyświetlania stanu gry"""
        with patch('builtins.print'):
            self.game.display_current_state()
            self.game.display.display_board.assert_called_once_with(
                self.game.board.board,
                self.game.board.queens,
                self.game.board.pawn_positions
            )


if __name__ == '__main__':
    unittest.main()