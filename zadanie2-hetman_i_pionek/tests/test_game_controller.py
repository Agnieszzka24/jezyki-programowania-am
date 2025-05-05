import unittest
from unittest.mock import patch, MagicMock
from game_controller import GameController
from chess_logic import ChessLogic


class TestGameController(unittest.TestCase):
    def setUp(self):
        self.controller = GameController()
        self.controller.board = MagicMock()
        self.controller.display = MagicMock()
        self.controller.board.pawn_positions = (0, 0)
        self.controller.board.queens = [(0, 0), (1, 1)]

    def test_initialize_game(self):
        """Czy gra poprawnie inicjalizuje planszę z losową liczbą hetmanów?"""
        # tymaczasowe zastępanienie metody mockiem
        with patch.object(self.controller.board, 'add_random_queen') as mock_queen, \
                patch.object(self.controller.board, 'add_random_pawn') as mock_pawn:
            #wywyłanie metody i spr czy została wywołana dokładnie raz
            self.controller._initialize_game()
            mock_queen.assert_called_once()
            mock_pawn.assert_called_once()

    def test_display_state(self):
        """Czy metoda wyświetla aktualny stan planszy?"""
        with patch.object(self.controller.display, 'display_board') as mock_display, \
                patch.object(ChessLogic, 'check_threats') as mock_check:
            self.controller._display_current_state()
            mock_display.assert_called_once()
            mock_check.assert_called_once_with(self.controller.board) # została wywłana raz i z odpowiednim argumentem

    def test_user_choice(self):
        """Czy wybór użytkownika jest poprawnie obsługiwany?"""
        with patch('builtins.input', return_value='1'):  # symulacja wyboru użytkownika
            choice = self.controller._get_user_choice()
            self.assertEqual(choice, 1)

        with patch('builtins.input', side_effect=['5', '2']):
            choice = self.controller._get_user_choice()
            self.assertEqual(choice, 2)

    def test_invalid_user_choice(self):
        """Czy program obsługuje nieprawidłowy wybór użytkownika?"""
        with patch('builtins.input', side_effect=['abc', '5', '3']), \
                patch('builtins.print') as mock_print:
            choice = self.controller._get_user_choice()
            self.assertEqual(choice, 3)
            self.assertTrue(mock_print.called)

    def test_cancel_queen_removal(self):
        """Czy można anulować usuwanie hetmana?"""
        with patch('builtins.input', return_value='0'):
            initial_queens = len(self.controller.board.queens)
            self.controller._remove_queen()
            self.assertEqual(len(self.controller.board.queens), initial_queens)

    def test_successful_queen_removal(self):
        """Czy hetman jest poprawnie usuwany z planszy?"""
        initial_count = len(self.controller.board.queens)
        with patch('builtins.input', return_value='1'):
            self.controller._remove_queen()
            self.assertEqual(len(self.controller.board.queens), initial_count - 1)

    def test_move_pawn(self):
        """Czy pionek jest poprawnie przemieszczany?"""
        with patch.object(self.controller.board, 'add_random_pawn') as mock_add:
            self.controller._move_pawn()
            mock_add.assert_called_once() #śledzi wywołanie metody

    def test_remove_queen(self):
        """Wywołanie metody usuwającej hetmana"""
        with patch('builtins.input', return_value='1'):
            self.controller._remove_queen()
            self.assertEqual(len(self.controller.board.queens), 1)

    def test_check_threats(self):
        """Czy metoda wymusza sprawdzenie zagrożeń? - czy została wywołana"""
        with patch.object(ChessLogic, 'check_threats') as mock_check:
            self.controller._check_threats()
            mock_check.assert_called_once_with(self.controller.board)

    def test_exit_game(self):
        """Czy gra poprawnie się zamyka?"""
        with patch('builtins.print') as mock_print:
            self.controller._exit_game()
            mock_print.assert_called_with("\nDziękujemy za grę!")