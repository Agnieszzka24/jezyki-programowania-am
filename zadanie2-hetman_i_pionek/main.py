from generate_board import GenerateBoard

if __name__ == "__main__":
    # Wyświelenie planszy
    board = GenerateBoard()

    board.add_random_queen(3)
    board.add_random_pawn()

    print("\n Plansza")
    board.display_board()

    print("\n Pozycje hetmanów:", [board.chess_notation(x,y) for x, y in board.queens])
    print("\n Pozycja pionka:", board.chess_notation(*board.pawn_positions))
