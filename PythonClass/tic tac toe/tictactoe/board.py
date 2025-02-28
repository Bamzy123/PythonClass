from tictactoe.my_exceptions import InvalidMoveException

class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, column, token, player=None):
        if not (0 <= row < 3 and 0 <= column < 3):
            raise InvalidMoveException("Move out of bounds!")
        if self.grid[row][column] != ' ':
            raise InvalidMoveException("Move already made!")

        if player is not None:
            token = player.get_token()
        self.grid[row][column] = token

    def check_winner(self):
        for row in self.grid:
            if row[0] != ' ' and row[0] == row[1] == row[2]:
                return row[0]
        for col in range(3):
            if self.grid[0][col] != ' ' and self.grid[0][col] == self.grid[1][col] == self.grid[2][col]:
                return self.grid[0][col]

        if self.grid[0][0] != ' ' and self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            return self.grid[0][0]
        if self.grid[0][2] != ' ' and self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
            return self.grid[0][2]
        return None

    def is_draw(self):
        return all(cell != ' ' for row in self.grid for cell in row) and self.check_winner() is None

    def __str__(self):
        rows = [" | ".join(row) for row in self.grid]
        return "\n------------\n".join(rows)