import unittest

from tictactoe.board import Board
from tictactoe.my_exceptions import InvalidMoveException
from tictactoe.player import Player


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player1 = Player("stephen", "X")
        self.player2 = Player("sam", "O")

    def test_initial_board(self):
        expected = [[' ' for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.board.grid, expected)

    def test_valid_move(self):
        self.board.make_move(0, 0, 'X', self.player1)
        self.assertEqual(self.board.grid[0][0], 'X')

    def test_invalid_move(self):
        self.board.make_move(0, 0, 'X')
        with self.assertRaises(InvalidMoveException):
            self.board.make_move(0, 0, 'O')

    def test_for_winner_at_initial(self):
        self.assertIsNone(self.board.check_winner(), "no winner yet")

    def test_for_winner_row(self):
        self.board.make_move(0, 0, 'X')
        self.board.make_move(0, 1, 'X')
        self.board.make_move(0, 2, 'X')
        self.assertEqual(self.board.check_winner(), "X", "winner")

    def test_for_winner_colomn(self):
        self.board.make_move(0, 0, 'O')
        self.board.make_move(1, 0, 'O')
        self.board.make_move(2, 0, 'O')
        self.assertEqual(self.board.check_winner(), "O", "winner")

    def test_that_winner_X_wins_slant_way(self):
        self.board.make_move(0, 0, 'X')
        self.board.make_move(1, 1, 'X')
        self.board.make_move(2, 2, 'X')
        self.assertEqual(self.board.check_winner(), "X", "winner")

    def test_that_winner_X_wins_anti_slant_way(self):
        self.board.make_move(0, 2, 'O')
        self.board.make_move(1, 1, 'O')
        self.board.make_move(2, 0, 'O')
        self.assertEqual(self.board.check_winner(), "O", "winner")

    def test_that_player_X_and_O_did_not_win(self):
        moves = [
            (0, 0, 'X'), (0, 1, 'O'), (0, 2, 'X'),
            (1, 0, 'O'), (1, 1, 'X'), (1, 2, 'O'),
            (2, 0, 'O'), (2, 1, 'X'), (2, 2, 'O')
        ]
        for row, column, token in moves:
            self.board.make_move(row, column, token)
        self.assertTrue(self.board.is_draw())

    def test_to_get_the_move_of_players(self):
        player = Player('X', "stephen")
        move = player.get_move()
        self.assertEqual(move, (1, 2))

if __name__ == '__main__':
    unittest.main()
