from tictactoe.game import Game
from tictactoe.player import Player


def main_app():
    print("Welcome to Your TicTacToe Dear User!")
    print("The rules of this game is simple:")
    print("""
        1. Enter the name you which to be called it this game.
        2. Enter your token (Symbol), you will be identified by your token in the game in this game we go by X and O as our token(Symbol).
        3. Please you are to enter between (1-9) in this game any number or any other character would be accepted.
        4. Enjoy your game!
        """
    )
    name1 = input("Enter your name player 1: ")
    token1 = input("Enter token for player 1 (e.g. X or O): ")
    name2 = input("Enter your name player 2: ")
    token2 = input("Enter token for player 2 (e.g. X or O): ")

    player1 = Player(name1, token1)
    player2 = Player(name2, token2)

    game = Game(player1, player2)
    game.play()


if __name__ == "__main__":
    main_app()