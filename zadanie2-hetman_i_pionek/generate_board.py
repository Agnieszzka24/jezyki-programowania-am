class GenerateBoard:
    def __init__(self, size = 8):
        self.size = size
        self.board = self.generate_empty_board()

    def generate_empty_board(self):
        return [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def display_board(self):
        header = "  " +" ".join([chr(97 + i) for i in range(0, self.size)])
        print(header)

        # for i , row in


