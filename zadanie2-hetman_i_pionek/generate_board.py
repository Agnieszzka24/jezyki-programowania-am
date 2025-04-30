class GenerateBoard:
    def __init__(self, size=8):
        if size < 1:
            raise ValueError("Size must be at least 1")
        self.size = size
        self.board = self.generate_empty_board()

    def generate_empty_board(self):
        return [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def display_board(self):
        header = "╤ " + " ".join([chr(97 + i) for i in range(self.size)]) + " ╤"
        print(header)

        for i, row in enumerate(self.board):
            row_number = f"{self.size - i} ░"
            cells = "░".join(row)
            print(f"{row_number}{cells}{self.size - i}")

        footer = "╧ " + " ".join([chr(97 + i) for i in range(self.size)]) + " ╧"
        print(footer)