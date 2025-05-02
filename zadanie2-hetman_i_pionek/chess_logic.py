class ChessLogic:
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

        # Ta sama przekątna
        if abs(qx - px) == abs(qy - py):
            return True

        return False

    @classmethod
    def find_threatening_queens(cls, queens, pawn_pos):
        """Znajduje wszystkie hetmany grożące pionkowi."""
        threatening = []
        for queen in queens:
            if cls.is_queen_threatening_pawn(queen, pawn_pos):
                threatening.append(queen)
        return threatening