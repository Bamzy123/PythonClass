from tictactoe.board import Board
from tictactoe.my_exceptions import InvalidMoveException

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % 2

    def play(self):
        while True:
            current_player = self.players[self.current_player_index]
            print(self.board)

            try:
                row, column = current_player.get_move()
                self.board.make_move(row, column, current_player.token, current_player)
            except InvalidMoveException as e:
                print(f"Invalid move: {e}. Please try again.")
                continue

            winner = self.board.check_winner()
            if winner is not None:
                print(self.board)
                print(f"Congratulations, {current_player.get_name()} wins!")
                break

            if self.board.is_draw():
                print(self.board)
                print("It's a tie or draw!")
                break

            self.switch_player()