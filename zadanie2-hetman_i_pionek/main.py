from generate_board import GenerateBoard
from chess_logic import ChessLogic
from display_board import DisplayBoard
from game_controller import GameController

import random


def get_random_queens_number():
    """Funkcja do losowania liczby hetmanów"""
    return random.randint(1, 5)



def check_if_queens_threaten_pawn(board):
    """Funkcja sprawdzająca czy hetmany grożą pionkowi i wyświetla ich pozycje"""
    threading_queens = ChessLogic.find_threatening_queens(board.queens, board.pawn_positions)

    if threading_queens:
        print("\n Pionek może być zbity przez:")
        for queen in threading_queens:
            print(f" - {board.chess_notation(*queen)}")
    else:
        print("\n Pionek jest bezpiczny")



if __name__ == "__main__":
    # Wyświelenie planszy
    board = GenerateBoard()
    display_board = DisplayBoard()
    game = GameController()


    queens_number = get_random_queens_number()

    board.add_random_queen(queens_number)
    board.add_random_pawn()

    print("\n Plansza")
    display_board.display_board(board.board, board.queens, board.pawn_positions)

    print("\n Pozycje hetmanów:", [board.chess_notation(x,y) for x, y in board.queens])
    print(" Pozycja pionka:", board.chess_notation(*board.pawn_positions))

    check_if_queens_threaten_pawn(board)

    game.run()