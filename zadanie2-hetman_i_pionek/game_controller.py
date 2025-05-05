import random
from display_board import DisplayBoard
from chess_logic import ChessLogic
from generate_board import GenerateBoard


class GameController:
    def __init__(self):
        """Inicjalizacja kontrolera gry"""
        self.board = GenerateBoard()
        self.display = DisplayBoard()



    def start_game(self):
        """Główna metoda uruchamiająca grę"""
        self._initialize_game()
        self.run()



    def _initialize_game(self):
        """Inicjalizacja nowej gry z losową liczbą hetmanów"""
        queens_number = random.randint(1, 5)
        self.board.add_random_queen(queens_number)
        self.board.add_random_pawn()



    def run(self):
        """Główna pętla gry"""
        while True:
            self._display_current_state()
            choice = self._get_user_choice()

            if choice == 1:
                self._move_pawn()
            elif choice == 2:
                self._remove_queen()
            elif choice == 3:
                self._check_threats()
            elif choice == 4:
                self._exit_game()
                break



    def _display_current_state(self):
        """Wyświetla aktualny stan planszy"""
        print("\n" + "=" * 40)
        print("AKTUALNA PLANSZA:")
        self.display.display_board(self.board.board, self.board.queens, self.board.pawn_positions) # wyświetlanie całej planszy
        print("\nPozycje hetmanów:", [self.board.chess_notation(x, y) for x, y in self.board.queens])
        print("Pozycja pionka:", self.board.chess_notation(*self.board.pawn_positions))
        ChessLogic.check_threats(self.board)



    def _get_user_choice(self):
        """Pobiera i waliduje wyboru użytkownika"""
        while True:
            print("\nOpcje:")
            print("1. Wylosuj nową pozycję dla pionka")
            print("2. Usuń hetmana")
            print("3. Sprawdź ponownie bicie")
            print("4. Zakończ grę")

            try:
                choice = int(input("Twój wybór (1-4): "))
                if 1 <= choice <= 4:
                    return choice
                print("Nieprawidłowy wybór. Wprowadź liczbę od 1 do 4.")
            except ValueError:
                print("Proszę wprowadzić liczbę.")



    def _move_pawn(self):
        """Obsługa zmiany pozycji pionka"""
        old_x, old_y = self.board.pawn_positions
        self.board.board[old_x][old_y] = ' '
        self.board.add_random_pawn()
        print(f"\nNowa pozycja pionka: {self.board.chess_notation(*self.board.pawn_positions)}")



    def _remove_queen(self):
        """Obsługa usuwania hetmana"""
        if not self.board.queens:
            print("\nBrak hetmanów do usunięcia!")
            return

        print("\nDostępne hetmany:")
        for i, (x, y) in enumerate(self.board.queens, 1):
            print(f"{i}. {self.board.chess_notation(x, y)}")

        try:
            choice = int(input("Wybierz numer hetmana (0 aby anulować): "))
            if choice == 0:
                return
            if 1 <= choice <= len(self.board.queens):
                x, y = self.board.queens.pop(choice - 1)
                self.board.board[x][y] = ' '
                print(f"Usunięto hetmana na pozycji {self.board.chess_notation(x, y)}")
            else:
                print("Nieprawidłowy numer hetmana!")
        except ValueError:
            print("Wprowadź poprawny numer!")



    def _check_threats(self):
        """Wymusza ponowne sprawdzenie zagrożeń"""
        ChessLogic.check_threats(self.board)



    def _exit_game(self):
        """Zamykanie gry z podsumowaniem"""
        print("\nDziękujemy za grę!")
