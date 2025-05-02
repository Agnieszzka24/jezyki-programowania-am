from generate_board import GenerateBoard
import random


def get_random_queens_number():
    """Funkcja do losowania liczby hetmanów"""
    return random.randint(1, 5)

if __name__ == "__main__":
    # Wyświelenie planszy
    board = GenerateBoard()

    queens_number = get_random_queens_number()

    board.add_random_queen(queens_number)
    board.add_random_pawn()

    print("\n Plansza")
    board.display_board()

    print("\n Pozycje hetmanów:", [board.chess_notation(x,y) for x, y in board.queens])
    print(" Pozycja pionka:", board.chess_notation(*board.pawn_positions))
