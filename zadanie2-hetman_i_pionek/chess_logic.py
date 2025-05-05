class ChessLogic:
    @staticmethod
    def is_queen_threatening_pawn(queen_pos, pawn_pos):
        """Sprawdza czy hetman grozi pionkowi."""
        qx, qy = queen_pos
        px, py = pawn_pos

        # To samo pole
        if (qx, qy) == (px, py):
            return False

        # Ta sama kolumna, wiersz lub przekątna
        return qx == px or qy == py or abs(qx - px) == abs(qy - py)

    @classmethod
    def find_threatening_queens(cls, queens, pawn_pos):
        """Znajduje wszystkie hetmany grożące pionkowi."""
        return [queen for queen in queens
                if cls.is_queen_threatening_pawn(queen, pawn_pos)]

    @classmethod
    def check_threats(cls, board):
        """Sprawdza i wyświetla zagrożenia pionka."""
        threats = cls.find_threatening_queens(board.queens, board.pawn_positions)

        if threats:
            print("\nPionek może być zbity przez:")
            for queen in threats:
                print(f" - {board.chess_notation(*queen)}")
        else:
            print("\nPionek jest bezpieczny")