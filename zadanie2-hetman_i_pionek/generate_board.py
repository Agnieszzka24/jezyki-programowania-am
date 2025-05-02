import random

class GenerateBoard:
    def __init__(self, size=8):
        # if size < 1:
        #     raise ValueError("Size must be at least 1")
        self.size = size
        self.board = self.generate_empty_board()
        self.queens = []  #przechowywanie pozycji hetmanów (x,y)
        self.pawn_positions = None



    def add_random_queen(self, k):
        """Dodaje k hetmanów na losowe pozycje"""
        for _ in range(k):
            while True:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
                if (x, y) not in self.queens and (x, y) != self.pawn_positions:
                    self.board[x][y] = 'Q'
                    self.queens.append((x, y))
                    break



    def add_random_pawn(self):
        """Dodaje piona na losową pozycje (inną niż hetman)"""
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if (x, y) not in self.queens:
                self.board[x][y] = 'P'
                self.pawn_positions = (x, y)
                break



    def generate_empty_board(self):
        """Generuje pustą planszę"""
        return [[' ' for _ in range(self.size)] for _ in range(self.size)]



    def chess_notation(self, x, y):
        """Konwertuje (x, y) na notację szachową np. a1, c4"""
        column = chr(97 + y)
        row = str(self.size - x)
        return f"{column}{row}"



    # def display_board(self):
    #     """Wyświetla planszę w formacie tekstowym"""
    #     GREEN = '\033[92m'
    #     RED = '\033[91m'
    #     RESET = '\033[0m'
    #
    #     header = "╤ " + " ".join([chr(97 + i) for i in range(self.size)]) + " ╤"
    #     print(header)
    #
    #     for i, row in enumerate(self.board):
    #         row_number = f"{self.size - i}"
    #         cells = []
    #         for cell in row:
    #             if cell == 'Q':
    #                 cells.append(f"{RED}Q{RESET}")
    #             elif cell == 'P':
    #                 cells.append(f"{GREEN}P{RESET}")
    #             else:
    #                 cells.append(f"░")
    #         print(f"{row_number} {' '.join(cells)} {self.size - i}")
    #
    #     footer = "╧ " + " ".join([chr(97 + i) for i in range(self.size)]) + " ╧"
    #     print(footer)