class DisplayBoard:
    """Klasa odpowiedzialna za wyświetlanie planszy"""

    def __init__(self, size=8):
        self.size = size

        self.GREEN = '\033[92m'
        self.RED = '\033[91m'
        self.ORANGE = '\033[38;5;208m'
        self.RESET = '\033[0m'

    def get_attacked_positions(self, queens, size):
        """Zwraca listę atakowanych pozycji przez hetmany (do kolorowania)"""
        attacked_positions = set()
        for qx ,qy in queens:
            # poziomo i pionowo
            for i in range(size):
                attacked_positions.add((qx, i)) # cały wiersz
                attacked_positions.add((i, qy)) # cała kolumna

            # przekątne
            for i in range(1, size):
                for dx, dy in [(1,1), (1,-1), (-1,1), (-1,-1)]:  # różne kierunki przekątnych
                    x, y = qx + i * dx, qy + i * dy # oblicza pozycje na przekątnej
                    if 0 <= x < size and 0 <= y < size: # granica planszy
                        attacked_positions.add((x, y))
        return attacked_positions

    def display_board(self, board, queens, pawn_pos, show_attacked=True):
        """Wyświetla planszę"""
        attacked = self.get_attacked_positions(queens, self.size) if show_attacked else set() # atakowane pozycje

        header = "╤ " + " ".join([chr(97 + i) for i in range(self.size)]) + " ╤"
        print(header)

        for i, row in enumerate(board):
            row_number = f"{self.size - i}" # 8-1
            cells = []
            for j, cell in enumerate(row):
                if (i, j) == pawn_pos:
                    cells.append(f"{self.GREEN}P{self.RESET}")
                elif (i, j) in [(q[0], q[1]) for q in queens]:
                    cells.append(f"{self.RED}Q{self.RESET}")
                elif (i, j) in attacked:
                    cells.append(f"{self.ORANGE}░{self.RESET}")
                else:
                    cells.append("░")
            print(f"{row_number} {' '.join(cells)} {self.size - i}")

        footer = "╧ " + " ".join([chr(97 + i) for i in range(self.size)]) + " ╧"
        print(footer)