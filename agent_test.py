"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import timeit

from importlib import reload

TIME_LIMIT_MILLIS = 150

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)
        self.minimax_player = game_agent.MinimaxPlayer()

    def test_minimax_player(self):
        time_millis = lambda: 1000 * timeit.default_timer()
        move_start = time_millis()
        time_left = lambda : TIME_LIMIT_MILLIS - (time_millis() - move_start)

        print("minimax_player is ")
        print(self.minimax_player.get_move)

        best_move = self.minimax_player.get_move(self.game, time_left)
        print('best move is ----')
        print(best_move)


if __name__ == '__main__':
    unittest.main()
