from generate_board import GenerateBoard
from display_board import DisplayBoard
from chess_logic import ChessLogic

import random

class GameController:
    def __init__(self):
        self.board = GenerateBoard()
        self.display= DisplayBoard()
        self.initialize_game()



    def initialize_game(self):
        """Inicializacja nowej gry"""
        queens_number = random.randint(1, 5)
        self.board.add_random_queen(queens_number)
        self.board.add_random_pawn()



    def get_user_choice(self):
        """Wyświtelnie menu i pobranie wyboru użytkownika"""
        print("\n Wybierz opcję:")
        print(" 1. Wylosuj nową pozycję dla pionka")
        print(" 2. Usunięcie dowolnego hetmana")
        print(" 3. Sprawdź ponownie bicie")
        print(" 4. Zakończ grę")

        while True:
            choice = input(" Twój wybór(1-4): ")
            if choice in ['1', '2', '3', '4']:
                return int(choice)
            print(" Niepoprawny wybór, spróbuj ponownie.")



    def move_pawn(self):
        """1. Losowanie nowej pozycji dla pionka"""
        old_x, old_y = self.board.pawn_positions
        self.board.board[old_x][old_y] = '░'
        self.board.add_random_pawn()
        print("\n Nowa pozycja pionka:", self.board.chess_notation(*self.board.pawn_positions))



    def remove_queen(self):
        """2. Usuwa wybranego przez użytkownika hetmana"""
        if not self.board.queens:
            print(" Nie ma hetmanów do usunięcia.")
            return False

        print("\n Dostępne hetmany do usunięcia:")
        for i, (x, y) in enumerate(self.board.queens):
            print(f" {i + 1}. {self.board.chess_notation(x, y)}")

        while True:
            try:
                choice = int(input(" Wybierz hetmana do usunięcia lub zero aby anulować: "))
                if choice == 0:
                    return False
                if 1 <= choice <= len(self.board.queens):
                    x, y = self.board.queens[choice - 1]
                    self.board.board[x][y] = '░'
                    del self.board.queens[choice - 1]
                    print(f" Usunięto hetmana z pozycji: {self.board.chess_notation(x, y)}")
                    return True
                print(" Niepoprawny wybór, spróbuj ponownie.")
            except ValueError:
                print(" Spróbuj jeszcze raz wprowadzić liczbę.")



    def check_pawn_threat(self):
        """3. Sprawdza czy pionek jest zagrożony"""
        threading_queens = ChessLogic.find_threatening_queens(self.board.queens, self.board.pawn_positions)
        if threading_queens:
            print("\n Pionek może być zbity przez:")
            for queen in threading_queens:
                print(f" - {self.board.chess_notation(*queen)}")
        else:
            print("\n Pionek jest bezpieczny")



    def display_current_state(self):
        """Wyświetla aktualny stan planszy"""
        print("\n Plansza")
        self.display.display_board(self.board.board, self.board.queens, self.board.pawn_positions)
        print("\n Pozycje hetmanów:", [self.board.chess_notation(x,y) for x, y in self.board.queens])
        print(" Pozycja pionka:", self.board.chess_notation(*self.board.pawn_positions))



    def run(self):
        """Uruchamia grę - główna pętla"""
        while True:
            self.display_current_state()
            self.check_pawn_threat()

            choice = self.get_user_choice()

            if choice == 1:
                self.move_pawn()
            elif choice == 2:
                self.remove_queen()
            elif choice == 3:
                self.check_pawn_threat()
            elif choice == 4:
                print(" Dziękuję za grę!")
                break











