class ChessLogic:
    """Klasa ChessLogic zawiera metody do sprawdzania zagrożeń pionka przez hetmany na szachownicy."""

    @staticmethod
    def is_queen_threatening_pawn(queen_pos, pawn_pos):
        """Sprawdza czy hetman grozi pionkowi."""
        qx, qy = queen_pos
        px, py = pawn_pos

        # To samo pole
        if qx == px and qy == py:
            return False

        # Ta sama kolumna lub wiersz
        if qx == px or qy == py:
            return True

        # Ta sama przekątna - różnica współrzędnych jest taka sama
        if abs(qx - px) == abs(qy - py):
            return True

        return False



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